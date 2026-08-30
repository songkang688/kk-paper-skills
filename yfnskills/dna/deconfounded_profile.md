# 去混杂后的作者区分度清单（袁非牛）

这是 P4 的最终产物：**扣除年代、方法范式、主题、venue、固定合作者、执笔人六类混杂之后，仍然站得住的特征**。

分三档：
- **CORE**：所有分组下都稳定，且在传给学生的稿件中会衰减（说明是个人特征而非实验室模板）。这是 P5 组装 Skill 时的主干。
- **CONDITIONAL**：真实存在但有明确的适用条件（年代、主题、执笔人），必须带条件使用。
- **REJECTED**：已判定为混杂或通用，不进 Skill 的风格部分。

判定依据全部在 `confound_audit.md`；量化数据在 `../_work/p4_micro_report.txt`。

---

## 一、CORE（8 条）

### CORE-1｜目的在前、机制在后（全文四节通用）

`To <purpose>, we <propose/design/present/adopt> <Module (ABBR)>.`

- **稳健性**：四个章节的目的从句密度全部 > 3/k；在年代、主题、venue、Tier 各分组下均存在。
- **为什么算个人特征而非模板**：Tier B 两篇（09、10，学生一作）的 Conclusion 目的从句密度为 **0**，而 A1/A2/A3 都在 6.2–7.4。A3 的 Results 密度也只有 1.4（A1 是 5.5）。**这个习惯在传给学生时会衰减，说明它属于作者本人。**
- **不给密度目标值**：密度受年代（Conclusion 3.3→6.4）与 venue（IEEE 11.2 vs Elsevier 3.3）影响，只要求"每个模块前面都有目的从句"这个结构约束。
- **Confidence**：high。

### CORE-2｜缺陷收敛为"某类信息缺失"，模块名承载该信息

诊断动词固定在 `discard / not involve / lose / not be modelled / ignore`；模块命名回指被丢失的信息。

- **稳健性**：45 个模块中 35 个（78%）可核验；跨四种主题、四个 venue、A1/A2/A3 三层成立；无 venue 或主题依赖。
- **年代下限**：2016 年。17（2012）与 21（2011）的诊断用统计学习语言，没有这一层。
- **Confidence**：high。

### CORE-3｜`our` 在 Results 暴涨、`we propose` 在 Conclusion 达峰

`our` 密度：Front 2.5 → Results **17.4**；`we propose` 密度：Results 1.3 → Conclusion **13.0**。两条曲线反向。

- **稳健性**：所有分组下方向一致（Results 的 our 在各组为 10.9–24.4；Conclusion 的 we propose 在各组为 10.1–16.8）。
- **操作含义**：Results 用 `our method / our <模块>` 作比较主语，不写 `we propose`；Conclusion 把每个模块重新宣告一遍。
- **Confidence**：high。

### CORE-4｜时态纪律：过去时被完全限制在 Results

`we + conducted/performed/implemented/compared/tested` 密度：Front 0、Methods 0、Results 2.8、Conclusion 0。

- **稳健性**：所有分组下 Front/Methods/Conclusion 均为 0。
- **注意**：**只保留"方法现在时、实验过去时、过去时只在 Results"这条分工。被动语态的高低已剔除（纯年代效应）。**
- **Confidence**：high。

### CORE-5｜证据锚点严格限制在 Methods 与 Results

`As shown in / as listed in` 密度：Front 0、Methods 2.7、Results 2.6、Conclusion 0。

- **例外白名单**：Introduction 允许引用一次难点示例图；Conclusion 的局限段允许引用失败案例图（13 号）。
- **有辨识度的子形式**：锚点与 `we find that` 合写（`As shown in Table 2, we find that ...`）。`we find that` 全语料 30 次，23 次在 Results。
- **Confidence**：high。

### CORE-6｜次优结果的非对称让步

`slightly` 描述对手优势或自身劣势；`obviously / distinctly / nearly` 描述自身优势。承认输掉的指标并给出精确数字，然后转到自己占优的维度。

- **稳健性**：`slightly` 全语料 20 次，18 次在 Results；A1/A2 层 6 篇无例外。
- **衰减证据**：Tier B 两篇改用 `comparable` 处理平手，副词对立消失。**又一个"传给学生会衰减"的特征。**
- **Confidence**：high（A1/A2 层）。

### CORE-7｜段落长度分工：Methods/Results 短段，Conclusion 长整段

段落长度中位数：Conclusion 164 → Front 126.5 → Results 85.2 → Methods 81.6。

- **稳健性**：所有分组下顺序一致。
- **扣除项**：Kang Li 参与的四篇 Conclusion 句长偏长（26.6 vs 20.8 词），**建模 Conclusion 语言时扣除 03、06、09、10**。段落长度本身不受合作者影响。
- **Confidence**：high。

### CORE-8｜多面板比较图中 our method 永远是最后一个面板

面板顺序：`(a) 输入 → (b) ground truth → (c)…(x) 对比方法（顺序与主表一致）→ 末位 = our method`。

- **稳健性**：6 个多面板比较图零反例，是全语料唯一可机械校验且无例外的规则。
- **Confidence**：high。

---

## 二、CONDITIONAL（7 条）

### COND-1｜因果解释的两档 hedge｜条件：执笔人

可核验的架构或数据事实用 `The reason is that`；不可核验属性或不利结果用 `The reason may be that`。全语料 50 条（flat 33 / hedge 17）。

- **条件**：A3（学生主导）的 hedge 密度是各层最低（1.3–1.9 vs A1/A2 的 2.2–4.4），且 04 号改用 `We conjecture / We suspect / We think` 的认知动词做 hedge。**复刻作者本人风格时用情态动词式；不要用认知动词式。**
- **Confidence**：medium-high。

### COND-2｜前提在前、后果在后（`, so` 因果尾句）｜条件：执笔人 + 章节

`<可核验前提>, so <设计后果>.` 密度 Front/Methods/Results 约 1.0–1.2/k，Conclusion 为 0。

- **条件**：A3 的密度只有 0.5/k（A1 是 3.4/k）。08、10、36 的 Methods 里为 0。
- **注意**：`so that` 全语料仅 6 次且 4 次集中在 16 号，**不是他的习惯**，主形式是逗号 + `so`。
- **Confidence**：medium-high。

### COND-3｜任务粒度阶梯与升级论证｜条件：主题

detection → recognition → segmentation → density estimation，并在正文显式论证新粒度更难更有信息量。

- **条件**：**仅限烟雾系列。** 非烟雾五篇（11、12、13、18、36）不参与，直接用领域标准任务名。
- **Confidence**：high（烟雾）／不适用（其他主题）。

### COND-4｜传统方案物理前提失效式过渡｜条件：主题

写清旧方案的工作原理 → 它必须满足的物理前提 → 该前提在目标场景不成立 → 因此需要视觉方法。

- **条件**：8 篇烟雾论文成立；11（去雾）、12/13（医学）无此段；36（超分）迁移为"插值方法过度平滑"的退化形式。
- **Confidence**：high（烟雾）／medium（作为可迁移论证形式）。

### COND-5｜局限与未来工作段｜条件：年代 2023 后

单独一段，局限给机制不只给现象，未来工作指向具体技术。

- **条件**：9 篇中 8 篇在 2023–2026；**16 号（2018）是深度反例且写得最细**（误差跨层累积放大）。年代趋势与"失效机制是否可分析"两种解释未能分离。
- **Confidence**：high（趋势）／medium（机制）。

### COND-6｜Related Work 以定位段收尾｜条件：存在独立 RW

`Inspired by <成功路线>, we also ...` 或 `However, above-mentioned methods do not ...`，段内必有显式差异化陈述。

- **条件**：样本量是 19 不是 22（17、21、31 无独立 RW）。19/19 篇无例外。36 号（2025）的定位段最弱，只说"仍有改进空间"。
- **Confidence**：high。

### COND-7｜坦诚式限定｜条件：证据薄弱

主动说出"这个模块不是必须的"或"我们证明不了"，单句插在正常肯定叙述里。

- **证据**：19 号 Conclusion `However, LPP is not compulsory, so we may not apply LPP if we do not care about dimensions and computation time`；19 号 Introduction `but it is difficult for us to theoretically prove it`；21 号 Discussion `So we do not know the performance on unknown videos`。
- **条件**：只有 19（2016）与 21（2011）两篇、三处证据，全部出自作者一手行文的篇目。
- **Confidence**：medium。数量少但性质高度一致，且这是最能体现"诚实度"的特征，建议保留并在 Skill 中作为可选项。

---

## 三、REJECTED（11 项）

| 项 | 剔除理由 |
|---|---|
| 被动语态密度高 | **纯年代效应。** A1 未控制时 Methods 19.4/k，控制年代后 11.2/k，与 A2 的 8.8 接近；Conclusion 甚至反转 |
| 名词化绝对水平 | **主题词汇效应。** 烟雾术语本身多 -tion/-ity（segmentation、estimation、translucency）。只保留章节间落差 |
| 缩写密度 | **venue 效应。** 同主题内 IEEE 的 Conclusion 缩写密度是 Elsevier 的 2.4 倍 |
| 标题的 `A/An + 评价形容词` 开头 | **venue 效应。** 无冠词开头集中在 IEEE，`A/An` 集中在 Elsevier |
| 表格标题大小写 | venue 模板（IEEE 全大写 / IEEE 句首 / Elsevier 句首三种并存） |
| 贡献列表的编号格式 | venue 模板（IEEE 多 `1)`，Elsevier 出现 `(1)` 与 bullet） |
| `The remainder of this paper is organized as follows.` | 期刊模板句。只保留"展开到小节级"这个子特征（02、07、08 三篇） |
| `Experiments show that our method outperforms ...` | 通用学术英语，22/22 出现只证明遵守惯例。保留的是"摘要不给数字"（21/22） |
| 一句一方法的 `Author et al. [n] proposed` 综述节奏 | 计算机视觉综述领域惯例。保留的是叠加其上的条件式缺陷从句 |
| `where` 逐符号定义 | 学术写作通行规范 |
| `above-mentioned / aforementioned`、`not only ... but also`、Results 标准小节名、`we propose` 高频、`so that` | 通用英语或领域惯例；`so that` 另因全语料仅 6 次且集中于单篇而不构成习惯 |

---

## 四、给 P5 的三条移交要点

1. **CORE 的 8 条是 Skill 的主干**，其中 CORE-1、CORE-2 是最有区分度的两条，且都有"传给学生会衰减"的证据支持它们属于个人特征而非实验室模板。这修正了 P2/P3 阶段"无法排除课题组模板"的保守结论——**结构骨架可能是模板化的，但目的从句、hedge 分工、非对称让步这些句子层特征是可分辨的执笔痕迹。**

2. **建模 Conclusion 语言时必须扣除 03、06、09、10 四篇**（Kang Li 参与），它们的 Conclusion 句长长 6 个词、保留被动语态、带 booster 词，而其余晚期论文这三项分别是 20.8 词、0、0。

3. **不得给出任何密度目标数值。** 目的从句密度受年代与 venue 影响（Conclusion 从 3.3 到 11.2），只能给结构约束（"每个模块前必有目的从句"），不能给"每千词 6 次"这类指标。P5 写 `SKILL.md` 时如果出现数值化的风格指标，属于超出证据。
