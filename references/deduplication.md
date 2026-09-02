# Deduplication Rules

## General principle

Keep the record closest to the consumption event, while retaining enough source detail to audit why another row was excluded.

Before excluding a duplicate that contains richer order or product detail, merge that detail into the kept row's `备注` or `关联证据`. Preserve the linked source, linked row ID, order ID when present, original description, and matching basis. Never let deduplication make the kept transaction less classifiable or less auditable.

## Explicit rules

| Situation | Keep | Exclude |
|---|---|---|
| Meituan order paid by WeChat | WeChat, enriched with the Meituan order/restaurant title | Meituan after its detail is linked |
| Meituan order paid by UnionPay or card | Meituan when it contains the order/restaurant detail | Generic bank/card row |
| JD purchase paid through Alipay | Alipay, enriched with the JD product description | JD after its detail is linked |
| JD detail vs generic bank/card merchant | JD when it contains item detail | Generic bank/card row |
| Bank row duplicates WeChat/Alipay | WeChat/Alipay | Bank row |
| UnionPay screenshot duplicates card/bank row | Source with clearer merchant detail | Generic duplicate |
| Same purchase exists in multiple sources | Most consumption-proximate and descriptive source | Other copies |

## Matching strategy

Use a tiered approach:

1. Exact order or transaction ID.
2. Same date, exact absolute amount, compatible payment channel.
3. Adjacent date, exact amount, matching merchant/payment account.
4. Same date and near amount only when a known discount or card rebate explains the difference.

Do not deduplicate solely because two unrelated rows share a date and amount. Mark ambiguous matches as duplicate candidates.

## Recommended source priority

Source priority depends on context rather than one universal ranking:

- WeChat and Alipay generally outrank bank/card rows.
- JD outranks a generic card row when JD contains the purchased item.
- For Meituan paid by WeChat, WeChat outranks Meituan per the user's SOP.
- For Meituan paid directly by UnionPay/card, Meituan may outrank a generic bank row.
- OCR rows should not outrank a clean structured wallet row unless OCR supplies materially better merchant detail and the structured source is only a generic channel label.

## Required audit fields

For every excluded duplicate, populate `去重说明` with:

- Kept row ID and excluded row ID
- Kept source
- Kept merchant
- Matching date and amount
- Matching basis, such as exact ID or same-day exact amount
- Detail copied into `关联证据`
