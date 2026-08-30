# P2 反例、剔除项与不确定性

本文件记录三类内容：反例（与规则不符的 Tier A 篇目）、被判为通用学术英语或模板而剔除的候选、以及混杂风险与不确定项。
P5 做证据裁决时必须先读本文件再定 confidence。

---

## 一、结构性反例：21 和 17 是"最不模板化"的两篇，不能当结构原型

这两篇是全语料唯一的独著论文，也是 Tier A1 里作者身份最确定的两篇（零合作者混杂）。但恰恰是它们不符合多数结构规则：

| 规则 | 21（2011，独著） | 17（2012，独著） |
|---|---|---|
| 独立 Related Work | 无（综述在 Introduction 1.1/1.2） | 无（综述在 §1） |
| 贡献列表 | 无（用 `at least two innovative ideas. First, ... Second, ...`） | 无（用 `The first contribution is ... The second contribution is ...`） |
| 标题 for 铰接 | 不符（任务在前，用 with） | 符合（但塞了四个槽位，20 词） |
| 摘要模块巡览 + 目的从句 | 不符（纯步骤枚举 `Firstly/Secondly/Thirdly/And fourthly`） | 符合 |
| 章节路线句 | 无 | 有 |
| 信息缺失式诊断（I6） | 无（停在"对旋转和光照敏感"） | 无（用统计学习语言：泛化性能、形状可变） |

**结论：他的"结构 DNA"是 2016 年之后成型的，2011–2012 的独著论文只能用于语言层面取样，不能用于结构层面建模。** 这一点必须带进 P4 和 P5，否则会把"最纯的作者身份"和"最典型的作者结构"混为一谈。

另外 31（2016）虽然有贡献陈述和路线句，但仍无独立 Related Work，属过渡形态。

## 二、被剔除或必须降级的候选（判为通用学术英语 / 领域惯例 / 出版社模板）

1. **`The remainder of this paper is organized as follows.`** — 期刊模板句，IEEE 与 Elsevier 稿件普遍存在。22 篇里 14 篇有。**剔除出个人风格**。仅保留其子特征"展开到小节级"（02、07、08 三篇），且标为 medium-high。

2. **`Experiments show that our method outperforms state-of-the-art methods.`** — 通用学术英语。22/22 出现只能证明他遵守惯例。**句式本身剔除**；保留的是"摘要里不给数字"（21/22）这一条可判别行为。

3. **一句一方法的 `Author et al. [n] proposed ...` 综述节奏** — 计算机视觉综述的领域惯例，几乎所有 CV 论文都这样写。**作为个人风格剔除**；保留的是叠加在上面的条件式缺陷从句（R4/I5）。

4. **`above-mentioned` / `aforementioned` 回指** — 通用学术英语。高频（12 篇）但不独占。**降级为 medium 偏好**，不进核心 DNA。注意语料内拼写不统一（`abovementioned` 与 `above-mentioned` 在 03 号同篇并存），这属笔误习惯，不可复刻。

5. **编号贡献列表（`1) 2) 3)` vs `(1)(2)(3)` vs bullet）** — 与 venue 模板强相关：IEEE 稿件多 `1)`，Elsevier 出现 `(1)` 与 bullet 两种。**格式选择剔除**；保留"3 项为众数"与"每项目的优先"两个子特征。

6. **`A/An + 评价形容词` 标题开头（T4）** — 明显 venue 相关。无冠词开头集中在 IEEE（04、07、09、10、13、18、20 全部无冠词），`A/An` 集中在 Elsevier。**降级为 medium，并强制标注 venue 条件。**

7. **`we propose` 高频** — 纯通用。不作为任何规则的证据。

8. **术语高频词（smoke、segmentation、feature、attention、network）** — 主题决定，不是风格。已排除。

## 三、混杂风险与必须扣减的重复计数

1. **03 与 07 的难点枚举高度重合。** 07 写 `inconspicuousness of small smoke, highly complicated texture by blending semi-transparent smoke and different background, multiple scales of smoke at fire different evolving stages, and disturbance of smoke-like objects, such as haze and clouds`；03 写 `unremarkable objects of small smoke, complex textures of translucent smoke mixed with complicated backgrounds, multi-scale smoke at different stages of fire evolution, and interference of haze, cloud and other smoke-like objects`。四项逐项对应，只换了同义词。07 与 Lin Zhang 共同一作，03 与 Kang Li 共同一作。**这是同一课题组的复用文本，I4 的证据计数已按 1 篇而非 2 篇处理。**

2. **12 与 13 的"合并各自优点"元论证几乎同句且共用同一引用编号 [33]。** 12（2023）`Combinative methods can keep individual benefits of different algorithms for final purposes [33].`；13（2024）`Combinative methods utilize the individual benefits of different algorithms [33].` **R9 的独立证据实际只有 19 与 12/13 两组，confidence 已定为 medium。**

3. **09 与 10（Tier B）复用了同一套结构模板**，且两篇一作都是 Kang Li，参考文献高度重叠。它们对 R1/R2/R5/A3/I8 的"支持"实际上说明**这套结构是课题组模板，会传给学生**，而不是袁非牛个人独有。这是本阶段最重要的混杂结论：
   > **P2 归纳出的结构规律（尤其 A3、I8、R1、R2、R5）在课题组层面复现，无法排除"实验室写作模板"这一解释。它们仍然可用于生成符合该作者风格的文本，但不得声称是他个人的独特标识。**
   05（Guiqian Wang 起草）、06（Kang Li 起草）也符合同一套结构，进一步支持这个解释。

4. **02 号清洗版本的括号引用数为 0**，因为 reader 提取时把编号引用替换成了作者名叙述。**不得用 02 做任何引用密度结论。** 引用密度的可用样本是其余 21 篇。

5. **17 号提取质量中低**，公式全部排除、Introduction 有两处 `[sentence head lost in extraction]` 与 `[sentence truncated in extraction]`。它对 I5（条件式失效）的支持来自完整保留的句子，可用；但不得用于任何长度、密度或段落数统计。

6. **主题混杂对 I1/I2 的影响已确认。** "真实代价开场"与"传统方案物理失效"两条在烟雾与医学论文成立，在超分（36）与去雾（11）不成立或形式退化。两条规则均已标注主题条件。这五篇非烟雾论文（11、12、13、18、36）是 P4 做主题去混杂的对照组，已在 `../corpus/tierA_list.md` 标注。

## 四、内部不一致（同一作者违反自己的较优实践）

1. **03 号违反 R8/I7。** 它在 Introduction 里直接点名 ENet、BiSeNet、ERFNet、LEDNet、DFANet 并逐个评价，与 Related Work 2.1 明显重叠；而 02、08 用抽象层级差干净地避开了重叠。说明 I7/R8 是他的较优实践而非铁律，规则 confidence 已定为 medium-high。

2. **36 号（2025，A1）的定位段最弱。** 只写 `there remain some improvements to be achieved, such as better balances between reconstruction accuracy and efficiency`，没有说明自己与谁不同。同时它的结论强度也是全语料最保守（`competitive performance`）、且无章节路线句。这三点同时出现在同一篇最晚期 A1 论文上，可能提示晚期写作变松，但**单篇不足以成为趋势**，需要 P3/P4 用 Methods 与 Results 的证据来判断。

3. **03 号摘要里的 `However` 用作让步而非转折**：`Experiments show that our method is significantly superior to existing state-of-the-art algorithms ... However, our method has less than 1 M network parameters.` 这是作者原文用法（清洗时按原样保留），语义上应为 `Moreover/Meanwhile`。属个别笔误，不建模。

## 五、遗留不确定项（交给 P3–P5）

1. A5（确定性强度分层）与结果实际强弱的对应关系需要 P3 的 Results 分析确认。目前只能确认"分层存在"且"不由年份或作者地位决定"。
2. I6（信息缺失式诊断）与 Methods 里模块命名的对应关系，需要 P3 建 `method_component_map.csv` 后才能完成闭环验证。
3. 引用密度的绝对数值未纳入规则，因为各篇提取完整度不同（括号引用总数 9–81）。若 P3 需要密度指标，应先按 `../corpus/section_coverage.csv` 剔除提取受损篇目。
4. Related Work 的样本量是 19。若 P5 要给 R 系列规则定 high，必须核对该规则在 19 篇里的实际覆盖数，而不是 22。
5. 04、18 两篇 A3 只做了结构核对，未逐段精读。它们由学生主导起草（04 共同一作是 Lin Zhang 与 Jing Wu，18 主导团队是 Wen/Huang/Ma），按 P1 约束本就不作一手语言证据，但如果 P4 需要它们的段落级证据，需回补精读。
