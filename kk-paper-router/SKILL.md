---
name: kk-paper-router
description: >-
  KK 论文任务总路由。所有论文相关请求先经过本 skill 判定意图，再转发到唯一对应的
  本地 skill：找创新点、读文献、找文献、搭框架、写初稿、润色翻译、画图、LaTeX、
  查引用、审稿、发表前终检、全局一致性检查、段落多版本对比、论文多方案对比、
  rebuttal、选会选刊。找创新点时先学近两年顶会顶刊 100 篇再发散，缺口分析用
  research-gap，收敛用 topic-framing，100 个候选选 3 个，可交付完整可训练代码。
  润色时强制逐段拆句、逐句执行润色，
  输出改前/改后/改了什么/为什么四列完整对照表，超过两段落盘为 md 文件。审稿时并行
  派发 5 个独立审稿子 agent（reviewforge-openreview、aaai-review-simulator、
  academic-paper-reviewer、scholar-evaluation、peer-review），各自保存独立报告，
  父进程汇总输出最终评审意见。Use when the user mentions 论文, paper, manuscript,
  审稿, 评审, 润色, 翻译论文, 写初稿, 终检, 最终审查, 一致性检查, 查引用, rebuttal,
  投稿, 选期刊, 找创新点, 选题, 研究缺口, or any academic paper task without
  naming a specific skill.
  用户明确点名某个 skill 时直接用该 skill，不经过本路由。
---

# KK 论文任务总路由

只做两件事：判定意图、按路由表转发执行。本 skill 自己不写论文、不审稿、不润色。
判定不了就问一句，不要猜。复合意图按表内顺序依次执行。

**进入某个模式前，必须先读对应 references 文件并逐条照做，不许凭记忆执行。**

## 路由表

| 用户在说什么 | 怎么办 |
|---|---|
| 找创新点 / 选题 / 找研究缺口 / 想 idea | 读 [references/ideation-mode.md](references/ideation-mode.md)，先学近两年顶会顶刊 100 篇，`research-gap` 找缺口，发散出候选后 `topic-framing` 收敛选 3，要代码时交付完整可训练 py 并对齐用户参考实现 |
| 读这篇论文 / 翻译论文 / 中英对照精读 | `nature-reader` |
| 找文献 / 检索相关工作 | `lit-search`，顶会论文优先 `conf-search` |
| 开新稿 / 搭框架 / 模板 / 真假与 XX 占位 / 投稿打包 | `paper-skill` |
| 写初稿 / 写或改章节 | 【写初稿模式】见下 |
| 润色 / 中译英 / 去 AI 味 / 缩写扩写 | 读 [references/polish-mode.md](references/polish-mode.md)，逐句润色，输出改前/改后/改了什么/为什么四列完整对照表 |
| 审稿 / 评审 / 看能不能中 / 模拟审稿人 | 读 [references/review-mode.md](references/review-mode.md)，并行派 5 个审稿子 agent，五份报告落盘后父进程综合 |
| 发表前最终审查 / 终检 / 投稿前过一遍 | 读 [references/final-check-mode.md](references/final-check-mode.md)，十步全面体检：一致性、逐句语法、标点微排版、公式符号、图表细节、引用文献、数值清零、格式合规（对齐官网实测）、投稿材料元数据、体检总表加 P0/P1/P2 报告 |
| 前后不对应 / 术语数值矛盾 / 一致性检查 | 读 [references/consistency-check.md](references/consistency-check.md) |
| 同一段落多个英文版本对比、选哪个表达 | `paragraph-compare-polish` |
| 论文多方案/多版本对比、选主线、版本合并 | `paper-version-compare` |
| 画实验结果图 / 消融图 | `scientific-visualization` |
| LaTeX 编译报错 / 公式排版 | `latex-writer` |
| 查参考文献真假 | `cite-verify` |
| 回复审稿意见 / rebuttal / 修回信 | `nature-response` |
| 选会选刊 | 期刊用 `journal-match`（按范围与影响力匹配并出报告）。会议没有专职 skill，走 `paper-skill` 的 venue 匹配流程，必要时联网查官方 CFP 与截稿 |

## 写初稿模式

固定三层，不许跳：

1. `paper-skill`：先定能写什么。真假、证据状态、`XX` 占位、目标 venue 格式。
2. `research-paper-writing`：逐章节写故事，一段一个意思，claim 对齐实验。
3. 写完问用户是否接润色模式。初稿阶段不做句级润色，避免故事没定就抠字。

## 全局铁律

- 稿内 `XX` 与 `AUTHOR_INPUT_NEEDED` 按证据缺失处理，任何环节不得编造
  数据、引用或官方政策。
- 审稿与写作不混在同一轮。

## 明确不转发

- `awesome-ai`、`humanizer`、`ai-text-humaniser`：与 scipilot 同层重复
- `nature-writing`、`nature-polishing`：Nature 文风，CV 会刊不对口
- `academic-paper`、`academic-pipeline`、`paperskills`：避免出现第二个总管

用户执意点名这些时照用，但提醒一句与现有层重复。
