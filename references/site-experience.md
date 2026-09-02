# Bookkeeping Site Experience

## Contents

1. Tool ownership
2. Site lifecycle
3. Data and privacy boundary
4. Source isolation
5. Information architecture
6. Visual benchmark
7. Decision quality
8. Validation

## Tool ownership

Use the installed Codex skills `sites:sites-building` and `sites:sites-hosting` instead of hand-authoring a standalone HTML report.

1. Read both Sites skill instructions before starting site work.
2. Keep site code in a dedicated site directory, never at the bookkeeping workspace root. Use `<approved-year-folder>/bookkeeping-site` when available; otherwise use `<active-workspace>/site/bookkeeping-<scope-key>`, where the scope key is `YYYY` or `YYYY-YYYY` for a cross-year period.
3. Read `.openai/hosting.json` before creating a site. Reuse its opaque `project_id` when present and never call `create_site` more than once for the same site.
4. Build and validate the complete site before hosting.
5. Push the exact validated source, save one version, deploy it privately, and wait for a terminal deployment result.
6. Return the deployed URL as the primary page deliverable and record it in the bookkeeping execution record.

## Site lifecycle

- Prefer one private Sites project per calendar year so each two-month cycle improves one durable financial-management product instead of creating disconnected pages. Before creating it, check the canonical site directory within the user-approved destination for `.openai/hosting.json`.
- For a period crossing calendar years, use one explicitly named cross-year scope such as `2026-2027`; do not silently reuse either annual project.
- Use a review route or state for source checks, duplicates, classification questions, receipts/refunds, and financial-profile changes.
- Use a report route or state for the finalized decision dashboard.
- After each meaningful user reply, update the ledger first, regenerate only unresolved review items, and deploy a new version to the same site.
- Do not present the report state as final until actionable pending items reach zero. If the user accepts unresolved items for temporary use, label every view `阶段性处理（含未决）`.
- Preserve the final Excel workbook as the detailed portable ledger. Treat the site as the analysis and decision layer.

## Data and privacy boundary

- Deploy privately by default. If only shared or public deployment is available, obtain explicit approval for the exact access level before publishing.
- Never upload raw statement files, screenshots, full account numbers, source credentials, or unmasked personal identifiers.
- Publish only the derived and masked fields needed for confirmation or analysis.
- Keep exact row-level detail in the Excel workbook by default. On the final site, prefer aggregate category views; include masked transaction detail only when it materially supports a decision.
- Keep the normalized ledger and evidence map in local audit artifacts. The site may consume a reviewed derived data file generated from the reconciled ledger and financial metrics; remove account identifiers, exact source paths, and fields not needed for the displayed decision.
- Use browser storage only for device-local draft answers or preferences. Do not treat browser state as the accounting source of truth.
- Commit a user's decision to the ledger only after the answer is returned through the conversation or another explicitly approved durable workflow.
- If the user declines the available shared or public access level, do not publish. Deliver the Excel workbook, retain the validated local site build, label online deployment as blocked by access choice, and ask for an approved hosting path.

## Source isolation

- Initialize Sites only inside the dedicated site directory. Do not place raw inputs, work files, OCR JSON, spreadsheets, PDFs, screenshots, full ledgers, audit records, or symlinks to them inside that directory.
- Copy in only reviewed derived data required by the UI. Treat every derived data file as publishable content and inspect it for names, account identifiers, exact locations, and unnecessary transaction detail.
- Keep the site repository limited to source code, dependency manifests and lockfiles, `.openai/hosting.json`, public assets, and explicitly reviewed derived data.
- Before pushing, inspect the exact committed file list. Fail the deployment if it contains bookkeeping source files or unexpected `.xlsx`, `.csv`, `.numbers`, `.pdf`, OCR, screenshot, ledger, or audit artifacts. Do not rely on `.gitignore` as the only safeguard.

## Information architecture

Build the first viewport around the current decision, not generic dashboard navigation.

### Review state

Show, in this order:

1. Period, checkpoint name, and reconciliation status
2. One explicit instruction describing what the user must do
3. Exact remaining question count
4. Questions with stable IDs, transaction evidence, reason for review, suggested answer, and answer controls
5. A copyable response summary
6. Completed or superseded state when no questions remain

Support filtering when the question count is large, but keep every unresolved item visible and countable.

### Final report state

Show, in this order:

1. Period, `记账完成度`, `财务复盘完成度`, and pending status
2. One-sentence verdict and the highest-priority next action
3. Net spending, monthly average, offsets, coverage, and monthly cash flow
4. Current asset and liability snapshot with evidence dates
5. Goal-to-asset-role map and near-term funding gaps
6. Resilience, solvency, concentration, and wealth-progress metrics
7. Changes since the prior confirmed snapshot
8. Prior-action review and the next two months' one to three actions
9. Category/resource allocation, budget pressure, and exceptional changes
10. Expandable masked detail, refunds/netting, assumptions, and audit basis

When the financial review is incomplete, keep the bookkeeping report final if its transaction checkpoints are resolved. Replace unsupported metrics with `待补资产快照` and name the missing evidence; never display old values as current.

### Diagnosis-first spending view

When the report includes consumption analysis, make the first spending section answer one concrete question such as “why is non-housing monthly spending still this high?” before showing detailed category tables.

1. Keep housing and other confirmed hard commitments in a separate cash-flow-floor section. Exclude them from adjustable-consumption rankings and state the exclusion.
2. Decompose the non-housing monthly average into three to six understandable resource blocks that add back to the displayed total.
3. Show which blocks drove each month. A low-spending-month comparison may be shown only as a dated reference, never silently labeled a budget or sustainable baseline.
4. Compare transaction count with gross positive amount by decision band. Make it visually obvious when many small transactions contribute less than a modest number of medium-value decisions.
5. Show an amount-versus-controllability view when at least eight meaningful categories exist. Label controllability, living-floor, adjustable, recurring, and periodic/project roles as suggestions unless confirmed by the user; never overwrite the ledger's consumption category.
6. Keep essential conclusions visible without hover. Put exact rows and audit detail below the diagnostic charts.
7. Do not judge whether spending is “high,” “safe,” or affordable without current income, savings goals, and near-term cash commitments. Explain composition and leverage instead.

## Visual benchmark

Match the quality bar of a polished Codex/ChatGPT product surface:

- Use a calm, modern, restrained visual system with strong typography, generous spacing, clear hierarchy, and accessible contrast.
- Prefer a neutral background, white or subtly tinted surfaces, one primary accent, and semantic green, amber, and red only where meaning requires them.
- Avoid generic dashboard chrome, dense sidebars, ornamental gradients, decorative charts, and unnecessary imagery.
- Keep the most important number and the next decision obvious within the first viewport.
- Use consistent radius, spacing, type, and number-format tokens across review and report states.
- Format currency and percentages consistently and align numeric columns for scanning.
- Use CNY/RMB for all bookkeeping amounts. Explicitly configure and verify the rendering runtime so a generic `currency` formatter cannot fall back to USD; check cards, axes, labels, tooltips, tables, expanded views, and exports.
- Make tables searchable or filterable when helpful, horizontally safe on narrow screens, and never the only way to understand a conclusion.
- Use accessible chart components or HTML/CSS-based visuals. Do not use hand-authored decorative SVG illustrations.
- Give every chart a title, unit, legend, direct labels where practical, and a short plain-language interpretation. Do not require hovering to read essential values.
- Support keyboard, touch, reduced-motion preferences, and mobile widths.
- Keep the social-preview image privacy-safe: reuse the site's palette and title treatment, but exclude amounts, merchants, personal names, exact dates, account data, and financial findings.

## Decision quality

Every insight must connect evidence to an action:

- State what changed or dominates.
- Quantify its effect.
- Distinguish fixed commitments from flexible spending.
- Recommend the smallest high-leverage adjustment or the next question to investigate.
- Show funding source, destination, amount or rule, timing, stop condition, and verification evidence for every action.

Do not reward mere transaction-count reduction. Optimize for clearer resource allocation, budget ownership, and better future decisions.

## Validation

Before deployment:

- Reconcile all displayed totals, counts, chart values, and percentages to the final ledger summary.
- Confirm stable question IDs and ensure answered questions no longer appear as pending.
- Confirm old, estimated, missing, and current financial values are visually distinct.
- Confirm no raw account identifiers or local file paths entered the site source or deployable derived data.
- Reconcile asset totals, current principal, cash-reserve deductions, goal amounts, and action values to local audit artifacts.
- Confirm links, routes, filters, copy controls, empty states, and keyboard labels are coherent.
- Confirm every displayed currency unit is CNY/RMB and no `$`, `USD`, or dollar-formatted fallback remains.
- Run the production build and fix every real failure.
- Validate narrow-screen behavior from the implementation and build output. Perform browser screenshots or interaction testing only when the user explicitly requests browser testing.
- Deploy the exact validated source and wait for successful status before sharing the URL.
