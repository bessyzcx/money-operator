# Classification Rules

## Rule ownership

Classification rules belong to the current user, not to the skill author. Apply sources in this order:

1. The user's confirmed category or budget file.
2. The user's saved merchant rules from a prior cycle.
3. Explicit product, order, or memo evidence in the current statements.
4. A neutral starter taxonomy.

Never import merchant examples, category exceptions, thresholds, or budgets from another user's workspace.

## Neutral starter taxonomy

Use this only when the user has no existing taxonomy. Keep it broad in the first pass and split a category only when the data or a decision requires it.

| Category | Typical evidence |
|---|---|
| 居住 | 房租、住房贷款利息、物业、水电燃气 |
| 餐饮与食材 | 餐厅、外卖、超市、生鲜；金额足够大时可拆分“外食”与“食材” |
| 交通 | 公共交通、网约车、铁路、停车、加油、租车 |
| 日常生活 | 日用品、通信、小额便利消费 |
| 医疗与保障 | 医院、药房、体检、保费 |
| 教育与成长 | 课程、书籍、职业资格、学习订阅 |
| 娱乐与旅行 | 影音、游戏、景点、住宿、度假 |
| 家庭与人情 | 抚养、宠物、礼物、人情往来；根据用户家庭情况拆分 |
| 购物与数字服务 | 服饰、数码、软件、会员、云服务 |
| 税费与利息 | 税款、手续费、非住房贷款利息 |
| 一次性/项目 | 装修、搬家、婚礼、大额医疗等不应盲目年化的支出 |
| 待确认 | 证据不足，且会影响决策的交易 |

## Special rules

- Use the purchased item, order title, or memo before the platform name. A marketplace, super-app, or payment processor is not a spending category.
- Do not automatically classify mixed retailers or marketplaces without item evidence when the amount is material.
- Flag personal transfers using the user's confirmed threshold. If none exists, rank transfers by materiality and ask only about those that could change the period conclusion.
- Deposit expense: wait for confirmation, then exclude if tracked in a separate receivables ledger.
- Moving, renovation, or other one-off items: create a separate category and do not compare with the annual operating budget.

## Receipt handling

Negative amount means receipt/refund in the normalized ledger. Do not automatically net it unless its nature is known.

| Receipt type | Treatment |
|---|---|
| AA repayment | Offset the associated spending category |
| Refund | Offset the original category |
| Deposit return | Offset or exclude according to the receivables ledger rule |
| True income / salary | Exclude from the spending report |
| Wealth-management movement | Exclude |
| Unknown receipt | `待确认后纳入` |

## Budget source

Use only a user-confirmed budget file, explicitly stated target, or prior confirmed profile. If no budget exists:

- Show actual amount and share, not budget utilization.
- Do not label a category over budget.
- Offer to turn the first clean period into a baseline after the user reviews one-off items; do not silently call actual spending a target.

## Budget normalization

Calculate budget pressure only against a matching user-confirmed budget and disclose the basis. For partial/event scopes, obtain the user's intended allocation before applying any proportional rule below; otherwise show actuals without utilization. Missing sources never establish full budget coverage.

1. Count fully covered calendar months. Only if daily proration is confirmed, use covered days divided by calendar days for a partial month; never prorate fixed bills or an event budget automatically.
2. Monthly budget: `user-confirmed monthly budget × fully covered calendar months` only for matching full-month scope. For partial dates, events, missing sources or disjoint segments, apply `period-scope.md`; do not automatically prorate or count every touched month as a full month.
3. Quarterly budget: `quarterly budget × covered months ÷ 3`.
4. Annual budget: calculate each calendar year's covered share as `annual budget × covered months in that year ÷ 12`, then sum the shares.
5. Observation or Separate: show `无预设预算`; do not calculate a utilization percentage or mark it over budget.
6. Compare category net spending after confirmed refunds and AA offsets with the adjusted budget. Also show gross spending when offsets materially change the conclusion.
7. Do not assume unused budget carries forward across periods unless the user defines that rule.
8. Label accepted but unresolved items separately; never let them silently change the budget-pressure result.
