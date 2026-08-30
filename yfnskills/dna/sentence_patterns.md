# 句子功能转移模式（袁非牛）

七种功能转移 + 四个已量化的高频构式。
每条给：结构描述、改写过的示意句（**不是原文，可直接当模板用**）、原文证据位置、反例。
按 00 号规则，本文件不建立逐句模仿库，不收录高辨识度完整原句；原句仅以片段形式作为证据引用。

---

## S1｜方法 → 目的（全语料最强的一条，四个章节通用）

- **结构**：`To + <目的动词短语>, we + <propose/design/present/adopt/introduce> + <模块名（缩写）>.` 目的在前，机制在后，二者之间不插入其他成分。
- **为什么**：这是他唯一贯穿摘要、贡献列表、Methods 组件小节、Conclusion 模块复述四处的句法。密度全文 3.0–5.6/k，Conclusion 最高。
- **示意句（改写，可直接套用）**：
  - `To suppress the interference of texture-like background, we design a Boundary Contrast Module (BCM).`
  - `To keep the channel dimension unchanged after fusion, we insert a point-wise convolution before concatenation.`
  - `To further reduce the number of learnable parameters, we replace the standard convolution with a grouped one.`
- **变体**：`In order to <目的>, ...`（16、21 用）；`For the sake of <名词>, ...`（01、11、20 用，多用于简化性说明）；`Aiming at solving this problem, ...`（02、07 用）；`Motivated by <某成功经验>, we ...`（30、36、18 用）；`Inspired by <某成功经验>, we also ...`（12、13、16 用）。
- **原文证据**：02 的 `To capture long-range dependencies of pixels, we propose a novel attention ...`；13 的 `To reduce semantic gaps between them, we propose a Bi-directional Attention Gate module (Bi-AG) ...`；06 连续四个组件小节全部以此开头；01 的 Conclusion `To enlarge receptive fields for encoding more semantic information, we stack ...`。密度统计见 `microstyle_by_section.md` MS7。
- **反例**：20 号整个 Methods 只有 1 个目的从句（该节主体是复述 KPCA/GPR 既有理论）；21、31、17 各约 4 个。**触发条件是"模块是否原创"，不是年代。**
- **Confidence**：high。
- **Avoid**：不要写成 `We propose X. X is used to <目的>.`（先名后用）；不要在一个目的从句后面挂两个模块。

## S2｜现状 → 缺陷

- **结构**：先用一句概述某类方法能做到什么，紧接着用 `but / however / Although ...` 指出它丢了什么。缺陷必须落在"某类信息被丢弃 / 未被建模 / 丢失"上，动词固定在 `discard / not involve / lose / not be modelled / ignore` 这一组。
- **示意句**：
  - `Although channel attention effectively reweights feature responses, it completely discards the positional relations among pixels.`
  - `Multi-scale pooling enlarges receptive fields, but the interactions across scales are not modelled.`
  - `Existing fusion strategies concatenate features from adjacent levels, so the structural information embedded in the level sequence is lost.`
- **原文证据**：31 的 `Although traditional LBP histograms can represent features of smoke images well, they completely discard the spatial distribution of LBP codes`；16 的 `multi-scale extensions do not involve relations between scales`；12 的 `long-rang dependency information has not been modelled well in most CNN based methods`；13 的 `the encoding process inevitably leads to losses of local details and global context information`。
- **反例**：17（2012）与 21（2011）的缺陷诊断用统计学习语言（泛化性能差、对旋转光照敏感），不是信息缺失语言。**这条句式在 2016 年之后才成型。**
- **Confidence**：high（2016 年后）。
- **Avoid**：不要写 `the performance is limited` / `the accuracy is low` 这类无内容的缺陷断言。

## S3｜前提 → 后果（`, so` 因果尾句）

- **结构**：`<可核验的前提事实>, so <设计后果或约束>.` 前提在前，后果在后，顺序不可倒。
- **示意句**：
  - `The two branches output tensors with different numbers of channels, so they cannot be added element-wisely.`
  - `Average pooling preserves low-frequency responses, so its output serves as a global prior for the subsequent attention.`
  - `Smoke boundaries occupy only a small portion of pixels, so a pixel-balanced loss is required.`
- **原文证据**：13 的 `The CNN and Transformer encoders respectively produce 2D feature maps and 1D patch embedding features, so they are not aligned`；16 的 `Each L_k in the scale space is in different sharpness but shares the same resolution, so that 3D samplings can be easily computed`；30 的 `Smoke image edges are always curved, so Curvelet is almost the optimal representation of a singular smooth curve`。密度 Front/Methods/Results 均约 1.0–1.2/k，Conclusion 为 0。
- **反例**：08、10、36 的 Methods 里此类句为 0。`so that` 全语料仅 6 次（16 号占 4 次），**不要把 `so that` 当成他的习惯**，主形式是逗号 + `so`。
- **Confidence**：medium-high。
- **Avoid**：不要倒过来写 `Therefore we design X because Y`。

## S4｜操作 → 解释（公式与符号）

- **结构**：`<公式编号>` 之后立刻 `where <符号> is/denotes <含义>, <符号> is ..., and <符号> is ...`，一句定义完全部新符号；需要时再补一句该式的直觉含义。多个同类符号用 `respectively` 收束。
- **示意句**：
  - `where F_in denotes the input feature map, W_g is the grouped convolution kernel, and σ(·) is the sigmoid function.`
  - `where H, W and C are the height, width and channel number of the feature map, respectively.`
- **原文证据**：08 的一个 `where` 定义九个符号并用了三次 `respectively`；36 的 `where W_p(·) is a 1×1 point-wise convolution, φ(·) is GELU [39], and H_f(·) is the adaptive feature fusion module`；31 的 `where x and y are the two LBP codes, and ||·|| denotes a distance measure`。
- **反例**：20 号 13 个公式引用只配 2 个 `where`（符号沿用文献惯例）。
- **Confidence**：high（做法）／**low（作为个人风格，这是学术写作通行规范）**。可复刻但不作为区分性特征。
- **Avoid**：不要把符号定义拆散到后文；不要用 `obviously` / `it is easy to see` 跳过推导。

## S5｜证据锚点 → 观察

- **结构**：两种写法。分离式 `<Table/Fig N> lists/shows <什么>.` 独立成句，观察放下一句；合写式 `As shown in <Table N>, we find that <观察>.`
- **示意句**：
  - `Table 3 lists the quantitative comparison results on the two real-world datasets.`
  - `As shown in Table 4, we find that removing the fusion module reduces mIoU by 2.1% while saving only 3% of parameters.`
  - `From Fig. 7, we can find that our predictions preserve thin structures better than the compared methods.`
- **原文证据**：07 与 05 都用 `Table II/1 lists quantitative comparison results on the three synthetic datasets`；02 的 `As shown in Table 2, we find that a network capturing both spatial and channel information achieves better performance`；30 的 `From Table 2, we find that our method achieves lower FARs than other methods`。`we find that` 全语料 30 次，其中 **23 次在 Results**（01 号 5 次最多）。锚点密度 Methods 2.7/k、Results 2.6/k，Front 与 Conclusion 为 **0**。
- **反例**：04、36 的锚点句只有 3 条（该两篇更多用 `TABLE N presents/provides` 的变体）。
- **Confidence**：high（位置边界）／medium（作为个人风格，锚点化是领域惯例；有辨识度的是"锚点 + we find that"的合写）。
- **Avoid**：不要在 Introduction 或 Conclusion 正文里放表号；不要写无出处的观察。

## S6｜观察 → 比较（非对称让步）

- **结构**：`<对手> achieves slightly higher <指标> than our method` + `but / although ... our method is obviously/distinctly lower/better in <另一指标>`。副词分工固定：`slightly` 描述对手优势或自身劣势，`obviously / distinctly / nearly` 描述自身优势。
- **示意句**：
  - `Method X obtains slightly higher recall than ours on the second subset, but our false alarm rate is distinctly lower on all four subsets.`
  - `Although our accuracy exceeds the baseline by only 0.8%, the inference latency is reduced by nearly one half.`
- **原文证据**：19 的 `Although DRs of our methods are slightly smaller than the original LBPs on Set2, Set3, and Set4, our methods achieved distinctly lower false alarm rates and error rates on all the sets`；31 的 `PLBP RIU2 has slightly higher DRs than our method, but FARs and ERRs of our method are obviously lower`；12 的 `Although our method only surpasses TransUNet by 1% in term of DSC, it improves nearly 10% in the HD metric`；20 号给出 94.22% vs 94.02% 的精确数字不做掩饰。
- **量化**：`slightly` 全语料 20 次，其中 **18 次在 Results**；集中在 19（6 次）、31（4 次）、09（3 次）。
- **反例**：09、10（Tier B，学生一作）用 `comparable` 处理平手（`is comparable to that of PIDNet, but the former has significantly reduced parameters`），走"性能持平 + 代价更低"路线，副词对立不明显。这两篇的 `slightly` 出现 3 次但用于描述数量级差异而非让步。
- **Confidence**：high（在 A1/A2 层）／medium（在 Tier B 层已弱化）。
- **Avoid**：不要只报赢的指标；不要把输掉的指标说成"基本持平"而不给数字。

## S7｜比较 → 结论或限定（因果解释的两档 hedge）

- **结构**：见 `../playbook/results_playbook.md` RS3 的完整处理。要点：可核验的架构或数据事实用 `The (main) reason is that ...`；不可核验的属性或不利结果用 `The (main) reason may be that ...`。
- **示意句**：
  - flat：`The main reason is that our decoder restores the feature maps to the input resolution before prediction.`
  - hedge：`The reason may be that the samples in this subset have much smaller within-class variance.`
- **量化**：全语料 50 条，flat 33 / hedge 17；Results 段内 flat 23 / hedge 13。
- **反例**：04 号用认知动词而非情态动词 hedge（`We conjecture that ...` / `We suspect the main reason is that ...` / `We think the main reasons are twofold.`）——该篇由学生共同一作起草，可能是执笔人信号，但单篇证据。
- **Confidence**：medium-high。
- **Avoid**：解释自己失败时不要用 flat 式断言。

## S8｜段尾 → 承接

- **结构**：三种收尾方式，按段落功能选择。
  1. **定位式收尾**（Related Work 段、Introduction 评述段）：`Inspired by <某成功路线>, we also <动作>.` 或 `However, above-mentioned methods do not <缺陷>.`
  2. **消融结论式收尾**（Results 消融段）：`..., so it means that <该模块> plays an important role in <功能>.`
  3. **前提后果式收尾**（Methods 段）：见 S3。
- **示意句**：
  - `Inspired by the success of frequency-domain modelling, we also introduce a spectral branch into the encoder.`
  - `Removing this module degrades mIoU by about 2%, so it means that the cross-scale interaction plays an important role in representing thin smoke.`
- **原文证据**：02 的 `However, above-mentioned methods do not fully focus on ... Inspired by the recent successes of attention models, we design ...`（两种连用）；07 的 `Second, the removal of stacked Att-ConvGRUs causes a performance degradation of approximately 3%, so it means that the multi-stage stacking of Att-ConvGRUs plays an important role in learning effective features`。
- **量化**：`above-mentioned / aforementioned` 全语料 29 次，其中 **18 次在 Front**（Introduction 与 Related Work），13 号与 16 号各 4 次最多。
- **Confidence**：high（Related Work 定位式，19/19 篇无例外）／medium（其余两式）。
- **Avoid**：不要让段落停在最后一篇被引文献上；不要用 `In conclusion` 作段尾（那是 Conclusion 章的词）。

---

## 四个已量化的高频构式

### C1｜`not only ... but also ...`（35 次，全语料最高频的显式构式）

分布：Front 11、Methods 9、Results 11、Conclusion 4。集中在 06（6 次）、05（5 次）、16（4 次）、03（3 次）。
用途：把两个价值点绑在一句里，常用于贡献陈述与结果陈述。
- 示意：`Our module not only enlarges the receptive field but also keeps the channel dimension unchanged.`
- 原文证据：31 摘要 `our approach not only has better performance than existing methods in smoke detection, but also has good performance in texture classification`；07 Introduction `Segmented smoke regions not only provide an important clue for fire detection, but also accurately indicate the location of fire`。
- **Confidence**：medium。35 次的绝对频次高，但 `not only ... but also` 是通用英语构式，只有"在贡献与结果句里成对使用价值点"这个用法算个人偏好。

### C2｜`we (can) find that`（30 次，23 次在 Results）

见 S5。与证据锚点合写是有辨识度的组合。**Confidence**：medium-high。

### C3｜`above-mentioned / aforementioned`（29 次，18 次在 Front）

见 S8。**Confidence**：medium（偏好）／low（独占性，通用学术英语）。注意 03 号同篇内 `abovementioned` 与 `above-mentioned` 拼写不统一，属笔误习惯，复刻时统一用带连字符形式。

### C4｜`slightly`（20 次，18 次在 Results）

见 S6。是非对称让步的关键副词。**Confidence**：high（作为让步装置）。

---

## 明确不作为特征的项

- `we propose` 高频 —— 纯通用。
- `Experiments show that ...` —— 通用学术英语。
- `so that` —— 全语料仅 6 次，且 4 次集中在 16 号一篇，**不是习惯**。
- `where` 符号定义 —— 学术写作规范，见 S4。
- 名词化整体偏高 —— 学术英语普遍特征，只有"Front/Conclusion 高、Results 低"的**章节间落差**才是可用信号（见 MS6）。
