# 研究思维 DNA（袁非牛）— 跨篇高层模式

来源：22 篇逐篇推理链（`reasoning_chains.md`）+ 45 个模块的问题-目的-命名对应表（`../evidence/method_component_map.csv`）+ 闭环核对表（`../evidence/evidence_chain.csv`）。

按 00 号规则：只描述文本里能看出来的推理组织方式，不声称知道作者真实心理，不为拟合虚构技术事实。

**读法**：R1–R3 是核心，有 10 篇以上支撑且跨主题跨年代成立。R4–R7 是次级模式，有 4–9 篇支撑。R8 是单篇独特案例，不进核心 DNA 但值得记录。

---

## R1｜把表面症状收敛为"某类信息缺失"，再让模块名承载这类信息（核心）

- **模式**：不管起点是精度低、误报多还是速度慢，诊断的落点始终是"某类信息被丢弃 / 未被建模 / 丢失了"。紧接着提出的模块用这类信息命名，于是模块名本身就是诊断结论的重述。
- **可核验证据**：45 个模块里 **35 个（78%）** 的命名直接或部分回指了被诊断为缺失的信息。最干净的几例：
  - 「传统 LBP 直方图完全丢弃了 LBP 码的空间分布」→ `Sub Oriented Histograms of LBP`（31）
  - 「多尺度扩展未涉及尺度间关系」→ `3D local differences across scales`（16）
  - 「上下 LBP 码分解导致信息丢失」→ `joint histograms` 保留共现（19）
  - 「局部空间细节与全局语义信息的矛盾」→ `Cubic-cross Convolutional Attention`（扩感受野）+ `Count Prior Attention`（注入全局计数）（02）
  - 「Curvelet 系数被当整体特征，频间关系未利用」→ `Dual-encoded LBP`（30）
  - 「多尺度融合只用拼接或相加，无法建模跨尺度内在结构」→ `Newton Interpolation Module`（05）
- **诊断动词固定**：`discard / not involve / lose / not be modelled / ignore`。
- **成型时间**：2016 年之后。17（2012）与 21（2011）的诊断用的是统计学习语言（泛化性能差、对旋转光照敏感），没有这一层。
- **Confidence**：high。跨 2016–2026、四种主题、四个 venue、A1/A2/A3 三层都成立。
- **Avoid**：不要提出一个与诊断出的信息缺失无关的模块；不要用 "performance is limited" 代替具体的信息缺失描述。

## R2｜互补双路：让两个分支承担不对称的角色，再专门设计融合（核心）

- **模式**：先论证两类表示各有所长且缺陷互补，然后并列两条路，最后**把融合本身当成一个需要单独设计的模块**——这一步是关键，他很少用简单相加或拼接了事。
- **不对称角色的具体分工**（跨 12 年反复出现）：
  - 深/浅：`deep path for global context / shallow path for local fine information`（08）
  - 粗/细：coarse 与 fine 两条分割路径（08）
  - CNN/Transformer：`CNN for spatial and contextual features / Transformer for long-range dependencies`（12、13、06）
  - 空域/频域：spatial 与 Curvelet 域（30）、Fourier 频域与空域（10、09）
  - 空间/通道：SEM 管空间细节、CAM 管通道依赖（03）；HPA 管空间、MSCA 管通道（36）
  - 分割/分类：分割主干 + 分类辅助分支（07、04）
  - 两个坐标系：双坐标系估计两个方向（31）
- **融合被单独设计的证据**：`Feature Complementary Module`（12）、`Bi-directional Attention Gate`（13，双输入双输出）、`Multi-level Attention Coupled Module`（06）、`Feature Fusion Module + Global Coefficient Path`（03）、`a very small network containing only add, convolution and activation layers`（08）、`Adaptive Feature Fusion`（36）。
- **元论证句**：`Combinative methods can keep individual benefits of different algorithms for final purposes`（12）／`Combinative methods utilize the individual benefits of different algorithms`（13）／`Features by different methods have respective advantages, so it is natural for us to combine different features together`（19）。
- **Confidence**：high（12 篇以上支撑，跨 2016–2026）。**但注意 12 与 13 的元论证句几乎同句且共用引用编号 [33]，独立证据实为 19 与 12/13 两组。**
- **Avoid**：不要在方法本身没有对偶性时硬造双路；不要用裸的 concat/add 当融合（他明确把这当成被批评的对象，见 05 的 `instead of feature concatenation or summation`）。

## R3｜任务粒度阶梯：主动把问题定义得更难，并在正文论证升级的合理性（核心）

- **模式**：他不只是换任务，而是**显式论证新任务比旧任务提供更多信息、也更难**，把粒度升级本身当成贡献。
- **原文证据**：
  - `smoke segmentation is a far more difficult task than smoke recognition`（08）
  - `Smoke segmentation offers more information than smoke detection since it performs dense prediction over each pixel`（01）
  - `Smoke density estimation provides more information than smoke segmentation, but it is far more challenging than smoke segmentation`（01）
  - `Image based smoke detection has two basic tasks, which are recognition of smoke and localization of smoke`（20）
- **标题上的粒度演进**：detection（2011、2012、2016、2016、2017）→ recognition（2018、2019）→ segmentation（2019、2022、2023、2026）→ density estimation（2020）。
- **配套动作**：粒度升级带来标注困难时，他用合成数据解决而不是回退任务（01 用 3D 流体仿真生成 RGBA 纯烟并线性混合背景；08 用图像合成生成分割数据集）。这是"把难题拆成可解的子问题"的具体做法。
- **Confidence**：high（限烟雾系列）。非烟雾主题的五篇（11、12、13、18、36）不参与这个阶梯，直接用领域标准任务名。
- **Avoid**：不要用比实际贡献更强的任务名——他在正文里明确区分了这几级。

## R4｜代价维度是一等目标，不是附属说明

- **模式**：参数量、FLOPs、推理速度被当成与精度并列的目标，会写进标题、摘要、结论，并在精度落后时用来完成非对称让步。
- **证据**：03 的标题就叫 `A lightweight network`，摘要与结论都强调 `less than 1 M network parameters`；36 的标题含 `Efficient`；09、10 为实时性单列 Results 小节；36 用 `removing AFF reduces parameters by only 8%, but PSNR decreases by 0.16dB` 反向论证模块必要性；10 用 `approximately 57x fewer parameters` 的倍数表达。
- **Confidence**：high（轻量类论文，2023 年后尤为明显）。
- **Avoid**：不要只在结论提代价而实验不报；不要用"很快"这类无数值表述。

## R5｜阈值敏感性是他最持久的攻击点

- **模式**：批评传统方法时，最常用的落点是"依赖预先指定的阈值，而阈值随场景变化"。这个攻击点从 2011 一直用到 2020。
- **证据**：21 的 `Histogram equalization is often performed ... However, histogram equalization may decrease other characteristics`；31 的 `It is very difficult for users to specify appropriate thresholds, which greatly affect experimental results`；19 的 `LTP uses a pre-specified threshold`；01 的 `Background models greatly depend on pre-specified thresholds, which vary in different scenes and burning materials, so the selection of thresholds greatly affects detection results`；16 的 `dynamic feature extraction requires background modeling or frame differences, which are often based on thresholds`。
- **对应的设计倾向**：用可学习的量替代人工阈值（11 用回归学置信比替代固定比值；17 用 AdaBoost 选特征替代预先指定特征；16 用学习的投影矩阵替代手工设计）。
- **Confidence**：high（2011–2021，5 篇以上直接证据）。
- **Avoid**：这个攻击点在深度学习时代已基本失效，写当代论文时不要套用；他自己在 2022 年后也换成了"感受野/长程依赖"这类结构性攻击点。

## R6｜问题、模块、贡献、消融、图表五者互相镜像

- **模式**：Introduction 枚举的难点数量、贡献列表的条数、Methods 的模块数、消融变体数、定性图的面板组数之间保持对应关系，读者可以逐项对照。
- **证据**：16 号最典型——Introduction 显式写 `The main flaws of LBP-like methods are three folds: (1)(2)(3)`，贡献列表四条，Methods 五个小节，消融覆盖学习类方法对比与 SOTA 对比。01 号的消融图 Fig. 8 四个面板逐级加一个组件，与 Table I 的四个变体行一一对应。13 号的失败案例图 Fig. 9 被 Conclusion 的局限段逐行引用（`as shown in the top three rows` / `as shown in the bottom three rows`）。
- **可核验数据**：45 个模块中 38 个有对应消融变体（84%）。
- **Confidence**：high（作为可校验的自洽性要求）。
- **Avoid**：不要出现 Methods 里有但消融没测的模块；不要让图注的面板描述与消融表的变体名不一致。

## R7｜借用外部数学工具时先复述再改造

- **模式**：当方法建立在一个成熟的外部工具上（LBP、LTP、Curvelet、KPCA、GPR、Newton 插值），他会专设一个小节把该工具讲清楚（含公式），再用后续小节讲自己的改动。
- **证据**：`2.1 Local Binary Patterns`（31）、`3.1. Local binary patterns`（19）、`A. LBP features / B. KPCA / C. GPR`（20，四节里三节是复述）、`3.1 Curvelet transform`（30）、`3.2.2. Newton interpolation theory`（05，2025 年仍如此）。
- **触发条件**：**是否借用外部工具，不是年代。** 05 号是 2025 年的深度网络，但因为借了 Newton 插值，同样设了复述小节。
- **副作用**：这类论文的目的从句密度明显偏低（20 号 Methods 只有 1 个），因为复述小节不需要交代"我们为什么造这个"。
- **Confidence**：high。
- **Avoid**：复述小节里不要夹自己的改动；纯网络论文里不要插 CNN/Transformer 的教科书式介绍。

## R8｜元层面统一：把已有方法放到同一个坐标系里，再在坐标系上取一个新点（单篇，独特）

- **模式**：11 号（去雾）做了一件全语料唯一的事——它没有直接提新模块，而是先把三个已知先验（暗通道先验、滤波先验、颜色椭球先验）统一到"通道最小值升序曲线"这一条曲线上，指出每个先验都对应曲线上的某个点，然后提出"取一个可调的点"作为新先验。
- **原文**：`we individually put the values of several existing image dehazing priors on the curve of sorted values to propose a framework for unifying and understanding these priors. Then we propose a confidence ratio to specify the probability of each channel-minimized value within a range, and thus we can intuitively find a suitable point from the curve, which is actually defined as a novel prior.`
- **为什么值得记录**：这是最高抽象层的一次论证——贡献不是一个模块，而是一个把竞争者全部纳入的参数化框架，自己的方法只是框架里的一个可控参数。
- **Confidence**：**low（单篇）**。不进核心 DNA。
- **备注**：这篇的 Results 也是全语料因果解释密度最高的（4 条 flat + 多条 hedge），且 Discussion 段是清洗者合成的，不可作证据。

---

## 明确不作为研究思维特征的项

1. **"受某成功方法启发"（Inspired by ...）** —— 学术论文通用叙述方式，不是个人思维特征。保留的是它在 Related Work 末段的**位置固定性**（19/19 篇），那属于结构规则 R5 而非思维 DNA。
2. **"消融验证每个模块"** —— 深度学习时代的领域标准做法。保留的是"消融变体按递进式逐级加回组件"这个具体形式（01 号 Fig. 8）。
3. **"用合成数据解决标注困难"** —— 这个做法本身在烟雾领域已相当普遍。保留的是它与 R3（任务粒度升级）的绑定关系：他是为了支撑更难的任务定义才去做合成数据。
4. **主题相关的技术偏好（LBP 家族、注意力机制、频域变换）** —— 这是研究方向而不是思维方式，已排除。
