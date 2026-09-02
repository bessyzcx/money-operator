---
name: personal-bimonthly-bookkeeping
description: Set up a new user's account and transaction-source profile, then run an auditable two-month bookkeeping and financial operating-review cycle from wallet, marketplace, bank, card, spreadsheet, PDF, and screenshot data. Use for 首次启动、账户与账单来源盘点、整理账单、去重分类、预算审核、生成双月账本，或更新资产负债、目标与下一周期行动；使用私有确认页和决策报告，终稿交付 Excel 与在线报告链接。
---

# Personal Bimonthly Bookkeeping

Run an auditable two-month cycle that ends with a financial decision, not only a categorized ledger.

## Choose the operating mode

Before requesting statements, look in the active workspace for `记账配置_最新.json`.

- If it is missing, unreadable, belongs to another person, or the user says this is their first use, read `references/first-run.md` and complete first launch before Phase 1.
- If it exists, summarize the saved scope and source list in plain language. Ask only what changed, then update the workspace-owned profile.
- If the user only wants installation or orientation, point them to `用户工具包.md`; do not begin a bookkeeping run.

Never copy a prior user's source list, account names, budget, merchant rules, or financial values into a new user's profile.

## Operating principles

- Finish transaction correctness before drawing financial conclusions.
- Keep bookkeeping completion and financial-review completion as separate states. Missing asset data must not block a reconciled bookkeeping final.
- Separate `事实`、`假设`、`用户目标`、`建议` in every financial review.
- Use the user's goals, time horizon, income risk, and existing concentrations. Never impose a universal reserve size, withdrawal rate, or asset-allocation ratio.
- Separate housing and other hard commitments from adjustable consumption in comparisons, rankings, and behavior analysis. Treat them as the cash-flow floor unless the user explicitly requests another scope.
- Make the final dashboard explain why the result occurred and which decision could change it; do not stop at category totals and descriptive charts.
- Prefer three verified actions over a long advice list. Every action must name an amount or rule, source and destination, trigger or due date, stop condition, and next review date.
- Preserve source evidence and metric definitions so the next two-month cycle can explain what changed.

Close each cycle only after the outputs can answer:

1. Where did money go during the period?
2. Did net worth and financial optionality improve or weaken, and why?
3. Which risk or goal now deserves the next unit of money, time, or attention?
4. What are the next two months' one to three actions?
5. Were the prior actions completed, and did the intended metric change?

## Required workflow

### Phase 1: close the books

1. Determine the exact period, normally two full calendar months.
2. Load the confirmed source profile from `记账配置_最新.json`. Read `templates/source-checklist.md`, generate a checklist from that profile, and show it on the private review site. Do not add the example sources unless the user confirmed them.
3. Pause the formal full bookkeeping workflow if a required source in the user's profile is neither provided nor explicitly marked as having no transactions. Allow partial processing only when the user explicitly requests it, and label every output `阶段性处理`.
4. Inventory every attachment with original filename, format, period, and processing status.
5. Convert Numbers files, OCR screenshots, parse structured files, and normalize all sources.
6. Produce an internal unified ledger before classification. Report source counts, date range, and duplicate candidates on the deployed review site.
7. Read and apply `references/deduplication.md`.
8. Read and apply `references/classification.md`.
9. Update and privately deploy a focused confirmation page. Ask only about the cases specified in the classification reference.
10. Identify every included receipt/refund before calculating final net amounts.
11. Reconcile all confirmations. Generate the final workbook and privately deploy the decision-oriented report site using `references/outputs.md`.
12. Update reusable merchant rules and the bookkeeping execution record, including the deployed report URL.

### Phase 2: run the financial operating review

13. After the ledger is reconciled, read `references/financial-review.md`.
14. Look for the latest user-owned `财务状态_最新.json`, prior final workbook, or prior asset snapshot in the active workspace or user-approved destination. Never store personal values in the skill folder or deployable site source.
15. Read `templates/financial-profile.md`. On the same private review site, ask only for missing or changed items:
    - Current asset and liability balances with snapshot dates
    - Income, job stability, dependants, and near-term cash commitments
    - Goals that must not depend on market performance
    - Target reserve rule, asset roles, and investment automation rule
    - Changes since the previous review
16. Treat financial-review inputs as non-blocking for the bookkeeping final. If balances are missing, complete Phase 1 and label the financial section `待补资产快照` or `部分估算`; do not carry old balances forward as current facts.
17. Update three connected views:
    - Income and spending view from the reconciled ledger
    - Cash-flow view including debt service, transfers, and investment flows
    - Point-in-time asset and liability snapshot
18. Calculate only metrics supported by current data. Build an internal JSON input and run `scripts/calculate_financial_metrics.py`; preserve its input, output, and warnings as local audit artifacts. Show formulas, included accounts, snapshot dates, and confidence labels.
19. Compare with the previous confirmed snapshot and explain net-worth changes as operating surplus, debt-principal change, market/valuation change, other capital change, or scope adjustment.
20. Diagnose the highest-leverage gap across resilience, solvency, concentration, goal funding, and earning capacity.
21. Read `references/consumption-behavior.md`. Build the diagnosis-first consumption views: explain the non-housing monthly average as an additive composition, identify monthly drivers, separate the suggested living floor from adjustable and periodic/project spending, analyze decision-oriented transaction bands, and rank categories by amount and suggested controllability. Calculate a clearly labeled consumption-deliberation threshold only when supported.
22. Generate no more than three ranked actions for the next two months. Convert continuous-investing, consumption-friction, and asset-role principles into automation only after the user's safety reserve and near-term goals are protected.
23. Add the financial review, goal status, prior-action review, and new action tracker to the final workbook and the private report site. Update `财务状态_最新.json` and append the period to `财务复盘历史.csv` after user confirmation.

## Input handling

### Preferred transaction formats

- WeChat, Alipay, Meituan, JD: `.xlsx` or `.csv`; `.numbers` is acceptable when Numbers App is available.
- ICBC credit card: original `.csv`.
- Banks: original `.xlsx`, `.csv`, or text-readable `.pdf`.
- UnionPay and image-only statements: clear, continuous screenshots showing date, merchant, amount, and account.

Never ask the user to pre-delete repayments, transfers, refunds, salary, or duplicates. They are reconciliation evidence.

### Numbers conversion

On macOS, export each Numbers document separately through Numbers App to `.xlsx`.

- Export one document at a time. Parallel GUI exports can export the wrong front document.
- Verify the exported workbook title and first data rows before parsing.
- Keep converted workbooks in a dedicated build directory; do not overwrite originals.
- If Numbers App is unavailable, ask the user to export to `.xlsx` or `.csv` rather than attempting to decode `.iwa` files ad hoc.

### OCR

Use `scripts/ocr_images.swift` when Swift and Vision are available.

- Store raw OCR JSON as an audit artifact.
- Parse dates only from date-like lines with contextual markers such as weekdays. Do not treat amounts such as `79.11` as dates.
- Retain the screenshot filename on every OCR-derived row.
- Mark OCR-derived records for review when merchant or amount is uncertain.
- Cross-check OCR records against wallet and bank sources before including them.

## Normalized transaction schema

Every row must contain:

| Field | Meaning |
|---|---|
| 行ID | Stable local identifier preserved across rebuilds |
| 日期 | `YYYY-MM-DD` |
| 来源 | Recognized source label; allow new banks and payment channels |
| 商户 | Complete original merchant or best OCR reconstruction |
| 金额 | Positive = expense; negative = receipt/refund |
| 备注 | Original product, memo, or transaction description |
| 原始交易类型 | Original source transaction type |
| 支付方式 | Card, balance, wallet, or payment channel |
| 订单号 | Source order or transaction ID |
| 分类初稿 | Initial category |
| 最终分类 | Confirmed or rule-derived final category |
| 处理建议 | 建议纳入 / 建议排除 / 待确认后纳入 |
| 最终处理 | 纳入 / 排除 / 重复排除 / 待确认 |
| 待确认 | Specific reason requiring user input |
| 确认编号 | Stable question ID when user confirmation is required |
| 去重说明 | Kept source or excluded duplicate explanation |
| 决定依据 | Rule, evidence, or user answer supporting final treatment |
| 关联证据 | Product/order detail merged from linked or excluded source rows |

For the financial review, add separate derived fields when data supports them:

| Field | Meaning |
|---|---|
| 财务属性 | 消费费用 / 债务本金 / 利息税费 / 投资 / 内部转账 / 收入 / 其他资本变动 |
| 必要性 | 必要 / 可调整 / 不适用 / 待确认 |
| 是否一次性 | 是 / 否 |
| 口径说明 | Why the row differs between budget, cash-flow, and net-worth views |
| 决策金额区间 | Decision-oriented amount band based on positive original consumption amount |
| 决策层级 | 日常 / 提醒 / 慎重 / 小项目; derived from the user's confirmed thresholds |

Do not overwrite the user's consumption category with these accounting attributes.

## Accounting boundaries

Exclude from spending by default:

- Internal account transfers
- Credit-card repayments
- Salary, wealth-management movements, fund subscriptions, provident-fund account flows
- Deposit payments or returns when the user confirms they belong to a separate receivables ledger
- Records explicitly marked `不计收支`

Do not silently exclude:

- Refunds that should offset a spending category
- AA repayments
- Large personal transfers with unclear purpose
- Installment charges whose accounting period is unclear

For a mortgage payment, the budget view may show the full cash outflow as housing cost. The net-worth bridge must split principal from interest when evidence permits: principal reduces cash and debt; interest is an expense. If the split is unavailable, label the bridge incomplete instead of inventing it.

## Confirmation checkpoints

### Checkpoint A: source completeness

Do not begin the formal full bookkeeping run until every required transaction source in the user's confirmed profile is resolved. A generic platform list is not evidence of this user's sources. Optional financial-review inputs never block Phase 1.

### Checkpoint B: initial ledger and duplicates

Show total rows, source counts, date range, and duplicate candidates. Wait for confirmation before treating the ledger as final.

### Checkpoint C: focused classification questions

Ask only about:

- Personal transfers above the user's confirmed attention threshold, or materially large relative to this period when no threshold exists
- Transactions abnormally large for that user, merchant, or category
- First-seen unmatched merchants above the user's threshold, or material to the period when no threshold exists
- Platform merchants whose purchased item cannot be determined

### Checkpoint D: receipts and netting

List all included negative amounts and have the user label each as AA repayment, refund, deposit return, true income, wealth-management movement, or other.

### Checkpoint E: financial profile delta

After Phase 1 is resolved, deploy a short private form containing only missing or changed financial facts and goals. Allow `本期不更新资产` as a valid answer. Clearly state which analyses will remain unavailable.

## Draft and final output policy

- Use `sites:sites-building` and `sites:sites-hosting` for user-facing review pages and the final report. Read `references/site-experience.md` before site work.
- Treat the privately deployed site as the primary page deliverable. Produce an offline HTML export only when explicitly requested.
- Do not create a draft workbook unless explicitly requested or the site cannot preserve a required audit interaction.
- Make every confirmation view task-oriented: exact remaining count, stable IDs, evidence, suggested answer, and copyable response.
- After each user response, update the ledger first, rebuild only unresolved items, and deploy a new version to the same private site.
- Do not label an artifact final while actionable bookkeeping items remain.
- Phase 1 final deliverables remain `记账_MM-MM月_最终版.xlsx` and the private deployed URL for `预算审核报告_MM-MM月`.
- Enhance those same deliverables with asset, goal, and action sections when supported; do not create a disconnected advice report.
- Show `记账完成度` and `财务复盘完成度` separately.
- Reuse one Sites project for the approved scope, normally one calendar year. Reuse an existing opaque `project_id`.
- Deploy privately by default. Never publish personal financial data publicly without explicit approval of the resolved access level.
- Keep merchant rules, execution record, financial state, and history as local supporting audit artifacts, never inside the skill package or deployable site source.

## Quality checks

Before delivery:

- Confirm every source file is represented and the requested period is enforced.
- Reconcile duplicate exclusions, refunds, and bank/card totals where available.
- Scan for malformed OCR dates and impossible amounts.
- Verify formulas and render every workbook sheet at least once.
- Reconcile every displayed value and chart to the final summary; test routes, links, mobile width, labels, units, legends, copy controls, and keyboard labels.
- Verify every website currency surface—KPI, axis, tooltip, table, narrative, export, and expanded chart—renders CNY/RMB (`¥` or `CNY`), never a renderer's default USD.
- Run the production site build, deploy the exact validated source privately, and wait for deployment success.
- Verify facts, assumptions, goals, and recommendations are visibly separated.
- Verify every balance shows snapshot date, source, and confirmed/estimated/old/missing status.
- Verify future loan interest is not included in current liabilities.
- Verify debt principal, interest, consumption, repayment, and internal transfers are not double-counted.
- Verify two-month anomalies and one-off spending are not blindly annualized.
- Verify missing current balances do not appear as precise current metrics.
- Verify prior-period comparison uses the same scope or explains the scope change.
- Verify final actions are at most three, funded, measurable, and reviewable next cycle.
- Verify transaction-band charts reconcile to positive original consumption amount and disclose whether housing, refunds, transfers, and investment flows are excluded.
- Verify no broad band hides a material medium-value spending cluster; split `300–1000` at least into decision-useful sub-bands when that range is material.
- Verify consumption thresholds are dated recommendations derived from explicit inputs, not claims that the user can afford every purchase below them.
- Archive or clearly supersede stale drafts.

## Privacy

- Never include raw statements, account numbers, personal goals, or financial values in the skill package.
- Keep original inputs unchanged.
- Store generated artifacts only in the active workspace or a user-approved destination.
- Mask account numbers in summaries unless the final workbook requires an already-masked identifier.
- Keep every deployed bookkeeping site private by default and publish only derived, masked data needed for review or analysis. Never upload raw statement files.
- Keep the deployable site in the dedicated directory defined by `references/site-experience.md`; never initialize or commit a Sites project from the bookkeeping workspace root.

## Supporting resources

- Read `references/first-run.md` when no valid user profile exists, ownership or household scope changed, or the user asks to reconfigure sources.
- Read `references/deduplication.md` before matching duplicate transactions.
- Read `references/classification.md` before assigning categories.
- Read `references/outputs.md` before creating deliverables.
- Read `references/site-experience.md` before building or deploying a review or report site.
- Read `references/financial-review.md` before updating balances, goals, metrics, or actions.
- Read `references/consumption-behavior.md` before setting purchase thresholds, designing amount-band charts, or recommending spending-friction habits.
- Run `scripts/calculate_financial_metrics.py --example` to inspect the anonymous input contract, then use the script for supported metrics. Never replace a missing inclusion/deduction flag with an assumed `false`.
- Use `templates/source-checklist.md` at the start of every new period.
- Use `templates/first-run-profile.md` to guide a new user through setup without exposing the internal JSON schema.
- Use `templates/review-response.md` for transaction corrections.
- Use `templates/financial-profile.md` for the first financial review and later delta checks.
