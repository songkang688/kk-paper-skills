# Introduction Playbook（袁非牛）

证据基础：22 篇 Introduction 全文（其中 16 篇逐段精读，6 篇结构核对）。
逐段 move map 见下；结构统计见 `../_work/p2_struct.txt`。

标准 move 序列：
`应用与真实代价 → 传统方案及其物理局限 → 任务分类/流程分解 → 任务难点枚举（归因到对象属性）→ 现有方法逐条评述并附条件式失效 → 表示层面诊断 → 设计动机与模块预览 → 贡献列表 → 章节路线`

其中第 3、4、6 步和贡献列表的写法是可辨识度最高的部分；第 1、2 步受主题强约束；第 9 步是模板句，不算个人风格。

---

## I1｜第一段落在真实世界代价上，不落在"研究热点"上

- **When**：写 Introduction 第一段。
- **Why**：他的开场一律指向具体后果（火灾伤亡、财产损失、消防员安全、临床诊断负担），而不是"该方向受到广泛关注"。
- **Do**：第一段写清"这个任务失败会导致什么真实损失，以及谁受益"。
- **Language/Structure**：
  - `Smoke detection is necessary and important for public safety and security, since smoke always emerges before flame.`（01）
  - `Segmented smoke regions not only provide an important clue for fire detection, but also accurately indicate the location of fire. It is very important for realizing automatic fire detection in intelligent robots to avoid casualties of firefighters.`（07）
  - `Smoke segmentation is very important for early fire detection that can avoid casualties and property losses. In addition, some leaky chemical substances may produce colored smoke, so smoke segmentation methods can help guide inspection devices to precisely locate the leaky point ...`（03）
  - `Melanoma is a common skin tumor of high malignancy ... Traditionally, malignant skin lesions can be manually labeled and reviewed by experienced dermatologists, but the process is exceedingly cumbersome and time-consuming.`（13）
- **Evidence**：真实代价开场出现在 01、03、07、13、19、21、30、31、02 等篇，跨 2011–2024，跨烟雾与医学。03、07 还会额外补一个"次级应用场景"来扩大意义（化学品泄漏定位、智能机器人）。
- **Counterexamples**：36（超分）和 12（医学分割）走的是纯任务定义开场，没有代价陈述；11（去雾）落在"影响下游视觉任务"这个技术性代价上而非人身代价。
- **Confidence**：medium-high。在烟雾与医学主题上稳定；在低风险任务（超分）上不适用。
- **Avoid**：不要写 "has attracted increasing attention in recent years"、"has become a hot topic"；语料的 Introduction 首段 0 次使用这类句式。

## I2｜第二段用"传统方案的物理局限"完成向本领域的过渡（主题条件）

- **When**：任务存在一个非视觉的传统替代方案（传感器、人工标注、插值算法）。
- **Why**：他习惯先立一个具体的旧方案当靶子，用它的物理限制推出视觉方法的必要性，而不是空泛地说"传统方法效果不好"。
- **Do**：写清旧方案的工作原理 → 它必须满足的物理前提 → 该前提在目标场景下不成立 → 因此需要视觉方法。
- **Language/Structure**：
  - `Traditional smoke detectors usually detect the presence of combustion products through an ionization or photometry based sensors. But it takes a long time for combustion products to reach these sensors in outdoor or open spaces and in the case of a strong wind, combustion products may even be blown away, thus failing to give fire alarms.`（21）
  - `Exposure of traditional fire sensors to combustion products is required because these sensors need to analyze particles, temperature or humidity. Hence, traditional fire sensors must be installed in close proximity to fires. This limits conventional fire detection technologies to applications only in small or indoor spaces.`（19）
  - `These detectors are usually required to be installed in the close proximity of fires; otherwise fires cannot be detected at all.`（17）
  - `Traditional interpolation methods, such as bilinear and bicubic resampling, provide a basic solution to image super-resolution, but they often produce over-smoothed edges and fail to recover high-frequency details.`（36，同一逻辑迁移到超分）
- **Evidence**：8 篇烟雾论文（21、17、19、31、20、30、02、01）都有这个"传感器物理前提失效"段落，措辞高度一致（`installed in close proximity` / `combustion products` / `open or large spaces` 反复出现）。36 号把同一论证形式迁移到了插值算法上。
- **Counterexamples**：11、12、13 没有这个段落，直接进入方法谱系。所以这是**主题条件下的模式**，不是无条件规律。
- **Confidence**：high（限烟雾主题）／medium（作为可迁移的论证形式）。
- **Avoid**：不要在没有传统替代方案的任务上硬造这一段；不要把旧方案写成"精度低"，要写成"物理前提不成立"。

## I3｜显式的任务分类或流程分解，用可数结构写出来

- **When**：进入方法评述之前，需要给读者一个坐标系。
- **Why**：这是他最稳定的组织习惯之一：先把领域切分成可数的类别或步骤，后面所有讨论都挂在这个切分上。
- **Do**：用 `can be classified / divided / categorized into N categories` 或 `consists of / contains N steps, which are A, B, and C` 显式给出切分，并给每一类命名。
- **Language/Structure**：
  - `Video-based fire detection is one of the computer vision-based methods and can be classified into two categories: video-based flame and video-based smoke detections.`（21）
  - `According to objects for detection, vision based fire detection methods can be classified into two categories: flame detection and smoke detection.`（31）
  - `Strictly, smoke detection can be divided into two categories. The first category is to merely judge whether there is smoke in an image or not. It is also known as whole image smoke recognition. The other one is not only to identify whether there is smoke, but also to indicate the accurate location of smoke.`（08）
  - `Visual smoke detection can be roughly categorized into traditional and deep learning-based methods.`（01）
  - `Image based smoke detection has two basic tasks, which are recognition of smoke and localization of smoke, respectively.`（20）
  - `The general framework of single frame-based smoke detection in large wild scenes mainly contains three steps, which are image partition, feature extraction for every patch, classification of each patch and holistic decision of an image.`（16）
  - `In general, a typical CAD system for automatic skin lesion segmentation consists of four steps: image preprocessing, segmentation of skin lesions, image feature extraction, and image classification.`（13）
- **Evidence**：7 篇有显式切分（21、31、08、01、20、16、13），跨 2011–2024，跨烟雾与医学两个主题，跨独著与多作者。`which are ..., respectively` 这个收尾在 20 和 16 中重复出现。
- **Counterexamples**：11、12、36 没有显式切分句，而是靠 Related Work 的小节标题隐式完成切分。02 号把切分压缩成 `The first way ... Another way ...`（见 I7）。
- **Confidence**：high。这是跨主题、跨年代、跨作者位置都成立的组织特征。
- **Avoid**：不要给出切分却不命名类别；不要切成三类以上还不给每类一句解释。

## I4｜难点用"N folds"或"main reason(s) may be"枚举，且必须归因到对象属性

- **When**：论证任务为什么难。
- **Why**：他把难点当成可枚举的清单来处理，而且归因对象始终是研究对象的固有属性，配合一个明显的认知性 hedge。
- **Do**：`The reasons are N folds: 1) ..., 2) ..., 3) ...` 或 `The main reason(s) may be A, B, C, and D.` 每一项都是对象的一个属性。
- **Language/Structure**：
  - `It is a challenging task to recognize smoke from a single image. The reasons are four folds: 1) smoke seriously blurs images and decreases image contrast, 2) smoke appearance is easily affected by environments, 3) smoke usually has translucency property that makes smoke textures mixing with background ones, and 4) smoke boundaries are very fuzzy.`（01）
  - `The main flaws of LBP-like methods are three folds: (1) manually designed features require domain knowledge, (2) multi-scale extensions do not involve relations between scales, (3) high-order extensions lack noise resistance.`（16）
  - `The main reason may be inconspicuousness of small smoke, highly complicated texture by blending semi-transparent smoke and different background, multiple scales of smoke at fire different evolving stages, and disturbance of smoke-like objects, such as haze and clouds.`（07）
  - `The main reason is that the texture in smoke is not as clear as that in other objects, such as leaves or rocks.`（20）
- **Evidence**：`N folds` 结构在 01、16 两篇出现（2020、2018）；`The main reason(s) may be/is that` 的 hedge 化归因在 01、03、07、20、02 出现。hedge 词 `may` 在归因句里高频，说明他不把因果分析写成断言。
- **Counterexamples**：03 号（`The main reasons may be unremarkable objects of small smoke, complex textures of translucent smoke ..., multi-scale smoke ..., and interference of haze, cloud and other smoke-like objects.`）与 07 号的四项难点几乎逐项对应。**这两篇分别与 Lin Zhang 和 Kang Li 共同一作，属于同一课题组的复用文本，不能当成两条独立证据。**
- **Confidence**：medium-high。结构证据充分，但需扣掉 03/07 的重复计数。
- **Avoid**：不要把难点归因到"网络容量不足""训练不稳定"；不要用无 hedge 的 `The reason is` 去写推测性归因。

## I5｜逐条评述现有方法时，缺陷写成条件式失效而不是笼统评价

- **When**：Introduction 里评述他人方法。
- **Why**：他的批评几乎都带触发条件，读起来像故障分析而不是贬低。
- **Do**：`<方法摘要>. If / Once / When <场景条件>, the method may give false alarms / fails / becomes unstable.` 或 `<方法> depends greatly on <前提>, which varies in ..., so ...`
- **Language/Structure**：
  - `If the scene lacks apparent edges or has cluttered objects, the method may give false alarms.`（17）
  - `Once the scene lacks obvious edges or cluttered objects, the method raises false alarms.`（30）
  - `Background models greatly depend on pre-specified thresholds, which vary in different scenes and burning materials, so the selection of thresholds greatly affects detection results.`（01）
  - `Although some methods of texture analysis, such as co-occurrence matrix methods [14], are insensitive to rotation, it depends greatly on illumination conditions.`（21）
  - `The dark channel prior provides an efficient way to enhance the visibility of hazy images, but it cannot accurately handle bright areas and it is sensitive to noises.`（11）
  - `it is very difficult for users to specify appropriate thresholds, which greatly affect experimental results [1]`（31）
- **Evidence**：条件式失效句在 17、30、01、21、11、31、19、02 均可见，跨 2011–2022，跨烟雾与去雾。`depends greatly on` / `greatly affect` 这一对搭配反复出现。阈值敏感性是他最常用的攻击点（01、31、21、19 都提）。
- **Counterexamples**：`Although these methods have achieved encouraging results, but they cannot capture local and global information well.`（13）是笼统评价而非条件式失效；深度学习时代的评述整体更笼统，因为攻击点从"阈值"转成了"感受野/长程依赖"这类结构性缺陷。
- **Confidence**：high（手工特征时代）／medium（深度学习时代，评述趋于抽象）。
- **Avoid**：不要写 `the method performs poorly` 或 `the accuracy is low` 这类无条件断言；语料里没有。

## I6｜把缺陷收敛到"某种信息被丢弃/未被建模"，模块名直接对应被丢的信息

- **When**：从评述过渡到自己的动机。
- **Why**：这是他的核心论证动作：无论表面症状是什么，最终都归结为某类信息缺失，然后提出的模块用名字宣告要补回这类信息。
- **Do**：写 `Although X works well, it discards / does not involve / loses <某类信息>.` 紧接着 `To capture <该类信息>, we propose <以该信息命名的模块>.`
- **Language/Structure**：
  - `Although traditional LBP histograms can represent features of smoke images well, they completely discard the spatial distribution of LBP codes. To extract this spatial distribution information, it is necessary to consider the relationship between the two LBP codes.`（31）→ 模块名 `Sub Oriented Histograms`（承载空间关系）
  - `each LTP code is usually decomposed into an upper LBP code and a lower LBP code, but this leads to loss of information. Hence, we use joint histograms to preserve the co-occurrence of upper and lower LBP codes`（19）
  - `(2) multi-scale extensions do not involve relations between scales`（16）→ 模块 `3D local differences across scales`
  - `The main reason is the contradiction between local spatial details and global semantic information.`（02）→ 模块 `Cubic-cross Convolutional Attention`（扩大感受野）＋`Count Prior Attention`（补全局类别信息）
  - `long-rang dependency information has not been modelled well in most CNN based methods`（12）→ 模块 `Transformer 编码器 + Feature Complementary Module`
  - `the encoding process inevitably leads to losses of local details and global context information`（13）→ 模块 `Bi-directional Attention Gate` + `Boundary Aware Decoder`
- **Evidence**：信息缺失式诊断在 31、19、16、02、12、13、07、01、03、11 均可见，跨 2016–2024，跨全部四种主题，跨手工特征与深度学习两种范式。动词固定在 `discard` / `not involve` / `lose` / `not be modelled` / `ignore` 这一组。
- **Counterexamples**：17 号（2012）的诊断是"泛化性能差、Haar 特征形状可变"，偏统计学习语言而非信息语言；21 号（2011）几乎没有这层诊断，直接从"现有方法对旋转和光照敏感"跳到方法。所以这个论证动作是在 2016 年之后才成型的。
- **Confidence**：high（2016 年之后）。这是最有作者区分度的一条，因为它同时约束了论证方式和命名方式。
- **Avoid**：不要提出一个和诊断出的信息缺失无关的模块；不要用 "performance is limited" 代替具体的信息缺失描述。

## I7｜用"The first way ... Another way ..."压缩现有解法，为 Related Work 留出展开空间

- **When**：论文有独立的 Related Work 章节。
- **Why**：他用这个句式在 Introduction 里给出解法的分支，然后在 Related Work 用小节逐个展开，从而控制两节的重叠。
- **Do**：Introduction 里用 2–3 句概括"业界试过的几条路"，每条路一句话；Related Work 把每条路做成一个小节。
- **Language/Structure**：
  - `The first way of aggregating multi-scale contexts and capturing long-range dependencies has been widely used ... One effective way is to fuse multi-scale feature maps from different levels. ... Another way is to use attention mechanisms.`（02，对应 RW 的 2.1 上下文嵌入 / 2.2 注意力机制）
  - `There are two main ways to deal with this issue [25]. The first way is to feed images with different sizes to the network, but it is time consuming. The second one is to fuse feature maps from different layers using skip operations, hence it is effective and efficient. In our method, we follow the second way to address the scale issue.`（08）
  - `Solutions to this problem can be generally divided into three kinds of techniques: dilation filters, encoder-decoder structures and short-cut connections.`（01）
- **Evidence**：02、08、01、12 均用此压缩式；且这些论文的 Related Work 小节与 Introduction 提到的"way"一一对应。08 号还额外表明了自己选哪条路（`we follow the second way`），这是很干净的定位动作。
- **Counterexamples**：03 号（有 4 个 RW 小节）在 Introduction 里没有对应的压缩句，导致 Introduction 与 RW 2.1 有明显重叠。这是同一作者内部的不一致，注意不要当成规则的必然。
- **Confidence**：medium-high。
- **Avoid**：不要在 Introduction 里就把某条路的具体方法逐个点名（那是 Related Work 的活）；也不要压缩后在 RW 里换一套完全不同的切分轴。

## I8｜贡献列表：3 项为主，每项以目的或动作开头，列表前有固定引导句

- **When**：Introduction 收尾。
- **Why**：他的贡献列表格式稳定，且每一项的内部写法与摘要的目的从句规则（A3）一致。
- **Do**：引导句用 `The main contributions of this paper / our method are summarized as follows:`，然后 3 项（必要时 2–5 项），编号用 `1) 2) 3)` 或 `(1)(2)(3)`。每项首句是 `We propose/design <模块>` 或 `To <目的>, we <动作>`，随后 1–3 句解释该模块如何工作以及为什么有效。最后一项通常是"把前面模块整合成整个网络"。
- **Language/Structure**：
  - 引导句变体：`The main contributions of this paper are summarized as follows`（02、08、12、16、30）／`The main contributions of our method are summarized as follows`（03、11）／`are as follows`（01、13）／`can be summarized as follows`（05、19）／`are listed as follows`（07、30）。
  - 末项整合式：`We propose a Cubic-cross convolutional attention and Count prior Embedding Network (CCENet) for smoke segmentation by stacking ResNet50, CCA and CPA.`（02）／`By fully integrating AEM, SEM, CAM and FFM, we propose an efficient lightweight network ...`（03）／`We propose a Bi-directionally Fused Boundary Aware Network (BiFBA-Net) by integrating a dual-encoding structure ..., a progressive decoding structure ..., and a deep supervision scheme ...`（13）
- **Evidence**：项数分布：2 项（05、11、17、20、31）、3 项（01、02、03、06、07、10、12、13、30、36）、4 项（04、16）、5 项（09）。众数为 3（10 篇）。末项整合式出现在 02、03、13、12 等篇。编号形式与 venue 相关：IEEE 稿件多用 `1)`，Elsevier 稿件出现 `(1)` 和 bullet 两种。
- **Counterexamples**：21 号（2011，独著）完全没有贡献列表，只在 Introduction 末尾用 `This paper presents at least two innovative ideas on the video-based smoke detection. First, ... Second, ...` 代替。19、20、31、17 用序数散文而非列表。所以列表化是 2019 年之后才固定下来的。
- **Confidence**：high（2019 年之后）。**但编号与 bullet 的选择明显受 venue 模板影响，不得当作个人风格。**
- **Avoid**：不要把贡献写成实验结果（"我们取得了 SOTA"不是贡献项）；不要让贡献项数超过 5；不要在贡献项里第一次引入未解释的缩写。

## I9｜"at least N contributions"的谦抑式限定是早期特征，已消失

- **When**：仅在需要复刻 2011–2017 风格时使用。
- **Why**：他早期习惯给贡献数量加 `at least` 这个下限式 hedge，后期完全不用了。
- **Do**：`This paper at least has two main contributions to <任务>.` / `This paper has at least two main contributions.` / `This paper presents at least two innovative ideas on ...`
- **Evidence**：21（2011，独著）`presents at least two innovative ideas`；17（2012，独著）`This paper at least has two main contributions to video smoke detection`；20（2017，一作＋通讯）`This paper has at least two main contributions.`。三篇全部是 Tier A1，全部在 2017 年及以前。
- **Counterexamples**：2018 年之后 19 篇论文中 `at least` 用于贡献数量的次数为 0。
- **Confidence**：high（作为年代标记）／不适用（作为当前写作建议）。
- **Avoid**：写当代论文时不要用这个句式，它会让文本读起来像十年前的稿子。

## I10｜章节路线句：存在但非必需，且他的展开粒度到小节

- **When**：Introduction 最后一句。
- **Why**：这句本身是期刊模板句，没有个人风格价值；但**他展开到小节而不是章节**这一点有辨识度。
- **Do**：若写，用 `The remainder of this paper is organized as follows.` 起头；若上一节有小节，可用省略并置的方式把小节也映射出来。
- **Language/Structure**：小节级路线句：`Related work on semantic segmentation is given in Section II-A, smoke segmentation in Section II-B, and recurrent networks in computer vision in Section II-C.`（07）／`Related work on FCNs for object segmentation is given in Section II-A, and smoke segmentation in Section II-B.`（08）／`Related work on context information embedding is given in Section 2.1, attention mechanism in Section 2.2, and smoke segmentation methods in Section 2.3.`（02）
- **Evidence**：14/22 篇有路线句；缺失的 8 篇是 03、04、10、18、20、21、30、36。小节级并置写法出现在 02、07、08 三篇（都是他自己一作或共同一作的分割系列）。
- **Confidence**：low（作为个人风格）／medium-high（小节级并置这一子特征）。**"The remainder of this paper is organized as follows" 是通用学术英语与期刊模板句，必须标记为非个人风格。**
- **Avoid**：不要把它当作必写项；2025 年的两篇 A1（36）就没有写。
