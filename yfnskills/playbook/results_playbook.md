# Results Playbook（袁非牛）

证据基础：22 篇 Results 全节（合计 43,156 词，句数 48–154 句/篇）。小节树、证据锚点、因果句、hedge 与让步句统计见 `../_work/p3_struct.txt`。

**这份 playbook 里最有价值的是 RS4（次优结果的非对称让步）与 RS3（带 hedge 的因果解释）。这两条是全语料里最难被通用学术英语解释掉的 Results 特征。**

标准小节序列：`数据集 → 实现细节/实验设置 → 评价指标 → 消融 → 与 SOTA 比较 → 真实场景/视频 →（复杂度或实时性）`

---

## RS1｜消融在前、比较在后

- **When**：安排 Results 小节顺序。
- **Why**：他多数论文先用消融证明每个模块有用，再拿整体去和 SOTA 比，让读者先接受模块的合法性。
- **Do**：把 `Ablation Studies` 放在 `Comparison with State-of-the-Art` 之前。
- **Language/Structure**：`4.3. Ablation studies → 4.4. Comparison on synthetic datasets`（02）；`4.3. Ablation experiments → 4.4. Comparisons with other methods`（03）；`C. Ablation Studies → D. Comparison With SOTA`（04）；`D. Ablation Experiments → E. Comparison With State-of-the-Art Methods`（09、10）；`D. Ablation Studies → E–H. Results on ISIC 2016/2017/2018/PH2`（13）；`B. Ablation Study and Analysis → C. Comparisons With State-of-the-Art Methods`（36）。
- **Evidence**：消融在前 8 篇（02、03、04、06、09、10、13、36），比较在前 4 篇（05、08、12、18）。8:4。
- **Counterexamples**：05（`4.2. Comparison experiments → 4.3. Ablation experiments`）、08（`C. Performance comparisons → D. Ablation analysis`）、12（`4.3/4.4 experiments → 4.5. Ablation studies`）、18（`Comparison with State-of-the-arts → Ablation Study`）。四个反例横跨 2019–2025，不构成年代趋势。
- **Confidence**：medium-high。
- **Avoid**：不要把消融拆散插在各个比较小节之间；语料里 0 篇这样做。

## RS2｜每个观察都挂在显式证据锚点上

- **When**：陈述任何实验观察。
- **Why**：他不允许出现无出处的结论，每一段观察前面必有一个"哪张表/哪张图"的锚点。
- **Do**：先写锚点句 `Table N lists/shows ...` 或 `As shown in Table N, ...` 或 `Fig. N shows ...`，再写观察。
- **Language/Structure**：
  - `Table II lists quantitative comparison results on the three synthetic datasets.`（07）
  - `Table 1 lists quantitative comparison results on the three synthetic datasets.`（05，与 07 同句式）
  - `As shown in Table 2, we find that a network capturing both spatial and channel information achieves better performance than one extracting single information.`（02，锚点与观察压在同一句）
  - `From Table 2, we find that our method achieves lower FARs than other methods on three testing data sets.`（30）
  - `As shown in TABLE I, removing AFF reduces the number of network parameters by only 8%, but the average PSNR decreases by 0.16dB.`（36）
- **Evidence**：锚点句数量：24（11）、22（05）、14（18）、12（13）、10（01、09、19）、下限 3（04、36）。`we find that` 与锚点连用是他的高频组合（02、30、01、05）。
- **Confidence**：high（做法）／medium（作为个人风格，锚点化是领域惯例）。真正有辨识度的是"锚点 + we find that"的合写形式。
- **Avoid**：不要写"实验表明我们的方法更好"而不指明表号。

## RS3｜因果解释分两档：可核验的事实用 "The reason is that"，不可核验或不利的结果用 "The reason may be that"

> **本条已按 P4 的全语料统计修正。** P3 初稿曾判断"hedge 式占主导"，实际计数是 flat 式 33 次、hedge 式 17 次（全文四节合计；其中 Results 段内 flat 23 次、hedge 13 次）。两种形式都常用，真正的规律不是哪个更多，而是**什么时候用哪个**。

- **When**：需要解释某个数字为什么高或低。
- **Why**：他给机制解释时会按"这个解释读者能不能自己核验"来选 hedge 强度。能从论文自身结构核验的用断言式，依赖不可观测属性或解释不利结果的用推测式。
- **Do**：
  - **用 flat 式 `The (main) reason is that ...`**：解释自己方法为什么赢、竞争方法的已知架构缺陷、数据集规模等可核验事实、消融变体的结构性后果。
  - **用 hedge 式 `The (main) reason may be that ...`**：解释自己方法为什么输或某模块为什么没增益、数据分布或对象外观等不可观测属性、图像质量等外部因素。
- **Language/Structure**：
  - **flat 式，解释自己为什么赢（可核验的架构事实）**：
    `The main reason is that our attention module captures both spatial and channel information to perfectly model long-range dependency.`（02）／`The main reason is that our CSSAM module provides a large amount of smoke texture information, which effectively decreases useless information.`（03）／`The reason is that MACM can facilitate more extensive interactions between global and local information.`（06）／`The main reason is that our method upsamples feature maps to the size of original images before final prediction.`（07）／`The main reasons are that our method creates a dual-encoding structure with Transformers and CNNs, and designs Bi-AG to bi-directionally fuse features.`（13）
  - **flat 式，解释消融变体的结构性后果**：`The main reason is that without the assistance of the classification module, our method is changed from the multi-task joint training to the single-loss training, directly resulting in slow convergence of network training.`（07）
  - **flat 式，解释竞争方法的已知架构缺陷或数据集事实**：`The first reason is that SegNet does not adopt the same skip layers as other methods.`（08）／`The reason is that both Set3 and Set4 contain far more images than Set2, so the curves show stable results in a more macroscopic perspective.`（16）／`The main reason is that the 'haze-line' prior cannot perfectly model the formation of haze in bright regions.`（11）
  - **hedge 式，解释自己方法的退化或模块无增益**：
    `The main reason may be that the white smoke video has very poor image quality.`（01）／`The main reason may be that the CPA module is designed to assist pixel classification in the image level and the three test datasets do not contain smoke-like objects, such as cloud.`（02）／`The reason may be that dense connections tend to extract more contextual information than spatial details.`（05）／`The main reason may be that our CNN and Transformer encoders start to recover feature maps from the 4x down-sampled feature maps, which already lose detailed spatial information.`（12 的 Conclusion 局限段）
  - **hedge 式，解释不可观测的数据分布或对象属性**：
    `The reason may be that human organs have inherent smooth surfaces.`（12）／`The reason may be that the within-class variance between samples is small in KTH-TIPS but large in FMD.`（16）／`The reason may be that the within-variances of samples in Set3 are not so big as those in Set2 and Set4.`（16）／`The main reason may be that smoke has no fixed shapes.`（31）／`The reason may be that the edge of smoke is not as salient as other objects.`（31）
  - **hedge + 编号列表**：`The reasons may be: 1) After Curvelet transform, an original image is decomposed into sub-bands. ...`（30）
  - **与 `N folds` 枚举合用**：`The reasons are two folds: (1) the resolution of our samples is 48 × 48, which is too small for the 2nd layer to capture rich textures, and (2) the best classifying hyper-planes of MSD-1L and MSD-2L are not located at the same decision threshold t = 0.`（16）
- **Evidence**：全语料 50 条因果解释句，flat 33 条、hedge 17 条。flat 式出现在 01、02、03、04、05、06、07、08、09、11、13、16、19、20、31 共 15 篇；hedge 式出现在 01、02、03、05、06、07、12、13、16、30、31 共 11 篇。分工统计：17 条 hedge 里约 13 条解释的是不可核验属性或不利结果；33 条 flat 里约 28 条解释的是可核验的架构或数据事实。
- **Counterexamples**：
  1. `The main reason may be that CCA has cubic-cross convolutional kernels to produce large receptive fields.`（02）——这是可核验的设计事实却用了 hedge。
  2. `The primary reason is the computational cost associated with the Fourier transform in the encoder.`（09）——这是自身局限却用了 flat。
  3. **04 号用完全不同的 hedge 装置**：`We conjecture that one of the main reasons is ...` / `We suspect the main reason is that ...` / `We think the main reasons are twofold.` 用认知动词而非情态动词做 hedge。04 号是 A3、由学生共同一作起草，这可能是一个可用于区分执笔人的信号，但只有单篇证据。
  4. 17、21 的 Results 里没有因果解释句（08、20 各只有 1–2 条 flat 式）。所以这条规则只在"Results 里有独立解释内容"的论文里适用。
- **Confidence**：medium-high（分工规律）／high（两种形式都是他的常用手段这一事实）。**不再声称 hedge 式占主导。**
- **Avoid**：不要用 `This is obviously because` / `It is clear that`；不要给出无机制内容的空解释（"因为我们的方法更好"）；不要在解释自己失败时用 flat 式断言。

## RS4｜次优结果用非对称让步处理：对手用 slightly，自己用 obviously/distinctly（核心特征）

- **When**：某个指标上输给了对比方法。
- **Why**：他从不隐藏输掉的指标，但会用副词强度差把读者的注意力引到自己占优的指标上。这个副词对立是稳定且刻意的。
- **Do**：先如实承认 `<对手> achieves slightly higher <指标> than our method`，紧接着用 `but/although ... obviously/distinctly/nearly <数值> ...` 转到自己占优的指标或维度。
- **Language/Structure**：
  - `Although DRs of our methods are slightly smaller than the original LBPs on Set2, Set3, and Set4, our methods achieved distinctly lower false alarm rates and error rates on all the sets.`（19）
  - `PLBP RIU2 has slightly higher DRs than our method, but FARs and ERRs of our method are obviously lower than PLBP [...].`（31）
  - `W-Net [46] achieves slightly higher mIoUs on DS02 and DS03 than our method.`（03，直接承认输给自己的前作，随后转向参数量优势）
  - `On the data set of kth-tips, SVM-RBF achieved an accuracy rate of 94.22%, which is slightly higher than an accuracy rate of 94.02% obtained by KPCA-GPR.`（20，给出两个精确数字，差距 0.2%，不做掩饰）
  - `Although the DRs of our method do not exceed the ones of other methods obviously, the ROCs illustrate that our method outperforms others, which means that the best classification planes are not always at t=0.`（30，换评价视角而非换指标）
  - `Although our method only surpasses TransUNet by 1% in term of DSC, it improves nearly 10% in the HD metric and is well ahead of other models.`（12，1% vs 10% 的量级对比）
- **Evidence**：非对称让步在 03、12、19、20、30、31 共 6 篇出现，跨 2016–2023，跨 IEEE/Elsevier/KSII，跨烟雾与医学。副词分工无例外：`slightly` 只用于描述对手的优势或自己的劣势，`obviously` / `distinctly` / `nearly` 用于自己的优势。
- **Counterexamples**：09、10（Tier B）用 `comparable` 处理平手（`The segmentation performance of FSIHAN-B is comparable to that of PIDNet, but the former has significantly reduced parameters and FLOPs`），走的是"性能持平 + 代价更低"的路子而非承认落后，副词对立不明显。
- **Confidence**：high。
- **Avoid**：不要只报自己赢的指标；不要把输掉的指标说成"基本持平"而不给数字。

## RS5｜消融必须与 Methods 的模块一一对应，且用递进式变体

- **When**：设计和描述消融实验。
- **Why**：他的消融是"逐个加回模块"的递进结构，与 Methods 的模块清单严格对齐，形成可追溯闭环。
- **Do**：为每个 Methods 模块设一个变体；变体命名或图注按"基线 → 加一个 → 再加一个"排列；每个变体给出掉了多少性能，并说明该模块负责什么。
- **Language/Structure**：
  - `To validate the importance of wave-shaped structures and short-cut connections, we selectively remove some of short-cut connections and wave-shaped structures to produce several variants of our method, as shown in Fig. 8.`（01）配套图注：`Fig. 8. Ablation analysis. (a) an encoder-decoder network; (b) an encoder-decoder network with short-cut connections (U-Net); (c) wave-shaped structures with short-cut connections of encoder and decoder; (d) wave-shaped structures with short-cut connections of encoder, decoder, crests and troughs.` —— 四个面板逐级加一个组件。
  - `Second, the removal of stacked Att-ConvGRUs causes a performance degradation of approximately 3%, so it means that the multi-stage stacking of Att-ConvGRUs plays an important role in learning effective features.`（07，掉多少 + 因此说明什么）
  - `To validate the effectiveness of MACM, we design a series of variant experiments, as shown in Table 2.`（06）
  - `To find an optimized weight α for regulating the relative importance of the two losses, we experiment with a set of regulation weights ranging between 0 and 1, as shown in Table 4.`（03，损失权重也做扫描）
- **Evidence**：消融小节在 20 篇中存在（21、30 无独立消融）。模块↔消融的对应关系见 `../evidence/evidence_chain.csv`，其中 01、02、03、07、09、10、13、36 形成完整闭环。
- **Counterexamples**：21（2011）与 30（2019）没有消融小节，只有整体比较；这两篇的模块合法性靠理论论证而非实验拆解。
- **Confidence**：high（2019 年后）。
- **Avoid**：不要出现 Methods 里有但消融里没测的模块；反之也不要消融里出现 Methods 未定义的变体名。

## RS6｜真实场景与视频测试单列小节，作为泛化性证据

- **When**：主实验用的是合成或公开数据集。
- **Why**：他很清楚合成数据的可信度问题，所以固定补一个真实数据小节，把它当成泛化性论证而不是补充材料。
- **Do**：在比较小节之后加 `Experiments on real smoke scenes` / `Test on videos` / `Experimental Results in Real-World Scenarios` 小节，用定性图为主，明确说明真实数据没有 ground truth 时如何判断。
- **Language/Structure**：`4.5. Experiments on real smoke scenes | 4.6. Experiments on sequential images of smoke videos`（02）、`4.2.2. Test on real smoke images | 4.2.3. Test on a real smoke video`（05）、`E. Test on videos`（08）、`F. Experimental Results in Real-World Scenarios`（10）、`F. Smoke Density Estimation on Real Videos | G. Visual Detection of Auto Exhausts by Our Method`（01）、`Smoke detection in videos`（17）。
- **Evidence**：11 篇有独立真实场景/视频小节。01 号还额外加了一个跨任务应用小节（汽车尾气检测），把泛化性推到任务之外。
- **Confidence**：high（烟雾系列）。
- **Avoid**：不要把真实场景结果混进主比较表；不要在没有 ground truth 的真实图上报定量指标。

## RS7｜Results 只做观察与机制解释，不做研究意义升华

- **When**：写 Results 各小节的收尾句。
- **Why**：他把"意义、局限、未来工作"严格留给 Conclusion，Results 里的解释始终停在机制层。
- **Do**：观察句后最多写一句机制解释（用 RS3 的 hedge 句式），然后进入下一个锚点。不要写"这说明我们的方法对消防安全有重要价值"。
- **Language/Structure**：典型收尾 `so it means that the multi-stage stacking of Att-ConvGRUs plays an important role in learning effective features.`（07）——停在"该模块重要"，不外推。`which implies that a small lr is a better choice in later training stage`（04）——停在超参结论。
- **Evidence**：22 篇 Results 里未发现研究意义升华句。局限性讨论只在 08 号的 `F. Limitations of our method` 子节出现（该子节被作者自己放在 Results 内，是全语料唯一一例），其余论文的局限全在 Conclusion。
- **Counterexamples**：08 号的 Limitations 子节确实在 Results 里，内容是三条对象属性难点 + 速度不足。但它有独立小节标题，属于作者显式标注的例外，不是把讨论散入观察句。
- **Confidence**：high。
- **Avoid**：不要在 Results 里写 future work；不要把 Results 的观察句升级成 claim。

## RS8｜实时性与复杂度作为独立维度报告，与精度并列而非附属

- **When**：论文声称轻量或高效。
- **Why**：他把参数量、FLOPs、推理速度当成一等指标，会为它们单列小节，并在精度落后时用它们完成非对称让步（配合 RS4）。
- **Do**：单列 `Real-Time Inference Performance` / `Lightweight experiments` / `Comparisons of memory and inference time` 小节；报告参数量、FLOPs、FPS；与精度形成明确的取舍陈述。
- **Language/Structure**：
  - `F. Real-Time Inference Performance`（09）、`4.4. Lightweight experiments`（05）、`TABLE V MEMORY AND INFERENCE TIME COMPARISONS ON ×4 SR`（36）
  - `Compared to SAGINN (101.1M parameters), FSIHAN-L achieves comparable performance with approximately 57x fewer parameters.`（10，用倍数而非百分比表达代价优势）
  - `As shown in Table 3, our method achieves the highest accuracy of 83.2% among compared methods while maintaining a relatively small number of parameters (46M).`（02，精度与代价同句）
  - `As shown in TABLE I, removing AFF reduces the number of network parameters by only 8%, but the average PSNR decreases by 0.16dB.`（36，用"省得少、掉得多"论证模块必要性）
- **Evidence**：09、10、05、36、03、02 均有代价维度的独立报告或同句对比。03 号在摘要与结论都强调 `less than 1 M network parameters`。
- **Confidence**：high（轻量类论文）。
- **Avoid**：不要只在结论里提参数量而实验里不报；不要用"很快"这类无数值表述。
