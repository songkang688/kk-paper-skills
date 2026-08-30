---
name: paragraph-compare-polish
description: >-
  顶刊审稿人视角的同段落多英文版本对比与润色推荐，标准对齐 Pattern Recognition、
  IEEE TIP、IEEE TMI、Medical Image Analysis，深度学习图像分割方向。对 Version
  A/B/C 从技术准确性、学术语气、清晰度、逻辑、贡献突出度、简洁度、审稿人友好度、
  句式、误读风险十维评分，输出 Overall Impression、Comparison Table、Revision
  Table（改前/改后/修改理由）、Key Differences、Most Recommended Version、
  Final Polished Version 及其中文翻译、Why This Version Works Better。首要原则：
  技术准确性 > 逻辑严谨性 > 审稿人可读性 > 语言优雅度，禁止引入原文不存在的贡献、
  结论或因果。Use when the user provides multiple English versions of the same
  paragraph (Version A/B/C, 版本A/B/C) and asks 哪个版本好, 段落对比, 对比润色,
  选哪个表达, or wants a recommended and polished final version.
---

# 段落多版本对比加推荐

按 [references/protocol.md](references/protocol.md) **逐字执行**，从角色设定、
逐版本判断、评分对比表、改写表、关键差异分析，到最推荐版本、Final Polished
Version、中文翻译和最终检查清单，二十三节全部照做，不许跳节、不许改输出结构。

执行要点：

1. 首要原则不可动摇：技术准确性 > 逻辑严谨性 > 审稿人可读性 > 语言优雅度。
2. 用户提供 Original Chinese 时，以中文原文为技术语义基准，技术忠实度高于英语流畅度。
3. 任何改写不得引入原文不存在的技术贡献、模块功能、实验结果、性能优势、因果关系。
4. 输出必须包含改前、改后、修改理由和推荐版中文翻译，禁止「同上」「略」等省略。
5. 用户说明段落位置（Abstract/Intro/Method 等）时按位置调整标准，没说明按
   Methodology 严格标准。
6. 评分只针对用户给的版本文本，不虚构版本间不存在的差异。

与其他 skill 的边界：单一版本的常规润色走 `scipilot-writing-skill`；整篇论文
多方案对比走 `paper-version-compare`。本 skill 只处理同一段内容的多版本比较。

与润色系统互通：产出 Final Polished Version 时，句子改写调用
`scipilot-writing-skill` 执行，并遵守 kk-paper-router polish-mode 的
11 条 KK 语句风格要求（学术风格、不用长难句、正文少用冒号、用词直白、
不堆并列、包装不超证据等）。**Final Polished Version 的句子改写必须同时按
polish-mode 的四列契约逐句给出：改前完整句 | 改后完整句 | 改了什么 | 为什么，
无需修改的句子也进表并写明它为何成立，禁止「同上」「略」。**protocol 第三节
允许对比表只挑关键差异，那是针对版本对比表；最终润色版一律逐句四列，两者不冲突。
稿件已有 `paper_context/<稿件名>/` 吃透档案时，先读档案再对比，术语和技术判断
以档案与基准稿为准。

交付：结果超过两段就落盘到
`compare_reports/<venue>_<YYYYMMDD-HHMM>-段落对比.md`，落盘验收后**立即转同名
PDF**，不等用户开口要。venue 先从 `paper_context` 的 anchor 复用，查不到才在
开跑前一次问清，问完一路做到交付，中间不停。
