# First launch

Use this flow before processing any statements when the workspace has no valid user-owned profile.

## Outcome

Create `记账配置_最新.json` in the active workspace or a user-approved private destination. It must describe whose money is in scope, the recurring transaction sources, how they connect, and which sources are required for a complete period. Do not store balances, transaction data, full account numbers, passwords, identity numbers, or statement passwords in this file.

## Conversation design

Treat the user as unfamiliar with bookkeeping and file formats.

1. Explain in one sentence: first launch builds a personal source map so future cycles do not depend on a generic checklist.
2. Use `templates/first-run-profile.md`. Ask for ordinary-language answers; accept screenshots of an app or bank-account list when the user cannot name every source.
3. Do not ask the user to identify duplicate rules, accounting categories, or data schemas. Infer the likely payment chain and show it back for confirmation.
4. Ask only a second round for gaps that could cause missing or double-counted transactions.
5. Mask identifiers to a user-recognizable label such as `招行信用卡••1234`. Never request a full card or bank-account number.

## Source-map rules

Separate three layers:

- `transaction_sources`: sources that may contribute ledger rows, such as wallets, shopping platforms, banks, cards, cash logs, or family reimbursements.
- `cross_check_sources`: sources used only to verify completeness because another source usually has richer transaction detail.
- `financial_snapshot_sources`: balances used only for the optional asset and liability review.

For every transaction source record:

- friendly masked name and source type
- included person or household role
- normal export format, or `unknown`
- whether it is required every period
- likely payment relationship to another source
- active, newly added, or retired status

An order platform and its payment wallet may both be required even when they overlap; this helps deduplication. A source is `cross_check_only` only after the user confirms the main transaction detail exists elsewhere.

## Minimum profile contract

The exact JSON shape may evolve, but preserve these top-level meanings:

```json
{
  "profile_version": 1,
  "owner_label": "本人",
  "household_scope": ["本人"],
  "base_currency": "CNY",
  "default_cycle": "two_full_calendar_months",
  "transaction_sources": [],
  "cross_check_sources": [],
  "financial_snapshot_sources": [],
  "classification_preferences": {
    "existing_category_file": null,
    "attention_threshold_cny": "unknown"
  },
  "budget_preferences": {
    "budget_file": null,
    "comparison_enabled": false
  },
  "privacy": {
    "mask_account_identifiers": true,
    "private_site_only": true
  },
  "confirmed_at": "YYYY-MM-DD",
  "needs_review": []
}
```

Do not invent missing values. Use `unknown` or add the item to `needs_review`.

## Confirmation and handoff

Show a short summary before saving:

- Who is included
- Which sources must be provided each period
- Which sources are cross-check only
- Which formats the user already knows how to export
- What remains unknown

Ask whether the user already has a category list or budget only as an optional final item. If not, use a neutral starter taxonomy and report actuals without an over-budget judgment. Never inherit the package author's budget or merchant history.

After confirmation, save the profile outside the skill folder, generate the first period's checklist from it, and continue to Phase 1. If the user is not ready to collect files, stop after giving a personalized preparation list; first launch is still complete if the source map is confirmed.

At each later cycle, ask `这期有没有新增或停用的账户？` before relying on the saved profile.
