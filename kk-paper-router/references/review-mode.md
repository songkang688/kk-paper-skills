# 审稿模式（5 子 agent 并行）

1. 先确认材料：论文全文或文件路径、目标 venue。venue 先从 `paper_context` 的
   anchor 复用；稿件路径和 venue 都查不到，才在开跑前一次性问齐，问完一路审到
   综合意见，中间不停。默认 5 路全审，用户点了某几路才只跑那几路。
   稿件还没建吃透档案（`paper_context/<稿件名>/`）的，先走接稿吃透模式再审。
   报告目录 `paper_reviews/<venue>_<YYYYMMDD-HHMM>/`，venue 用官方短名。
2. 并行派发 5 个子 agent，每个只加载一个审稿 skill，互相独立、不共享结论。
   每个子 agent 的 prompt 里必须写明基准稿绝对路径和 `paper_context` 档案路径：
   - `reviewforge-openreview`：OpenReview 五人审加总评，主审稿系统
   - `aaai-review-simulator`：会议向交叉验证，Fatal/Major/Minor
   - `academic-paper-reviewer`：期刊向五人团加魔鬼代言人
   - `scholar-evaluation`：ScholarEval 逐维打分
   - `peer-review`：8 维评分加雷达图
3. 每个子 agent 报告独立落盘到 `paper_reviews/<venue>_<YYYYMMDD-HHMM>/`：
   `01-reviewforge.md`、`02-aaai.md`、`03-journal-team.md`、
   `04-scholar-eval.md`、`05-peer-review.md`。
4. 五份齐后父进程综合，写 `00-final-verdict.md` 并在对话给结论：
   共识问题（至少 3 份点到即必修）、分歧与裁决、最致命问题、
   平均评分与方差、P0/P1/P2 修改清单。五份分报告与综合意见落盘后立即转同名 PDF，
   分报告零散的先合并成一份总报告再转，全部归拢在同一个报告目录。
5. 稿内 `XX` 与 `AUTHOR_INPUT_NEEDED` 按证据缺失处理，任何一家不得编造
   数据、引用或官方政策。
