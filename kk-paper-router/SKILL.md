---
name: kk-paper-router
description: >-
  KK 论文任务总路由。所有论文相关请求先经过本 skill 判定意图，再转发到唯一对应的
  本地 skill：读文献、找文献、搭框架、写初稿、润色翻译、画图、LaTeX、查引用、审稿、
  逐句终检、rebuttal、选刊。审稿意图时并行派发 5 个独立审稿子 agent
  （reviewforge-openreview、aaai-review-simulator、academic-paper-reviewer、
  scholar-evaluation、peer-review），各自保存独立报告文件，父进程汇总共识与分歧后
  输出最终评审意见。Use when the user mentions 论文, paper, manuscript, 审稿,
  review my paper, 润色, 翻译论文, 写引言, 查引用, rebuttal, 投稿, 选期刊, or any
  academic paper task without naming a specific skill. 用户明确点名某个 skill 时
  直接用该 skill，不经过本路由。
---

# KK 论文任务总路由

只做两件事：判定意图、转发到对应 skill。本 skill 自己不写论文、不审稿、不润色。
用户不需要说用哪个 skill，说清要干什么即可。

## 路由表

| 用户在说什么 | 转发到 |
|---|---|
| 读这篇论文 / 翻译论文 / 中英对照精读 | `nature-reader` |
| 找文献 / 检索相关工作 / 找可引论文 | `lit-search`（顶会论文优先 `conf-search`） |
| 开新稿 / 搭框架 / 模板 / 真假与 XX 占位 / 投稿打包 | `paper-skill` |
| 写或改章节（Abstract/Intro/Method/实验叙事） | `research-paper-writing` |
| 润色 / 中译英 / 去 AI 味 / 缩写扩写 / 图表标题措辞 | `scipilot-writing-skill` |
| 画实验结果图 / 消融图 / 误差线 | `scientific-visualization` |
| LaTeX 编译报错 / 公式符号 / 排版 | `latex-writer` |
| 查参考文献真假 / 核对元数据 | `cite-verify` |
| 审稿 / 评审 / 看能不能中 / 找问题 | 【审稿模式】见下 |
| 投稿前逐句终检 / 逐句精修 | `论文kk终极检查`（仅用户明确要终检时） |
| 回复审稿意见 / rebuttal / 修回信 | `nature-response` |
| 不知道投哪个期刊 | `journal-match` |

判定不了就问一句，不要猜。复合意图按表内顺序依次执行，例如翻译加润色先
`nature-reader` 再 `scipilot-writing-skill`。

## 写作固定顺序

涉及写稿时永远按这个顺序，不许跳层：

1. `paper-skill`：先定能写什么，真假、XX、引用政策。
2. `research-paper-writing`：把章节故事写顺。
3. `scipilot-writing-skill`：最后只动表达，不动数值与结论。

## 审稿模式（5 子 agent 并行）

触发：审稿、review、评审、帮我看看这篇能不能投、模拟审稿人。

1. 先确认材料齐不齐：论文全文或文件路径、目标 venue。缺了先问，不要空跑。
2. 并行派发 5 个子 agent，每个子 agent 只加载一个审稿 skill，互相独立、不共享结论：
   - `reviewforge-openreview`：OpenReview 五人审加总评，主审稿系统
   - `aaai-review-simulator`：会议向交叉验证，Fatal/Major/Minor
   - `academic-paper-reviewer`：期刊向五人团加魔鬼代言人
   - `scholar-evaluation`：ScholarEval 逐维打分
   - `peer-review`：8 维评分加雷达图
3. 每个子 agent 把完整报告写入独立文件，目录固定为
   `paper_reviews/<YYYYMMDD-HHMM>/`（放在当前工作区）：
   - `01-reviewforge.md`
   - `02-aaai.md`
   - `03-journal-team.md`
   - `04-scholar-eval.md`
   - `05-peer-review.md`
4. 五份全部落盘后，父进程读全部报告做综合，写入 `00-final-verdict.md` 并在对话里给结论：
   - 共识问题：至少 3 份报告都点到的，列为必修
   - 分歧点：各家评分或判断冲突处，说明谁更可信、为什么
   - 最致命问题与最能拉分的改动
   - 平均评分与方差（按各家可比分数折算）
   - P0 / P1 / P2 修改清单
5. 子 agent 给的每条批评必须落在论文材料上。稿内 `XX` 与 `AUTHOR_INPUT_NEEDED`
   按证据缺失处理，禁止任何一家编造数据、引用或官方政策。
6. `论文kk终极检查` 不进审稿派发。它是逐句精修，只在用户明确说终检时单独转发。

## 明确不转发

- `awesome-ai`、`humanizer`、`ai-text-humaniser`：与 scipilot 同层重复
- `nature-writing`、`nature-polishing`：Nature 文风，CV 会刊不对口
- `academic-paper`、`academic-pipeline`、`paperskills`：避免出现第二个总管

用户执意点名这些时照用，但提醒一句与现有层重复。
