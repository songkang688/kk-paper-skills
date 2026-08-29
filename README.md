# kk-paper-skills

写 AI/CV 论文的整套本地 Agent Skills，含一个总路由。装好之后不用记 skill 名，直接说要干什么，`kk-paper-router` 会转发到对应技能。

## 安装

克隆后把各技能目录复制（或软链）到任一被扫描的技能目录，例如：

```bash
git clone https://github.com/songkang688/kk-paper-skills.git
cd kk-paper-skills
for d in */; do ln -sfn "$(pwd)/${d%/}" ~/.cursor/skills/"${d%/}"; done
```

Codex 用户把目标换成 `~/.codex/skills/` 即可。

## 技能一览

| 干什么 | 技能 |
|---|---|
| 总路由，判定意图并转发 | `kk-paper-router` |
| 读论文、中英对照翻译 | `nature-reader` |
| 找文献 | `lit-search`，顶会论文用 `conf-search` |
| 框架、模板、防造假占位 | `paper-skill` |
| 章节初稿（CV 叙事） | `research-paper-writing` |
| 润色、翻译、去 AI 味 | `scipilot-writing-skill` |
| 实验结果图 | `scientific-visualization` |
| LaTeX 编译与排版 | `latex-writer` |
| 参考文献真假核验 | `cite-verify` |
| 审稿：OpenReview 五人审 + 总评 | `reviewforge-openreview` |
| 审稿：会议向交叉验证 | `aaai-review-simulator` |
| 审稿：期刊向 + 魔鬼代言人 | `academic-paper-reviewer` |
| 审稿：逐维打分 | `scholar-evaluation` |
| 审稿：8 维雷达图 | `peer-review` |
| 同段落多英文版本对比与润色推荐 | `paragraph-compare-polish` |
| 论文多方案/多版本对比与主线抉择 | `paper-version-compare` |
| 回复审稿意见 | `nature-response` |
| 选期刊 | `journal-match`（会议由 `paper-skill` venue 流程兜底） |

## 审稿模式

对路由说审稿，它会并行派发 5 个子 agent（reviewforge、aaai、期刊团、scholar-eval、peer-review），各自独立出报告，落盘到 `paper_reviews/<时间>/01-05` 五个文件，父进程汇总共识、分歧和 P0/P1/P2 清单写入 `00-final-verdict.md`。

## 润色模式

对路由说润色，它会先按段落再按句子拆分，每句独立跑一遍 `scipilot-writing-skill`，最后汇总成四列完整对照表：改前、改后、改了什么、为什么。不超过两段直接在对话里给表，超过两段落盘为 `polish_reports/<时间>-润色对照.md`。

## 终检模式

对路由说发表前最终审查，它会跑一次十步全面体检：全局一致性、逐句语言体检（语法、时态、拼写、用词、句长、lint）、标点与微排版（中英文标点、连字符与破折号、数字单位空格、缩写标点）、数学公式与符号、图表细节（编号、图注自足、三线表、有效数字、色盲可读）、引用与参考文献双向核对、数值一致与占位符清零、格式合规（联网抓官方模板，实测页数、字体嵌入、匿名处理）、投稿材料与元数据（含 PDF 属性泄匿名检查），最后输出体检总表和按 P0/P1/P2 分级的问题清单，每条带位置、原文、建议改法。

## 写作固定顺序

`paper-skill` 定真假 → `research-paper-writing` 写故事 → `scipilot-writing-skill` 润表达。审稿与写作不混在同一轮。

## 说明

- 各技能保留原作者的 LICENSE 与出处，见各目录。
- 所有审稿输出为非官方自检，不代表任何会议或期刊，也不预测真实中稿。
