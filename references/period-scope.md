# Arbitrary dates and event scope
This reference controls all period-dependent instructions elsewhere. Monthly views in other references are conditional, never a required cadence.

Confirm a start/end date (inclusive), or event label and inferred dates. Unknown boundaries remain unknown until resolved. Store requested scope independently of actual source coverage; minimum/maximum transaction dates do not prove export coverage. Support cross-year intervals and multiple disjoint batches. Ask whether an event includes only event spending or all spending during those dates.

Record per source: export start/end, covered segments, missing segments, known no-activity segments, and selection filters. Combine overlapping exports without duplicating transactions. Gaps are not zeros. Process available data with visible coverage caveats.

Use totals first. Choose daily/weekly/monthly/event categories only when informative. A short trip needs event categories, not a monthly trend. If comparing periods, disclose differences in duration, accounts, currency, and purpose. Compare like-for-like subsets or decline the trend claim.

For whole, fully covered calendar months, monthly mean = total / number of complete months. For partial/disjoint/event coverage do not call total / 2 a monthly average, and do not use the count of calendar months touched as denominator. A daily rate is permitted only with known covered days and scope; disclose denominator. Optional monthly equivalent = daily rate × 365.2425 / 12, labeled an extrapolation, never sustainable spending. Avoid extrapolating event-only or incomplete-source data.

Monthly calculator inputs require an independently supported representative baseline, not merely this run's total. Leave unsupported inputs missing. Preserve actual snapshot dates and do not roll older balances to the interval end.

Budget comparison requires matching scope and dates. Prorate only if the user confirms that rule; fixed bills and event budgets are not automatically daily costs. Link refunds outside scope as evidence, separately show in-period cash flow and optional event net cost, and never count the same refund twice.

Use filenames with years and dates: 记账_2026-08-17_2026-09-05_最终版.xlsx and 账单洞察_2026-08-17_2026-09-05.md. For disjoint coverage use a safe event/run label and list exact segments inside. Unresolved decisions use 阶段性 rather than 最终版. A reconciled subset may be final only for its explicitly declared scope and must retain 已提供资料范围内 and the coverage gaps. Follow-up timing is user-selected or action-specific, not automatically monthly/bimonthly.

Validation examples:
- Aug 17–Sep 5 is 20 inclusive days, not two complete months.
- Dec 20–Jan 10 spans years; filenames retain both years.
- January + March exports do not establish February coverage.
- A 10-day trip is not a sustainable monthly living-cost baseline.
