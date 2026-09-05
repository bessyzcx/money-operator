---
name: money-operator
description: Reconcile messy personal or household statements from any date range or life event and produce traceable ledgers and spending insights. Use for 首次启动、任意时期或阶段账单整理、去重分类、收支核对、消费洞察及可选资产负债复盘。Adapt to the current AI's capabilities; no specific AI vendor or monthly cadence is required.
---

# Money Operator

Turn messy records into a ledger the user can trace and insights they can act on. Support a trip, a move, several weeks, irregular months, a year, or a historical backlog.

## First launch

Read `references/runtime.md` and `references/period-scope.md` before promising outputs. Confirm people, dates or event, currency, and the question to answer. Accept existing uploads and infer a proposed scope from them. No provider, plugin, or website host is mandatory.

Read `references/first-run.md` and use `templates/first-run-profile.md` when no user-owned profile is available in the workspace or attachments. Returning users only confirm changes. Never reuse another person's accounts, budgets, merchant rules, or values. If the user only wants setup, finish with a personalized preparation list; otherwise continue with supplied records.

## Reconcile records

1. Generate `templates/source-checklist.md` from the actual scope. Record requested dates and each source's coverage separately; missing records are not zero activity.
2. Inventory attachments by filename, source, format, dates, and processing status. Keep originals unchanged. Process available records even when others are missing; label results `已提供资料范围内` and list gaps. Do not claim complete household coverage without evidence.
3. Prefer XLSX/CSV, then supported PDF reading or OCR. If Numbers is unavailable, request an XLSX/CSV export. `scripts/ocr_images.swift` is an optional macOS helper; native image reading or another available OCR tool may substitute. Retain filenames and uncertainty on extracted rows. Check dates and amounts.
4. Read `references/deduplication.md`. Link order, wallet, and bank records, preserving duplicate exclusions. Do not ask users to delete transfers, repayments, salary, or refunds before reconciliation.
5. Read `references/classification.md`. Apply user-confirmed rules and categories. Without a budget, report actuals without an invented over-budget judgment.
6. Show source counts, date coverage, duplicate candidates, and proposed treatment. Use `templates/review-response.md` in chat, a file, or an available private surface. Ask only necessary questions about material ambiguity, transfers, unusual amounts, and unknown purchases.
7. Identify included receipts/refunds and distinguish AA repayments, refunds, deposits, income, investments, and transfers. Preserve unmatched and out-of-period links without silently changing the scope.
8. Apply answers and recompute totals using an actual calculation tool. If none is available, provide preparation/classification assistance and a continuation record; do not claim numerically verified results.
9. Read `references/outputs.md` and deliver the ledger, audit evidence, and insights in supported formats. Separate coverage gaps from unresolved decisions. Use `最终版` only for a declared scope with all actionable decisions resolved, prominently retaining any incomplete coverage label.

## Ledger contract

Keep these fields in the ledger or equivalent tables:

- 行ID、日期、来源、原始文件、商户、金额、币种、备注、原始交易类型、支付方式、订单号
- 分类初稿、最终分类、处理建议、最终处理、待确认、确认编号、去重说明、决定依据、关联证据

Keep stable row/question IDs. Dates use YYYY-MM-DD; positive amounts mean expense, negative amounts mean receipt/refund. Preserve source signs separately when needed. Unknowns remain unknown. Never sum currencies without a documented conversion basis.

Spending normally excludes internal transfers, card repayments, salary, investment movements, and confirmed separate deposits; retain them in cash-flow/audit records. Refunds and AA receipts may offset spending. Clarify unclear material transfers. Split mortgage principal from interest only with evidence: principal changes cash and debt; interest is an expense. A full-payment cash-outflow view must disclose its basis.

## Spending insights

After reconciliation read `references/consumption-behavior.md`. Quantify the largest supported drivers, recurring versus event spending, refund effects, and decisions dominating the amount. Separate housing and hard commitments from adjustable spending. Distinguish facts, inferences, and hypotheses; never invent regret or purchase value.

Apply `references/period-scope.md` to granularity and denominators. Trips, partial months, and missing-source records are not normal monthly baselines. Budget comparisons need a matching confirmed budget. Without comparable history describe the supplied period rather than a trend. End with at most three actions timed to the user's situation, not a fixed two-month cycle.

## Optional financial review

Missing assets/income never block spending insights. When requested, read `references/financial-review.md` and `templates/financial-profile.md`. Ask only for missing or changed dated balances, liabilities, income, goals, and commitments.

Run `scripts/calculate_financial_metrics.py` when Python is available; otherwise use its documented formulas in an actual calculation tool, retaining inputs, formulas, missing values, and warnings. Never claim the script ran if it did not. Its monthly inputs require independently supported monthly costs/income: do not pass an arbitrary-period total as monthly spending.

Keep spending, cash flow, and point-in-time assets distinct. Explain net-worth changes only between comparable dated snapshots. Show bookkeeping, coverage, and financial-review status separately. Save user-owned state after confirmation, or return a portable continuation record if persistence is unavailable.

## Delivery, privacy, and verification

Core outputs are a traceable ledger and supported insights. Excel is preferred when available; CSV/copyable tables and a text report are valid fallbacks. Read `references/site-experience.md` only for optional HTML/hosting. Missing hosting never blocks bookkeeping.

Save personal profiles, merchant rules, decisions, and balances outside this toolkit. Without filesystem persistence, return a continuation file/text for the user to save. Never claim cross-chat memory without evidence. Do not request passwords, verification codes, or full account numbers. Publishing needs approval of destination and access; an unlisted link is not proof of private access.

Before delivery reconcile source counts, included/excluded rows, duplicate removals, expenses, refunds, and net totals. Check boundaries, gaps, currencies, and pending decisions. Verify formulas and files with available tools, disclosing unavailable verification. Visual reports must match the ledger. Never invent downloadable files, deployed links, missing data, or successful tool runs.

For user setup see `用户工具包.md`. `START_HERE.md` contains a standalone chat workflow when the folder cannot be loaded.
