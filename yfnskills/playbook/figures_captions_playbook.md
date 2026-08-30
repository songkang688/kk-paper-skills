# Figures / Tables / Captions Playbook（袁非牛）

证据基础：22 篇共 419 条图表标题（11,605 词）。逐篇统计见下表；原文见 `../_work/p3_captions/`。

**重要前提：表格内容在全语料的提取中普遍丢失，只有图表标题存活（见 `../corpus/cleaning_log.md`）。所以本 playbook 只能覆盖"图注写法"与"图的角色分工"，无法覆盖表格内部的排版、字体、配色实现。不得猜测绘图软件与字体名。**

| Paper_ID | 图注条数 | 总词数 | 平均词/条 | 子图标记数 |
|---|---|---|---|---|
| 11_Confidence_Prior_PR2021 | 30 | 1242 | 41.4 | 91 |
| 04_SAGINN_TIP2024 | 26 | 711 | 27.3 | 41 |
| 05_NewtonInterpolation_PR2025 | 26 | 744 | 28.6 | 29 |
| 01_WaveShaped_TIP2020 | 24 | 821 | 34.2 | 29 |
| 16_MultiScale_IS2018 | 24 | 359 | 15.0 | 19 |
| 06_MIFNet_PR2025 | 23 | 751 | 32.7 | 43 |
| 08_Deep_Smoke_Segmentation_2019 | 22 | 166 | 7.5 | 3 |
| 09_MultiStage_TIP2026 | 22 | 561 | 25.5 | 27 |
| 07_CGRNet_TIP2021 | 21 | 616 | 29.3 | 26 |
| 18_DualGuided_TMM2024 | 21 | 716 | 34.1 | 15 |
| 10_FrequencySpace_TCE2025 | 20 | 671 | 33.6 | 8 |
| 31_SubOriented_KSII2016 | 20 | 350 | 17.5 | 19 |
| 03_Lightweight_PR2023 | 19 | 759 | 39.9 | 16 |
| 21_LBP_LBPV_FireSafety2011 | 18 | 402 | 22.3 | 15 |
| 02_CCENet_PR2022 | 16 | 278 | 17.4 | 22 |
| 13_BiDirectional_TIP2024 | 16 | 715 | 44.7 | 39 |
| 17_DoubleMapping_PR2012 | 16 | 538 | 33.6 | 29 |
| 12_CNN_Transformer_PR2023 | 14 | 453 | 32.4 | 9 |
| 19_HighOrder_LTP_IS2016 | 13 | 391 | 30.1 | 15 |
| 30_DualEncoded_KSII2019 | 11 | 141 | 12.8 | 6 |
| 36_FeatureAggregation_TCE2025 | 11 | 177 | 16.1 | 9 |
| 20_GP_IEEEAccess2017 | 6 | 43 | 7.2 | 0 |

---

## V1｜图注分两档：概念/架构图给极短名词短语，比较/消融图给长枚举

- **When**：写任何图注。
- **Why**：他的图注长度不是均匀的，而是按图的角色两极分化。架构图靠正文解释，比较图必须自带完整图例。
- **Do**：架构图、流程图、算子示意图用一个名词短语（5–15 词）；定性比较图、消融图、失败案例图用长枚举（30–60 词），把每个面板对应什么写清。
- **Language/Structure**：
  - 短档：`Fig. 1. Imaging model of smoke particles.`（01）／`Fig. 5. A wave-shaped network formed by two encoder-decoder structures.`（01）／`Fig. 2. The overall framework of the proposed BiFBA-Net.`（13）／`Fig. 2. Modified LBP texture operator with block distance (LBP_{8,1}).`（21）／`Fig. 9. Training error curve of the neural network.`（21）
  - 长档：`Fig. 10. Results of synthetic data. (a) Synthetic images. (b) Corresponding ground truths. Results of (c) FCN, (d) SegNet, (e) SMD, (f) TBFCN, (g) Deeplab v1, (h) ESPNet, (i) HG-Net 2, (j) HG-Net 8, and (k) our method.`（01）／`Fig. 1. Examples of challenging raw skin lesion images. (a)-(c) are blurred boundaries; (d)-(f) are the presence of artifacts like air bubbles; (g)-(i) are skin lesions that vary in size and shape and are partially occluded by hair and marks.`（13）
- **Evidence**：同一篇内部的两档并存在 01、13、21、11、03 均可见。跨篇平均词/条从 7.2（20）到 44.7（13），差异主要由该篇是否有多面板定性比较图决定，而不是由年代决定（2018 年的 16 号是 15.0，2019 年的 08 号是 7.5）。
- **Counterexamples**：20 号（2017，A1）全篇 6 条图注、平均 7.2 词、0 个子图标记，是全语料最简的图注体系；30 号（2019）12.8 词、6 个子图标记，同属简约。两篇都是前深度学习时代且图数少。
- **Confidence**：high（两档分化）／medium（具体词数区间）。
- **Avoid**：不要给架构图写长段解释（那是正文的活）；不要给多面板比较图只写一句总述而不列面板。

## V2｜多面板顺序固定，自己的方法永远排最后一个面板（核心特征）

- **When**：做定性对比图。
- **Why**：这个顺序在他所有比较图里没有例外，是一个可机械校验的硬规则。
- **Do**：面板顺序为 `(a) 输入 → (b) ground truth → (c)…(x) 各对比方法（顺序与主比较表一致）→ 最后一个面板 = our method`。
- **Language/Structure**：
  - `Fig. 10. Results of synthetic data. (a) Synthetic images. (b) Corresponding ground truths. Results of (c) FCN, (d) SegNet, (e) SMD, (f) TBFCN, (g) Deeplab v1, (h) ESPNet, (i) HG-Net 2, (j) HG-Net 8, and (k) our method.`（01）
  - `Fig. 11. Segmentation results of real smoke images. (a) Real images. Results of (b) FCN, (c) SegNet, (d) SMD, (e) TBFCN, (f) Deeplab v1, (g) ESPNet, (h) HG-Net 2, (i) HG-Net 8, and (j) our method.`（01，真实图无 GT，所以 (b) 直接进对比方法，our method 仍在末位）
  - `Fig. 5. Visual comparisons with different methods on the ISIC 2016 dataset. (a) Input images, and (b) corresponding ground truth masks. The results by (c) Attention U-Net, (d) CPFNet, (e) FAT-Net, (f) U-Net, and (g) our method.`（13，Fig. 6/7/8 同结构）
  - `Fig. 9. Some images from the three test data sets. (a) A composited smoky image and (b) its corresponding ground truth from DS01, and (c) its predicted density map. (d)–(f) DS02 sample pair and prediction. (g)–(i) DS03 sample pair and prediction.`（01，三个数据集各占一组三联，组内顺序一致）
- **Evidence**：01 号 Fig.10/11、13 号 Fig.5/6/7/8 共 6 个多面板比较图，our method 全部在末位，无例外。
- **Confidence**：high。
- **Avoid**：不要把 our method 放在中间或第一个；不要让图注里的方法顺序与主比较表的行顺序不一致。

## V3｜颜色语义在图注里显式定义，且每张用到该约定的图都重复一遍

- **When**：图里用颜色或线型编码语义。
- **Why**：他不依赖读者记住前面的约定，宁可在每张图注里重复。这个冗余是刻意的。
- **Do**：在图注末尾加一句颜色/线型约定说明；同一约定在后续每张图的图注里原样重复。
- **Language/Structure**：13 号在 Fig. 5、6、7、8、9 五张图注里逐一重复同一约定，措辞几乎一致：
  - `The red curves are ground truth contours, and the green ones denote the boundaries of segmented results.`（Fig. 5）
  - `The red curves are ground truth contours, and the green ones are the contours of segmented results.`（Fig. 6）
  - `The red curves denote ground truth contours, and the green ones are the contours of segmented results.`（Fig. 7、8）
  - `Red curves denote ground truth contours, and green ones are the contours of segmented results.`（Fig. 9）
  6 号的图注同样交代配色：`As shown in Fig. 6, purple denotes predicted background regions, and highlight color marks smoke ones.`（出现在正文，说明约定意识贯穿）
- **Evidence**：13 号五次重复是最强证据；03、06、09 的图注也有配色说明。
- **Counterexamples**：措辞在五次重复间有微小漂移（`are` / `denote` 互换，第五次省略了定冠词）。这说明是手写重复而非模板复制，属于真实的个人习惯痕迹。
- **Confidence**：medium-high。主证据集中在单篇，但该篇的五次重复本身具有内部一致性。
- **Avoid**：不要写"颜色含义同上图"；不要在正文定义颜色而图注不提。

## V4｜消融图用递进式面板，每个面板比前一个多一个组件

- **When**：需要用图说明消融设计。
- **Why**：他的消融图不是并列展示变体，而是按"逐级加回组件"排列，图注本身就构成消融逻辑的说明。
- **Do**：面板从最简基线开始，每个面板增加一个组件，图注逐条写出该面板包含什么。
- **Language/Structure**：`Fig. 8. Ablation analysis. (a) an encoder-decoder network; (b) an encoder-decoder network with short-cut connections (U-Net); (c) wave-shaped structures with short-cut connections of encoder and decoder; (d) wave-shaped structures with short-cut connections of encoder, decoder, crests and troughs.`（01）
  配套正文：`Fig. 8a is just an encoder-decoder network without any short-cut connections by removing a wave crest from our W-Net. ... Fig. 8b is just a U-Net with four short-cut connections. In Fig. 8c, we add a wave-shaped structure to Fig. 8b, but we do not reuse any information on crests and troughs ... Fig. 8d is the proposed W-Net, which adopts short-cut connections between crests, troughs and decoding layers.`
- **Evidence**：01 号是完整范例，图注与正文逐面板对应。
- **Confidence**：medium（单篇完整证据，但与 RS5 的递进式消融相互印证）。
- **Avoid**：不要在消融图里同时改两个组件；不要让图注的面板描述与消融表的变体名不一致。

## V5｜表格标题是单行名词短语，大小写由 venue 决定（非个人风格）

- **When**：写表格标题。
- **Why**：表标题一律极简，只说"比较什么、在哪个数据集上"。大小写形式完全跟随期刊。
- **Do**：`<Comparisons/Experiments> <of/with 什么> <on 哪个数据集>`，一行结束，不加解释。
- **Language/Structure**：
  - IEEE 全大写：`TABLE I COMPARISONS FOR ABLATION ANALYSIS`／`TABLE II COMPARISONS OF HARD SEGMENTATION`／`TABLE III COMPARISON RESULTS OF SMOKE DETECTION ON VIDEOS`（01）；`TABLE V MEMORY AND INFERENCE TIME COMPARISONS ON ×4 SR`（36）
  - IEEE 句首大写：`TABLE III. Comparisons with state-of-the-art methods on ISIC 2016.`（13）
  - Elsevier 句首大写：`Table 1. Experimental results on the training and testing image sets.`／`Table 2. Smoke detection performance comparisons on videos.`（21）
- **Evidence**：22 篇的表标题全部是单行名词短语，无一例带解释性从句。
- **Confidence**：high（单行名词短语）／**排除（大小写形式，纯 venue 模板）**。
- **Avoid**：不要在表标题里写结论；不要把指标定义写进表标题（那属于评价指标小节）。

## V6｜图的角色分工固定为七类，且每类在论文中的位置也固定

- **When**：规划全文配图。
- **Why**：他的图集合非常有规律，每篇按同一套角色配置。
- **Do**：按下面七类配图，并放在对应章节：
  1. **难点示例图** → Introduction。`Fig. 1. Examples of challenging raw skin lesion images.`（13）／`Some challenging examples for smoke segmentation are shown in Fig. 1.`（07 正文）
  2. **概念/成像模型图** → Methods 开头。`Fig. 1. Imaging model of smoke particles.`（01）／`Fig. 1. LBP texture operator.`（21）
  3. **总体架构图** → Methods 总览小节。`Fig. 2. The overall framework of the proposed BiFBA-Net.`（13）／`Fig. 6. The overall deep wave-shaped network ...`（01）
  4. **模块细节图** → 各组件小节。`Fig. 3. The Bi-Attention Gate fusion module. (a) Details of the proposed Bi-AG based fusion module. (b) A single attention gate block.`（13）／`Fig. 4. The structure of the proposed Multi-Scale Channel Attention (MSCA) module. (a) MSCA; (b) Token Learner.`（36）
  5. **消融图** → Results 消融小节（见 V4）
  6. **定性比较图** → Results 比较小节（见 V2），且合成数据与真实数据各一张
  7. **失败案例图** → Conclusion 的局限段或 Results 末尾。`Fig. 9. Visualization of some failure cases.`（13，被 Conclusion 的局限句直接引用）
  另有可选的**数据集样例图**（`Fig. 7. Background images from (a) CBCL StreetScenes, (b) Pascal VOC and (c) Baidu people segmentation dataset.`（01）／`Fig. 8. Some samples from the image database: (a) smoke images and (b) non-smoke images.`（21））与**权衡散点图**（`Fig. 1. Comparisons of ×4 image super-resolution on the Urban100 dataset.`（36），把精度-参数量权衡放在首图）。
- **Evidence**：七类角色在 01、13、21、36 四篇中可完整对应；失败案例图出现在 13、08（Fig. 8 false positives）；权衡散点作首图出现在 36、03（`as illustrated in Fig. 1`）。
- **Confidence**：medium-high。
- **Avoid**：不要缺少难点示例图（他的烟雾论文几乎都有）；不要把失败案例图放在比较图之前。

## V7｜必须剔除的出版社插入句

- **What**：`(For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)`
- **出现位置**：21 号的 Fig. 6、Fig. 10、Fig. 12 图注末尾。
- **判定**：这是 Elsevier 排版系统自动插入的句子，不是作者写的。**不得作为图注风格证据，不得在生成时复现。**
- **同类需警惕项**：`[NOTE: table contents not present in extracted text.]` 是清洗时加的标记（13 号多处），也不是原文。
