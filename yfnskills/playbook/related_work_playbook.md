# Related Work Playbook（袁非牛）

**样本量是 19 篇，不是 22 篇。** 17、21、31 三篇没有独立 Related Work，文献综述写在 Introduction 里（详见 `../corpus/section_coverage.csv`）。这三篇分别是 2012 独著、2011 独著、2016 一作＋通讯，说明"独立 Related Work"是 2016 年之后才固定的做法。

小节标题全清单见 `../_work/p2_struct.txt` 的 `RW_SUBS` 字段。

---

## R1｜分类轴按技术谱系切，不按时间切

- **When**：规划 Related Work 的小节。
- **Why**：他的小节标题全部是技术路线或任务名，没有一个是"早期方法/近期方法"这种时间轴。
- **Do**：把小节命名为技术路线（注意力机制、因式分解卷积、频域学习、CNN 与 Transformer 结合）或任务（烟雾分割、皮肤病灶分割）。时间顺序只在小节内部体现。
- **Language/Structure**：实际小节标题：`Context information embedding | Attention mechanism | Smoke segmentation`（02）；`Semantic segmentation | Smoke semantic segmentation | Factorized convolution | Attention models`（03）；`CNN based methods | Transformer based methods | CNN and Transformer combined methods`（12）；`CNN-Based SR Methods | Attention Mechanisms for SR | Efficient SR Models`（36）；`Smoke Detection | Smoke Segmentation | Lightweight Framework`（09）。
- **Evidence**：13 篇有小节的论文，共 38 个小节标题，其中按时间命名的为 0 个。小节数分布：2 个（05、08、13）、3 个（04、06、07、09、10、12、18、36）、4 个（03）。众数 3。
- **Counterexamples**：01、11、16、19、20、30 有 Related Work 但不分小节（长段落连写）。不分小节的 6 篇里有 5 篇是 2020 年及以前，所以分小节化也是随年代增强的。
- **Confidence**：high。
- **Avoid**：不要用 "Traditional methods" / "Deep learning methods" 当小节标题——那是 Introduction 里的切分（见 I3），不是 Related Work 的轴。

## R2｜最后一个小节留给本文贡献所属的技术谱系

- **When**：小节排序。
- **Why**：他把自己方法的直接来源放在最后一个小节，这样 Related Work 结尾就能自然接上"我们受此启发"的定位段。
- **Do**：排序为 `[一般任务] → [本文的具体任务] → [本文贡献所在的机制]`，让机制小节收尾。
- **Language/Structure**：03 的贡献是轻量注意力，末节是 `Attention models`；07 的贡献是注意力卷积 GRU，末节是 `Recurrent Networks for Computer Vision`；09/10 的贡献是轻量化，末节都是 `Lightweight Framework`；12 的贡献是 CNN+Transformer 互补，末节是 `CNN and Transformer combined methods`；13 的贡献是双编码器，末节是 `CNN and Transformer Hybrid Networks`；18 的贡献是频域原型，末节是 `Frequency Domain Learning`；36 的贡献是高效 SR，末节是 `Efficient SR Models`；06 的末节是 `Transformer and CNN combined methods`。
- **Evidence**：13 篇有小节的论文里 10 篇符合（03、06、07、09、10、12、13、18、36，以及 05 的两节 `Semantic segmentation → Smoke semantic segmentation` 属退化情形）。
- **Counterexamples**：02（末节是 `Smoke segmentation`，机制节 `Attention mechanism` 排在中间）、04（末节是 `Smoke Semantic Segmentation`）、08（末节是 `Smoke segmentation`）。这三篇把任务节放在最后。所以规则强度是 10:3，属倾向。
- **Confidence**：medium-high。
- **Avoid**：不要让 Related Work 结束在一个与本文贡献无关的小节上，否则后面的定位段会显得突兀。

## R3｜一句一方法的枚举节奏，`Author et al. [n] + 过去时动词`

- **When**：小节内部铺陈文献。
- **Why**：他的综述节奏极其规整，一个句子处理一个工作，几乎不合并。
- **Do**：`<第一作者姓> et al. [n] proposed/presented/used/adopted/designed/introduced <方法>, which <一句话机制说明>.` 连续排列。
- **Language/Structure**：
  - `Zhou et al. [55] analyzed structures and occurrence probabilities to propose a new LBP operator ... Guo et al. [9] encoded signs and magnitudes of 1st order derivatives ... Ren et al. [37] presented Noise Resistant Local Binary Patterns by correcting uncertain bits ... Liao et al. [20] regarded the top 80% frequent patterns as dominant features ...`（19）
  - `Wen et al. [12] proposed a difference vector plus KPCA method ... Lei et al. [13] used Kernel Principal Component Analysis (KPCA) to improve ... Xu et al. [14] applied KPCA in patch-based texture descriptors ... Zhou et al. [15] proposed a single-image super-resolution method ...`（20）
- **Evidence**：这个节奏在 19、20、11、30、36、13、12、02、03、08 等全部有 Related Work 的篇目里一致。引用括号总数：最多 81（04）、74（08）、66（03），最少 9（17，因为它没有独立 RW 且提取受损）。
- **Counterexamples**：02 号的清洗版本里括号引用数为 0——该篇 reader 提取时把数字引用换成了作者名叙述（`Wang et al. presented ...` 无编号）。**这是提取产物，不是作者写法，不能用来做引用密度结论。**
- **Confidence**：high（节奏）／**low（作为个人风格）**。一句一方法 + `et al. [n] proposed` 是计算机视觉综述的通用写法，必须标记为领域惯例。真正有区分度的是这个节奏上叠加的缺陷从句（见 R4）。
- **Avoid**：不要把三四个工作合并成一句"许多方法都做了 X [3,5,8,12]"；语料里这种合并引用很少。

## R4｜缺陷从句紧贴方法句，并且指向本文要补的那类信息

- **When**：铺陈完一批文献，准备转向自己的方法。
- **Why**：他不会把所有批评攒到小节末尾，而是边铺边评；而且这些评语最终会汇聚到同一个信息缺失上（与 Introduction 的 I6 呼应）。
- **Do**：在方法句后直接加 `but/however <具体缺陷>`；小节末尾再用一句把这些缺陷归并成一类信息缺失。
- **Language/Structure**：
  - `However, these methods are supposed to fuse features in a spatial-wise manner.`（02，为后面的"跨空间与通道耦合"铺路）
  - `However, the relations between different scales were still not investigated.` / `However, these kinds of methods achieved limited improvements since the relations between features from different scales were not effectively explored.`（16，同一缺陷在小节里说了两次，逐步收紧）
  - `However, LDA projects features to a space of dimension at most c − 1, where c is the number of classes. For a binary classification in smoke detection, the projected space is one-dimensional. As an alternative, we adopt unsupervised KPCA to retain more information`（20，用具体数学后果否定对手，然后给替代）
  - `These above-mentioned methods have achieved encouraging results, but they cannot capture local and global information well.`（13）
  - `Although Curvelet transform provides a powerful multi-scale capability to extract discriminative smoke features, Curvelet-based image classification methods are limited to features, since the Curvelet coefficients are regarded as a holistic features extracted from the whole images [19]. To this end, we propose a duplex feature coding approach`（30）
- **Evidence**：缺陷从句在 19 篇有 RW 的论文里全部出现。20 号那种"用对手方法的数学性质推出其在本任务上退化"的批评方式最有辨识度（LDA 在二分类退化为一维），在 16、30 也有较弱形式。
- **Confidence**：high（边铺边评 + 缺陷收敛）。
- **Avoid**：不要写无指向的批评（"效果不够好"）；不要把批评全部堆在小节最后一段。

## R5｜Related Work 必须以定位段收尾，开头用 "Inspired by" 或 "However/Although above-mentioned"

- **When**：Related Work 最后一段。
- **Why**：这是他最稳定的收尾动作，19 篇无例外。它把综述与自己的方法缝合起来。
- **Do**：写一段，两种开头任选：肯定式 `Inspired by <某成功路线>, we also <动作>`，或否定式 `However, above-mentioned methods do not <缺陷>`。段内必须出现一句显式差异化陈述。
- **Language/Structure**：
  - `However, above-mentioned methods do not fully focus on segmentation of smoke boundaries and extraction of long-range dependencies. Inspired by the recent successes of attention models, we design a cubic-cross convolutional attention to efficiently capture long-range dependencies, a count prior attention to extract global information ..., and finally combine these two attention modules to jointly solve ...`（02，两种开头连用）
  - `Different with previous work, we propose a two-path encoder-decoder FCN by combining skip and encoder-decoder structures for smoke segmentation. As far as we know, this is the first paper to adopt skip layers and two paths in a single end-to-end network for smoke segmentation.`（08）
  - `Inspired by the success of GRU based methods, we also propose an attention convolutional GRU module to learn the spatial correlation and long-range context dependence of smoke. This is the first time the attention convolutional GRU has been used for image semantic segmentation.`（07）
  - `Inspired by successful applications of both learning based features and local features, we first compute 3D local differences from training samples, then learn cross-scale and high-order features ... To our knowledge, feature learning methods have not been used for smoke recognition ..., so the proposed method is quite novel and original in the literature.`（16）
  - `In this paper, we also propose a single image dehazing method. ... Different from previous single image dehazing approaches, our method is built on a statistical analysis and a probability model of local patches.`（11）
  - `Although some achievements have been made by existing methods, there remain some improvements to be achieved, such as better balances between reconstruction accuracy and efficiency.`（36，只有否定式，没有显式差异化——见反例）
- **Evidence**：19/19 篇的 Related Work 都以定位段收尾。`Inspired by` 开头出现在 02、07、16、03、13、30 等；`However/Although above-mentioned` 开头出现在 02、08、13、36、03。
- **Counterexamples**：36 号（2025，A1）的收尾段只指出了"还有改进空间"，没有把自己的方法与谁不同讲清楚，是全语料里定位最弱的一篇。这提示晚期论文的定位段有变松的迹象，但只有一例，不足以成为趋势。
- **Confidence**：high。
- **Avoid**：不要让 Related Work 以最后一篇被引文献结束；不要在定位段里第一次引入新的技术背景。

## R6｜"above-mentioned/aforementioned"是他的标准回指装置

- **When**：需要回指前文提到的一批方法。
- **Why**：他极其频繁地用这一组词做集合回指，且拼写不统一。
- **Do**：用 `above-mentioned methods` / `abovementioned methods` / `the aforementioned ...` / `Above-mentioned methods extract features in spatial domains.`
- **Evidence**：出现在 02、03、08、12、13、16、30、36、01、17、07、19 等篇。同一作者内部拼写不统一：03 号同时出现 `abovementioned`（无连字符）与 `above-mentioned`；21 号用 `aforementioned`。
- **Confidence**：medium（作为回指偏好）／**low（作为独占风格）**。这类词在学术英语里普遍存在，只有"高频 + 拼写不统一"这个组合才算个人痕迹，而拼写不一致更像笔误习惯而非可复刻的风格。
- **Avoid**：不要为了拟合风格故意写错拼写；复刻时统一用 `above-mentioned`。

## R7｜自引用第三人称化，不标注是自己的工作

- **When**：需要引用自己的前作。
- **Why**：他把自己的前作和别人的工作放在同一叙述层，用 `Yuan et al. [n] proposed ...` 处理，不做作者身份提示。
- **Do**：`Yuan et al. [n] <过去时动词> <方法>, which <机制说明>.` 与相邻的他人工作句式完全一致。
- **Language/Structure**：
  - `Yuan et al. [23] stacked several encoders and decoders to form a Wave-shaped Network (W-Net) ... Yuan et al. [24] designed a two-path U-shaped architecture ... Yuan et al. [28] proposed cubic-cross convolutional and count prior attentions.`（12，一段里三次自引）
  - `Yuan et al. [44] and Frizzi et al. [45] proposed deep smoke segmentation methods based on CNNs.`（03，把自己与他人并列在同一句）
  - `Yuan et al. [53] proposed a Waveshaped deep neural Network (W-Net) for smoke density estimation. It is actually a method for soft segmentation of smoke, but more challenging than hard smoke segmentation.`（07，自引后仍附加评价）
- **Evidence**：第三人称自引出现在 01、02、03、07、12、16、20、30 等篇，累计十余次。
- **Counterexamples**：19 号（2016）是唯一用第一人称标注的：`In our previous work, we proposed a fast accumulative motion orientation model based on integral image [48], histograms of Local Binary Pattern (LBP) and Local Binary Pattern Variance (LBPV) based on pyramids [50], and shape-invariant features on multi-scale partitions with AdaBoost [47] for smoke detection.` 一句串三个自引。
- **Confidence**：medium-high。主流做法证据充分，但存在一个明确反例，且反例出现在早期。
- **Avoid**：不要在自引后加"我们之前的工作已经证明"这类自我背书；语料里自引附带的评价都是中性或指出其局限（如 07 对 W-Net 的评价）。

## R8｜与 Introduction 的重叠控制：Introduction 给"路线"，Related Work 给"方法"

- **When**：两节都要写文献时。
- **Why**：他用抽象层级差来避免重复，而不是靠删内容。
- **Do**：Introduction 只说"业界试过 N 条路 + 每条路一句评价"（见 I7），不点具体方法名；Related Work 把每条路展开成小节，逐篇点名并附缺陷。
- **Language/Structure**：02 号 Introduction 写 `One effective way is to fuse multi-scale feature maps from different levels. ... Another way is to use attention mechanisms.` 完全不点方法名；Related Work 的 2.1/2.2 才出现 FCN、SegNet、U-Net、PSPNet、Deeplab v3、RecoNet、DANet、SENet、BiSeNet、EMANet 等具体名字。08 号同理：Introduction 写 `There are two main ways ... The first way is ... The second one is ...`，Related Work 的 II-A 才展开 FCN/SegNet/U-Net 的技术差异。
- **Evidence**：02、08、12、01 四篇的两节抽象层级差清晰可查。
- **Counterexamples**：03 号在 Introduction 里就点了 ENet、BiSeNet、ERFNet、LEDNet、DFANet 五个具体方法并给了评价，与 Related Work 2.1 的内容明显重叠。这是他自己论文之间的不一致，说明这条规则是他的较优实践而非铁律。
- **Confidence**：medium-high。
- **Avoid**：不要在 Introduction 就给出方法级的逐条评述；也不要在 Related Work 里重复 Introduction 已经下过的路线判断。

## R9｜跨谱系借用时显式声明"合并不同算法的各自优点"

- **When**：本文方法是两种既有路线的结合。
- **Why**：他有一个固定的元论证：不同算法各有长处，所以合并是自然的。这句会作为结合类工作的合法性依据反复出现。
- **Do**：写 `Combinative methods can keep individual benefits of different algorithms for final purposes.` 或 `Features by different methods have respective advantages, so it is natural for us to combine different features together to enhance robustness.`
- **Language/Structure**：
  - `Features by different methods have respective advantages, so it is natural for us to combine different features together to enhance robustness.`（19）后面紧跟 `Our experiments validate that feature combination truly improves performance, but it is difficult for us to theoretically prove it.`
  - `Combinative methods can keep individual benefits of different algorithms for final purposes [33].`（12）
  - `Combinative methods utilize the individual benefits of different algorithms [33].`（13）
  - `According to the above-mentioned analyses, Transformers and CNNs are naturally complementary to each other. From this perspective, we believe that combining these two kinds of CNNs and Transformers can overcome the weaknesses of two models and strengthen their advantages simultaneously.`（12）
- **Evidence**：19（2016）、12（2023）、13（2024）三篇出现近乎同义的声明，其中 12 与 13 的措辞几乎一致且都挂在同一个引用编号 [33] 上，跨了 7 年。
- **Counterexamples**：无反例，但要注意 12 与 13 是相邻年份的同系列医学分割论文，可能属同一段文本的复用而非两条独立证据。
- **Confidence**：medium。措辞一致度很高，但独立证据实际只有 19 和 12/13 两组。
- **Avoid**：19 号那句 `but it is difficult for us to theoretically prove it` 是难得的坦诚式限定，值得保留这种诚实度；但不要滥用成为回避论证的借口。
