# Methods Playbook（袁非牛）

证据基础：22 篇 Methods 全节（合计 48,433 词）。模块树、公式引用数、目的从句与因果句统计见 `../_work/p3_struct.txt`；模块清单见 `../evidence/method_component_map.csv`。

标准骨架：`总览 → 组件（逐个）→ 损失/优化 → 实现细节`。模块树深度 2–3 层，小节数 3–11 个，众数 5–6。

---

## M1｜Methods 开头先给总览小节，且总览里交代数据流走向

- **When**：Methods 第一小节。
- **Why**：他几乎总是先用一个独立小节把整体结构讲完，再拆模块，避免读者在读组件时不知道它们怎么串起来。
- **Do**：第一小节命名为 `Architecture Overview` / `The Overall Structure` / `Overall Pipeline of Our Network` / `The overall flowchart of our method`，内容包含输入尺寸、经过哪些阶段、每阶段交给哪个模块、最后如何输出。
- **Language/Structure**：`A. Architecture Overview`（04）、`A. Overall Framework of the Network`（09）、`A. The Whole FSIHAN Framework`（10）、`3.1. Architecture overview`（12）、`A. The Overall Structure`（13）、`A. Overall Pipeline of Our Network`（36）、`The overall flowchart of our method`（11）、`Overview`（18）、`3.4. The overall framework of our method`（16，放在中段）。
- **Evidence**：9 篇有显式总览小节。11 号的总览段是典型写法：`Fig. 2 shows the overall flowchart of our method consisting of learning and dehazing stages. In the learning stage, we compute ...`。20 号的总览用了 `The overall flowchart of the data processing pipeline is shown in Fig. 1. The rectangles in solid lines represent approaches that are involved ...`，连图例约定都在总览里交代。
- **Counterexamples**：02 号把 `3.3. Network architecture` 放在**最后**，先讲两个注意力模块再讲整体；16 号的总体框架放在 3.4（五节里的第四节）。所以总览前置是主流而非铁律。
- **Confidence**：medium-high。
- **Avoid**：不要在没有总览的情况下直接进第一个模块；不要在总览里给公式（公式留给组件小节）。

## M2｜每个组件小节的第一句先重述它要解决的问题，再给操作（核心特征）

- **When**：进入任何一个组件小节。
- **Why**：这是 P2 的 A3 规则在 Methods 层的延续。他不允许模块凭空出现，每个模块前面必有一个"因为存在什么缺陷/需要什么能力"的引子。
- **Do**：小节首句写 `To <目的> / To address this problem / To overcome this limitation, we <propose/design> <模块名>`，随后才给操作细节与公式。
- **Language/Structure**：
  - `To address this problem, we design a dual-encoder with Transformer and CNN, as shown in Fig. 1.` → `To overcome this limitation, we propose a Local Feature Enhancement Transformer (LFE-Former) for encoding.` → `To address these issues, we propose a Local Feature Enhancement Propagation (LFEP) module to replace MSA.` → `To circumvent this issue, our CNN encoder is only used to extract local information.`（06，连续四个模块全部如此）
  - `To reduce semantic gaps between them, we propose a Bi-directional Attention Gate module (Bi-AG) to fully exchange information from the two encoding paths.`（13）
  - `To reduce computational complexity, we propose a Cubic-cross Convolutional Attention module (CCA) to efficiently model long-range dependencies of smoke pixels, as shown in Fig. 1.`（02）
  - `To preserve the spatial correlation of 2D features, we propose the Att-ConvGRU by first replacing all fully connected layers of the 1D GRU with convolutional ones and then connecting the input signal Xt with the hidden state Ht−1.`（07）
  - `To mine more structures in sequential feature maps, we use the above-mentioned newton interpolation method to estimate a new feature map from these sequential feature maps, instead of feature concatenation or summation.`（05，同时点明被替代的旧做法）
- **Evidence**：目的从句在 22 篇 Methods 里的出现次数：11 次（02、07、11、16、19）、10 次（01、12、13）、9 次（04、10、36 的变体）、8 次（06）、下限 1 次（20）。跨全部四种主题、四个 venue、2011–2026 全区间。
- **Counterexamples**：20 号（2017，A1）整节只有 1 个目的从句（`For the sake of simplicity, we just use histograms of LBP codes ...`），因为该篇 Methods 主要是复述 KPCA 与 GPR 的既有理论，不是提出新模块。31、21、17 的目的从句也偏少（4 次），同属"复述既有算子 + 小改动"的写法。**所以这条规则的强度与"模块是否原创"相关，不与年代相关。**
- **Confidence**：high。
- **Avoid**：不要写 `We propose module X. X consists of ... X is used to ...`（先名后用）；不要在一个小节里同时引入两个新模块。

## M3｜模块内部严格按"输入→操作→中间表示→输出→目的"推进，尺寸显式写出

- **When**：描述单个模块的内部机制。
- **Why**：他的模块描述可执行性很高，读者基本能照着实现，关键是张量尺寸和变换顺序都写出来。
- **Do**：给出输入张量的符号与尺寸，逐步描述变换（转置、卷积、池化、reshape），每步说明产生什么中间表示，最后给输出尺寸并说明与输入的关系。
- **Language/Structure**：
  - `To capture pixel dependencies along the width axis, we first transpose the input feature tensor with the size of h×w×C to produce a new feature tensor with the size of h×C×w, then convolve the transposed tensor, and finally transpose the convolved tensor back to keep the same size as the input feature tensor.`（02，一句话完成"转置→卷积→转置回"的完整链）
  - `To keep the channel number unchanged, the number of feature maps by pyramid pooling is reduced to one fourth of the input channel number by convolutions.`（02，显式交代通道数守恒）
  - `To align CNN features with Transformer ones, we first adopt a 1 × 1 convolution to adjust the channel dimension of CNN features to E in each stage.`（13）
  - `To further improve computational efficiency, we use 1D convolutions to reduce the channel number of a feature map to one-kth of the original channel number.`（03）
  - `In our implementation, d_Xl = 576 and h = 9, so we use d_k = d_Xl/h = 64 for each head.`（13，把超参具体值直接写进正文）
- **Evidence**：`first ... then ... finally` 的三段式变换描述在 02、07、13、31、16 反复出现；尺寸与通道数的显式声明在 02、03、12、13、36 常见。
- **Confidence**：medium-high。这一条部分是深度学习论文的通行做法，但"通道数守恒/尺寸复原"的主动交代比领域平均更细。
- **Avoid**：不要用"经过若干卷积后"这类模糊表述；不要省略 reshape 前后的尺寸。

## M4｜公式后紧跟 where 逐符号定义，公式本身不承担解释

- **When**：给出任何公式。
- **Why**：他把公式当成形式化记录，解释责任完全交给前后的文字，公式后必有符号表。
- **Do**：公式编号后立刻写 `where <符号> is/denotes <含义>, <符号> is ..., and <符号> is ...`，一句话把全部新符号定义完。必要时在 where 之后再补一句该式的直觉含义。
- **Language/Structure**：
  - `where β is a linear coefficient with range (0,1) used to control the concentration of smoke, IR, IG and IB are the red, green and blue channels of a pixel in an observed smoke RGB image I, respectively, SR, SG and SB are respectively ... and BR, BG and BB are respectively ...`（08，一个 where 定义九个符号，`respectively` 三次）
  - `where W_p(·) is a 1×1 point-wise convolution, φ(·) is GELU [39], and H_f(·) is the adaptive feature fusion module.`（36）
  - `where x and y are the two LBP codes, and ||·|| denotes a distance measure that can be L1 or L2 norms [24].`（31）
- **Evidence**：`where` 出现次数与公式引用数正相关：11 号 65 个公式引用配 13 个 where、18 号 29 配 21、30 号 22 配 15、31 号 20 配 11、16 号 46 配 13。全语料无一篇在给出新符号后不定义。
- **Counterexamples**：20 号只有 2 个 where 对 13 个公式引用——因为该篇的公式多为 KPCA/GPR 的标准形式且符号沿用文献惯例。
- **Confidence**：high。
- **Avoid**：不要把符号定义拆散到后文；不要用 `obviously` / `it is easy to see` 跳过推导，语料里没有。

## M5｜损失函数是 Methods 的最后一个小节

- **When**：安排 Methods 小节顺序。
- **Why**：他把损失当成"把所有模块联合起来训练"的收口，因此固定放在最后。
- **Do**：最后一个小节命名为 `Loss Function` / `Joint Loss Function` / `Training Loss` / `Deep Supervisions` / `Multiple objective function`，逐项列出各分量损失及其权重，说明每一项监督哪个模块的输出。
- **Language/Structure**：`D. Loss Function`（01）、`3.4. Loss function`（03）、`D. Smoke-Aware Loss`（04）、`Multiple objective function`（06）、`D. Loss and Final Result`（07）、`G. Joint Loss Function`（09）、`E. Loss Function`（10）、`D. Deep Supervisions`（13）、`Training Loss`（18）。
- **Evidence**：9 篇把损失放在 Methods 末位或次末位。01 号的损失更进一步：摘要与 Introduction 都强调 `a complicated loss function that includes four errors of smoke density, smoke color, background color, and composited observed color`，四项损失分别对应四个被监督的量。
- **Counterexamples**：02 号把 `3.2.3. Count loss` 嵌在计数先验模块内部（因为该损失只监督那一个模块），随后 `3.3. Network architecture` 收尾；12、05 没有独立损失小节。手工特征时代的论文（21、17、19、20、30、31、16）没有损失小节，取而代之的是最后一小节讲分类器（`Classification with the neural network`、`Feature and classifier for smoke detection`、`Classification using SVM with GKO`）。
- **Confidence**：high（深度学习论文）。手工特征论文的等价位置是"分类器小节"，同样在最后。
- **Avoid**：不要把损失放在总览里；不要只给总损失公式而不说明各项监督什么。

## M6｜前提在前、后果在后，用 ", so/thus" 收尾设计决策

- **When**：需要说明某个设计选择的必然性。
- **Why**：他的句子经常先摆事实前提，再用 so/thus 把设计后果或约束推出来，读起来是推导而不是宣告。
- **Do**：`<前提事实>, so <后果/因此需要这样设计>.`
- **Language/Structure**：
  - `The CNN and Transformer encoders respectively produce 2D feature maps and 1D patch embedding features, so they are not aligned.`（13）
  - `Each L_k in the scale space is in different sharpness but shares the same resolution, so that 3D samplings can be easily computed.`（16）
  - `The internal structure of Att-ConvGRU is complicated, so too many cycles will seriously reduce computational efficiency.`（07）
  - `Smoke image edges are always curved, so Curvelet is almost the optimal representation of a singular smooth curve.`（30）
  - `Average-pooling tends to preserve more overall or low-frequency information about objects, so the result by global average pooling is a good prior knowledge of global context.`（03）
  - `Smoke has important visual characteristics, such as low image contrast, low color saturation and small gradient magnitude, so edge, LBP and color features are combined together to propose a robust feature vector.`（17）
- **Evidence**：`, so/thus/hence` 句在 Methods 里的出现次数：10 次（16）、8 次（13）、6 次（01、07、31）、5 次（03、05）。跨 2012–2025，跨全部主题。0 次的是 08、10、36。
- **Confidence**：medium-high。
- **Avoid**：不要倒过来写成 `Therefore we design X because Y`；他的顺序始终是前提在前。

## M7｜手工特征时代先复述既有算子再提改动，深度学习时代直接给新模块

- **When**：判断该不该在 Methods 里花篇幅讲背景算法。
- **Why**：他的 Methods 篇幅分配随范式明显变化，早期论文有大段既有算子复述。
- **Do**：若方法建立在某个成熟算子（LBP、LTP、Curvelet、KPCA、GPR、Newton 插值）之上，先用一个小节把该算子讲清楚（含公式），再用后续小节讲自己的改动；若是端到端网络，直接从总览进模块。
- **Language/Structure**：复述型小节：`2.1 Local Binary Patterns`（31）、`3.1. Local binary patterns`（19）、`A. LBP features | B. Kernel principal component analysis (KPCA) | C. Gaussian process regression (GPR)`（20）、`2.1. LBP | 2.2. LBPV`（21）、`3.1 Curvelet transform`（30）、`3.2.2. Newton interpolation theory`（05）。
- **Evidence**：手工特征时代 7 篇（21、17、19、20、30、31、16）的 Methods 词数中位数约 2,400，其中相当篇幅是既有算子复述；20 号整节四个小节里三个是复述。05 号（2025）虽是深度网络，但因为借用了 Newton 插值理论，同样专设 `3.2.2. Newton interpolation theory` 复述小节——说明触发条件是"借用外部数学工具"，不是年代。
- **Counterexamples**：纯网络论文（02、03、04、06、09、10、12、13、36）无复述小节。
- **Confidence**：high。
- **Avoid**：复述小节里不要夹入自己的改动；也不要在纯网络论文里插入 CNN/Transformer 的教科书式介绍（那属于 Related Work）。
