# 产物命名（venue + 时间戳）

每次干活的输出目录和报告文件必须带投稿目标和时间戳，方便同一稿多投、多次修改互不覆盖。

## 格式

```
<前缀>_<venue>_<YYYYMMDD-HHMM>
```

- **venue**：官方短名。IEEE TIP → `TIP`，ICASSP → `ICASSP`，Pattern Recognition → `PR`。空格改下划线，只留字母数字和下划线，不用中文全称、不用空格、不用斜杠。
- **时间戳**：开工那一刻的本地时间，精确到分钟，例 `20260831-0021`。
- **没给 venue 先问再动手**。禁止 `unknown`、`tmp`、默认名、光写时间戳。吃透档案或用户消息里已经有目标 venue 的，直接用，不必再问。
- 同一分钟开两次，后面加 `-2`、`-3`。

## 各模式对照

| 模式 | 路径 |
|---|---|
| kkstoryline | 论文旁边 `kkstoryline_work_<venue>_<YYYYMMDD-HHMM>/` |
| 润色（超两段） | `polish_reports/<venue>_<YYYYMMDD-HHMM>-润色对照.md` |
| 审稿 | `paper_reviews/<venue>_<YYYYMMDD-HHMM>/` |
| 终检 | `final_check/<venue>_<YYYYMMDD-HHMM>-终检报告.md` |
| 找创新点 | `ideation/<主题>_<venue>_<YYYYMMDD-HHMM>/` |
| yfnskills 任务夹 | 在它自己的 `polish-vN/` 等名字前加同一套前缀，或把整个任务夹放进 `yfn_<venue>_<YYYYMMDD-HHMM>/` |

## 公共资产 vs 投稿产物（划分原则）

产物分两类，放两处，别混：

- **稿件级公共资产 → `paper_context/<稿件名>/`**（论文旁边，不带 venue、不带
  时间戳，一篇论文一份，跨投稿跨 skill 复用）：格式转换的 `paper.md`、抽出的
  `images/`、章节切分 `sections/`、`paragraph_index.md`，以及吃透分析
  `00-anchor.md`（含 venue 历史）、`01-digest.md`、`02-code-map.md`。
  换期刊重投不重建，只在 anchor 里记一行新 venue。
- **本次投稿特有产物 → `<前缀>_<venue>_<YYYYMMDD-HHMM>/`**：意见、todolist、
  润色对照、审稿报告、终检报告、成稿三格式——凡是跟"投这一次这一家"绑定的，
  都带 venue 和时间戳，换期刊就新开一个，互不覆盖。

判断口诀：换个期刊还能原样用的，进 paper_context；换个期刊要重做的，进带
时间戳的工作目录。任何模式需要基础提取（全文文本、分节、段落索引）时先查
paper_context，缺才补建到那里，绝不各自把 PDF 重新转一遍。

## PDF 与合并交付规范（所有模式通用）

重要交付产物产出后必须同步转同名 PDF，别拖到最后、别不转。谁产出谁负责转；
子 agent 只产 md 时，由父进程/主流程在验收通过后立即转。

- **必须转 PDF 的重要产物**：审稿的 5 份分报告与综合意见、润色四列对照表、
  终检报告、一致性清单、段落/版本对比报告、ideation 的 top3、kkstoryline 每步
  的意见/todolist/润色/成稿、yfnskills 的定稿。纯过程草稿（papers.md、
  candidates.md 等）可不转。
- **同步转**：每份重要 md 落盘并验收通过后**立即** `python md2pdf.py <md 或目录>`，
  不等整条流程结束；中途中断也已有 PDF。
- **零散产物先合并再转**：一个任务产出多个分片 md（如 yfnskills 分节润色、
  kkstoryline 的 part1~6）时，最后按逻辑顺序合并成一个总版 md 再转 PDF，分片保留。
  合并总版命名 `<venue>_<YYYYMMDD-HHMM>_<类型>_merged.md`（+同名 pdf），
  例 `TIP_20260831-0021_polish_merged.md`。
- **资料归拢**：同一任务的所有产物（分片、合并总版、PDF、附图）放进同一个带
  venue+时间戳的工作目录，交付时给目录绝对路径 + md/pdf 清单。
- **工具与降级**：优先 `md2pdf.py`，退 `pandoc`；转换失败必须如实告知原因与补救
  命令，不静默跳过。

## 续跑

用户说从某步继续、重跑某步时，先按 venue 找最新那份时间戳目录。指定了完整目录名就用指定的。旧的光秃名 `kkstoryline_work/` 若还在，当历史目录读，新跑一律用带 venue 和时间戳的名字。
