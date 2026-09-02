# Output Requirements

## Contents

1. Process views
2. Summary metrics
3. Final Excel workbook
4. Final deployed report site
5. Final deliverables
6. Verification

## Process views: deployed site first

Use the private deployed Sites project as the default user-facing review surface. Keep normalized ledgers, OCR evidence, match results, and calculation tables as internal build artifacts until finalization. Do not use a standalone local HTML file as the primary review experience.

Create a separate route or progressively updated review view for each applicable checkpoint:

1. Source completeness
2. Duplicate candidates
3. Focused classification questions
4. Receipts/refunds and netting
5. Financial-profile delta

Each review view must:

- State the exact action the user must take.
- Display the exact unresolved item count.
- Use stable question IDs such as `Q01`.
- Show date, source, merchant, amount, original description, reason for confirmation, and a specific suggested response.
- Preserve entered answers when practical and provide a copyable response block.
- Regenerate with only unresolved items after answers are applied.
- Show a completion state when the remaining count reaches zero.
- Be deployed privately to the same Sites project after each meaningful checkpoint update.
- Show only the transaction detail necessary to answer the question. Mask account identifiers and personal names, and shorten sensitive merchant or location text when the omitted detail does not affect the decision.

Do not create a process-stage `.xlsx` unless the user explicitly requests it or the site cannot support a required audit task.

## Summary metrics

Show:

- Period
- Raw row count
- Included row count
- Excluded row count
- Actionable pending row count
- Source counts
- Category gross expenses, receipts/refunds, and net amount

Count pending rows only when they are not already excluded.

## Final Excel workbook

Name it `记账_MM-MM月_最终版.xlsx`.

Include at least:

1. `总览` or `说明与汇总`
2. Category and budget summary
3. Monthly trend
4. Included personal transaction detail
5. Excluded and duplicate audit
6. Full normalized audit ledger
7. User confirmation decisions
8. Source checklist/reconciliation

When financial-review inputs are available, also include:

9. `资产负债表`: prior and current snapshots, source dates, status, roles, and formulas
10. `净资产变动`: operating surplus, principal change, valuation change, other capital change, scope adjustment, and unexplained difference
11. `目标与行动`: goal funding status, prior-action review, and the next period's one to three actions
12. `指标历史`: append-only bimonthly metrics with stable definitions
13. `消费决策`: positive original consumption by decision band, count share, amount share, threshold rules, exceptions, and prior-period habit results when supported

If current balances are missing, keep the current fields blank and label them `待补资产快照`; never copy old values into a current column.

Retain original descriptions and processing decisions. Use filters, frozen headers, readable widths, typed dates and currency values, formula-driven summaries, and restrained colors.

## Final deployed report site

Title the report `预算审核报告_MM-MM月` and publish it to the existing private Sites project. Use `sites:sites-building` for implementation and validation, then `sites:sites-hosting` for deployment.

Include:

- Total included net spending
- Monthly average and period coverage
- Offset amount
- Pending amount and count
- Total row count
- Monthly gross-versus-net cash-flow visualization
- Category/resource-structure visualization
- A diagnosis-first explanation of the non-housing monthly average that reconciles its component blocks to the displayed total
- A monthly driver view that separates recurring living costs, adjustable spending, and periodic/project effects when supported
- Budget-pressure visualization for categories with budgets
- Two to four concise insights that identify the highest-leverage decisions
- A decision-oriented single-transaction amount chart when transaction detail is available. Use positive original consumption amount, show both transaction count and gross amount share, and split material medium-value ranges rather than defaulting to a broad `300–1000` band.
- An amount-versus-controllability view when category coverage is sufficient, with suggested roles clearly distinguished from confirmed facts
- Housing and other confirmed hard commitments shown as a separate cash-flow floor and excluded from adjustable-consumption rankings
- The user's current `关注线`、`慎重线`、`小项目线`, with derivation date, formula or evidence, exclusions, and the exact action triggered at each level
- Expandable category sections
- Category net amount and budget progress
- Aggregated category detail by default
- Masked transaction detail only when it materially supports a decision; keep the complete row-level ledger in Excel
- Separate pending and netting sections
- Separate `记账完成度` and `财务复盘完成度`
- Asset and liability snapshot with dates and evidence status when available
- Goal-to-asset-role map
- Resilience, solvency, concentration, broad financial coverage, and strict wealth-progress metrics with visible formulas
- Prior-period change explanation
- Prior-action review and no more than three funded, measurable actions for the next two months
- Compact assumptions and missing-data section

Visualizations must use final reconciled values, show labels and units, remain readable on mobile widths, and link to relevant detail sections when useful. Prefer decision-support views over decorative charts. Follow `site-experience.md` for information architecture, visual direction, privacy, and deployment lifecycle.

Do not show an opaque overall financial grade. A traffic light is allowed only when its condition and user-selected target are visible.

Do not present a classification draft as final. The final report must show zero actionable pending items. If the user accepts unresolved items for temporary use, label the site and workbook `阶段性处理（含未决）` and do not call either artifact final.

## Final deliverables

After user confirmation, generate:

- `记账_MM-MM月_最终版.xlsx`
- A private deployed URL for `预算审核报告_MM-MM月`

Create an offline `.html` export only when the user explicitly asks for one. Also update the merchant/category rules and execution record as supporting audit artifacts, including the deployed URL. Do not substitute them for the two user-facing final deliverables.

When Phase 2 is confirmed, also update local supporting artifacts:

- `财务状态_最新.json`: current goal profile, definitions, snapshot provenance, and open actions
- `财务复盘历史.csv`: one comparable row per period

Store them only in the approved bookkeeping workspace; never put them in the site repository.

## Verification

- Verify every review-view heading count against its embedded rows.
- Confirm all internal links, routes, and anchors resolve.
- Confirm answered questions no longer appear as pending.
- Inspect key workbook ranges and formulas.
- Scan for formula errors.
- Render every sheet once and correct clipping or unreadable columns.
- Verify the report-site totals and plotted values against the final summary.
- Verify the displayed budget basis and period-adjusted budget for every utilization percentage.
- Verify responsive layout, visualization labels, keyboard-accessible controls, expandable details, and totals.
- Verify every financial metric shows snapshot date, scope, formula, and evidence status.
- Verify old, estimated, and missing balances are visibly distinct from confirmed current facts.
- Verify remaining loan principal excludes future interest.
- Verify the net-worth bridge does not double-count debt principal, consumption, transfers, or investments.
- Verify user goals and assumptions are not presented as facts.
- Verify final actions include source, destination, amount/rule, timing, stop condition, next review date, and evidence.
- Verify decision bands total to the stated positive original consumption population and that count share and amount share use the same denominator.
- Verify diagnostic resource blocks reconcile to non-housing net spending and low-spending-month references are not labeled as budgets.
- Verify all site and export currency formats are explicitly CNY/RMB across cards, charts, axes, tooltips, tables, and expanded views; fail validation if USD appears.
- Verify threshold habits are assessed by observable behavior such as pauses, cancellations, substitutions, usage, or deliverables; do not invent savings from unrecorded purchases.
- Run a successful production build, deploy the exact validated version privately, and wait until deployment succeeds.
- Archive or clearly supersede stale process drafts after finalization.
