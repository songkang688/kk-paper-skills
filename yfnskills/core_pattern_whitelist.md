# 核心规则白名单（可直接指导写作）

裁决标准（P5 统一执行）：
- **high**：3 篇以上 Tier A 支撑，跨年代或跨主题成立，无有力反例
- **medium-high**：3 篇以上 Tier A 支撑但有明确适用条件，或有可解释的反例
- **medium**：2 篇以上 Tier A 支撑，或存在文本复用需扣减计数
- **low**：单篇依赖、有明显反例、或与通用学术英语区分不开 → **不进本白名单**，移入 `overgeneralization_blacklist.md` 留档

登记表 93 条规则中，80 条进入白名单，13 条移出。完整字段见 `evidence_register.csv`。

---

## 第一层：跨章节主干（6 条，全部 high 或 medium-high）

这六条是 Skill 的骨架。生成任何章节时都必须满足。

| ID | 规则 | Confidence | 关键判据 |
|---|---|---|---|
| **X1** | **目的在前、机制在后**：`To <purpose>, we <propose/design/adopt> <Module (ABBR)>` | high | 17 篇 Tier A 支撑；四个章节全部 > 3/k；**Tier B 的 Conclusion 密度为 0，A3 的 Results 仅 1.4/k，说明会向学生衰减，属个人特征** |
| **X2** | **缺陷收敛为"某类信息缺失"，模块名承载该信息** | high | 10 篇直接证据；45 个模块中 35 个（78%）命名可核验回指；2016 年后成型 |
| **X3** | **`our` 在 Results 暴涨、`we propose` 在 Conclusion 达峰** | high | 全 22 篇方向一致（Results 的 our 为 10.9–24.4/k；Conclusion 的 we propose 为 10.1–16.8/k） |
| **X4** | **过去时严格限于 Results** | high | Front/Methods/Conclusion 的过去时实验动词中位数全部为 0 |
| **X5** | **证据锚点严格限于 Methods 与 Results** | high | Front 与 Conclusion 的锚点密度为 0；白名单例外见下 |
| **X6** | **锚点与 `we find that` 合写** | medium-high | `we find that` 30 次，23 次在 Results |

**X5 的两个白名单例外**：Introduction 允许引用一次难点示例图（07 号）；Conclusion 的局限段允许引用失败案例图（13 号）。

## 第二层：章节规则（按写作顺序，58 条）

### Title（5 条进白名单，T4 移出）
- **T1** high｜机制在前任务在后用 `for` 铰接。18 篇 Tier A；反例仅 08（三词极简）与 21（任务在前用 `with`）。
- **T2** high｜标题写机制全称，缩写留给摘要首次定义。22 篇标题含网络缩写者为 0。
- **T3** medium-high｜机制槽位偏好成对双路命名（`Dual-` / `Bi-` / `double` / `A and B complementary`）。7 篇。
- **T5** high（限烟雾）｜任务名取最精确粒度并在正文论证升级。
- **T6** medium｜槽位不超过两个，9–14 词；不得写数据集名、参数量、性能数字。

### Abstract（6 条全部进白名单）
- **A1** medium-high｜首句难点归因到对象物理/视觉属性。10 篇。
- **A2** high｜钩连句 `To solve these problems, we propose X (ABBR)` 并回指第一句难点。12 篇。
- **A3** high｜逐模块巡览，每模块前置目的从句，用 `first → then → In addition → Finally` 串联。17 篇。
- **A4** high（仅"不给数字"）｜结尾固定 `Experiments show that ...`；**21/22 篇摘要不给具体数值**（唯一例外 19 号）。句式本身是通用英语，只有"不给数字"进白名单。
- **A5** medium-high｜确定性强度分层，与年份和作者地位无关（36 号 2025 A1 用最保守的 `competitive`）。
- **A6** medium-high｜180–260 词，长度增长花在模块数不在背景。

### Introduction（8 条进白名单，I8 移出）
- **I1** medium-high｜首段落在真实世界代价上，不写 `has attracted increasing attention`。
- **I2** high（限烟雾）｜传统方案物理前提失效式过渡。非烟雾主题不适用。
- **I3** high｜显式任务分类或流程分解（`can be classified into N categories` / `consists of N steps, which are ...`）。7 篇，跨烟雾与医学。
- **I4** medium-high｜难点用 `N folds` 或 `The main reason(s) may be` 枚举，归因到对象属性。**已扣除 03 与 07 的文本复用。**
- **I5** high（手工特征期）/medium（深度期）｜缺陷写成条件式失效（`If the scene lacks ..., the method may give false alarms`）。
- **I6** medium-high｜用 `The first way ... Another way ...` 压缩解法为 Related Work 留展开空间。
- **I7** high（2019 后，仅项内写法）｜贡献列表 3 项为主，每项以目的或动作开头，末项整合成整个网络。**编号与 bullet 的格式选择是 venue 模板，不进白名单。**
- **I9** medium-high（仅小节级）｜章节路线句展开到小节级（`Section II-A ... II-B ... II-C`）。**路线句本身是模板句，不进白名单。**

### Related Work（7 条进白名单，R3 与 R6 移出）
- **R1** high｜分类轴按技术谱系切，不按时间切。38 个小节标题中按时间命名者为 0。
- **R2** medium-high｜末小节留给本文贡献所属谱系。10:3。
- **R4** high｜缺陷从句紧贴方法句，并在小节末收敛到本文要补的信息。
- **R5** high｜Related Work 以定位段收尾（`Inspired by ...` 或 `However, above-mentioned methods do not ...`），段内必有显式差异化。**19/19 篇无例外**（样本量是 19，不是 22）。
- **R7** medium-high｜自引用第三人称化（`Yuan et al. [n] proposed ...`），不加自我背书。唯一反例是 19 号的 `In our previous work`。
- **R8** medium-high｜用抽象层级差控制与 Introduction 的重叠。
- **R9** medium｜跨谱系借用时声明合并各自优点。**12 与 13 措辞几乎同句且共用引用 [33]，独立证据实为两组。**

### Methods（6 条进白名单，M4 移出）
- **M1** medium-high｜Methods 开头给总览小节并交代数据流。9 篇。
- **M2** high｜每个组件小节首句先重述要解决的问题。与 X1 同源。**触发条件是"模块是否原创"，不是年代**（20 号复述既有算子，只有 1 个目的从句）。
- **M3** medium-high｜模块内部按输入→操作→中间表示→输出推进，尺寸与通道数显式写出。
- **M5** high（深度学习论文）｜损失函数是 Methods 最后一个小节。手工特征论文的等价位置是分类器小节。
- **M6** medium-high｜前提在前、后果在后，用逗号 + `so` 收尾。**注意 `so that` 全语料仅 6 次且 4 次集中在 16 号，不是习惯。**
- **M7** high｜借用外部数学工具时先复述再改造。触发条件是是否借用工具，不是年代（05 号 2025 年仍如此）。

### Results（8 条全部进白名单）
- **RS1** medium-high｜消融在前、比较在后。8:4。
- **RS2** high（做法）｜每个观察挂在显式证据锚点上。
- **RS3** medium-high｜因果解释分两档：可核验的架构或数据事实用 `The reason is that`；不可核验属性或不利结果用 `The reason may be that`。**全语料 50 条：flat 33 / hedge 17。**
- **RS4** high（A1/A2 层）｜次优结果用非对称让步：`slightly` 描述对手优势，`obviously / distinctly / nearly` 描述自身优势。**Tier B 已退化为 `comparable`。**
- **RS5** high（2019 后）｜消融与模块一一对应，用递进式变体。38/45 模块有对应消融。
- **RS6** high（限烟雾）｜真实场景与视频测试单列小节。11 篇。
- **RS7** high｜Results 只做观察与机制解释，不做意义升华。22 篇无升华句。
- **RS8** high（轻量类）｜实时性与复杂度作为独立维度报告，用倍数表达代价优势。

### Discussion（1 条进白名单，D1/D2/D3/D5 移出）
- **D4** high｜**默认不写独立 Discussion，把内容三分**：机制解释进 Results、局限与未来工作进 Conclusion 末段、文献对比判断进 Related Work 定位段。18 篇支撑。
- 其余四条（D1/D2/D3/D5）全部单篇依赖，移入黑名单留档。**Discussion 的实际样本量是 1。**

### Conclusion（6 条全部进白名单）
- **C1** medium-high｜开头重述难点，且比摘要更具体。
- **C2** high｜模块复述保留目的从句。13 篇。与 X1 同源。
- **C3** high｜与摘要的信息差：增加难点展开、机制细节、局限与未来工作；不增加新数字与新对比对象。
- **C4** medium-high（仅时态分工）｜方法现在时、实验过去时。**被动语态的高低是纯年代效应，已剔除。**
- **C5** high（趋势）/medium（机制）｜局限与未来工作段给机制不只给现象；未来方向指向具体技术。9 篇，其中 8 篇在 2023 年后。
- **C6** medium｜坦诚式限定，主动降低自己组件的必要性。19 与 21 两篇三处。

### Figures / Tables / Captions（6 条进白名单，V7 移出为剔除项）
- **V1** high（两档分化）｜图注分两档：架构图短名词短语，比较与消融图长枚举。
- **V2** high｜**多面板顺序固定，our method 永远是最后一个面板。6 图零反例，是全语料唯一可机械校验且无例外的规则。**
- **V3** medium-high｜颜色语义在图注显式定义，且每张用到该约定的图都重复一遍。
- **V4** medium｜消融图用递进式面板，每个面板比前一个多一个组件。
- **V5** high（仅"单行名词短语"）｜表格标题是单行名词短语。**大小写形式是 venue 模板，已剔除。**
- **V6** medium-high｜图的角色分工七类且位置固定。

## 第三层：微观语言与句式（12 条进白名单）

- **MS1** high｜句长 17–22 词；四节之间几乎不变；Conclusion 控制在 25 词内。**建模 Conclusion 时扣除 03、06、09、10（Kang Li 参与，句长 26.6 词）。**
- **MS2** high｜段落长度是区分章节的手段：Methods/Results 每段 80–90 词，Conclusion 允许 150–200 词单一长段。
- **MS3** high｜Conclusion 主体不 hedge、不用因果尾句、不用证据锚点；不确定性集中到局限段。
- **MS4** medium-high（仅落差）｜Front 与 Conclusion 抽象名词化、Results 具体动词化。**名词化的绝对水平是主题词汇效应，已剔除。**
- **S1/S2/S3/S5/S6/S7/S8**｜七种功能转移，分别对应 X1、X2、M6、RS2、RS4、RS3、R5。详见 `dna/sentence_patterns.md`。
- **CX1** medium（仅用法）｜`not only ... but also ...` 在贡献与结果句里成对绑定价值点。35 次，全语料最高频构式。
- **CX2** medium-high｜`we find that`（30 次，23 次在 Results）。
- **CX4** high｜`slightly` 作让步关键副词（20 次，18 次在 Results）。

## 第四层：研究思维（6 条进白名单，RD8 移出）

- **RD1** high｜信息缺失式诊断与模块命名闭环（同 X2）。
- **RD2** high｜互补双路：让两分支承担不对称角色，再**专门设计融合模块**，不用裸 concat 或 add。12 篇。
- **RD3** high（限烟雾）｜任务粒度阶梯与升级论证。
- **RD4** high（轻量类）｜代价维度是一等目标。
- **RD5** high（2011–2021，限早期风格）｜阈值敏感性是最持久的攻击点；对应设计倾向是用可学习量替代人工阈值。**写当代论文不得套用。**
- **RD6** high｜问题、模块、贡献、消融、图表五者互相镜像，可逐项对照。

---

## 使用优先级

写作时若规则冲突，按此顺序取舍：

1. **事实性红线**（见 `SKILL.md`）永远优先于任何风格规则。
2. **第一层跨章节主干**（X1–X6）优先于章节规则。
3. **high** 优先于 **medium-high** 优先于 **medium**。
4. 带条件的规则（限烟雾、限轻量类、限早期风格）在条件不满足时直接跳过，不要变形套用。
