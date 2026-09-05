# Consumption Behavior and Decision Thresholds

Apply `period-scope.md` first. Monthly averages, monthly drivers, budgets and recurring baselines below apply only when source coverage and purpose support them. Otherwise use selected-period totals and event or daily/weekly views; do not manufacture monthly inputs. Use `runtime.md` for calculation, persistence and output fallbacks; no hosted site is required.

Use this reference after the ledger is reconciled and before recommending spending controls. The goal is to add friction only where it changes decisions, not to make every small purchase cognitively expensive.

## 1. Use the correct evidence population

For purchase-decision psychology, analyze included rows with:

- `财务属性 = 消费费用`
- Positive original purchase amount
- Housing excluded only when the user requests a consumption-only view; state the scope
- Refunds, AA receipts, transfers, debt principal, investments, and income excluded from the decision-band population

Keep this gross positive-purchase view separate from net category spending. Reconcile the population by transaction count and amount before charting.

## 2. Design decision-oriented amount bands

Start with this candidate ladder when CNY transactions have enough coverage:

```text
≤50
50–100
100–200
200–300
300–500
500–700
700–1000
1000–2000
>2000
```

Adapt the outer bands to the observed distribution, but preserve finer resolution around the user's behavioral pressure zone. Never use `300–1000` as one band when it contains a material amount share or different purchase decisions.

For every band calculate:

- Transaction count and count share
- Gross positive amount and amount share
- Main categories and merchants
- Recurring versus one-off mix when supported

Identify the earliest band where count share is modest but amount share becomes material. Treat its lower edge as a candidate `关注线`; do not choose the threshold solely from a generic rule.

### Explain the “I already spend carefully” paradox

Do not infer overspending from a monthly average alone. Build a diagnosis that separates transaction frequency from financial impact:

- Show the count and gross positive amount share for every band side by side.
- State when numerous low-value transactions contribute little while a smaller medium-value cluster contributes most of the amount.
- Split `300–1000` into at least `300–500` and `500–1000` whenever that range is material; use finer bands when different decisions occur inside it.
- Reconcile band totals to gross positive non-housing consumption. Disclose refunds and AA offsets separately instead of allocating them back into purchase-size bands.

Also regroup net non-housing spending for diagnosis without changing the ledger category:

1. Decompose the monthly average into a small number of resource blocks that sum to the reported value.
2. Compare those blocks by month to identify the real drivers of high periods.
3. Add suggested roles such as `生活运行参考`, `可调整与体验`, and `周期性/项目支出` only as derived attributes.
4. When at least eight categories exist, plot or tabulate monthly amount against suggested controllability and prioritize high-amount, high-controllability areas.

A low-spending month or short-period average is a comparison reference, not a budget. Do not call spending high, low, affordable, or excessive without the user's income, savings target, and near-term commitments.

## 3. Calculate a personalized reference threshold

When current liquid assets and stable annual wage income are supported, show this book-derived behavioral reference:

```text
消费决策参考阈值
=（流动资产 + 稳定工资年收入 × 20）÷ 10,000
```

Requirements:

- State the currency and date of both inputs.
- State whether income is gross or take-home; prefer stable take-home income for a conservative operating rule when both are available.
- Exclude illiquid property and values marked missing or stale from liquid assets.
- Label the result `行为参考值`, not affordability, budget, or safe-to-spend capacity.
- Round down to a memorable CNY 50 or 100 increment when proposing an operating rule; show the unrounded result.
- Recalculate after a material income or liquid-asset change.

Use the formula as one signal. Compare it with the observed pressure band and the user's own regret history.

## 4. Set three levels of friction

### 关注线

Set near the lower edge of the first material pressure band. Trigger a 10-second check:

1. What problem does this solve?
2. What happens if I do not buy it now?
3. Do I already own a workable substitute?

### 慎重线

Use the personalized reference threshold, adjusted downward when the ledger shows a lower pressure band or repeated regret. Trigger:

- An overnight delay for non-urgent discretionary purchases
- Purpose, expected usage, and cheapest workable alternative
- A check against the monthly category or flexible-spending budget

### 小项目线

Use a memorable, user-confirmed threshold above the deliberation line. Do not hardcode one universal amount. Require a three-minute value case:

1. Objective: the concrete problem or result
2. Usage: expected frequency or duration
3. Alternative: existing, rental, used, or lower-cost option
4. Return: health, time, skill, relationship, or earning-capacity benefit
5. Exit: return, resale, cancellation, or maximum acceptable loss

A practical default is to require at least four of the five checks, plus a 24-hour delay, for non-urgent discretionary purchases.

Maintain explicit exceptions for emergencies, mandatory payments, and routine essentials already governed by a confirmed budget. The exception list must not become a catch-all.

## 5. Use investing as an optional consumption brake

For discretionary splurges, offer an optional rule: invest an equal amount when making the purchase. Apply it only after the safety reserve, debt obligations, and near-term goals are protected.

This rule exposes opportunity cost and reduces impulsive spending. It does not replace salary-date automated investing and must not encourage the user to invest money needed soon.

## 6. Diagnose the human driver

Classify the likely driver only when evidence or user confirmation supports it:

- Convenience or time saving
- Planned utility
- Health or relationship value
- Identity signaling or external validation
- Mood repair or self-reward
- Novelty and upgrade seeking
- Subscription inertia
- Scarcity, promotion, or fear of missing out

Do not moralize. The operating question is whether the purchase creates durable value relative to the next-best use of the same money.

For learning, equipment, or career spending, require a deliverable, usage plan, market signal, negotiation milestone, customer test, or revenue opportunity. Spending on self-improvement is not automatically an investment.

## 7. Review the habit next cycle

Track only observable, low-burden signals:

- Purchases reaching each threshold
- Purchases actually paused
- Purchases cancelled, downgraded, rented, bought used, or replaced
- High-value purchases with actual usage or deliverables
- Optional matched-investment executions

Do not estimate money "saved" from purchases the user never recorded. Compare threshold-band count and amount share with the prior comparable period, then keep, raise, or lower the thresholds based on decision quality and burden—not on guilt.

## 8. Store reusable user data safely

In the user-owned `财务状态_最新.json`, preserve:

- Threshold input values, dates, sources, and income definition
- Unrounded reference threshold and rounded operating thresholds
- Attention, deliberation, and project rules
- Exception list
- Most common confirmed behavioral drivers
- Prior-cycle habit results and next review date

Never store the user's personal values, merchant history, or thresholds inside the skill package.

Principle references:

- Nick Maggiulli, *Just Keep Buying*: automate continuous investing; treat equal-amount investing as a discretionary-spending brake.
- David Weng, *资产配置行动指南*: connect financial, physical, and human assets; use a personal decision threshold and reduce identity-driven consumption.
