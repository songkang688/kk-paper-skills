# 终检模式（发表前最终审查）

按顺序五步，产出一份终检报告：

1. 【全局一致性检查】（见下），先抓前后不对应。
2. 【格式合规检查】对齐官网要求，硬指标逐项实测，不靠目测：
   - 先联网获取目标 venue 官方 author guidelines 与模板（如 ICASSP Paper Kit、
     Elsevier GFA）。拿不到就标 `UNVERIFIED`，禁止凭记忆编官方要求。
   - 页数：用 `latex-writer` 实际编译 PDF 数页，区分正文页限与参考文献页
     （如 ICASSP 的 4 页正文加 1 页仅参考文献）。
   - 模板与版式：documentclass、单双栏、页边距、行距是否用官方模板，禁改样式文件。
   - 字体：`pdffonts` 核对字体全部嵌入，图内文字不小于 venue 最小字号要求。
   - 图表：分辨率不低于 300dpi 或矢量，图注位置与格式、编号连续、
     正文全部引用，色彩打印和色盲可读。
   - 参考文献样式、匿名方式（单盲/双盲对应作者栏处理）、PDF 大小与
     补充材料命名。
   - 产出四列对照表：官方要求、实测值、是否合规、怎么修。
3. `paper-skill` 投稿材料检查单：cover letter、highlights、声明（数据可用性、
   COI、伦理、AI 使用）、引用政策，并确认全文 `XX` / `AUTHOR_INPUT_NEEDED`
   已清零，没清零列为 P0。
4. `scipilot-writing-skill` 全文语言终检：跑 `writing_lint.py`，残留 AI 指纹、
   转义、标点问题逐条列出。
5. 汇总为 `final_check/<YYYYMMDD-HHMM>-终检报告.md`：问题按 P0（不改必拒）/
   P1（强烈建议）/ P2（锦上添花）分级，每条给位置、问题、建议改法。
