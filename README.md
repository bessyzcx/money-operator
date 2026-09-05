# Money Operator
### 把混乱账单，变成看得懂的账本和用得上的洞察。
### Turn messy statements into a clear ledger—and useful next steps.

[中文](#中文) · [English](#english) · [立即开始 / Start here](./START_HERE.md)

## 中文
不用等月底，也不用养成每天记账的习惯。一次旅行、搬家、几周开销、跨年流水，或积攒很久的旧账，都可以从现有资料开始。

Money Operator 是一套可交给 AI 执行的账单整理流程与工具包。它先弄清你的范围和来源，再合并、去重、分类、核对，解释钱花在哪里、哪些决策值得关注。

### 你会得到什么
- **能核对的账本**：消费不重复，退款有去向，每笔处理有依据。
- **看得懂的洞察**：主要支出、事件影响、固定负担和可调整开销。
- **少而具体的行动**：最多三件下一步值得做的事。
- **可续接的记录**：下次继续旧账或补新资料，不必重讲全部规则。

账本优先导出 Excel/CSV；工具不支持导出时提供可复制表格。报告可直接在对话里阅读，也可输出文件。在线网站是可选增强，不是使用门槛。

### 现在开始，无需先安装
1. 打开 [开始指令](./START_HERE.md)，复制到你正在用的 AI。
2. 告诉它想整理哪段日期、哪个事件，或直接上传已有账单。
3. 跟着回答少量必要问题，先拿到资料盘点和个人来源清单。

例如：
> 帮我整理 2026 年 8 月 17 日到 9 月 5 日的账。我主要用微信和信用卡，想知道搬家到底花了多少。先看已有文件，缺什么再告诉我。

### 首次使用：先认识你的账
AI 会确认这次算谁的钱、日期或事件范围、想解决的问题，以及支付 App、购物平台、银行卡和现金等来源。记不清可以说“不确定”，不需要懂财务术语。

每次按本次范围确认来源，不默认你使用某个平台。能保存文件时生成私人配置；不能保存时交给你一份续接记录，下次再上传。不会要求密码、验证码或完整卡号。

### 怎么准备资料
首选银行或平台导出的 Excel（.xlsx）或 CSV；其次是可读 PDF、清晰截图。Numbers 文件若当前 AI 无法读取，请先导出 Excel。
- 尽量让不同来源覆盖同一段日期；有缺口也可以先开始。
- 保留退款、转账、还款和重复记录，由 AI 判断，不必预清洗。
- 截图保留日期、商户、金额，遮住完整账户信息。
- 资产、贷款余额和收入仅在需要进一步财务复盘时提供。

只有旅行账，就分析旅行；缺两个月，就说明缺两个月。不会把局部记录冒充全年完整支出，也不会把一次搬家开销直接推成日常月均。

### 换一个 AI，也能从同一流程开始
本工具包按能力适配，不绑定品牌：
| 当前工具的能力 | 可以交付 |
|---|---|
| 读文件、实际计算、生成文件 | 可核对账本、文件报告和续接记录 |
| 能读和计算，不能导出 | 可复制表格和文字洞察 |
| 只能对话或看图 | 来源盘点、分类辅助、待确认清单；金额需另行核验 |

“流程通用”不等于任何 AI 都能生成 Excel、处理任意数量附件或发布网站。首次启动会说明限制；不具备计算能力时，不会宣称完整账本已核验。目前未在所有第三方 AI 产品上逐一实测。

### 可选：安装为 Skill
在支持自定义 Skill 的工具中，让它读取本仓库，并说：
> 请按你当前工具支持的方式安装 money-operator，保留 SKILL.md、references、templates 和 scripts，并验证能否识别。若不支持安装，就按 START_HERE.md 在本次对话中执行。

安装目录由当前工具决定，不要照搬另一个产品的路径。下载 ZIP 后，可将解压文件夹改名为 money-operator。agents/openai.yaml 只是可选界面信息，其他工具不需要它。已有旧版 personal-bimonthly-bookkeeping 的用户请先备份并停用旧版，避免两套规则同时生效。

### 隐私与边界
工具包不含作者的账单或个人账户数据。你的资料应留在自己选择的 AI/私人工作区；上传前确认平台的数据设置符合需要。没有预算不判断超支，没有当前资产数据不计算财务安全。任何在线发布都要先确认目标和访问权限。

[完整用户指南](./用户工具包.md) · [AI 主流程](./SKILL.md) · [范围与计算口径](./references/period-scope.md)

## English
You do not need to wait for month-end or maintain a daily bookkeeping habit. Start with a trip, a move, a few weeks, cross-year statements, or a backlog of old records.

Money Operator is a portable AI workflow and toolkit. It maps your sources, reconciles overlapping records, classifies transactions, and explains the spending decisions that matter.

### What you get
- A traceable ledger with duplicate decisions and linked refunds.
- Evidence-backed insights into spending drivers, events, fixed commitments and adjustable costs.
- Up to three concrete next steps.
- A continuation record you can carry into another session.

Excel/CSV is preferred when file export is available; copyable tables and text reports are valid alternatives. A hosted website is optional.

### Start without installation
1. Copy the prompt from [START_HERE.md](./START_HERE.md) into your AI.
2. Describe your dates or event, or upload the records you already have.
3. Answer focused questions to establish scope and source coverage.

Example:
> Reconcile my August 17–September 5, 2026 statements. I mostly use a wallet and a credit card. I want to understand the cost of moving. Start with the files I have and identify gaps.

First launch establishes whose money is included, the interval/event, your question, sources, and the AI's actual capabilities. A saved private profile or portable continuation record supports later sessions; automatic long-term memory is not assumed.

### Prepare your records
Prefer original XLSX/CSV exports, then readable PDFs or clear screenshots. Export Numbers to Excel if the current tool cannot read it. Keep dates, merchants and amounts visible while masking full account identifiers. Do not pre-delete transfers, repayments, refunds or duplicates. Incomplete records are welcome, with gaps disclosed. Assets, liabilities and income are optional for a deeper review.

An event-only ledger stays event-only. Missing intervals are not zero spending. Partial periods are not silently converted into a normal monthly baseline.

### Capability-based compatibility
| Available capability | Supported outcome |
|---|---|
| File reading, real calculation, file export | Reconciled ledger, report files, continuation record |
| Reading and calculation without export | Copyable tables and text insights |
| Chat or image reading only | Preparation, classification assistance and questions; totals need external verification |

The workflow is portable; identical automation is not guaranteed in every AI. It has not been individually tested in every third-party product. Missing calculation or hosting capabilities are disclosed, not invented.

### Optional Skill installation
Ask a tool that supports custom skills to install this repository as money-operator using its own supported installation method. Keep SKILL.md, references/, templates/ and scripts/ together; agents/openai.yaml is optional UI metadata. If skills are unsupported, use the standalone starter instead. Rename the extracted folder to money-operator if needed. Existing personal-bimonthly-bookkeeping users should back up and disable the old installation to avoid conflicting instructions.

### Privacy and limitations
No author's statements or personal account data are included. Check your chosen AI's data settings before uploading. Personal state belongs in your private workspace, not this repository. Publishing requires approval of destination and access. Budget, trend and financial-safety claims require matching evidence.

[Start now](./START_HERE.md) · [Workflow](./SKILL.md) · [Runtime adaptation](./references/runtime.md) · [Period rules](./references/period-scope.md)
