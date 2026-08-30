# Abstract Playbook（袁非牛）

证据基础：22 篇摘要全文。长度 144–285 词，中位数约 213 词。
逐句 move map 依据：`../_work/p2_front/` 的 Abstract 段；结构统计见 `../_work/p2_struct.txt`。

标准 move 序列（22 篇中 19 篇完整符合）：
`难点/背景 → "To <目的>, we propose <总方法>" → 逐模块巡览（序数连接词 + 目的从句）→ 实验结论`

**这份 playbook 里最重要的一条是 A3（目的在前、机制在后）。它是全语料最稳定、最可操作、也最难被通用学术英语解释掉的特征。**

---

## A1｜开头把难点归因到对象的物理/视觉属性，不归因到数据或指标

- **When**：写摘要第一句。
- **Why**：他不用"该领域很重要"或"现有数据集不足"开场，而是直接点出研究对象本身的哪个属性导致任务难。
- **Do**：第一句给出 `对象 + 具体属性 + 因此难`，属性要是可观察的物理或视觉性质。
- **Language/Structure**：
  - `It is very challenging to accurately segment smoke images because smoke has some adverse properties, such as semi-transparency and blurry boundary.`（02）
  - `It is a challenging task to recognize smoke from visual scenes due to large variations in the color, texture, shapes of smoke.`（19）
  - `Smoke has semi-transparency property leading to highly complicated mixture of background and smoke.`（07）
  - `It is quite challenging to visually identify skin lesions with irregular shapes, blurred boundaries and large scale variances.`（13）
  - `Visual smoke recognition is a challenging task due to large variations in shape, texture and color of smoke.`（30）
- **Evidence**：10/22 用"难点在前"开场（02、04、05、06、07、13、17、19、30、31），且这 10 篇的难点全部归因到对象属性（半透明、边界模糊、形状/纹理/颜色变化大、非刚性）。跨 2012–2025、跨烟雾与医学两个主题。
- **Counterexamples**：5 篇用"目的/方法在前"（03、08、11、16、20），7 篇用"领域/任务定义在前"（01、09、10、12、18、21、36）。所以这不是唯一开场式。特别注意 21（2011，独著）用的是最平淡的领域开场 `Video surveillance systems are widely applied in a variety of fields.`
- **Confidence**：medium-high。作为首选开场式可用；"难点必须归因到对象属性"这一条在所有采用难点开场的篇目里无例外，confidence high。
- **Avoid**：不要把难点归因到"缺少数据集""指标不统一""算力不足"；语料里 0 篇这样写。也不要用 "In recent years, deep learning has attracted increasing attention" 这类空转开场。

## A2｜第二个 move 用一句话给出总方法，并显式回指第一句的难点

- **When**：难点说完，进入方法。
- **Why**：他不会让难点和方法之间出现空档，一定有一句把两者钩住。
- **Do**：`To solve these problems / Aiming at solving these problems / To overcome ..., we propose <总方法名>`。
- **Language/Structure**：
  - `Aiming at solving these problems, we first fuse convolutional results along different axes ...`（02）
  - `To solve these problems, we propose a Classification-assisted Gated Recurrent Network (CGRNet) for smoke semantic segmentation.`（07）
  - `To overcome the difficulties in discriminating small or blurred skin lesions, we propose a Bi-directionally Fused Boundary Aware Network (BiFBA-Net).`（13）
  - `To solve the problem, we stack several convolutional encoder-decoder structures together to propose a wave-shaped neural network, termed W-Net.`（01）
  - `To overcome shortages of conventional hand-crafted features, we propose a learning based feature extraction method ...`（16）
- **Evidence**：19/22 篇有这句显式钩连（缺失的是 21、11、12，它们的摘要用不同的组织方式）。缩写在这一句首次定义（`(CGRNet)`、`(BiFBA-Net)`、`termed W-Net`），与标题规则 T2 配套。
- **Counterexamples**：11 号（去雾）把方法直接作为第一句的主语，没有独立的钩连句；12 号先用两句介绍 Transformer 背景才进入方法。
- **Confidence**：high。
- **Avoid**：不要用 "In this paper, we propose" 单独成句而不回指难点——语料里的 "In this paper" 主要出现在 Introduction 而非摘要。

## A3｜逐模块巡览：每个模块前面必须有一个目的从句（核心特征）

- **When**：摘要主体，介绍 2–5 个模块。
- **Why**：这是他最稳定的句法习惯。他几乎不会先说模块名再解释用途，而是永远"先说要达到什么，再说造了什么"。
- **Do**：每个模块写成 `To <purpose>, we <propose/design/present/adopt> <Module Name (ABBR)>`。用序数连接词把模块串起来：`first → then → In addition → Finally`。
- **Language/Structure**：
  - 03：`To enhance the ability of feature encoding, we first propose an Attention Encoding Module (AEM) ...` / `For the middle-level features of encoding stages, we propose a Spatial Enhancement Module (SEM) to boost ...` / `In the highest level of encoding stages, we present a Channel Attention Module (CAM) to explicitly model interdependency between channels.` / `Finally, we design a Feature Fusion Module (FFM) and a Global Coefficient Path (GCP) to fuse ...`
  - 02：`To embed global category information, we propose a count prior structure to model and supervise the count of smoke pixels.` / `To ensure the network can correctly extract a count prior map, we impose a regression loss on ...` / `Then we multiply ...` / `Finally, we use ResNet50 for feature encoding, and stack CCA and CPA together to propose ...`
  - 36：`we first propose a Hybrid Pixel Attention (HPA) block to capture both local and non-local information at a low computational cost.` / `To further exploit channel information, we design a Multi-Scale Channel Attention (MSCA) block ...` / `Finally, we adopt an Adaptive Feature Fusion (AFF) module, which can enhance ...`
  - 19：`To improve computational efficiency, we apply Locality Preserving Projection (LPP) to reduce the dimension of HLTP.` / `To further improve performance, we present a noise resistant mechanism to remove noisy derivatives ...`
  - 30：`A Curvelet transform is used to ...` / `Then we extract ...` / `Afterwards, we encode the histogram map again to generate ...` / `Finally, we adopt Gaussian Kernel Optimization (GKO) algorithm to search the optimal kernel parameters ...`
- **Evidence**：22 篇中 20 篇的摘要主体是这种"目的从句 + 模块"的链式结构。序数连接词的使用近乎无例外：`Finally` 出现在 13 篇摘要的最后一个模块句前。`To further improve performance / To further exploit / To further ...` 作为递进标记出现在 19、36、30、02 等多篇。
- **Counterexamples**：21 号（2011，独著）用的是 `The method involves four steps. Firstly, ... Secondly, ... Thirdly, ... And fourthly, ...` 的纯步骤枚举，每步没有目的从句——这是全语料唯一的纯流程式摘要。11 号用"框架 → 发现 → 优势"的论证式组织，也不是模块巡览。
- **Confidence**：high。这是唯一一条在 A1、A2、A3、Tier B 各层、2016–2026 全区间、四个 venue、四种主题上都成立的句法规律。
- **Avoid**：不要写成 `We propose module A. Module A is used to ...`（先名后用）；不要省掉序数连接词让模块并列堆叠；不要在一个句子里塞两个模块。

## A4｜结尾固定为"实验 + 比较结论"，数字通常不进摘要

- **When**：摘要最后 1–2 句。
- **Why**：他的结尾句式高度固定，且刻意不在摘要里给具体数值。
- **Do**：`Experiments / Experimental results / Extensive experiments (on <数据集类型>) show / demonstrate / validate that our method outperforms / is superior to <对比对象>.` 需要时再补一句次级结论。
- **Language/Structure**：
  - `Experiments on both synthetic and real smoke datasets show that our method outperforms existing state-of-the-art methods.`（02）
  - `Extensive experiments validate that our method significantly outperforms existing state-of-art algorithms on smoke datasets, and also obtain satisfactory results on challenging images with inconspicuous smoke and smoke-like objects.`（07）
  - `Extensive experiments on public datasets show that our BiFBA-Net achieves higher segmentation accuracy, and has much better ability of boundary perceptions than compared methods. It also alleviates both over-segmentation of small lesions and under-segmentation of large ones.`（13）
- **Evidence**：22/22 篇的结尾句都以 `Experiments` / `Experimental results` / `Extensive experiments` 起头。补充次级结论句出现在 01、07、08、13、31、03 等篇。
- **Counterexamples**：只有 19 号在摘要里给了数字（`detection rates above 94% with false alarm rates below 1.33%`），22 篇里唯一一例。03 号的补充句用了违反直觉的连接词：`Experiments show that our method is significantly superior to ... **However**, our method has less than 1 M network parameters.`（此处 However 表让步，属作者原文用法，已在清洗时按原样保留）。
- **Confidence**：high（句式）／high（不给数字，21/22）。
- **Avoid**：不要在摘要里列表格数字或多个数据集的逐项指标；不要用 "we achieve SOTA" 这种缩写式断言。

## A5｜确定性强度分层，晚期 A1 论文反而更保守

- **When**：选择结论句的强度词。
- **Why**：他的强度词不是一律最高档，存在可辨的分层，而且这个分层不随年份单调变强。
- **Do**：按证据强弱选词。压倒性优势用 `significantly outperforms` / `is significantly superior to`；一般优势用 `outperforms` / `achieves better performance than`；证据有限或与 SOTA 接近时用 `competitive` / `good` / `satisfying` / `promising`。
- **Language/Structure**：强档 `significantly outperforms`（07）、`significantly surpasses the state-of-the-art`（12）、`significantly better performance`（11）、`significantly superior to`（03）；中档 `outperforms existing methods`（01、02）；弱档 `achieves competitive performance`（36）、`achieve good classification accuracy`（30）、`achieves satisfying results`（01 次级句）、`better performance than most existing methods`（16，注意 `most` 这个限定词）。
- **Evidence**：强弱两档在同一年代内并存（2021 的 07 用强档、2021 的 11 也用强档，但 2019 的 30 用弱档、2025 的 36 用弱档）。16 号用 `most existing methods` 主动缩小比较范围。
- **Counterexamples**：36 号是 2025 年的 Tier A1（一作＋唯一通讯），却用了全语料最保守的 `competitive performance`；这说明强度不是由年份或作者地位决定的，而是跟结果本身挂钩。这条反例很重要，它排除了"晚期越自信"的简单解释。
- **Confidence**：medium-high。分层现象证据充分；具体选词与结果强度的对应关系需要 P3 的 Results 分析来确认。
- **Avoid**：不要一律套 `significantly outperforms`；不要用 `far better`、`the best` 这类无限定的比较级，语料里没有。

## A6｜长度与信息预算

- **When**：定稿摘要。
- **Why**：他的摘要长度稳定，且长度增长几乎全部花在模块数量上，不花在背景铺垫上。
- **Do**：目标 180–260 词。背景 + 钩连不超过 2 句；模块巡览占 60%–70% 篇幅；结论 1–2 句。
- **Evidence**：144–285 词，中位数 213。最短 144（36，只有 3 个模块）；最长 285（13，有双编码器 + 三个解码器 + 六个损失要交代）、269（03，五个模块）。长度与模块数正相关，与背景长度无关。
- **Counterexamples**：无实质反例，21 号（213 词）虽然组织方式不同但长度落在区间内。
- **Confidence**：medium-high。
- **Avoid**：不要用超过 2 句写领域重要性；不要因为摘要短就补背景，应该补模块的目的说明。
