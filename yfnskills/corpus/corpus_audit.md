# yfnskills 语料审计（P1）

审计范围：`clean_corpus/`（22 篇）、`section_map.csv`、`section_coverage.csv`、`cleaning_log.md`、`tierA_list.md`。
审计方式：脚本全量扫描 + 逐项人工核对原始分片注记。发现问题当场修正，修正内容记录在第三节。

## 一、六项必查结论

| 编号 | 检查项 | 结论 | 依据 |
|---|---|---|---|
| 1 | 中文内容混入正文 | **通过** | 对 22 个文件全量正则扫描 CJK 码点（U+4E00–U+9FFF），命中 0 处。18 号的中文污染集中在参考文献块，该段已整体排除；09、13 的中文图注锚点已被英文图注替换 |
| 2 | Tier C / Tier U 论文混入 | **通过** | 14（Tier U，三作且通讯不可考）与 15（Tier C，四作且无通讯证据）均不在 22 篇中。语料清单 24 篇，两篇按规则排除 |
| 3 | 参考文献混入正文 | **通过（附使用约束）** | 三份清洗日志逐篇记录了解交错过程；参考文献在 clean 文件里位于独立的 References 章节。约束见第二节第 1 条 |
| 4 | 图表标题混入正文 | **通过（存在格式不一致）** | 22 篇全部有图注且与正文隔离。但两种约定并存：G 分片 7 篇放在文末附录，H/I 分片 15 篇用行内引用块。已在覆盖表 Captions 列区分标注 |
| 5 | Paper_ID 前后一致 | **通过** | 22 个文件名、250 行 section_map、22 行覆盖表、authorship_weights.csv 的 ID 完全一致，无孤立项、无重名冲突 |
| 6 | 公式重建是否留标记 | **通过** | 所有重建公式均有就地 HTML 注释标注待 PDF 核验；无法重建处标为丢失而非臆造。17 号按严格政策整体排除了乱码公式 |

补充扫描：NUL 字节 0 个（04、13 原文各含 2 个，都在断裂公式块内，清洗时已剥离）；文件名重复 0 个。

## 二、必须带进 P2–P6 的使用约束

1. **建模只能取正文章节。** 允许取 Title、Abstract、Introduction、RelatedWork、Methods、Results、Discussion、Conclusion 和图注；**禁止**从 References、Acknowledgments、Other（作者简介、利益声明、数据可用性、CRediT）取语言证据。参考文献的可靠性在各篇之间差异极大（逐字保留、被压缩、被截断、整段排除、仅占位符五种状态并存），当语言证据用会引入严重偏差。

2. **Discussion 章节证据严重不足，这是本语料最硬的一条限制。** 22 篇里：
   - 真正独立成节且与 Conclusion 分开：**仅 1 篇**（21_LBP_LBPV_FireSafety2011）
   - 作者自己把 Discussion 并入 Results 标题：1 篇（12，原标题 "4. Experiments and discussion"）
   - 作者写了承担 Discussion 功能的子节：1 篇（08，Results 内的 "F. Limitations of our method"）
   - **由清洗者按规范拆出、原文并无此节：1 篇（11）——不得当作作者写 Discussion 的证据**
   - 其余 18 篇没有 Discussion，相关内容散在 Results 与 Conclusion 里
   P3 执行时必须据此把 Discussion 规律降级为"有限证据倾向"，并且明确写清 11 号不算证据。

3. **RelatedWork 缺 3 篇。** 17、21、31 没有独立 Related Work，文献综述写在 Introduction 里。这本身是一条可用的结构观察（早期论文倾向合并），但 P2 归纳 Related Work 规律时样本量是 19 而不是 22。

4. **两篇论文的正文由学生起草，CRediT 有明确记录。** 05 的 Writing–original draft 是 Guiqian Wang，06 是 Kang Li，袁非牛只做 review & editing / conceptualization / funding。作者权重按规则不变（A2 / A3），但 P2–P4 不得把这两篇的正文当作他的一手行文。

5. **Tier B 两篇（09、10）只能佐证或反驳**，不得独立产生任何风格特征。且这两篇与彼此共享作者与参考文献，混杂风险高。

6. **17 号提取质量中低**，只能从标记为干净完整的段落取样，公式部分已整体缺失。

7. **主题混杂已内建于语料**：22 篇里有 5 篇不是烟雾任务（11 去雾、12 医学分割、13 皮肤病灶分割、18 少样本分割、36 超分辨率）。P4 去混杂时这 5 篇是判断"主题效应 vs 个人风格"的天然对照组。

8. **年代跨度 2011–2026**，方法范式从手工特征（21、17、31、19、16、20、30）跨到深度学习（其余），语言与结构必须分年代建模，不能平均。

## 三、本次审计做出的修正

1. **section_map.csv 新增两列。** `shard` 记录来源分片；`anchor_type` 记录锚点类型。原因：G 分片用行号（`L12`），H/I 分片用块锚点（`S001`/`C001`），三份表直接合并会让锚点列语义不一致。合并后 250 行中 line 型与 block_anchor 型并存，下游按 `anchor_type` 分别处理即可。

2. **section_coverage.csv 的 Discussion 列改为四值精确分类**，替换掉原先笼统的 present/absent。原因：直接标 present 会把清洗者合成的 11 号和作者真写的 21 号混为一谈，等于给后续阶段埋一个假证据。

3. **修正 21 号 Conclusion 的误判。** 原判 `present_merged`，但原始注记明确写 "Discussion and Conclusion NOT merged in this source"，改为 `present`。这是自动化关键词匹配踩到 "merged" 一词造成的假阳性。

4. **修正 19 号 Methods 的误判。** 原判 `present_merged`，实际注记里的 "merged" 指一段被误标为图注的正文被合并回 S38，与章节合并无关，改为 `present`。

5. **Captions 列全部重判。** 原先靠 section_map 的 Other 行是否含 "caption" 字样判断，导致 8 篇被误判为 absent。改为直接扫描 clean 文件内容，统计行内引用块图注数量与文末图注附录，结果 22 篇全部有图注，并区分标注 `present_appendix` / `present_blockquote(n)` / `present_inline(n)`。

6. **保留三份原始分片清洗日志**到 `cleaning_log_shards/`，避免统一版合并时的信息损失不可追溯。

## 四、未修正但已记录的问题

以下问题需要原始 PDF 才能闭合，不阻塞后续步骤，清单见 `cleaning_log.md` 第四节：重建公式的 PDF 核验（11 篇）、缺失或截断的参考文献（8 篇）、07 号丢失的 IV.D 小节、16 号推断的小节标题、若干处 `[...]` 截断。

这些都集中在公式、参考文献和小节编号上，不影响 P2–P4 需要的段落级行文证据。
