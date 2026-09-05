# Runtime adaptation
Use capabilities, not product names, to choose the workflow. SKILL.md and references are ordinary text instructions; agents/openai.yaml is optional display metadata, not a dependency.

Check available attachment reading, calculation/code execution, file export, and persistence. State the resulting mode briefly. With tools, verify them on a tiny non-sensitive table (10 + 20 - 5 = 25), and when exporting, reopen the produced file. Without tools do not pretend a self-description proves execution.

- File reading + calculation + export: produce a reconciled ledger and downloadable report; use Python helper when available.
- Reading + calculation, no file export: provide copyable CSV/tables and report text, split into numbered batches without silently dropping rows.
- Text/image reading only: guide setup, classify manageable supplied records, list ambiguity, and return a handoff. Totals are unverified until checked with a calculation tool; never call a large ledger final.
- Cannot read an attachment: request a supported export or pasted rows. Do not claim to have read it.

No persistent workspace: provide a user-owned continuation record with people, requested scope, coverage, confirmed rules, decisions, pending IDs, and processed batch IDs. The user saves it and supplies it next time. Do not depend on automatic chat memory.

No Python: use an available spreadsheet/calculation tool to reproduce formulas and retain evidence; no calculation tool means unsupported numerical metrics remain unavailable. No Swift/Vision: use available OCR/image reading and check uncertain amounts. No private hosting: return local HTML, Markdown/text, and ledger instead. Do not upload data just to reproduce the author's environment.

Read only relevant references; if they are inaccessible use the standalone START_HERE workflow and disclose the limitation. Never tell a user to install a nonexistent plugin or promise every AI supports the same outputs.
