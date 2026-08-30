# Style DNA — 去混杂后的作者区分度清单

这是扣除年代、方法范式、主题、venue、固定合作者、执笔人六类混杂之后仍然站得住的特征。
判定过程与控制对照数据见 `dna/confound_audit.md` 与 `dna/deconfounded_profile.md`。

**为什么这些算个人特征而不是实验室模板**：P2 与 P3 阶段曾无法排除"这是课题组写作模板"的解释。P4 的分层比较给出了反证——**CORE-1（目的从句）与 CORE-6（非对称让步）在传给学生的稿件里会衰减**：Tier B 两篇（学生一作）的 Conclusion 目的从句密度为 0，而其他各层都在 6.2–7.4/k；Tier B 的非对称让步退化成了 `comparable`；Tier A3 三篇的 hedge 密度是各层最低，04 号还改用 `We conjecture / We suspect / We think` 的认知动词做 hedge。结构骨架可能是模板化的，但这些句子层特征是可分辨的执笔痕迹。

---

## CORE（8 条，无条件适用）

### CORE-1 目的在前、机制在后
`To <purpose>, we <propose/design/present/adopt> <Module (ABBR)>.`
四个章节的目的从句密度全部 > 3/k；在年代、主题、venue、Tier 各分组下均存在。**这是全语料唯一贯穿摘要、贡献列表、Methods 组件小节、Conclusion 模块复述四处的句法。**
衰减证据：Tier B 的 Conclusion 为 0，A3 的 Results 仅 1.4/k（A1 是 5.5）。
**不给密度目标值**——密度受年代（Conclusion 3.3→6.4）与 venue（IEEE 11.2 vs Elsevier 3.3）影响，只要求"每个模块前面都有目的从句"这个结构约束。

### CORE-2 缺陷收敛为"某类信息缺失"，模块名承载该信息
诊断动词固定在 `discard / not involve / lose / not be modelled / ignore`。
45 个模块中 35 个（78%）的命名可核验回指被诊断为缺失的信息。
最干净的几例：「传统 LBP 直方图完全丢弃 LBP 码的空间分布」→ `Sub Oriented Histograms of LBP`；「多尺度扩展未涉及尺度间关系」→ `3D local differences across scales`；「多尺度融合只用拼接或相加，无法建模跨尺度内在结构」→ `Newton Interpolation Module`。
年代下限 2016 年——2011 与 2012 的两篇独著用的是统计学习语言，没有这一层。

### CORE-3 `our` 与 `we propose` 的反向分工
`our` 密度：Introduction 2.5 → Results **17.4**（7 倍）。
`we propose` 密度：Results 1.3 → Conclusion **13.0**（全文峰值，比 Methods 还高一倍）。
Results 的主语是被比较的对象，不是提出的动作；Conclusion 是重新宣告。所有分组下方向一致。

### CORE-4 过去时严格限于 Results
`we conducted / performed / implemented / compared / tested` 的密度在 Introduction、Methods、Conclusion 全部为 0，只在 Results 出现（2.8/k）。
**注意只保留时态分工。被动语态的高低已剔除**——那是纯年代效应（Methods 19.4→9.6，Conclusion 19.9→3.7）。

### CORE-5 证据锚点严格限于 Methods 与 Results
`As shown in / as listed in` 密度在 Introduction 与 Conclusion 为 0，Methods 2.7、Results 2.6。
两个白名单例外：Introduction 可引一次难点示例图；Conclusion 的局限段可引失败案例图。

### CORE-6 次优结果的非对称让步
`slightly` 描述对手优势或自身劣势；`obviously / distinctly / nearly` 描述自身优势。承认输掉的指标并给精确数字，然后转到占优维度。
`slightly` 全语料 20 次，18 次在 Results；A1/A2 层 6 篇无例外。
衰减证据：Tier B 改用 `comparable` 处理平手，副词对立消失。

### CORE-7 段落长度分工
段落长度中位数：Conclusion 164 → Introduction 126.5 → Results 85.2 → Methods 81.6。
Methods 与 Results 用短段落（一段一个模块或一个观察），Conclusion 用长整段。
**建模 Conclusion 语言时扣除 03、06、09、10**（Kang Li 参与，Conclusion 句长 26.6 词、保留被动语态、带 booster 词，而其余晚期论文这三项是 20.8 词、0、0）。

### CORE-8 多面板比较图中 our method 永远是最后一个面板
6 个多面板比较图零反例，是全语料唯一可机械校验且无例外的规则。

---

## CONDITIONAL（7 条，条件不满足就跳过）

| ID | 特征 | 条件 |
|---|---|---|
| COND-1 | 因果解释的两档 hedge（可核验用 flat，不可核验或不利结果用 hedge） | **执笔人敏感。** A3 的 hedge 密度最低（1.3–1.9 vs A1/A2 的 2.2–4.4），04 号改用认知动词。复刻作者本人风格时用情态动词式 |
| COND-2 | 前提在前、后果在后（逗号 + `so`） | **执笔人 + 章节。** A3 密度仅 0.5/k（A1 是 3.4/k）；Conclusion 为 0。注意 `so that` 全语料仅 6 次且 4 次集中单篇，**不是习惯** |
| COND-3 | 任务粒度阶梯与升级论证 | **仅限烟雾系列。** 非烟雾五篇不参与，直接用领域标准任务名 |
| COND-4 | 传统方案物理前提失效式过渡 | **仅限有非视觉替代方案的任务。** 8 篇烟雾论文成立；去雾与医学无此段；超分退化为"插值过度平滑" |
| COND-5 | 局限与未来工作段 | **2023 年后风格。** 9 篇中 8 篇在 2023–2026；16 号（2018）是深度反例且写得最细，年代趋势与"失效机制是否可分析"两解释未分离 |
| COND-6 | Related Work 以定位段收尾 | **需存在独立 Related Work。** 样本量 19 不是 22（17、21、31 把综述写在 Introduction 里）。19/19 无例外 |
| COND-7 | 坦诚式限定（主动降低自己组件的必要性） | **证据薄弱时使用。** 仅 19（2016）与 21（2011）两篇三处，全部出自作者一手行文的篇目。是最能体现诚实度的特征，建议保留为可选项 |

---

## 三条使用铁律

1. **不得给任何风格指标设数值目标。** 目的从句密度在 Conclusion 从 3.3/k 到 11.2/k 都出现过（受年代与 venue 影响）。只能给结构约束。
2. **不得把 Tier B 与 A3 的写法当作者本人风格。** 那些差异恰恰是"作者本人 vs 学生执笔"的分界线。
3. **不得刻意写被动语态。** 完整剔除理由见 `overgeneralization_blacklist.md` 第三类。
