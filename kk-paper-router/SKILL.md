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
  父进程汇总输出最终评审意见。提到袁老师/袁非牛/yfn 风格时整条任务转 yfnskills
  按其内部工作流执行。要一键大改、故事线升级加逐句润色时转 kkstoryline 七步
  流水线自治执行。Use when the user mentions 论文, paper, manuscript,
  审稿, 评审, 润色, 翻译论文, 写初稿, 终检, 最终审查, 一致性检查, 查引用, rebuttal,
  投稿, 选期刊, 找创新点, 选题, 研究缺口, 袁老师风格, kkstoryline, 一键改论文,
  故事线, 跑实验, 训练, GPU, 论文转PPT, 组会汇报, 研究进展, 画图, 图转PPT,
  图片转可编辑, 复现这张图, 图转VBA, or any academic
  paper task, including when the user explicitly names a specific skill.
  用户即使点名某个具体 skill，也先经过本路由套上附加约束与联动再转发执行，
  不要跳过路由。点名只省去判定意图这一步，不豁免路由层写的约束。
---

# KK 论文任务总路由

**这是整套系统的大脑。任何论文相关请求都先到这里判定意图、套上约束、再派发，
用户点名某个 skill 也不例外。**

只做三件事：判定意图、套上该模式的附加约束与跨 skill 联动、按路由表转发执行。
本 skill 自己不写论文、不审稿、不润色。复合意图按表内顺序依次执行。
**一句话就要能开工**：范围类一律用默认直接跑，不为确认而停；确实要问的一次问齐，
问完按流程一路走到交付。

**进入某个模式前，必须先读对应 references 文件并逐条照做，不许凭记忆执行。**

## 路由表

| 用户在说什么 | 怎么办 |
|---|---|
| 第一次给论文全文 / 稿件文件 / 代码包 | 读 [references/intake-mode.md](references/intake-mode.md)，先吃透：锚定基准路径、全文精读落盘 `paper_context/<稿件名>/`、向用户汇报理解。之后才进其他模式 |
| 找创新点 / 选题 / 找研究缺口 / 想 idea | 读 [references/ideation-mode.md](references/ideation-mode.md)，先学近两年顶会顶刊 100 篇，`research-gap` 找缺口，发散出候选后 `topic-framing` 收敛选 3，要代码时交付完整可训练 py 并对齐用户参考实现 |
| 读这篇论文 / 翻译论文 / 中英对照精读 | `nature-reader`。**这里指读懂别人的论文。若用户是要把自己的中文稿翻成英文投稿，走润色模式的中译英；点名袁老师风格的走 `yfnskills`** |
| 找文献 / 检索相关工作 | `lit-search`，顶会论文优先 `conf-search` |
| 开新稿 / 搭框架 / 模板 / 真假与 XX 占位 / 投稿打包 | `paper-skill` |
| 写初稿 / 写或改章节 | 【写初稿模式】见下 |
| 用袁老师风格写 / 改 / 中翻英 / 审阅把关挑毛病 / 回复审稿（提到袁老师、袁非牛、yfn） | `yfnskills` 整条接管：接稿问诊后按其内部四条工作流走（整篇初稿、润色、中翻英、rebuttal），交付 md+PDF 成对。**不套 polish-mode 四列契约**，**语句与写作规则**冲突时以 yfnskills 为准；**交付层规则一律以本路由为准**（目录 `yfn_<venue>_<时间戳>/`、落盘即转 PDF、复用 `paper_context`、rebuttal 先读 `paper_reviews/`），事实性红线两边一致 |
| 跑 kkstoryline / 一键改论文 / 故事线升级加逐句润色 | `kkstoryline` 七步流水线自治执行。**先定 venue 再建目录** `kkstoryline_work_<venue>_<YYYYMMDD-HHMM>/`（例 `kkstoryline_work_ICASSP_20260831-0021`），然后切分、双份意见、ToDoList、六路逐句润色、汇总、三格式成稿。路由不拆解其步骤。**第 5 步逐句润色必须注入** polish-mode 的 11 条语句风格，润色调 `scipilot-writing-skill` 并跑 writing_lint。基础提取先查 `paper_context/<稿件名>/` 复用、缺才补建到那里（跨投稿跨 skill 共用），不重复转换 |
| 润色 / 中译英 / 去 AI 味 / 缩写扩写 | 读 [references/polish-mode.md](references/polish-mode.md)。**给了整篇论文就默认全文润色，不问范围**。三级拆分：先把全文切成几个部分、每部分拆段落、每段拆句子，逐句执行，输出改前/改后/改了什么/为什么四列完整对照表；部分数 ≥5 时按部分并行派子 agent，父进程按原顺序拼成总表再转 PDF。点名袁老师风格的转 `yfnskills` |
| 审稿 / 评审 / 看能不能中 / 模拟审稿人 | 读 [references/review-mode.md](references/review-mode.md)，并行派 5 个审稿子 agent，五份报告落盘后父进程综合。**点名让袁老师审阅把关的走 `yfnskills`，不派 5 路** |
| 发表前最终审查 / 终检 / 投稿前过一遍 | 读 [references/final-check-mode.md](references/final-check-mode.md)，十步全面体检：一致性、逐句语法、标点微排版、公式符号、图表细节、引用文献、数值清零、格式合规（对齐官网实测）、投稿材料元数据、体检总表加 P0/P1/P2 报告 |
| 前后不对应 / 术语数值矛盾 / 一致性检查 | 读 [references/consistency-check.md](references/consistency-check.md) |
| 同一段落多个英文版本对比、选哪个表达 | `paragraph-compare-polish` |
| 论文多方案/多版本对比、选主线、版本合并 | `paper-version-compare` |
| 跑实验 / 自动实验循环 / 训练跑得怎么样 / GPU 空不空 | 读 [references/experiment-mode.md](references/experiment-mode.md)：开跑用 `auto-experiment`，查进度用 `experiment-status`，查卡用 `gpu-monitor`。ideation 交付的代码是实验对象，`MEMORY_LOG.md` 的结果回流当写作数值底本 |
| 论文转 PPT / 组会汇报 / 文献汇报幻灯片 | `nature-paper2ppt`，出中文 PPTX 加讲稿备注。**只用这一个，不许用 `pptx`、`presenton`、`baoyu-slide-deck`**——那三个是通用做片子的，不懂论文汇报的叙事结构与讲稿分工。启动带上 `paper_context/<稿件名>/` 吃透档案，贡献点、数值、图表说明直接取档案，不重读全文；没建档的先走 intake。产物落 `slides_<venue或主题>_<YYYYMMDD-HHMM>/`，PPTX 是成品格式不转 PDF |
| 写研究进展 / 阶段汇报 / 本周做了什么 | `progress-report`，读 `MEMORY_LOG.md` 与实验日志出结构化进展报告 |
| 画实验结果图 / 消融图 | `scientific-visualization`，从数据出图 |
| 把这张图做成可编辑的 / 图转 PPT 形状 / 复现论文里的架构图 / 图转 VBA | `kkimage-visio-ppt`：图片重建成可编辑 Office Shapes，出 `.bas` 宏加 `.pptx`，照它的硬触发条件把复杂原图元素保留为裁图。**只做「已有图片 → 可编辑图形」**——从数据画图走 `scientific-visualization`，从零设计示意图走 `baoyu-diagram`。重建自己论文的图时先读 `paper_context` 里的图注与模块名，不靠看图猜；图与正文不一致要报出来。产物落 `figures_<venue或主题>_<YYYYMMDD-HHMM>/` |
| LaTeX 编译报错 / 公式排版 | `latex-writer` |
| 查参考文献真假 | `cite-verify` |
| 回复审稿意见 / rebuttal / 修回信 | `nature-response`。启动时带上吃透档案，本地 `paper_reviews/` 里有模拟审稿报告的一并读入，把模拟审出的问题提前挡在回复里。点名袁老师风格的走 `yfnskills` 的 rebuttal_workflow |
| 选会选刊 | 期刊用 `journal-match`（按范围与影响力匹配并出报告）。会议没有专职 skill，走 `paper-skill` 的 venue 匹配流程，必要时联网查官方 CFP 与截稿 |

## 写初稿模式

固定三层，不许跳：

1. `paper-skill`：先定能写什么。真假、证据状态、`XX` 占位、目标 venue 格式。
2. `research-paper-writing`：逐章节写故事，一段一个意思，claim 对齐实验。
3. 初稿阶段不做句级润色，避免故事没定就抠字。三层跑完再提示可接润色模式，中途不停。

用户点名袁老师风格的初稿不走这三层，整条转 `yfnskills` 的 draft_workflow
（五路分节子 agent 并行加父节点融合，出 tex/pdf/docx）。

## 全局铁律

- **点名也先过路由**：用户即使说"用 XX skill 帮我……"，也先经过本路由再转发。
  原因是附加约束与跨 skill 联动全写在路由层，绕过就丢：kkstoryline 第 5 步
  注入 polish-mode 的 11 条语句风格、rebuttal 走 nature-response 时要读
  `paper_reviews/` 里的模拟审稿报告、所有模式启动都带 `paper_context` 吃透档案。
  路由先确认被点名 skill 的附加约束和联动，套上后再执行；点名只是缩短判定意图
  这一步，不等于豁免约束。
- **规则不因入口而变**：同一件事，单独点名调用和被路由联动调用，执行规则完全
  一致——四列契约、逐句全覆盖、命名带 venue 加时间戳、落盘即转 PDF、复用
  `paper_context`、开跑后不停，六条一视同仁。**唯一按入口变的是「用谁的语句
  风格」**：点名袁老师风格用 yfnskills 那套自成体系的规则，其余一律用
  polish-mode 的 11 条。这是选风格，不是松规矩。任何 skill 都不许拿「我是被
  直接点名的」或「我自成体系」当理由豁免上面六条。
- **产物命名**：每次干活的输出必须带投稿 venue 短名和时间戳，格式
  `<前缀>_<venue>_<YYYYMMDD-HHMM>`。venue 先从 `paper_context` 的 anchor 复用，
  查不到才在开跑前一次问清，问到就一路跑完不再停。细则见
  [references/output-naming.md](references/output-naming.md)。例：
  `kkstoryline_work_TIP_20260831-0021/`。
- 稿内 `XX` 与 `AUTHOR_INPUT_NEEDED` 按证据缺失处理，任何环节不得编造
  数据、引用或官方政策。
- 审稿与写作不混在同一轮。
- **一次问齐、流程中间不停**：范围类一律走默认直接开跑，不为确认而停——审稿默认
  5 路全审，润色默认全文，载体与语言方向按稿件自行判定，用户点了具体范围才按
  点的来。只有真正卡住流程的硬缺失（主要是 venue，且 `paper_context` 里也查不到）
  才在开跑前一次性问齐，问完一路执行到交付，步骤之间绝不停下等确认。
  别把一个流程切成一问一停。

  **开跑前的那一次问诊算在这一次里，不算违反本条**：yfnskills 的接稿问诊
  （投哪儿、做什么、改哪节）、intake 的吃透汇报、experiment-mode 的 brief 确认，
  都属于开工前的同一次交互，问完直接开跑。它们必须一次问完，不许分几轮问；
  凡是 `paper_context` 里查得到的（venue、稿件路径、任务类型）一律不问。
  开跑之后，任何模式都不许再停下等确认。
- **产物即 PDF**：凡是交付给用户的报告、对照表、回复信、清单、成稿（审稿五份加
  综合意见、润色四列对照、终检报告、一致性清单、段落与版本对比、kkstoryline 每步
  产物、yfnskills 定稿等），落盘验收后立即转同名 PDF；零散分片最后合并成一个
  总版 md 再转，产物归拢到同一个带 venue+时间戳的目录。子 agent 只产 md 时由
  父进程转。PPTX、最终 docx 这类本身就是成品格式的保留原格式。
- **接稿先吃透**：用户第一次给论文或代码，必须先走
  [references/intake-mode.md](references/intake-mode.md) 建档落盘。之后所有
  模式启动都带上基准稿路径和 `paper_context` 档案路径，一切改动以该稿为核心，
  派子 agent 时路径写进 prompt。`paper_context/<稿件名>/` 是稿件级公共资产
  （论文旁边、不带时间戳），基础提取（paper.md、章节切分、段落索引）一次做成、
  多模式多次投稿复用，任何模式不重复转换；带 venue 和时间戳的工作目录只放
  本次投稿特有产物。划分见 [references/output-naming.md](references/output-naming.md)。
- **技能互通**：各 skill 不是孤岛，执行中需要其他能力时直接调对应 skill。
  例如 `paragraph-compare-polish` 产出最终润色版时，润色执行必须遵守
  polish-mode 的四列契约与 11 条风格规则；`paper-version-compare` 选完主线
  要改稿时接润色模式；ideation 出的方案要写成章节时走写初稿模式。
  互通时各 skill 的铁律同时生效，冲突时以更严格的一方为准。
- **自治工作流的注入规则**：`yfnskills` 与 `kkstoryline` 都是完整流水线，
  路由不拆解其步骤，但要不要注入本系统的语言标准，按该流水线自己有多厚判断，
  两者不一视同仁。
  - `yfnskills` **不注入**：它自带 80 条规则白名单、按章节量化的语言画像、
    9 个章节 playbook，是一套自成体系的作者风格。塞 11 条 KK 风格会与它的
    硬规则打架（如目的从句结构、Results 不用 we propose、时态纪律），
    改坏它。**但「以 yfnskills 为准」只管语句与写作规则**：交付层的目录命名、
    落盘即转 PDF、复用 `paper_context`、rebuttal 先读 `paper_reviews/` 这四条
    以本路由为准，已抄进它 SKILL.md 文首，别再拿「自成体系」豁免掉。
  - `kkstoryline` **注入第 5 步**：它的润色标准卡流程厚但语言标准薄，
    句子层面只有「更紧凑更专业更地道」一句空话。派发 6 个润色子 agent 时
    把 polish-mode 的 11 条语句风格作为具体判据写进 prompt，执行调
    `scipilot-writing-skill` 并跑 writing_lint。该条已写进其 SKILL.md
    第五节派发模板 e) 条，含四处路径探测顺序；11 条原文另存一份在它的
    `prompts/提示词6_逐句润色执行.md` 里兜底，父进程漏填路径也不会退化成
    「更紧凑更专业更地道」那句空话。升级上游包后这两处都要重新加回。
  - 事实性红线三方本来一致，无需注入。吃透档案照常互通：`paper_context/` 是
    稿件级公共资产，先给它们带上；kkstoryline 的基础提取也落到那里，
    不在各自工作目录里重复转换。

## 明确不转发

- `awesome-ai`、`humanizer`、`ai-text-humaniser`：与 scipilot 同层重复
- `nature-writing`、`nature-polishing`：Nature 文风，CV 会刊不对口
- `academic-paper`、`academic-pipeline`、`paperskills`：避免出现第二个总管
- `pptx`、`presenton`、`baoyu-slide-deck`：通用幻灯片工具，论文汇报一律走
  `nature-paper2ppt`。**`pptx` 的 description 覆盖"任何涉及 .pptx 的场合"，
  是全库最容易抢走论文转 PPT 的一个**，看见它抢单就拉回 `nature-paper2ppt`

用户执意点名这些时照用，但提醒一句与现有层重复。
