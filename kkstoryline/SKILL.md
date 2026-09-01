---
name: kkstoryline
description: 论文故事线升级与逐句润色一键全流程流水线。当用户提供论文并要求"跑 kkstoryline / 一键改论文 / 故事线升级 + 逐句润色"时使用。父进程按七步状态机调度：预处理切分 → 确认投稿目标 → 双子 agent 修改意见 → ToDoList 与结构对比图 → 六子 agent 逐句润色 → 1-6全量汇总拼接与转PDF → 成稿三格式交付。支持断点续跑。
---

# kkstoryline v2 — 一键全流程（父进程调度版）

> **属于 kk-paper-skills 系统**：被直接点名进入时，**先完整读一遍
> `kk-paper-router/SKILL.md` 的全局铁律再开跑**，这是闸门不是提醒。四条附加约束：
> ① 第 5 步逐句润色必须注入 polish-mode 的 11 条语句风格（见第五节 e) 条，
> 父进程负责把绝对路径写进 prompt）；② 第 1 步基础提取先查
> `paper_context/<稿件名>/` 复用（论文旁边、稿件级、跨投稿共用），缺才补建到
> 那里，不塞进带时间戳的工作目录；③ 投稿产物目录必须是
> `kkstoryline_work_<venue>_<YYYYMMDD-HHMM>/`，先定 venue 再建目录；
> ④ 每步验收通过就立刻把该步 md 转 PDF，不攒到第 7 步（见第一节末与第七步）。
>
> 本仓库内部不许跳过路由；只有完全没装 `kk-paper-router` 的独立部署，才按本文件
> 自治执行。此段属本地增补，升级上游包后要加回。

## 一、执行模式

- **一键模式**：用户给论文（+ 可选投稿目标）→ 父进程按第二节七步顺序执行到底。建工作目录之前必须先有 venue（用户已给就用，没给就问一次），除此之外全程不停顿、不提问。
- **断点续跑**：每步开始前在论文旁边找本次对应的
  `kkstoryline_work_<venue>_<YYYYMMDD-HHMM>\pipeline_state.md`（同一 venue
  多份时用最新时间戳；用户指定了完整目录名就用指定的）。如果存在，从第一个
  未 `done` 的步骤继续，不重做已完成步骤。用户说"从第 N 步继续/重跑第 N 步"
  则照办。旧的光秃目录 `kkstoryline_work\` 只当历史读，新跑不许再用这个名字。
- **职责划分（本 Skill 的核心设计）**：本 SKILL.md 是唯一执行主控，负责调度、验收、返工、汇总；`prompts/` 下六个提示词是子 agent 的**质量标准卡**，规定各自产物的内容规格。派发子 agent 时必须使用第五节的派发模板，其中的"流水线覆盖条款"优先于提示词原文。
- 工具：md → PDF 用本目录根的 `md2pdf.py`（`python md2pdf.py <文件或目录>`；换机器先 `--check`）。**PDF 一律由父进程转，子 agent 只产 md、不转 PDF。但时机是「每步验收通过就立刻转该步的 md」，不是攒到第 7 步批量转**——第 1 步吃透档案、第 2 步修改意见、第 3 步 todolist 与结构对比图、第 4 步分节润色稿，各自过了验收门就立即转出同名 PDF。流程中途断了，已完成的步骤也各有 PDF 可看。第 7 步只负责补转剩余零散 md 和出合并总版。

## 二、七步总览

| 步 | 名称 | 执行者 | 输入 | 输出 | 验收门 |
|---|---|---|---|---|---|
| 1 | 基础提取（查 paper_context 复用） | 父进程 | 论文（pdf/tex/md/docx）、代码 + 已有的 `paper_context/<稿件名>/` | 落到 `paper_context/<稿件名>/`：`paper.md`、`images\`、`sections\`、`paragraph_index.md`（+同名 PDF） | 已有则复用不重造；新建则章节齐全、段落索引完成、PDF 非空 |
| 2 | 投稿目标写入 meta | 父进程 | 已定的 venue、paper_context 路径 | 工作目录根 `meta.md`（venue、占位符值、paper_context 与工作目录绝对路径）**及同名 `meta.pdf`** | venue 与目录名一致、meta.pdf 非空 |
| 3 | 双份修改意见 | 2 个子 agent 并行 | paper_context 的 paper.md、sections、工作目录 meta、代码 | `01_advice\A\`、`B\` 各含 `revision_report_full.md` + `storyline_comparison.md` | 覆盖标准卡全部阶段、无省略 |
| 4 | ToDoList 与对比图 | 1 个子 agent | paper_context 的 paper.md + A/B 两份意见 | `02_todolist\`：todolist_report.md、todolist_checklist.md、3 张 PNG | 八部分全覆盖、任务六要素齐、图或 Mermaid 兜底存在 |
| 5 | 逐句润色 ×6 | 6 个子 agent（并行或 3+3） | paper_context 的各 section 文件 + paper.md + 工作目录 todolist + A/B 意见 | `03_revision\part1~part6*.md` | 对照 paper_context 的 `paragraph_index.md` 逐段核数、逐句四列表（改前完整/改后完整/改了什么/为什么）全覆盖 |
| 6 | 1-6拼接汇总与转PDF | 父进程 | part1~part6 全量 md | `03_revision\revision_parts_1_to_6_merged.md/.pdf`、`04_final\revision_master.md/.pdf` | 完整按 1–6 顺序拼接总版、目录导读完备、同名 PDF 成功生成 |
| 7 | 成稿与三格式交付 | 父进程 | 原文 + 所有"改后" | `final_paper.tex/.docx/.pdf`（三格式强制，docx 有便携版 pandoc 兜底链）、全套 md 批量转 PDF、交付清单 | 三格式全部生成且非空、改动全部应用、清单发给用户 |

每步完成后：更新 `pipeline_state.md`，并向用户发一句进度（做了什么、产出在哪）。

## 三、目录布局（公共提取与投稿产物分离）

**先定 venue 和开工时间戳，再建目录，不许先建后改名。** 用户消息或吃透档案里
已有目标 venue 的直接用；没有就问一次（建目录前唯一允许的停顿，可与写 meta
合并）。venue 用官方短名（TIP、ICASSP、PR），空格改下划线。

两类目录都建在论文旁边，职责分开：

- **公共提取 `paper_context/<稿件名>/`**：稿件级，不带 venue、不带时间戳，
  一篇论文只一份，换期刊重投、换 skill 干活都复用。放格式转换与切分产物
  （规格见接稿吃透模式）。
- **投稿产物 `kkstoryline_work_<venue>_<YYYYMMDD-HHMM>/`**：本次投稿特有，
  意见、todolist、润色、成稿都在这里，换期刊就新开一个，互不覆盖。

```
X:\dir\
  paper.pdf
  paper_context\<稿件名>\        公共，跨投稿跨 skill 复用，不带时间戳
    00-anchor.md  01-digest.md  (02-code-map.md)
    paper.md(+.pdf)  images\
    sections\  s1_title_abstract_conclusion.md ... s6_figures_tables_misc.md (+.pdf)
    paragraph_index.md(+.pdf)
  kkstoryline_work_<venue>_<YYYYMMDD-HHMM>\   本次投稿特有
    pipeline_state.md   状态机：每步 status + 产物路径 + 备注；表头写明 venue、时间戳、引用的 paper_context 路径
    meta.md(+.pdf)      venue、期刊/会议、占位符值、paper_context 与工作目录绝对路径
    01_advice\A\        revision_report_full.md/.pdf, storyline_comparison.md/.pdf
    01_advice\B\        revision_report_full.md/.pdf, storyline_comparison.md/.pdf
    02_todolist\        todolist_report.md/.pdf, todolist_checklist.md, structure_*.png
    03_revision\        part1~part6*.md, revision_parts_1_to_6_merged.md/.pdf
    04_final\           revision_master.md/.pdf, final_paper.tex/.docx/.pdf/.md
```

`pipeline_state.md` 格式：一张表（步骤 / status / 开始与完成时间 / 产物 / 验收结果 / 返工次数），父进程是唯一写入者。向用户报进度时给出**两个目录的绝对路径**（paper_context 与本次工作目录）。

> 目录命名与公共提取分离是 kk-paper-skills 本地增补，升级上游包后要加回。
> 禁止再把 paper.md / sections / paragraph_index 塞进带时间戳的工作目录，
> 也禁止用光秃的 `kkstoryline_work\` 作为新跑目录。

## 四、各步细则

### 第 1 步：基础提取（父进程，先查 paper_context 复用）

**先看 `paper_context/<稿件名>/` 有没有现成的 `paper.md`、`sections/`、
`paragraph_index.md`（接稿吃透模式或上一次投稿已经建过）。齐全且非空就直接复用，
本步只补缺失项，不重复转换。** 产物一律落到 `paper_context/<稿件名>/`，
不落本次带时间戳的工作目录。缺什么补什么（下面同时等于完成接稿吃透的机械提取部分）：

1. 原始文件复制进 `paper_context\<稿件名>\`。格式转换出 `paper.md` + `images\`：
   - PDF → Python + PyMuPDF（`pip install pymupdf`）；退路 `markitdown` / `pdfplumber`；扫描版无文本层 → 告知用户需可复制文本的版本（允许的例外停顿）；
   - docx → `pandoc paper.docx -t gfm --extract-media=images -o paper.md`；
   - tex → 保留原 tex（第 7 步直接改 tex），另 pandoc 转 md 供分析。
2. **切分 sections**：把 paper.md 按章节拆成 6 个分节文件（对应六个润色 part；标题+摘要+结论合并为 s1；图表与杂项线索汇成 s6：全部图注、表格、缩写表、命名清单）。
3. **生成 `paragraph_index.md`**：每个 section 内逐段编号，记录每段首句前 10 个词和段落总数。这是第 5 步验收的机械依据，必须做。
4. 抽查转换质量：五大章节在、公式表格无大面积丢失；有问题换工具重转。
5. **即刻转 PDF（必要动作，不可省略）**：抽查通过后立即 `python md2pdf.py paper_context/<稿件名>`，把 `paper.md`、`sections\` 下 6 个分节文件、`paragraph_index.md` 全部转出同名 PDF；核对每个 PDF 存在且非空。转换失败按第七节红线降级并如实告知，但不得静默跳过。（复用已有档案时本步跳过。）

### 第 2 步：投稿目标写入 meta（父进程）

venue 在建目录前已经定过，这一步把它写进本次工作目录根的 `meta.md`：venue、
期刊/会议、`{{期刊1}}/{{期刊2}}` 或 `{{会议1}}/{{会议2}}`、`{{目标venue}}`、
代码路径、`paper_context/<稿件名>/` 绝对路径、本次工作目录绝对路径。若建目录时
只拿到主投、这里还缺备选，可以补问一次；venue 本身不许改到和目录名不一致。
写完后**即刻 `python md2pdf.py <meta.md 绝对路径>` 转出 `meta.pdf`（必要动作），
核对非空。**

### 第 3 步：双份修改意见（2 个子 agent 并行）

- 标准卡选择：**期刊** → A 用 `prompts/提示词1_期刊版_系统大改成稿.md`、B 用 `prompts/提示词4_期刊版_诊断三方案重写.md`；**会议** → A 用 `prompts/提示词2_会议版_大刀阔斧重构.md`、B 用 `prompts/提示词3_会议版_诊断三方案重写.md`。
- 用 Task 工具**同一条消息并行派发**两个 generalPurpose 子 agent，prompt 按第五节模板组装。
- 产物：各自目录下 `revision_report_full.md`（标准卡全部阶段的完整内容）+ `storyline_comparison.md`。

### 第 4 步：ToDoList 与结构对比图（1 个子 agent）

- 标准卡：`prompts/提示词5_修改总结与ToDoList执行版.md`；输入：`paper_context/<稿件名>/paper.md` + A/B 两份 revision_report + 两份 storyline_comparison。
- 产物：`todolist_report.md`（两部分结构）、`todolist_checklist.md`、`structure_before.png`、`structure_after.png`、`structure_comparison.png`。
- 画图：Python graphviz 或 matplotlib，中文字体 `Microsoft YaHei` 防乱码；画不出 → md 里给 Mermaid 源码兜底，不中断。
- 验收：建议消化表覆盖 A、B 且冲突有取舍；todolist 覆盖八部分、每任务六要素（改哪里/怎么改/为什么/优先级/工作量/完成标准）。

### 第 5 步：逐句润色 ×6（6 个子 agent，并行或 3+3 分批）

- 标准卡：`prompts/提示词6_逐句润色执行.md`。分工：part1 标题+摘要+Conclusion；part2 Introduction；part3 Related Work；part4 Method；part5 实验；part6 存在的问题（图、表、命名、符号、单位、格式、交叉引用）。
- 每个子 agent 输入：`paper_context/<稿件名>/sections/` 下自己的 section 文件（主要工作对象）、`paper_context/<稿件名>/paper.md`（通读保证上下文一致）、本次工作目录的 todolist、A/B 意见。**优先级必须写进 prompt：todolist 为主，意见为参考，冲突从 todolist。**
- 产物：`03_revision\part{n}_{部分名}.md`，太长可拆 `_1/_2/...`（4、5 个也行），必须完整；逐段独立、逐句做成四列表「改前完整版｜改后完整版｜改了什么｜为什么」（不改的句子也进表并给理由，改前改后都是完整版不省略）；需要引用的联网搜索并给论文名。第 6 步把六个 part 拼成的 `revision_master` 就是全篇逐句总表，第 7 步的 `final_paper` 三格式是应用全部"改后"的完整改后终稿（final）。
- **机械验收**：对照 `paper_context/<稿件名>/paragraph_index.md`——该 part 处理的段落数 = 索引段落数；抽查每段四列表齐全；part6 对照图表清单核全。缺 → resume 补全。

### 第 6 步：1-6全量拼接汇总与转PDF（父进程）

1. **全量拼接总版**：
   - 严格按论文章节与逻辑顺序将 Part 1 至 Part 6 的所有润色成果拼接合并为全量总版：
     * 保存于 `03_revision\revision_parts_1_to_6_merged.md`（方便在 revision 目录下快速查阅全集）；
     * 同时保存于 `04_final\revision_master.md` 作为全流程总交付报告；
   - 拼接格式规范：文件开头生成统一目录索引（TOC），每个部分之间加入导语与 ToDoList 对应映射条目。
2. **即刻转出高清 PDF**：
   - 使用 `python md2pdf.py` 立即将 `revision_parts_1_to_6_merged.md` 渲染转换为同名 `revision_parts_1_to_6_merged.pdf`，以及 `revision_master.pdf`；
   - 确保包含中英文对照、排版美观且无乱码，让作者既能看单 part 细节，也能通览全篇润色总版 PDF。

### 第 7 步：成稿与交付（父进程）

1. **改后论文成稿——三格式强制交付：`final_paper.tex` + `final_paper.docx` + `final_paper.pdf`，缺一不可**（把所有"改后"按顺序应用到原文）：
   - 源是 tex → 改出 `final_paper.tex`，xelatex/pdflatex 编译 `final_paper.pdf`（报错修到通过；无本地 latex 试 tectonic，再退 pandoc 并告知）；`pandoc final_paper.tex -o final_paper.docx` 出 Word 版；
   - 源是 docx（用户上传 Word 正文的常见情形）→ 直接改出 `final_paper.docx`（pandoc md→docx，尽量用 `--reference-doc=<原docx>` 保留原文样式），再 pandoc 转 `.tex`（standalone article）；PDF 用 latex 编译或 md2pdf 兜底；
   - 源是 pdf/md → 先 `final_paper.md`，再 pandoc 转 `.tex` 与 `.docx`；PDF 用 xelatex 或 md2pdf 兜底；
   - **pandoc 缺失时的兜底链（必须依次尝试，不许直接放弃 docx）**：先查 `d:\tools\pandoc\` 下是否已有解压好的 pandoc.exe → winget/choco 安装 → 从 GitHub releases 下载便携版 zip（`https://api.github.com/repos/jgm/pandoc/releases/latest` 取 `windows-x86_64.zip`，解压到 `d:\tools\pandoc\`，直接调用 pandoc.exe，无需管理员权限）→ 全部失败才允许缺 docx 交付，并在交付清单写明原因与安装命令；
   - 自查：三格式全部生成且非空；全部"改后"已应用；公式、图表引用、参考文献没丢；不确定处保留原文并在交付说明列出。
2. **批量转 PDF**：`python md2pdf.py <目录>` 处理 01_advice、02_todolist、03_revision、04_final 下全部剩余 md 文档。
3. **交付清单发给用户**：按步骤列出全部文件绝对路径。公共提取（paper/sections/paragraph_index md+pdf）在 `paper_context/<稿件名>/`；本次投稿产物（meta md+pdf、A/B 意见 md+pdf、storyline_comparison、todolist 套件+3 图、part1~6、1-6全量拼接总版 md+pdf、final_paper 三格式）在本次工作目录。并附一句每步做了什么。

## 五、子 agent 派发模板（组装 prompt 时逐项填）

```
你是 kkstoryline 流水线第 {N} 步的子 agent，负责 {任务名}。
1. 先完整阅读你的质量标准卡：{提示词文件绝对路径}，严格按其内容规格执行。
2. 占位符取值：{逐个列出，如 {{期刊1}}=TIP，{{目标venue}}=TIP，{{负责部分}}=part2：Introduction}。
3. 输入材料（全部先读完、吃透再动手）：{逐个列出绝对路径}。
4. 输出：写入 {输出目录与文件名}；文件开头注明负责范围与依据。
5. 流水线覆盖条款（优先于标准卡原文）：
   a) 只产 md，不转 PDF，不生成标准卡里"交付文件"阶段要求的 PDF/图片之外的额外文件（第 4 步的 3 张 PNG 除外，照常生成）；
   b) 联网检索只做趋势归纳与引用核实，不逐篇精读，不确定的标注"不确定"；
   c) 一次性完成、全部落盘、不许省略、不许编造论文中没有的数字与文献；
   d) 完成后回报：产出文件清单 + 每个文件覆盖的内容范围 + 自检结果。
   e) 【仅第 5 步逐句润色】句子层面的质量标准照 polish-mode 的「KK 语句风格
      追加要求」11 条执行。**父进程派发前必须先把路径探出来填进本条**，按下面
      顺序探测，命中第一个就用（`{SKILLS}` 代表本 skill 所在的 skills 根目录）：
        1. `{SKILLS}/kk-paper-router/references/polish-mode.md`
        2. `~/.agents/skills/kk-paper-router/references/polish-mode.md`
        3. `~/.codex/skills/kk-paper-router/references/polish-mode.md`
        4. `~/.cursor/skills/kk-paper-router/references/polish-mode.md`
      lint 脚本按同样顺序探
      `{同上}/scipilot-writing-skill/scripts/writing_lint.py`。
      **四处都探不到就把 11 条原文整段抄进 prompt**，不许让子 agent 自己找，
      更不许退回一句「更紧凑更专业更地道」了事。兜底：`prompts/提示词6_逐句润色
      执行.md` 里存了一份 11 条原文，探不到文件时从那里取。
      标准卡第 6 条「更紧凑更专业更地道」以那 11 条为具体判据；
      润色执行调 `scipilot-writing-skill`，写完跑它的 `scripts/writing_lint.py`
      自检，FAIL 项修掉或在改动汇总表里如实登记。四列表的「为什么」列里
      注明本句触发了 11 条中的哪几条。
```

> 第五节 e) 条是本地增补（kk-paper-skills 系统内的技能互通），不在 kkstoryline
> 上游包里。升级 kkstoryline 后需要重新加回这一条。

## 六、验收与返工规则

- 每步产物按第二节验收门核验：文件存在、非空、规格齐全（第 5 步按 paper_context 的 paragraph_index 机械核数）。
- 不合格 → resume 该子 agent，明确指出缺什么、补什么。**同一任务最多返工 2 次**；仍不合格则父进程在 pipeline_state 与交付清单中如实标注缺陷并继续流程，不卡死整条流水线。
- 并行的子 agent 互不等待；父进程在该步全部产物验收通过后才推进状态机。

## 七、红线

1. 不编造：意见、todo、润色必须基于论文实际内容；引用必须给真实论文名。
2. md 是唯一真实来源，PDF 只是阅读版。
3. 工具缺失先尝试安装，装不上就降级并明确告知，不静默跳过。
4. 除建目录前的 venue 问询与扫描版 PDF 无文本两种情况外，不向用户提问。

## 八、收尾自检清单

- [ ] pipeline_state.md 七步全部 done（或已如实标注缺陷）
- [ ] paper.md + images + sections + paragraph_index 齐全，且以上 md 已转出同名 PDF（第 1 步）
- [ ] meta.md 记录了 venue 与占位符，且 meta.pdf 已生成非空（第 2 步）
- [ ] A、B 意见与 storyline_comparison 齐全且覆盖标准卡全部阶段
- [ ] todolist 套件 + 3 张结构图（或 Mermaid 兜底）齐全
- [ ] part1~6 落盘且通过 paragraph_index 机械核数
- [ ] 03_revision 下 1-6 拼接总版 `revision_parts_1_to_6_merged.md/.pdf` 已生成
- [ ] `revision_master.md/.pdf` 汇总完成
- [ ] final_paper 三格式（tex + docx + pdf）全部生成且非空、改动全部应用
- [ ] 全部 md 批量转出 PDF
- [ ] 交付清单 + 分步进度已发给用户
