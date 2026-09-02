#!/usr/bin/env python3
"""Deterministically calculate auditable household-finance metrics from JSON.

The script uses only the Python standard library and never embeds user data.
Run ``python3 calculate_financial_metrics.py --example`` for the input schema.

Asset records are aggregated only when the corresponding boolean flag is
present for every record.  This prevents a missing classification from being
silently treated as ``false``.  Each net asset pool then subtracts principal
only when every liability explicitly states the matching deduction flag.
Current liabilities use outstanding principal only; ``future_interest`` is
reported separately and never added to debt.
"""

from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Iterable


MONEY_PLACES = 2
RATIO_PLACES = 6

ASSET_FLAGS = {
    "total_assets": ("total_asset", "include_in_total_assets"),
    "property_assets": ("property", "is_property"),
    "net_available_liquid_assets": (
        "net_available_liquid",
        "include_in_net_available_liquid",
    ),
    "broad_available_financial_assets": (
        "broad_available_financial",
        "include_in_broad_available_financial",
    ),
    "strict_long_term_investment_assets": (
        "strict_long_term_investment",
        "include_in_strict_long_term_investment",
    ),
}

LIABILITY_FLAG = ("current_liability", "include_in_current_liabilities")

LIABILITY_DEDUCTION_FLAGS = {
    "net_available_liquid_liability_deduction": (
        "subtract_from_net_available_liquid",
    ),
    "broad_available_financial_liability_deduction": (
        "subtract_from_broad_available_financial",
    ),
    "strict_long_term_investment_liability_deduction": (
        "subtract_from_strict_long_term_investment",
    ),
}

EXAMPLE_INPUT = {
    "assets": [
        {
            "label": "cash_account_a",
            "amount": 120000,
            "flags": {
                "total_asset": True,
                "property": False,
                "net_available_liquid": True,
                "broad_available_financial": True,
                "strict_long_term_investment": False,
            },
        },
        {
            "label": "diversified_investment_account",
            "amount": 300000,
            "flags": {
                "total_asset": True,
                "property": False,
                "net_available_liquid": False,
                "broad_available_financial": True,
                "strict_long_term_investment": True,
            },
        },
        {
            "label": "owner_occupied_property",
            "amount": 1800000,
            "flags": {
                "total_asset": True,
                "property": True,
                "net_available_liquid": False,
                "broad_available_financial": False,
                "strict_long_term_investment": False,
            },
        },
    ],
    "liabilities": [
        {
            "label": "property_loan",
            "principal": 700000,
            "future_interest": 180000,
            "flags": {
                "current_liability": True,
                "subtract_from_net_available_liquid": False,
                "subtract_from_broad_available_financial": False,
                "subtract_from_strict_long_term_investment": False,
            },
        },
        {
            "label": "short_term_consumer_debt",
            "principal": 20000,
            "future_interest": 3000,
            "flags": {
                "current_liability": True,
                "subtract_from_net_available_liquid": True,
                "subtract_from_broad_available_financial": True,
                "subtract_from_strict_long_term_investment": False,
            },
        }
    ],
    "monthly_expenses": {"living": 12000, "essential": 7500},
    "essential_expense_includes_debt_payment": False,
    "stable_monthly_income": {"amount": 30000, "basis": "after_tax"},
    "monthly_debt_payment": 5000,
    "sustainable_monthly_non_labor_income": 1000,
    "withdrawal_rate": 0.04,
}


class InputError(ValueError):
    """Raised when supplied JSON has an invalid shape or value."""


def _warning(warnings: list[dict[str, str]], code: str, message: str) -> None:
    if not any(item["code"] == code for item in warnings):
        warnings.append({"code": code, "message": message})


def _decimal(value: Any, field: str, *, allow_none: bool = False) -> Decimal | None:
    if value is None and allow_none:
        return None
    if isinstance(value, bool) or not isinstance(value, (Decimal, int, float, str)):
        raise InputError(f"{field} must be a JSON number")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise InputError(f"{field} must be a valid JSON number") from None
    if not result.is_finite():
        raise InputError(f"{field} must be finite")
    return result


def _nonnegative(value: Any, field: str, *, allow_none: bool = False) -> Decimal | None:
    result = _decimal(value, field, allow_none=allow_none)
    if result is not None and result < 0:
        raise InputError(f"{field} must be non-negative")
    return result


def _json_number(value: Decimal | None, places: int) -> int | float | None:
    if value is None:
        return None
    quantum = Decimal(1).scaleb(-places)
    rounded = value.quantize(quantum, rounding=ROUND_HALF_UP)
    if rounded == rounded.to_integral_value():
        return int(rounded)
    return float(rounded)


def _money(value: Decimal | None) -> int | float | None:
    return _json_number(value, MONEY_PLACES)


def _ratio(value: Decimal | None) -> int | float | None:
    return _json_number(value, RATIO_PLACES)


def _get_flag(record: dict[str, Any], aliases: Iterable[str], field: str) -> bool | None:
    flags = record.get("flags", {})
    if flags is None:
        flags = {}
    if not isinstance(flags, dict):
        raise InputError(f"{field}.flags must be an object")

    found: list[Any] = []
    for name in aliases:
        if name in flags:
            found.append(flags[name])
        if name in record:
            found.append(record[name])
    if not found:
        return None
    if any(not isinstance(value, bool) for value in found):
        raise InputError(f"{field} flag must be true or false")
    if any(value != found[0] for value in found[1:]):
        raise InputError(f"{field} contains conflicting flag aliases")
    return bool(found[0])


def _records(data: dict[str, Any], key: str) -> list[dict[str, Any]] | None:
    if key not in data or data[key] is None:
        return None
    value = data[key]
    if not isinstance(value, list):
        raise InputError(f"{key} must be an array")
    for index, record in enumerate(value):
        if not isinstance(record, dict):
            raise InputError(f"{key}[{index}] must be an object")
    return value


def _aggregate_assets(
    assets: list[dict[str, Any]] | None,
    warnings: list[dict[str, str]],
) -> dict[str, Decimal | None]:
    result = {name: None for name in ASSET_FLAGS}
    if assets is None:
        _warning(
            warnings,
            "MISSING_ASSETS",
            "assets is missing; asset-derived metrics are null.",
        )
        return result

    amounts = [
        _nonnegative(record.get("amount", record.get("value")), f"assets[{index}].amount")
        for index, record in enumerate(assets)
    ]
    for output_name, aliases in ASSET_FLAGS.items():
        flags = [
            _get_flag(record, aliases, f"assets[{index}].{aliases[0]}")
            for index, record in enumerate(assets)
        ]
        if any(flag is None for flag in flags):
            _warning(
                warnings,
                f"INCOMPLETE_{output_name.upper()}_FLAGS",
                f"At least one asset lacks the {aliases[0]} flag; {output_name} is null.",
            )
            continue
        result[output_name] = sum(
            (amount for amount, flag in zip(amounts, flags) if flag),
            Decimal(0),
        )
    return result


def _aggregate_liabilities(
    liabilities: list[dict[str, Any]] | None,
    warnings: list[dict[str, str]],
) -> dict[str, Decimal | None]:
    result = {
        "current_liabilities": None,
        "ignored_future_interest": None,
        **{name: None for name in LIABILITY_DEDUCTION_FLAGS},
    }
    if liabilities is None:
        _warning(
            warnings,
            "MISSING_LIABILITIES",
            "liabilities is missing; current liabilities and liability-netted asset metrics are null.",
        )
        return result

    principals: list[Decimal] = []
    future_interest: list[Decimal] = []
    current_flags: list[bool | None] = []
    for index, record in enumerate(liabilities):
        principals.append(
            _nonnegative(record.get("principal"), f"liabilities[{index}].principal")
        )
        future_interest.append(
            _nonnegative(
                record.get("future_interest", 0),
                f"liabilities[{index}].future_interest",
            )
        )
        current_flags.append(
            _get_flag(record, LIABILITY_FLAG, f"liabilities[{index}].current_liability")
        )

    result["ignored_future_interest"] = sum(future_interest, Decimal(0))
    if any(flag is None for flag in current_flags):
        _warning(
            warnings,
            "INCOMPLETE_CURRENT_LIABILITY_FLAGS",
            "At least one liability lacks current_liability; current liabilities are null.",
        )
    else:
        result["current_liabilities"] = sum(
            (
                principal
                for principal, flag in zip(principals, current_flags)
                if flag
            ),
            Decimal(0),
        )

    for output_name, aliases in LIABILITY_DEDUCTION_FLAGS.items():
        flags = [
            _get_flag(record, aliases, f"liabilities[{index}].{aliases[0]}")
            for index, record in enumerate(liabilities)
        ]
        if any(flag is None for flag in flags):
            _warning(
                warnings,
                f"INCOMPLETE_{aliases[0].upper()}_FLAGS",
                f"At least one liability lacks {aliases[0]}; the corresponding net asset metric is null.",
            )
            continue
        result[output_name] = sum(
            (principal for principal, flag in zip(principals, flags) if flag),
            Decimal(0),
        )
    return result


def _top_or_nested(
    data: dict[str, Any],
    top_key: str,
    parent_key: str,
    child_key: str,
) -> Any:
    if top_key in data:
        return data[top_key]
    parent = data.get(parent_key)
    if parent is None:
        return None
    if not isinstance(parent, dict):
        raise InputError(f"{parent_key} must be an object")
    return parent.get(child_key)


def _income(data: dict[str, Any]) -> tuple[Decimal | None, str | None]:
    income = data.get("stable_monthly_income")
    if income is not None:
        if isinstance(income, dict):
            amount = _nonnegative(
                income.get("amount"), "stable_monthly_income.amount", allow_none=True
            )
            raw_basis = income.get("basis")
        else:
            amount = _nonnegative(income, "stable_monthly_income")
            raw_basis = data.get("stable_monthly_income_basis")
    else:
        pre_tax = data.get("stable_monthly_pre_tax_income")
        after_tax = data.get("stable_monthly_after_tax_income")
        if pre_tax is not None and after_tax is not None:
            raise InputError(
                "provide only one of stable_monthly_pre_tax_income and "
                "stable_monthly_after_tax_income"
            )
        if pre_tax is not None:
            amount = _nonnegative(pre_tax, "stable_monthly_pre_tax_income")
            raw_basis = "pre_tax"
        elif after_tax is not None:
            amount = _nonnegative(after_tax, "stable_monthly_after_tax_income")
            raw_basis = "after_tax"
        else:
            return None, None

    basis_map = {
        "pre_tax": "pre_tax",
        "gross": "pre_tax",
        "税前": "pre_tax",
        "after_tax": "after_tax",
        "take_home": "after_tax",
        "net": "after_tax",
        "税后": "after_tax",
    }
    if raw_basis is None:
        return amount, None
    if not isinstance(raw_basis, str) or raw_basis not in basis_map:
        raise InputError(
            "stable_monthly_income.basis must be pre_tax or after_tax"
        )
    return amount, basis_map[raw_basis]


def _safe_divide(
    numerator: Decimal | None,
    denominator: Decimal | None,
    warnings: list[dict[str, str]],
    *,
    missing_code: str,
    missing_message: str,
    zero_code: str,
    zero_message: str,
) -> Decimal | None:
    if numerator is None or denominator is None:
        _warning(warnings, missing_code, missing_message)
        return None
    if denominator == 0:
        _warning(warnings, zero_code, zero_message)
        return None
    return numerator / denominator


def calculate_metrics(data: dict[str, Any]) -> dict[str, Any]:
    """Calculate metrics from a parsed JSON object."""
    if not isinstance(data, dict):
        raise InputError("the JSON root must be an object")

    warnings: list[dict[str, str]] = []
    assets = _aggregate_assets(_records(data, "assets"), warnings)
    liabilities = _aggregate_liabilities(
        _records(data, "liabilities"), warnings
    )
    current_liabilities = liabilities["current_liabilities"]
    ignored_future_interest = liabilities["ignored_future_interest"]

    living_raw = _top_or_nested(
        data, "monthly_living_expense", "monthly_expenses", "living"
    )
    essential_raw = _top_or_nested(
        data, "monthly_essential_expense", "monthly_expenses", "essential"
    )
    living = _nonnegative(
        living_raw, "monthly_expenses.living", allow_none=True
    )
    essential = _nonnegative(
        essential_raw, "monthly_expenses.essential", allow_none=True
    )
    debt_payment = _nonnegative(
        data.get("monthly_debt_payment"),
        "monthly_debt_payment",
        allow_none=True,
    )
    income, income_basis = _income(data)

    includes_debt = data.get("essential_expense_includes_debt_payment", False)
    if not isinstance(includes_debt, bool):
        raise InputError("essential_expense_includes_debt_payment must be true or false")

    if living is None:
        _warning(
            warnings,
            "MISSING_MONTHLY_LIVING_EXPENSE",
            "Monthly living expense is missing; living-expense denominators are null.",
        )
    if essential is None:
        _warning(
            warnings,
            "MISSING_MONTHLY_ESSENTIAL_EXPENSE",
            "Monthly essential expense is missing; essential runway is null.",
        )
    if debt_payment is None:
        _warning(
            warnings,
            "MISSING_MONTHLY_DEBT_PAYMENT",
            "Monthly debt payment is missing; debt-service pressure is null.",
        )
    if income is None:
        _warning(
            warnings,
            "MISSING_STABLE_MONTHLY_INCOME",
            "Stable monthly income is missing; debt-service pressure is null.",
        )
    elif income_basis is None:
        _warning(
            warnings,
            "MISSING_INCOME_BASIS",
            "Stable income was supplied without pre-tax/after-tax basis.",
        )

    total_assets = assets["total_assets"]
    property_assets = assets["property_assets"]
    liquid_asset_subtotal = assets["net_available_liquid_assets"]
    broad_asset_subtotal = assets["broad_available_financial_assets"]
    strict_asset_subtotal = assets["strict_long_term_investment_assets"]
    liquid_liability_deduction = liabilities[
        "net_available_liquid_liability_deduction"
    ]
    broad_liability_deduction = liabilities[
        "broad_available_financial_liability_deduction"
    ]
    strict_liability_deduction = liabilities[
        "strict_long_term_investment_liability_deduction"
    ]
    liquid_assets = (
        liquid_asset_subtotal - liquid_liability_deduction
        if liquid_asset_subtotal is not None
        and liquid_liability_deduction is not None
        else None
    )
    broad_assets = (
        broad_asset_subtotal - broad_liability_deduction
        if broad_asset_subtotal is not None
        and broad_liability_deduction is not None
        else None
    )
    strict_assets = (
        strict_asset_subtotal - strict_liability_deduction
        if strict_asset_subtotal is not None
        and strict_liability_deduction is not None
        else None
    )
    net_worth = (
        total_assets - current_liabilities
        if total_assets is not None and current_liabilities is not None
        else None
    )

    asset_liability_ratio = _safe_divide(
        current_liabilities,
        total_assets,
        warnings,
        missing_code="MISSING_ASSET_LIABILITY_RATIO_INPUT",
        missing_message="Total assets or current liabilities are missing; asset-liability ratio is null.",
        zero_code="ZERO_TOTAL_ASSETS",
        zero_message="Total assets are zero; asset-liability ratio is null.",
    )
    property_concentration = _safe_divide(
        property_assets,
        total_assets,
        warnings,
        missing_code="MISSING_PROPERTY_CONCENTRATION_INPUT",
        missing_message="Property or total assets are missing; property concentration is null.",
        zero_code="ZERO_TOTAL_ASSETS_FOR_PROPERTY_CONCENTRATION",
        zero_message="Total assets are zero; property concentration is null.",
    )
    living_runway = _safe_divide(
        liquid_assets,
        living,
        warnings,
        missing_code="MISSING_LIVING_RUNWAY_INPUT",
        missing_message="Net available liquid assets or monthly living expense are missing; living runway is null.",
        zero_code="ZERO_MONTHLY_LIVING_EXPENSE_FOR_RUNWAY",
        zero_message="Monthly living expense is zero; living runway is null.",
    )

    if includes_debt:
        essential_outflow = essential
    elif essential is not None and debt_payment is not None:
        essential_outflow = essential + debt_payment
    else:
        essential_outflow = None
    essential_runway = _safe_divide(
        liquid_assets,
        essential_outflow,
        warnings,
        missing_code="MISSING_ESSENTIAL_RUNWAY_INPUT",
        missing_message="Net liquid assets or the complete essential monthly outflow are missing; essential runway is null.",
        zero_code="ZERO_ESSENTIAL_MONTHLY_OUTFLOW",
        zero_message="Essential monthly outflow is zero; essential runway is null.",
    )
    debt_service_pressure = _safe_divide(
        debt_payment,
        income,
        warnings,
        missing_code="MISSING_DEBT_SERVICE_PRESSURE_INPUT",
        missing_message="Monthly debt payment or stable income is missing; debt-service pressure is null.",
        zero_code="ZERO_STABLE_MONTHLY_INCOME",
        zero_message="Stable monthly income is zero; debt-service pressure is null.",
    )

    annual_living = living * Decimal(12) if living is not None else None
    broad_multiple = _safe_divide(
        broad_assets,
        annual_living,
        warnings,
        missing_code="MISSING_BROAD_MULTIPLE_INPUT",
        missing_message="Broad financial assets or annual living expense are missing; broad multiple is null.",
        zero_code="ZERO_ANNUAL_LIVING_EXPENSE_FOR_BROAD_MULTIPLE",
        zero_message="Annual living expense is zero; broad multiple is null.",
    )
    strict_multiple = _safe_divide(
        strict_assets,
        annual_living,
        warnings,
        missing_code="MISSING_STRICT_MULTIPLE_INPUT",
        missing_message="Strict investment assets or annual living expense are missing; strict multiple is null.",
        zero_code="ZERO_ANNUAL_LIVING_EXPENSE_FOR_STRICT_MULTIPLE",
        zero_message="Annual living expense is zero; strict multiple is null.",
    )

    withdrawal_raw = data.get("withdrawal_rate")
    withdrawal_rate = _decimal(
        withdrawal_raw, "withdrawal_rate", allow_none=True
    )
    non_labor_income = _nonnegative(
        data.get("sustainable_monthly_non_labor_income", 0),
        "sustainable_monthly_non_labor_income",
    )
    target_capital: Decimal | None = None
    target_progress: Decimal | None = None
    uncovered_annual_expense: Decimal | None = None
    if withdrawal_rate is not None:
        if withdrawal_rate == 0:
            _warning(
                warnings,
                "ZERO_WITHDRAWAL_RATE",
                "Withdrawal rate is zero; target capital and progress are null.",
            )
        elif withdrawal_rate < 0 or withdrawal_rate >= 1:
            _warning(
                warnings,
                "INVALID_WITHDRAWAL_RATE",
                "Withdrawal rate must be a decimal fraction greater than 0 and less than 1.",
            )
        elif living is None:
            _warning(
                warnings,
                "MISSING_TARGET_CAPITAL_INPUT",
                "Monthly living expense is missing; target capital and progress are null.",
            )
        else:
            uncovered_monthly = max(living - non_labor_income, Decimal(0))
            uncovered_annual_expense = uncovered_monthly * Decimal(12)
            target_capital = uncovered_annual_expense / withdrawal_rate
            if target_capital == 0:
                _warning(
                    warnings,
                    "ZERO_TARGET_CAPITAL",
                    "Target capital is zero; capital progress has a zero denominator and is null.",
                )
            elif strict_assets is None:
                _warning(
                    warnings,
                    "MISSING_TARGET_PROGRESS_ASSETS",
                    "Strict long-term investment assets are missing; capital progress is null.",
                )
            else:
                target_progress = strict_assets / target_capital

    metrics = {
        "total_assets": _money(total_assets),
        "current_liabilities": _money(current_liabilities),
        "ignored_future_interest": _money(ignored_future_interest),
        "net_worth": _money(net_worth),
        "asset_liability_ratio": _ratio(asset_liability_ratio),
        "living_safety_cushion_months": _ratio(living_runway),
        "essential_safety_cushion_months": _ratio(essential_runway),
        "property_assets": _money(property_assets),
        "property_concentration": _ratio(property_concentration),
        "net_available_liquid_assets": _money(liquid_assets),
        "broad_available_financial_assets": _money(broad_assets),
        "strict_long_term_investment_assets": _money(strict_assets),
        "debt_service_pressure": _ratio(debt_service_pressure),
        "debt_service_income_basis": income_basis,
        "broad_living_expense_multiple": _ratio(broad_multiple),
        "strict_living_expense_multiple": _ratio(strict_multiple),
        "target_capital": _money(target_capital),
        "target_capital_progress": _ratio(target_progress),
    }

    bases = {
        "monthly_living_expense": _money(living),
        "monthly_essential_expense": _money(essential),
        "monthly_debt_payment": _money(debt_payment),
        "essential_runway_monthly_outflow": _money(essential_outflow),
        "stable_monthly_income": _money(income),
        "stable_monthly_income_basis": income_basis,
        "annual_living_expense": _money(annual_living),
        "sustainable_monthly_non_labor_income": _money(non_labor_income),
        "uncovered_annual_living_expense": _money(uncovered_annual_expense),
        "withdrawal_rate": _ratio(withdrawal_rate),
        "net_available_liquid_asset_subtotal": _money(liquid_asset_subtotal),
        "net_available_liquid_liability_deduction": _money(
            liquid_liability_deduction
        ),
        "broad_available_financial_asset_subtotal": _money(
            broad_asset_subtotal
        ),
        "broad_available_financial_liability_deduction": _money(
            broad_liability_deduction
        ),
        "strict_long_term_investment_asset_subtotal": _money(
            strict_asset_subtotal
        ),
        "strict_long_term_investment_liability_deduction": _money(
            strict_liability_deduction
        ),
    }

    return {
        "schema_version": "1.0",
        "metrics": metrics,
        "calculation_bases": bases,
        "scope_notes": [
            "current_liabilities sums flagged principal only and excludes all future_interest",
            "net available liquid assets equal the flagged asset subtotal minus principal flagged subtract_from_net_available_liquid",
            "broad available financial assets equal the flagged asset subtotal minus principal flagged subtract_from_broad_available_financial",
            "strict long-term investment assets equal the flagged asset subtotal minus principal flagged subtract_from_strict_long_term_investment",
            "essential runway adds monthly debt payment unless essential_expense_includes_debt_payment is true",
            "wealth multiples use annual living expense as the denominator",
            "target progress uses strict long-term investment assets",
        ],
        "warnings": warnings,
    }


def _load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle, parse_float=Decimal, parse_int=Decimal)
    except OSError as exc:
        raise InputError(f"unable to read input JSON: {exc.strerror or 'file error'}") from None
    except json.JSONDecodeError as exc:
        raise InputError(
            f"invalid JSON at line {exc.lineno}, column {exc.colno}"
        ) from None


def _write_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Calculate deterministic household-finance metrics from a JSON file."
    )
    parser.add_argument("input_json", nargs="?", help="path to the input JSON file")
    parser.add_argument(
        "--example",
        action="store_true",
        help="print an anonymous example input and exit",
    )
    args = parser.parse_args(argv)

    if args.example:
        if args.input_json:
            parser.error("input_json cannot be used with --example")
        _write_json(EXAMPLE_INPUT)
        return 0
    if not args.input_json:
        parser.error("input_json is required unless --example is used")

    try:
        result = calculate_metrics(_load_json(Path(args.input_json)))
    except InputError as exc:
        _write_json({"error": {"code": "INVALID_INPUT", "message": str(exc)}})
        return 2
    _write_json(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
