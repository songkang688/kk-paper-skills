# 逐篇研究推理链（Tier A 20 篇 + Tier B 2 篇）

链条格式：`Problem → Representation Failure → Design Principle → Module → Evidence → Claim`

与 `../evidence/evidence_chain.csv` 的分工：CSV 记录可核验的文本位置与闭环完整性；本文件补上 **Design Principle** 这一层，即他从"信息缺失"抽象出的设计原则。设计原则是从文本反推的，**属于推断层，已逐条标注置信度**。

按 00 号规则：不声称知道作者真实心理，只描述文本里能看出来的推理组织方式。

---

## Tier A1（6 篇）

### 21_LBP_LBPV_FireSafety2011（独著）
- **Problem**：传统烟感需接触燃烧产物，室外与大空间失效
- **Representation Failure**：现有纹理法对旋转与光照敏感；单尺度 LBP 只有局部信息
- **Design Principle**：*把同一算子搬到多个尺度上，让不同尺度承担不同的模式类型*（推断，medium）
- **Module**：三级图像金字塔 × 三种 LBP 模式 + LBPV 金字塔，直方图拼接
- **Evidence**：训练/测试集 + 烟雾与非烟雾视频；无消融
- **Claim**：特征对旋转与光照不敏感，方法在交互帧率下可行
- **链条状态**：partial（无消融）。**注意：本篇未上升到"信息缺失"式诊断**，停在"对旋转光照敏感"，是全语料最早的形态。

### 17_DoubleMapping_PR2012（独著）
- **Problem**：视频烟雾检测训练误差低但泛化差
- **Representation Failure**：Haar-like 特征形状可变；预先指定特征不如特征选择
- **Design Principle**：*先把特征空间做大做冗余，再用学习算法从中选*（推断，high——正文显式写了 `it is naturally believed that the feature selection method may probably obtain more robust features than the feature prespecification method`）
- **Module**：多尺度划分 + 双映射框架（图像→块特征→统计特征）+ AdaBoost 选择
- **Evidence**：ROC 对比 Haar-like 特征
- **Claim**：泛化性能更好，对几何变换更不敏感
- **链条状态**：partial。诊断层用统计学习语言，与 2016 年后的信息语言不同。

### 31_SubOriented_KSII2016（一作＋通讯）
- **Problem**：烟雾静态特征判别力不足；动态特征依赖阈值
- **Representation Failure**：传统 LBP 直方图**完全丢弃 LBP 码的空间分布**；LBP 码只是标签没有数值意义
- **Design Principle**：*当某个表示丢掉了一类关系，就设计一个新的度量把这类关系重新编码进来*（推断，high）
- **Module**：汉明距离替代欧氏距离估计 LBP 梯度 + 双坐标系 + 子方向直方图
- **Evidence**：四个烟雾数据集 + Brodatz 纹理集；无独立消融
- **Claim**：在烟雾检测上优于现有方法，纹理分类上也有好表现
- **链条状态**：partial（无消融）。**这是"信息缺失式诊断→模块命名"的最典型范例。**

### 20_GP_IEEEAccess2017（一作＋共同通讯）
- **Problem**：烟雾形状颜色密度纹理差异极大，难提鲁棒特征
- **Representation Failure**：LBP 类特征对烟雾不够（烟雾纹理不如树叶岩石清晰）；SVM 泛化不足；LDA 在二分类退化为一维
- **Design Principle**：*把分类流程拆成可替换的三段，每段只负责一件事*（推断，high——摘要与 Conclusion 都显式强调 `we can replace any steps of the pipeline by similar methods`）
- **Module**：LBP 特征提取 → KPCA 非线性降维 → GPR 建模分类
- **Evidence**：四个烟雾数据集 + kth-tips 纹理集；有 KPCA 有无对比
- **Claim**：KPCA 与 GPR 确实提升性能，明显优于同特征 + SVM
- **链条状态**：yes。**本篇的定位段用对手方法的数学性质（LDA 维度上界 c−1）推出其在本任务退化，是全语料最强的否定式定位。**

### 07_CGRNet_TIP2021（共同一作＋通讯）
- **Problem**：小/半透明/多尺度烟雾与类烟物体
- **Representation Failure**：DCNN 无循环结构，长程上下文依赖随深度变得不可辨
- **Design Principle**：*用序列建模结构补深度网络缺的长程依赖，并用图像级标签约束像素级预测*（推断，high）
- **Module**：Att-ConvGRU + MCCL + DPPM + 双分类辅助
- **Evidence**：三合成集 + 真实图；移除 Att-ConvGRU 掉约 3%
- **Claim**：显著优于现有 SOTA，在不显眼烟雾与类烟物体上也令人满意
- **链条状态**：yes（Results 缺 D 小节，消融覆盖无法完整核对）

### 36_FeatureAggregation_TCE2025（一作＋唯一通讯）
- **Problem**：SR 模型算力与显存开销大，无法部署到消费设备
- **Representation Failure**：自注意力二次复杂度；轻量注意力感受野小；通道信息未利用；低频结构信息在重建中被削弱
- **Design Principle**：*在低算力约束下用多种廉价注意力的组合替代单一昂贵注意力*（推断，medium-high）
- **Module**：HPA（LPA+DPA+SPA）+ MSCA + AFF
- **Evidence**：五个基准 + 三组消融（网络设计、窗口尺寸、AFF）；`removing AFF reduces parameters by only 8%, but PSNR decreases by 0.16dB`
- **Claim**：`achieves competitive performance ... with fewer network parameters`（全语料最保守的结论强度）
- **链条状态**：yes。**但定位段最弱**（只说"仍有改进空间"），且无章节路线句。

## Tier A2（11 篇，摘录关键层）

| Paper_ID | Representation Failure | Design Principle（推断，置信度） | Module |
|---|---|---|---|
| 19_HighOrder_LTP_IS2016 | LTP 只用一阶导数；上下 LBP 码分解**导致信息丢失**；高阶扩展缺噪声抗性 | *把被分解丢掉的共现关系用联合直方图保留，再叠加高阶信息*（high） | HLTP + 联合直方图 + LPP + HLTPMC |
| 16_MultiScale_IS2018 | 手工特征需领域知识；多尺度扩展**未涉及尺度间关系**；高阶扩展缺噪声抗性（显式三 folds） | *让数据自己学跨尺度的投影方向，再用加权把不同阶的贡献平衡*（high） | 3D 局部差分 + 学习投影矩阵 + 双编码 + Taylor 系数 |
| 08_Deep_Smoke_2019 | 手工特征难设计；多尺度问题；人工标注模糊烟雾困难 | *粗细两条路各管一件事，再用极小网络融合*（high） | 双路编解码 + 融合小网络 + 合成数据生成 |
| 30_DualEncoded_KSII2019 | Curvelet 系数被当整体特征；**频间关系未利用** | *在变换域上再做一次编码，把频带之间的分布关系抓出来*（high） | Dual-LBP + CLBP 拼接 + GKO-SVM |
| 01_WaveShaped_TIP2020 | 下采样丢空间细节；感受野不足以编码语义 | *靠堆叠而不是加深单个编解码器来同时扩感受野与保留复用路径*（high） | 波峰波谷结构 + 三类短连接 + 四项损失 |
| 11_Confidence_Prior_PR2021 | 已有先验受离群值影响且**无法控制抑制程度** | *先把已有先验统一到同一条曲线上，再在曲线上取一个可调的点*（high——这是全语料最独特的一次元层面设计） | 统一框架 + 置信先验 + 自适应比值回归 |
| 02_CCENet_PR2022 | 局部空间细节与全局语义**信息的矛盾**；缺图像级计数信息 | *用等效的长核卷积换取大感受野，用可监督的统计量注入全局信息*（high） | CCA + CPA + Count loss |
| 03_Lightweight_PR2023 | 算力受限；小烟细节不足；烟云难分 | *先用结构技巧降参，再用注意力把降参的损失补回来*（high——摘要显式写 `attention mechanism improves feature robustness to compensate for possible decrease in performance due to reduction of learnable parameters`） | CSSAM + SEM + CAM + FFM/GCP |
| 12_CNN_Transformer_PR2023 | CNN 缺长程依赖；Transformer 缺局部与平移不变性 | *两种归纳偏置互补，就让两条路都在，再设计专门的融合*（high） | 双编码器 + FCM + Transformer 解码器 |
| 13_BiDirectional_TIP2024 | 编码丢局部细节与全局上下文；两域特征未对齐；边界不准 | *融合要双向而不是单向，解码要渐进而不是一步*（high） | Bi-AG + CNN 解码器 + PD + BAD + 六损失 |
| 05_NewtonInterpolation_PR2025 | 多尺度融合只用拼接或相加，**无法建模跨尺度内在结构** | *把跨尺度特征序列看成函数采样，用插值理论去建模它的结构*（high） | NIM + 逐层升阶 |

## Tier A3（3 篇，学生主导起草）

| Paper_ID | Representation Failure | Design Principle（推断） | 备注 |
|---|---|---|---|
| 04_SAGINN_TIP2024 | 多尺度关键信息未全局交互；类间相似导致误分割 | *用分类任务的高层语义去调制分割表示*（medium） | RW 末节是任务节而非机制节，违反 R2；因果解释用 `We conjecture/suspect/think` 而非 `may be` |
| 06_MIFNet_PR2025 | 半透明烟雾与背景区分度弱；MSA 开销大且局部增强不足 | *用局部增强传播替代自注意力，再做多层耦合*（medium） | CRediT 明确 Kang Li 起草；与 09/10 共享结构模板 |
| 18_DualGuided_TMM2024 | GAP 与聚类的局限；域间差异 | *在频域生成原型以保留完整对象信息*（medium） | 主导团队为 Wen/Huang/Ma，一手风格价值低 |

## Tier B（2 篇，仅佐证）

| Paper_ID | 说明 |
|---|---|
| 09_MultiStage_TIP2026 | 五模块（CIAM/GCBAM/MGIM/GFM/EEM），链条完整，但与 10 号同构，一作同为 Kang Li |
| 10_FrequencySpace_TCE2025 | 三模块（FSIM/GMDF/HFAM），链条完整，与 09 号共享作者与参考文献 |

---

## 链条完整性汇总

- `Chain_Complete = yes`：18 篇
- `Chain_Complete = partial`：4 篇（17、21、30、31），**全部因为没有消融小节**，而不是因为诊断或模块缺失
- `Chain_Complete = no`：0 篇

模块层面（`../evidence/method_component_map.csv`，45 个模块覆盖 19 篇）：
- 命名回指了被诊断为缺失的信息：yes 29 项 + partial 6 项 = **35/45（78%）**
- 有对应消融变体：38/45
- 无消融：5 项，集中在 21、30、31 三篇

**结论：诊断→命名→消融→结果的四段闭环在这个语料里是真实存在且可核验的，缺口全部集中在早期无消融的四篇论文上。**
