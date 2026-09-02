# Financial Operating Review

Use this reference only after the transaction ledger is reconciled. The objective is to connect the user's three financial views to goals and the next two months of resource allocation.

## Contents

1. Evidence contract
2. Maintain the three views
3. Core metrics
4. Goal and asset-role map
5. Convert books into execution rules
6. Convert consumption evidence into a behavioral system
7. Rank no more than three actions
8. Output structure
9. Common errors

## 1. Evidence contract

Keep four blocks visibly separate:

| Block | Allowed content |
|---|---|
| 事实 | Dated, sourced, verifiable balances, income, and spending |
| 假设 | Valuation method, included accounts, annualization, target scenarios |
| 用户目标 | Desired runway, time horizon, future cash need, risk budget |
| 建议 | Actions derived from the gap between facts and goals |

For every balance record:

- Snapshot date
- Account or asset
- Asset/liability class
- CNY value and original currency when applicable
- Source
- Liquidity or restriction
- Goal/role
- Status: `已确认` / `估算` / `沿用旧值` / `缺失`
- Valuation method and valuation date for property or other non-traded assets

Never silently present an old or estimated value as current.

## 2. Maintain the three views

### Income and spending view

Use the reconciled ledger to show operating income and expenses. Report refunds and AA netting explicitly. Separate recurring operating spending from one-off spending.

Do not calculate savings from gross salary minus spending. Use net take-home income when available, and label the denominator.

### Cash-flow view

Show actual cash inflows and outflows, including debt service, internal transfers, and investment contributions. Internal transfers and investments affect cash location, not operating profit.

### Asset and liability snapshot

Use one stated snapshot date, ideally the last day of the two-month period.

- Include current assets at a supported value.
- Include liabilities at outstanding principal plus accrued amounts already owed.
- Exclude future scheduled loan interest from current liabilities.
- Track future interest or committed payments separately when useful.
- Include owner-occupied property in net worth, but do not include it in wealth-freedom capital without an explicit monetization plan.

Reconcile:

```text
期末净资产 = 期末总资产 - 期末总负债

净资产变动
≈ 经营结余
+ 债务本金变化的勾稽调整
+ 市场或估值变化
+ 赠与等其他资本变动
+ 统计范围或口径调整
```

Do not force the bridge to zero when source coverage is incomplete. Show the unexplained difference and what evidence is missing.

## 3. Core metrics

Calculate only supported metrics. Show formula, numerator, denominator, date, and confidence.

Create an internal JSON file and run:

```text
python3 scripts/calculate_financial_metrics.py <input.json>
```

Inspect the anonymous schema with `--example`. Set every asset inclusion flag and liability deduction flag explicitly. Preserve the script's `warnings`; a `null` metric means the report must show `不可可靠计算`, not a hand-filled estimate. Keep snapshot dates and evidence status alongside the script input because they are presentation and audit fields rather than calculation inputs.

### Resilience

```text
净可用流动资金
= 可快速变现且不受限的现金类资产
- 已指定给短期目标的资金
- 近期必须支付且未包含在月度基线内的款项

现金安全垫月数
= 净可用流动资金 ÷ 月度支出基线
```

Prefer a trailing six-month spending baseline. If only two months exist, label it `临时估算` and list annual or irregular costs not captured.

When classifications support it, show both:

- Current-lifestyle runway
- Minimum-lifestyle runway using user-confirmed essential expenses, mandatory debt payments, essential insurance, and annual necessary costs divided by 12

The user chooses the target runway based on income stability, dependants, insurance, and risk tolerance. Do not hardcode a universal number.

### Solvency and debt service

```text
资产负债率 = 期末总负债 ÷ 期末总资产

月度偿债压力 = 月度必须偿还的本金及当期利息 ÷ 稳定月收入
```

Keep the two ratios separate. State whether income is gross or take-home. Do not call asset-liability ratio `DTI`.

Always show:

- Consumer/revolving debt separately from mortgage principal
- Mortgage loan-to-value when current property value and related principal are supported
- Interest rate and early-repayment terms before recommending mortgage prepayment

### Concentration

```text
房产总资产集中度 = 房产市值 ÷ 家庭总资产

房产净权益集中度
=（房产市值 - 对应贷款本金）÷ 净资产

单一经济风险敞口
= 最大单一底层风险 ÷ 对应资产池
```

State the denominator. Merge overlapping funds or accounts when they represent the same underlying economic exposure. Consider correlation between career income, city, property, and local investments.

Do not apply a universal warning threshold. If possible, derive a risk budget:

```text
可接受最大敞口比例
≈ 用户可承受的净资产损失比例 ÷ 压力情景跌幅
```

### Wealth-freedom progress

Start with the user's desired lifestyle, not a generic retirement number.

Show fact-based multiples before any return assumption:

```text
广义金融覆盖倍数
= 可用金融净资产 ÷ 目标年度净支出

严格财富自由倍数
= 严格长期投资净资产 ÷ 目标年度净支出
```

For the broad measure, disclose whether cash reserve, restricted retirement assets, or other accounts are included. For the strict measure, exclude the independence reserve, money assigned to goals within three years, owner-occupied property without a monetization plan, vehicles, receivables, and assets unavailable within the target horizon.

Optionally show scenario progress:

```text
目标资本 = 尚未被稳定非劳动收入覆盖的年度支出 ÷ 用户选择的提取率

资本进度 = 可用于该目标的净投资资产 ÷ 目标资本

现金流覆盖率
= 可持续税后非劳动收入 ÷ 目标年度净支出
```

Treat the withdrawal rate as a user-selected scenario, never a fact or guarantee. Disclose which accounts are included. Do not count the same asset once as capital and again through its full income stream.

### Wealth-building capacity

When data supports it, show:

- New financial assets added during the period
- Planned versus completed long-term contribution
- Take-home operating surplus after one-off items
- Career-capital spend or time commitment if the user tracks it
- Income-source concentration and known job-risk changes

Do not equate more spending on courses or equipment with higher earning power. Tie career capital to a deliverable, market signal, or revenue opportunity.

## 4. Goal and asset-role map

For each goal, record:

| Field | Requirement |
|---|---|
| Goal | Specific outcome |
| Amount | Current estimate or `待定义` |
| Date/horizon | When the money is needed |
| Market dependency | Must not depend on market / may fluctuate |
| Funding account | Current asset or account |
| Current amount | Dated value |
| Gap | Amount and/or time gap |
| Funding rule | Monthly amount, trigger, or percentage |
| Review rule | Next date or change trigger |

Assign every material asset one primary job:

- Daily liquidity
- Independence/emergency reserve
- Near-term goal
- Stability/rebalancing
- Long-term growth
- Restricted retirement/provident fund
- Owner-occupied use
- Receivable or other special purpose

Flag money without a job, one asset serving incompatible goals, and market assets assigned to a goal that must not fluctuate.

## 5. Convert books into execution rules

Use these as principles, not product recommendations:

### Continuous buying

- Build a regular contribution from stable surplus after the safety reserve and near-term commitments are protected.
- Prefer diversified income-producing assets suited to the goal and horizon.
- Do not make the main investment process depend on market news, predicting a bottom, or willpower.
- Treat a spend-triggered rule such as “spend over X, invest Y” as a consumption brake only. It cannot replace the salary-date automation.
- In early accumulation, compare the value of improving earning power with the value of optimizing portfolio returns.

### Asset allocation as a system

- Start from the three financial views, human-capital risk, goals, and asset roles.
- Use low correlation and diversification to reduce dependence on one outcome.
- Add foreign-currency or global assets only when they serve diversification or a real future liability; disclose currency risk.
- Reject claims of simultaneously high return, high safety, and high liquidity.
- Set allocation from the user's horizon, loss capacity, and current concentrations. Never copy a fixed model portfolio into the skill.

Principle references:

- Nick Maggiulli, [Just Keep Buying](https://ofdollarsanddata.com/just-keep-buying/)
- Caixin summary of David Weng's book and the personal “three statements”: [有多少钱才能做资产配置？](https://mini.caixin.com/2026-03-07/102420425.html)
- Investor.gov, [Asset Allocation and Diversification](https://www.investor.gov/introduction-investing/getting-started/asset-allocation)
- CFPB, [An essential guide to building an emergency fund](https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/)

## 6. Convert consumption evidence into a behavioral system

Read `consumption-behavior.md`. Keep three concepts separate:

- `关注线`: the earliest material amount band; prompt a quick purpose check.
- `慎重线`: a personalized deliberation threshold; add time delay and alternatives.
- `小项目线`: a user-confirmed large discretionary threshold; require a short value case.

Do not optimize for the fewest transactions. Reduce low-value or identity-driven spending while preserving spending that protects health, relationships, time, or earning capacity. Treat career-capital spending as an investment only when it has a deliverable, usage plan, market signal, or revenue test.

Store the threshold inputs, formula, rounded operating rule, date, and exclusions in the user-owned financial state. Recalculate when income or liquid assets materially change. Never store personal threshold values in the skill package.

## 7. Rank no more than three actions

Generate candidates, then rank by:

```text
优先级
≈ 下行风险降低程度 × 紧迫性 × 可控性 ÷ 执行成本
```

Use this order:

1. Prevent cash depletion, missed payments, or forced selling.
2. Address expensive debt or an unmanaged concentration.
3. Automate funding for the highest-priority long-term goal or fill a decision-critical data gap.

When no safety or solvency item is urgent, compare an investment action with an earning-capacity action. Choose the one with the stronger expected effect on the user's market pricing or long-term funding capacity. Accept a career-capital action only when it names a deliverable, market signal, negotiation milestone, customer, or revenue test.

Every final action must contain:

```text
动作
负责人
资金来源
资金去向
金额或比例
触发日或截止日
停止条件
下次复核日
验收证据
```

Reject vague actions such as `多储蓄`、`少消费`、`分散投资`、`提升自己`.

## 8. Output structure

In the final private report site, show in this order:

1. One-sentence verdict
2. Bookkeeping and financial-review completeness
3. Period cash-flow and spending decisions
4. Current asset and liability snapshot
5. Goal progress and asset roles
6. Resilience, solvency, concentration, and wealth progress
7. Changes since the prior snapshot
8. The next two months' one to three actions
9. Consumption decision bands and threshold-habit review when supported
10. Assumptions, missing data, formulas, and risk notice

Use traffic lights only when the condition is transparent. Do not assign an opaque overall score or grade.

## 9. Common errors

- Mixing a two-month cash-flow period with an undated asset balance.
- Treating remaining principal plus all future interest as current liabilities.
- Counting mortgage principal as both consumption and net-worth loss.
- Counting credit-card purchase and repayment as two expenses.
- Treating gross income minus spending as savings.
- Treating credit limits, locked funds, or high-volatility assets as emergency cash.
- Annualizing an abnormal two-month period without adjustment.
- Using a stale property estimate as a current fact.
- Counting owner-occupied property in freedom capital without a monetization plan.
- Assuming many accounts means diversified underlying risk.
- Setting the same reserve months or asset ratio for every user.
- Carrying the previous balance forward without an `沿用旧值` label.
- Producing many generic suggestions instead of reallocating actual resources.
- Treating `300–1000` as one band when it hides a material medium-value cluster.
- Using net spending after refunds to analyze purchase-decision psychology; use positive original consumption for decision bands and show net spending separately.
- Turning a book formula into an affordability guarantee or a universal threshold.
- Applying approval friction to emergencies, mandatory payments, or routine essentials already covered by a budget.
