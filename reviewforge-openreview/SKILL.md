---
name: reviewforge-openreview
description: >-
  ReviewForge-OpenReview Edition (中文版终版): simulate five independent
  OpenReview-style reviewers plus a meta-review for AI/CV manuscripts.
  Uses official-style fields Summary, Soundness, Presentation, Contribution,
  Strengths, Weaknesses, Questions, Flag For Ethics Review, Rating,
  Confidence, Code Of Conduct; then Meta-Review, Decision Tendency, and a
  P0/P1/P2 revision plan. Use when the user says ReviewForge, OpenReview 审稿,
  五位审稿人, ICLR/NeurIPS/CVPR/AAAI review form, Soundness/Presentation/
  Contribution 打分, 按拒稿边缘审, or asks for a strict multi-reviewer
  OpenReview-format review of a paper. Unofficial self-assessment only.
---

# ReviewForge-OpenReview Edition（中文版终版）

非官方自检。不要声称代表 OpenReview、ICLR、NeurIPS、CVPR 或 AAAI，不要预测真实中稿。

完整流程、字段、评分定义、venue 适配和首次交互模板见 [references/protocol.md](references/protocol.md)。**按该文件逐字执行，不要改字段名，不要跳步。**

## 何时加载哪份文件

- 材料不齐（缺 venue 或正文）：只输出 `protocol.md` 里「四、首次交互模板」那段，不要提前审稿。
- 材料已齐：读完 `protocol.md` 全文，再按 Step 1–10 跑完。
- 用户点名更毒舌 / 按拒稿边缘审：执行 Step 9。

## 执行要点

1. 先确认投稿 venue。未定时按 `protocol.md` 让用户选顶会或顶刊，不要自己猜。
2. venue 确定后联网读官方 author / reviewer guidelines，只写一小段「本 venue 审稿侧重点摘要」，不要大段粘网页。
3. 自动生成五位独立审稿人（方法创新 / 理论严谨 / 实验证据 / 写作表达 / 领域落地），专长贴论文方向，五个人不能说同一套话。
4. 字段名保持英文，内容用中文。每位 reviewer 只输出规定字段。
5. 五人出完后再写 Meta-Review、Decision Tendency、Average Rating、Top Accept/Reject Reasons、Most Important Rebuttal Targets、Priority Revision Plan（P0/P1/P2）。
6. 批评必须落在用户给的材料上。缺实验、缺表、缺数就写材料不足，**禁止编造结果、引用、页码、官方政策原文**。稿里的 `XX` / `AUTHOR_INPUT_NEEDED` 按未完成证据处理，并据此降 Soundness / Contribution，不要当成已有数字。
7. 明确判断这篇更像顶会稿、顶刊稿，还是工程报告。

## 和本机其他审稿 skill 的关系

用户点名 ReviewForge / OpenReview 表格时用本 skill。不要和 `aaai-review-simulator`、`academic-paper-reviewer`、`peer-review`、`scholar-evaluation` 在同一轮混跑。
