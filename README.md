# Money Operator

> 把散乱账单，变成可审计、可行动的个人财务决策。
> Turn messy statements into an auditable personal finance operating system.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)](./SKILL.md)
![Private by Default](https://img.shields.io/badge/Privacy-Private%20by%20default-2E7D32)
![CNY Ready](https://img.shields.io/badge/Currency-CNY%20ready-D97706)

**[中文](#中文) · [English](#english)**

---

## 中文

### 记账不该结束在分类完了

大多数记账工具告诉你花了多少钱。Money Operator 还会继续追问：

- 这个数字是否齐全，有没有重复、退款或内部转账？
- 哪些是日常生活，哪些是一次性项目？
- 资产净值和财务选择权变好了，还是变弱了？
- 下两个月，优先级最高的 1–3 个行动是什么？

它是一个面向 Codex 的双月记账与财务复盘 skill。你提供原始账单，Codex 负责盘点、合并、去重、分类、追问必要信息，最后交付 Excel 账本和私有复盘报告。

### 你会得到什么

| 交付 | 它解决的问题 |
|---|---|
| **可追溯的 Excel 账本** | 每笔交易从哪里来、为什么纳入或排除，都有依据 |
| **私有在线报告** | 看清支出构成、变化原因和需要决策的地方 |
| **个人账户来源地图** | 第一次配置后，以后不用每期从头说明 |
| **可选的财务经营复盘** | 连接收支、资产负债、目标进度与下一周期行动 |

### 60 秒开始

1. 安装这个 skill。
2. 在 Codex 中打开你用来存放财务资料的私人文件夹。
3. 输入：

```text
使用 $personal-bimonthly-bookkeeping 做首次启动。
```

Codex 会先弄清你实际使用的支付 App、购物平台、银行卡和信用卡，再生成属于你的资料清单。

### 首次启动：每个人都从自己的账户开始

这个 skill 不会假设你一定使用微信、支付宝或某家银行。第一次使用时，它会引导你确认：

1. 这次是只算你，还是包含伴侣或家庭。
2. 你平时用哪些支付 App 和购物平台。
3. 钱从哪些银行卡、信用卡或现金扣除。
4. 哪些来源是主数据，哪些只用来交叉核对。
5. 这期是否有大额、退款、押金、借款或新增账户。

如果你不知道怎么回答，直接说“我不确定”就可以。也可以提供已遮住完整卡号的账户列表截图。

确认后，Codex 会在你的工作目录中保存 `记账配置_最新.json`。它只记录蒙版账户名和来源关系，不保存密码、验证码或交易流水。

### 需要准备什么

不需要先整理文件，也不要自己删除疑似重复、还款、退款、工资或转账。原始数据就是对账证据。

文件格式优先级：

1. `.xlsx` 或 `.csv`
2. 文字可读的 PDF
3. 清晰、连续，同时显示日期、商户和金额的截图

请不要提供支付密码、银行密码、短信验证码、身份证号或完整卡号。

### 它怎么工作

```text
首次账户配置
        ↓
来源完整性检查
        ↓
解析与合并原始流水
        ↓
去重、分类、退款冲抵
        ↓
只追问会影响结果的交易
        ↓
Excel 终稿 + 私有复盘报告
        ↓
下两个月的 1–3 个行动
```

用户永远有最终决定权。证据不足时，系统会将交易标记为待确认，而不是静默猜测。

### 安装

#### 让 Codex 帮你安装

下载或 clone 本仓库，然后对 Codex 说：

```text
请把这个 personal-bimonthly-bookkeeping skill 安装到我的个人 skills 目录，并验证它能被识别。
```

#### 手动安装

将完整的 `personal-bimonthly-bookkeeping` 文件夹复制到 Codex 个人 skills 目录。不要只复制 `SKILL.md`，`references/`、`templates/`、`scripts/` 和 `agents/` 也是 skill 的一部分。

macOS / Linux 常见位置：

```text
~/.codex/skills/personal-bimonthly-bookkeeping/
```

Windows 常见位置：

```text
%USERPROFILE%\.codex\skills\personal-bimonthly-bookkeeping\
```

重新打开 Codex 后，输入首次启动指令进行验证。不同版本的界面或目录可能变化；如遇到问题，让当前 Codex 检查其 skill 目录和可用 skill 列表。

### 隐私默认值

- 原始账单保持不变。
- 产出只存入当前工作目录或你批准的位置。
- 账户标识默认蒙版。
- 复盘站点默认私有。
- 不向可部署站点上传原始账单。
- 没有明确授权，不公开发布个人财务数据。

### 这个 skill 适合谁

**适合：**

- 账单分散在多个支付平台、银行和信用卡中的人。
- 希望保留原始证据，并能解释每个处理决定的人。
- 不想每天记账，但愿意每两个月做一次经营复盘的人。

**不是：**

- 银行或证券账户的自动交易工具。
- 税务、法律或持牌投资建议的替代品。
- 在证据不足时仍给出精确数字的黑盒。

### 更多指南

- [小白完整工具包](./%E7%94%A8%E6%88%B7%E5%B7%A5%E5%85%B7%E5%8C%85.md)
- [Skill 主流程](./SKILL.md)
- [首次启动规则](./references/first-run.md)
- [数据去重规则](./references/deduplication.md)
- [输出与校验规范](./references/outputs.md)

---

## English

### Bookkeeping should not end with categorized transactions

Most bookkeeping tools tell you how much you spent. Money Operator keeps going:

- Is the number complete, or does it contain duplicates, refunds, and internal transfers?
- Which costs belong to normal life, and which are one-off projects?
- Did net worth and financial optionality improve or weaken?
- What are the one to three actions that matter most over the next two months?

Money Operator is a Codex skill for bimonthly bookkeeping and personal finance operating reviews. You provide original statements. Codex inventories, parses, reconciles, deduplicates, and classifies them, asks only for decisions that materially affect the result, and produces an Excel ledger plus a private review report.

### What you get

| Deliverable | What it gives you |
|---|---|
| **Auditable Excel ledger** | A traceable reason for every included, excluded, deduplicated, or reclassified transaction |
| **Private review report** | A clear view of spending composition, period changes, anomalies, and decisions |
| **Personal source map** | A reusable map of your wallets, marketplaces, banks, and cards |
| **Optional financial operating review** | Connected views of cash flow, assets, liabilities, goals, and next-cycle actions |

### Start in 60 seconds

1. Install the skill.
2. Open your private finance workspace in Codex.
3. Enter:

```text
Use $personal-bimonthly-bookkeeping and guide me through first launch.
```

Codex first discovers the payment apps, marketplaces, banks, and cards you actually use. It then gives you a personalized statement checklist instead of assuming a generic account list.

### First launch is personal by design

Every user has a different money trail. First launch establishes:

1. Whether the scope covers you, a partner, or a household.
2. Which wallets and marketplaces you use.
3. Which bank accounts, cards, or cash sources fund those payments.
4. Which sources provide primary transaction detail and which are cross-check only.
5. Whether the period contains new accounts, large purchases, refunds, deposits, or debt movements.

If you do not know, say so. You can also provide a screenshot of an account list after hiding full account numbers.

The confirmed map is saved as `记账配置_最新.json` in your private workspace. It stores masked labels and source relationships, not passwords or transaction records.

### What to prepare

Keep source files untouched. Do not remove repayments, transfers, refunds, salary, or suspected duplicates yourself; they are reconciliation evidence.

Preferred formats:

1. `.xlsx` or `.csv`
2. Text-readable PDF statements
3. Clear, continuous screenshots showing date, merchant, and amount

Never provide payment passwords, bank passwords, verification codes, government ID numbers, or full card numbers.

### How it works

```text
First-launch source map
        ↓
Source-completeness check
        ↓
Parse and merge original statements
        ↓
Deduplicate, classify, and reconcile refunds
        ↓
Ask only about material unresolved items
        ↓
Final Excel ledger + private review report
        ↓
One to three actions for the next two months
```

The user remains the final decision-maker. Transactions with insufficient evidence stay visibly unresolved instead of being silently guessed.

### Installation

#### Ask Codex to install it

Download or clone this repository, then tell Codex:

```text
Install the personal-bimonthly-bookkeeping skill into my personal skills directory and verify that Codex can discover it.
```

#### Install manually

Copy the complete `personal-bimonthly-bookkeeping` directory into your Codex personal skills directory. Keep `SKILL.md`, `references/`, `templates/`, `scripts/`, and `agents/` together.

Common macOS / Linux location:

```text
~/.codex/skills/personal-bimonthly-bookkeeping/
```

Common Windows location:

```text
%USERPROFILE%\.codex\skills\personal-bimonthly-bookkeeping\
```

Restart Codex and run the first-launch prompt. Product versions may differ, so ask your current Codex installation to confirm its skill directory and discoverable skill list if needed.

### Privacy by default

- Original statements remain unchanged.
- Outputs stay in the active workspace or another user-approved location.
- Account identifiers are masked by default.
- Review sites are private by default.
- Raw statements are never added to deployable site source.
- Personal finance data is never published without explicit permission.

### Who it is for

**A good fit for people who:**

- Have transactions spread across multiple wallets, marketplaces, banks, and cards.
- Want evidence-preserving bookkeeping with explainable decisions.
- Prefer a high-quality bimonthly review to daily manual tracking.

**It is not:**

- An automated trading or bank-transaction tool.
- A replacement for tax, legal, or licensed investment advice.
- A black box that invents precise conclusions from incomplete data.

### Learn more

- [Beginner-friendly toolkit](./%E7%94%A8%E6%88%B7%E5%B7%A5%E5%85%B7%E5%8C%85.md)
- [Skill workflow](./SKILL.md)
- [First-launch protocol](./references/first-run.md)
- [Deduplication rules](./references/deduplication.md)
- [Output and QA specification](./references/outputs.md)

---

Built for people who want more than a completed ledger: a clearer allocation of money, attention, and next actions.
