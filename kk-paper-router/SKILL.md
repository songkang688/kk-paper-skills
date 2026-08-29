---
name: kk-paper-router
description: >-
  KK 论文任务总路由。所有论文相关请求先经过本 skill 判定意图，再转发到唯一对应的
  本地 skill：读文献、找文献、搭框架、写初稿、润色翻译、画图、LaTeX、查引用、审稿、
  发表前终检、全局一致性检查、段落多版本对比、论文多方案对比、rebuttal、选会选刊。
  润色时强制逐段拆句、逐句执行润色，
  输出改前/改后/改了什么/为什么四列完整对照表，超过两段落盘为 md 文件。审稿时并行
  派发 5 个独立审稿子 agent（reviewforge-openreview、aaai-review-simulator、
  academic-paper-reviewer、scholar-evaluation、peer-review），各自保存独立报告，
  父进程汇总输出最终评审意见。Use when the user mentions 论文, paper, manuscript,
  审稿, 评审, 润色, 翻译论文, 写初稿, 终检, 最终审查, 一致性检查, 查引用, rebuttal,
  投稿, 选期刊, or any academic paper task without naming a specific skill.
  用户明确点名某个 skill 时直接用该 skill，不经过本路由。
---

# KK 论文任务总路由

只做两件事：判定意图、按本文件的流程转发执行。用户不需要说用哪个 skill，
说清要干什么即可。判定不了就问一句，不要猜。

## 路由表

| 用户在说什么 | 怎么办 |
|---|---|
| 读这篇论文 / 翻译论文 / 中英对照精读 | `nature-reader` |
| 找文献 / 检索相关工作 | `lit-search`，顶会论文优先 `conf-search` |
| 开新稿 / 搭框架 / 模板 / 真假与 XX 占位 / 投稿打包 | `paper-skill` |
| 写初稿 / 写或改章节 | 【写初稿模式】见下 |
| 润色 / 中译英 / 去 AI 味 / 缩写扩写 | 【润色模式】见下 |
| 审稿 / 评审 / 看能不能中 / 模拟审稿人 | 【审稿模式】见下 |
| 发表前最终审查 / 终检 / 投稿前过一遍 | 【终检模式】见下 |
| 前后不对应 / 术语数值矛盾 / 一致性检查 | 【全局一致性检查】见下 |
| 同一段落多个英文版本对比、选哪个表达 | `paragraph-compare-polish` |
| 论文多方案/多版本对比、选主线、版本合并 | `paper-version-compare` |
| 画实验结果图 / 消融图 | `scientific-visualization` |
| LaTeX 编译报错 / 公式排版 | `latex-writer` |
| 查参考文献真假 | `cite-verify` |
| 回复审稿意见 / rebuttal / 修回信 | `nature-response` |
| 选会选刊 | 期刊用 `journal-match`（按范围与影响力匹配并出报告）。会议没有专职 skill，走 `paper-skill` 的 venue 匹配流程，必要时联网查官方 CFP 与截稿 |

## 润色模式（输出契约，必须逐条遵守）

执行者：`scipilot-writing-skill`。流程：

1. 判定载体（`.tex` / Word / 纯文本）和语言方向，用户没说先问一句。
2. 拆分：先按段落拆，再把每段拆成句子。
3. **每一句独立执行一遍润色**，遵守 scipilot 铁律（保守修改、只动表达不动数值、
   载体格式分流）。原句已够好就判「无需修改」，不为改而改。
4. 全部句子跑完后汇总成四列对照表：

   | 改前 | 改后 | 改了什么 | 为什么 |

   - 改前必须是完整原句，改后必须是完整可直接替换的句子。
   - 禁止缩写、禁止「同上」「略」「...」占位。
   - 无需修改的句子也要进表，改后写「无需修改」，为什么写清它为何成立。
5. 输出位置：
   - 输入不超过两段（或一句）：对照表直接放对话框。
   - 输入超过两段：写成 md 文件，路径 `polish_reports/<YYYYMMDD-HHMM>-润色对照.md`
     （放当前工作区），对话里给路径、句子总数、修改句数和主要问题类型摘要。
6. 交付前跑 scipilot 的 `scripts/writing_lint.py` 自检，命中 FAIL 必须修复或如实报告。

## 写初稿模式

固定三层，不许跳：

1. `paper-skill`：先定能写什么。真假、证据状态、`XX` 占位、目标 venue 格式。
2. `research-paper-writing`：逐章节写故事，一段一个意思，claim 对齐实验。
3. 写完问用户是否接润色模式。初稿阶段不做句级润色，避免故事没定就抠字。

## 审稿模式（5 子 agent 并行）

1. 先确认材料：论文全文或文件路径、目标 venue。缺了先问，不要空跑。
2. 并行派发 5 个子 agent，每个只加载一个审稿 skill，互相独立、不共享结论：
   - `reviewforge-openreview`：OpenReview 五人审加总评，主审稿系统
   - `aaai-review-simulator`：会议向交叉验证，Fatal/Major/Minor
   - `academic-paper-reviewer`：期刊向五人团加魔鬼代言人
   - `scholar-evaluation`：ScholarEval 逐维打分
   - `peer-review`：8 维评分加雷达图
3. 每个子 agent 报告独立落盘到 `paper_reviews/<YYYYMMDD-HHMM>/`：
   `01-reviewforge.md`、`02-aaai.md`、`03-journal-team.md`、
   `04-scholar-eval.md`、`05-peer-review.md`。
4. 五份齐后父进程综合，写 `00-final-verdict.md` 并在对话给结论：
   共识问题（至少 3 份点到即必修）、分歧与裁决、最致命问题、
   平均评分与方差、P0/P1/P2 修改清单。
5. 稿内 `XX` 与 `AUTHOR_INPUT_NEEDED` 按证据缺失处理，任何一家不得编造
   数据、引用或官方政策。

## 终检模式（发表前最终审查）

按顺序四步，产出一份终检报告：

1. 【全局一致性检查】（见下），先抓前后不对应。
2. `paper-skill` 投稿检查单：页数、格式、匿名要求、引用政策、伦理声明，
   并确认全文 `XX` / `AUTHOR_INPUT_NEEDED` 已清零，没清零列为 P0。
3. `scipilot-writing-skill` 全文语言终检：跑 `writing_lint.py`，残留 AI 指纹、
   转义、标点问题逐条列出。
4. 汇总为 `final_check/<YYYYMMDD-HHMM>-终检报告.md`：问题按 P0（不改必拒）/
   P1（强烈建议）/ P2（锦上添花）分级，每条给位置、问题、建议改法。

## 全局一致性检查（内置工作流）

专查前后不对应。执行者：`paper-skill`（证据映射）加 `research-paper-writing`
（reverse outline 与 claim-support alignment）。逐项过：

- 术语与缩写：同一概念全篇同名，缩写首次出现处定义，模块名、方法名前后一致。
- 符号与公式：符号含义唯一，方法章参数与实验章设置一致。
- 数值：同一指标在摘要、正文、表格、结论中的数字完全一致。
- 主张对证据：Abstract 和 Intro 的每条贡献都能指到具体实验或消融，指不到就降级。
- 图表：每个 Figure/Table 都被正文引用，编号、图注与正文描述一致。
- 结构：Intro 承诺的内容后文都兑现，Conclusion 不出现正文没有的新主张。

产出三列问题清单：位置、问题、建议改法。可单独调用，也作为终检模式第一步。

## 明确不转发

- `awesome-ai`、`humanizer`、`ai-text-humaniser`：与 scipilot 同层重复
- `nature-writing`、`nature-polishing`：Nature 文风，CV 会刊不对口
- `academic-paper`、`academic-pipeline`、`paperskills`：避免出现第二个总管

用户执意点名这些时照用，但提醒一句与现有层重复。
