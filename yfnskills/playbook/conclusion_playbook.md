# Conclusion Playbook（袁非牛）

证据基础：22 篇 Conclusion 全文（合计 4,841 词，98–400 词/篇，中位数约 200 词）。全文合并件见 `../_work/p3_conclusions_all.md`。

标准 move 序列：`难点重述（对象属性）→ 方法总述 → 模块逐个复述（带目的从句）→ 实验结论 →（局限与未来工作）`

---

## C1｜开头重述难点，且比摘要写得更具体

- **When**：Conclusion 第一句或第一段。
- **Why**：他不用"本文提出了……"直接开场，而是先把任务难点再讲一遍，而且往往比摘要展开得更细。
- **Do**：第一句给对象属性导致的难点，可用 1–3 句展开；然后才进入方法。
- **Language/Structure**：
  - `It is a highly ill-posed problem to estimate smoke density from a single image.`（01）
  - `Smoke has properties of semi-transparency, fuzzy boundary, time-varying shapes and colors. These smoke properties lead to a challenging task of smoke segmentation.`（02，两句式：先列属性，再下判断）
  - `In most fires, smoke exhibits very large variances of visual appearances, including highly different colors, shapes and textures. One of the adverse properties for visual processing is the semi-transparency of smoke, which may produce very complicated mixtures of smoke and background textures. This is one of the main reasons that leads to great difficulties in labelling and segmenting smoke regions.`（05，三句式，比该篇摘要的难点段更长）
  - `Smoke has very large variations in color, texture and shapes, so it is still a challenging task to accurately recognize smoke from visual scenes.`（19）
  - `Smoke often emerges earlier than flame, so smoke detection can provide very early fire detection. LBP and its variants are the most prominent in texture extraction, but most of them just consider each LBP code independently.`（31，先讲任务价值再讲方法层缺陷）
- **Evidence**：难点或缺陷重述开场出现在 01、02、05、10、11、12、17、19、20、21、31 共 11 篇。其中 05、02、11、12 的重述明显长于自己的摘要开头。
- **Counterexamples**：`In this paper, we propose ...` 直接开场的有 03、04、13、18；`In this study, we propose ...` 的有 06；`To improve ..., we propose ...` 的有 09、30、36、16。所以直接开场也占了将近一半。
- **Confidence**：medium-high（作为首选写法）。
- **Avoid**：不要在 Conclusion 开头引入摘要与 Introduction 都没提过的新难点。

## C2｜模块复述保留目的从句，这是跨章节不变量（核心特征）

- **When**：Conclusion 里逐个回顾模块。
- **Why**：P2 在摘要里发现的"目的在前、机制在后"句法（A3），在 Methods（M2）和 Conclusion 里同样成立。这是全语料唯一一条贯穿四个章节的句法规律。
- **Do**：每个模块写成 `To <目的>, we <propose/design/introduce/adopt> <模块>`，与摘要里的目的从句用不同措辞但保持同一结构。
- **Language/Structure**：
  - `To enlarge receptive fields for encoding more semantic information, we stack convolutional encoder-decoder structures together to propose a wave-shaped neural network (W-Net). To maximize data flow and feature re-usage degree, we resize and copy the outputs of previous encoding layers to corresponding decoding layers ...`（01，连续两个）
  - `In order to achieve powerful features and fast processing speed, we propose a Channel Split and Shuffle Attention Module ... To improve the segmentation performance of small or inconspicuous smoke objects, a spatial enhancement module is proposed ...`（03）
  - `To take into account both local and global information, we integrate convolution structures and self-attention mechanisms ... To improve the robustness of network representation and alleviate inter-class similarity, ... we propose a PHSA ...`（04）
  - `To address the semi-transparent nature of smoke and its weak differentiation from the background, we design an LFE-Former encoder ... Moreover, to fully integrate global and local information, we design a Multi-level Attention Coupled Module (MACM) ...`（06）
  - `To fully exchange information, we propose a Bi-directional Attention Gate (Bi-AG) to fuse features in an attention way. To refine spatial details and contextual semantics, we propose three progressive decoders with six supervised losses ...`（13）
  - `To further obtain discriminant features, KPCA is adopted to non-linearly map the LBP-like features into a low-dimensional space ... To improve generalization performance, GPR is used to model classification as a Gaussian Process ...`（20，被动语态版）
  - `To capture spatial distribution of features, we propose a novel and computationally simple approach ...`（31）
  - `To further enhance spatial details in the reconstruction process, we introduce an Adaptive Feature Fusion (AFF) module ...`（36）
- **Evidence**：目的从句式模块复述出现在 01、03、04、05、06、07、09、11、13、16、20、31、36 共 13 篇，跨 2011–2026、四个 venue、四种主题、A1/A2/A3 三层。
- **Confidence**：high。作为跨章节不变量，它比任何单章节规则都更值得进核心 DNA。
- **Avoid**：不要在 Conclusion 里用与摘要完全相同的句子复述模块，措辞要换但结构保留。

## C3｜与摘要的信息差：Conclusion 加机制细节和局限，不加新结果

- **When**：判断 Conclusion 该写多少、写什么。
- **Why**：他的 Conclusion 不是摘要的缩写或复制，两者有稳定的分工。
- **Do**：相对摘要，Conclusion 里**增加**：难点的展开、模块的机制细节、局限与未来工作；**保持不变**：结论强度词；**不增加**：新的实验数字、新的对比对象。
- **Language/Structure**：对照 12 号——摘要的模块句是 `we cross-wisely concatenate these complementary features to propose a Cross-domain Fusion Block (CFB)`；结论则展开成 `The feature fusion module uses cross-domain concatenation, feature correlation and dual attention methods to effectively combine these features from CNN and Transformer domains.` 同一模块，结论给了三种手段的枚举。
  16 号的结论更极端：用整整两段（`Our method can extract multi-order, multi-scale features ... In this way, a compact and discriminative feature space is created ...`）重新论证方法为什么有效，这部分内容在摘要里完全没有。
- **Evidence**：22 篇中没有一篇在 Conclusion 引入新的定量结果。局限性只出现在 Conclusion（9 篇），摘要 0 篇。结论强度词与摘要一致的有 01、02、05、07、11、12 等。
- **Counterexamples**：21 号的 Conclusion 开头引入了一个摘要里没有的新论证——`With the rapid development of video science and technology, cameras with large storage are getting so cheap that video surveillance systems are widely applied in a variety of fields.`（硬件成本下降）。这是唯一一例在 Conclusion 里新增论据。
- **Confidence**：high。
- **Avoid**：不要在 Conclusion 里第一次给出数字；不要把摘要整段搬过来。

## C4｜时态与语态：方法用现在时，实验用过去时，早期论文的方法复述常用被动

- **When**：写 Conclusion 的动词。
- **Why**：他的时态分工稳定，但语态随年代有明显漂移。
- **Do**：方法陈述用现在时主动（`we propose`）；实验陈述用过去时（`We performed experiments on ...` / `Several experiments were performed`）。若刻意复刻早期风格，方法复述可用被动。
- **Language/Structure**：
  - 现在时主动（主流）：`we propose a Cubic-cross Convolutional Attention (CCA) to capture ...`（02）
  - 过去时实验：`We performed experiments on three synthetic smoke datasets and a realistic smoke dataset collected from the internet.`（08）／`Several experiments were performed to evaluate robustness of these features.`（17）
  - 早期被动式方法复述：`a double mapping framework is proposed to extract shape-invariant features based on partitions`（17）／`KPCA is adopted to non-linearly map ...` `GPR is used to model classification ...`（20）／`LBP encoding is applied to the histogram map`（30）／`a novel video smoke detection method is proposed`（21）
  - 2023 年后的被动残留：`a spatial enhancement module is proposed`（03）
- **Evidence**：被动式方法复述集中在 17（2012）、21（2011）、20（2017）、30（2019），2020 年后基本转为主动（03 仍有一处残留）。
- **Confidence**：medium-high。年代漂移清晰，但样本在每个年代都不多。
- **Avoid**：不要在同一篇里混用两种语态复述同类模块；03 号的混用是可指出的不一致。

## C5｜局限与未来工作段：2023 年后才成为标配，且要给机制不只给现象

- **When**：Conclusion 最后一段。
- **Why**：这是他写作里最清晰的年代趋势之一，而且他写的局限普遍带机制解释，不是套话。
- **Do**：单独一段，先说局限（给机制），再说未来方向（给具体做法而非"进一步研究"）。
- **Language/Structure**：
  - 有机制的局限：`Although our method achieves pleasing segmented results, our limitation lies in the extraction of boundary details. The main reason may be that our CNN and Transformer encoders start to recover feature maps from the 4x down-sampled feature maps, which already lose detailed spatial information. In the future, we will explore novel networks without downsampling feature maps ...`（12，局限 + hedge 式机制 + 对应的具体改法）
  - `Although our network achieves excellent performance, it deeply depends on the levels of encoded features that directly determine the overall order of interpolation polynomials. Higher orders not only increase the computation complexity of interpolations, but also augment the risk of overfitting. Hence, a suitable order may play a key role ... Order optimization in a layer by layer manner may be a good choice.`（05）
  - `However, a limited number of projection vectors inevitably produces reconstruction errors, which will be passed to deeper layers and be accumulatively magnified, especially in the case of non-linear operations applied to feature maps. Hence, a strategy of backward propagation is needed for error correction.`（16，2018 年的早期例外，机制写得最细）
  - 带失败案例引用：`It fails to segment skin lesions with complex edge structures, as shown in the top three rows of Fig. 9. It cannot completely overcome the difficulty in processing extremely low contrast images, as shown in the bottom three rows of Fig. 9.`（13，局限句直接挂图注锚点）
  - 只有未来工作没有局限：`Future work will explore the application of MIFNet in real surveillance systems ...`（06）／`In the future, we will explore more possibilities about further utilizing the rich image information in the frequency domain.`（18）／`In future work, we plan to incorporate frequency-domain representations [60] ... Additionally, we aim to reduce the computational cost of normalization by exploring adaptive alternatives ...`（36，给了具体技术与引用）
- **Evidence**：有局限或未来工作段的 9 篇：05(2025)、06(2025)、09(2026)、10(2025)、12(2023)、13(2024)、16(2018)、18(2024)、36(2025)。**8 篇集中在 2023–2026，16 号（2018）是唯一的早期例外。** 无此段的 13 篇全部在 2022 年及以前（01、02、03、04、07、08、11、17、19、20、21、30、31）。
- **Counterexamples**：16 号（2018）打破了纯年代解释——它的局限段写得比多数晚期论文更深入（误差在层间累积放大）。所以这条趋势不是单纯的年代效应，也可能与"方法是否有可分析的失效机制"相关。
- **Confidence**：high（年代趋势）／medium（机制深度与年代的关系）。
- **Avoid**：不要写"未来我们将进一步改进方法"这类空话；语料里每一条未来工作都指向具体技术（逐层阶数优化、反向传播纠错、无下采样网络、频域表示、DyT 归一化替代）。

## C6｜坦诚式限定：主动降低自己组件的必要性

- **When**：某个组件其实是可选的，或某个论断无法证明。
- **Why**：他有一个少见但一致的习惯——主动说出"这个部件不是必须的"或"我们证明不了"，而不是让读者自己发现。
- **Do**：在合适位置直接写出来，不加辩解。
- **Language/Structure**：
  - `Additionally, we apply a manifold dimensionality reduction method, Locality preserving Projection (LPP), to reduce the dimension of HLTP. **However, LPP is not compulsory, so we may not apply LPP if we do not care about dimensions and computation time.**`（19 号 Conclusion，主动说自己的一个模块可以不用）
  - `Our experiments validate that feature combination truly improves performance, **but it is difficult for us to theoretically prove it.**`（19 号 Introduction）
  - `So we do not know the performance on unknown videos. That is the lower limit of smoke detection of the video system.`（21 号 Discussion）
- **Evidence**：19（2016，A2）两处、21（2011，A1）一处。跨两篇、两个年代。
- **Confidence**：medium。只有两篇论文的三处证据，但这三处的性质高度一致，且都出自作者一手行文的篇目（19 一作、21 独著）。
- **Avoid**：不要把它变成通篇自我怀疑；这三处都是单句，插在正常的肯定叙述里，比例很低。
