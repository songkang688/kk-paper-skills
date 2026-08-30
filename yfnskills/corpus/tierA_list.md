# yfnskills 建模名单（Tier A 为主，Tier B 仅佐证）

目标作者：Feiniu Yuan（袁非牛）。权重来自 `../repo/fnypro1/stage00/authorship_weights.csv`，规则见 P1 固定规则第 3 条。
语料 24 篇经作者身份审计后：**22 篇进入本名单**，14（Tier U）与 15（Tier C）已排除。

## Tier A1｜权重 1.00（独著，或一作/共同一作且通讯）——6 篇

| Paper_ID | 年份 | Venue | 主题 | 身份依据 | 风格取样价值 |
|---|---|---|---|---|---|
| 21_LBP_LBPV_FireSafety2011 | 2011 | Fire Safety Journal 46 | 视频烟雾检测（LBP/LBPV 金字塔 + BP 网络） | 独著 | **最高**。零合作者混杂，提取质量高，结构完整，且是全语料唯一有独立 Discussion 的论文 |
| 17_DoubleMapping_PR2012 | 2012 | Pattern Recognition 45(12) | 视频烟雾检测（手工形状不变特征 + AdaBoost） | 独著 | 高（身份）／受限（文本）。提取质量中低，只能用标记为干净的段落 |
| 31_SubOriented_KSII2016 | 2016 | KSII TIIS 10(4) | 烟雾检测与纹理分类（LBP 码梯度 + SVM） | 一作 + 明确通讯 | 高。参考文献逐字保留，正文可用；无独立 Related Work |
| 20_GP_IEEEAccess2017 | 2017 | IEEE Access 5 | 烟雾检测（LBP + KPCA + 高斯过程回归） | 一作 + 明确共同通讯 | **最高**。提取质量全语料最好之一，前深度学习时代的最强锚点 |
| 07_CGRNet_TIP2021 | 2021 | IEEE TIP 30 | 烟雾语义分割（Att-ConvGRU、双分类辅助） | 共同一作 + 明确通讯 | 高。深度学习时代最强锚点。注意正文可能与共同一作学生 Lin Zhang 共写 |
| 36_FeatureAggregation_TCE2025 | 2025 | IEEE TCE 71(4) | 高效图像超分辨率（CFAN） | 一作 + 唯一明确通讯 | 高。晚期最强锚点，提取质量高。主题混杂：超分辨率，非烟雾 |

## Tier A2｜权重 0.90（一作/共同一作，通讯未证实或明确属他人）——11 篇

| Paper_ID | 年份 | Venue | 主题 | 备注 |
|---|---|---|---|---|
| 19_HighOrder_LTP_IS2016 | 2016 | Information Sciences 372 | 烟雾检测与纹理分类（LTP/LBP + LPP + SVM） | 一作，通讯脚注丢失，保守定 A2 |
| 16_MultiScale_MultiOrder_IS2018 | 2018 | Information Sciences 468 | 烟雾识别与纹理分类（学习型局部差分特征） | 一作，通讯不可考。参考文献逐字保留 |
| 08_Deep_Smoke_Segmentation_2019 | 2019 | Neurocomputing 357 | 烟雾分割（双路粗细 FCN + 合成数据生成） | 一作。**本地文本是 preprint 版**，编辑加工较少，反而更接近作者原始行文 |
| 30_DualEncoded_KSII2019 | 2019 | KSII TIIS 13(4) | 图像烟雾识别（Curvelet Dual-LBP + GKO-SVM） | 一作，但通讯明确指派给学生 Xue Xia 与 Jinting Shi。**这是"一作不等于通讯"的反证** |
| 01_WaveShaped_TIP2020 | 2020 | IEEE TIP 29 | 烟雾密度估计（W-Net + 合成 RGBA 数据） | 一作，IEEE 脚注丢失，保守定 A2 |
| 11_Confidence_Prior_PR2021 | 2021 | Pattern Recognition 119 | 图像去雾（统计先验 + 回归，非深度） | 一作。主题混杂：去雾。合作者 Qian/Huang 不在常规团队内 |
| 02_CCENet_PR2022 | 2022 | Pattern Recognition 131 | 烟雾分割（cubic-cross 注意力 + 计数先验） | 一作，Elsevier 通讯脚注丢失 |
| 03_Lightweight_PR2023 | 2023 | Pattern Recognition 137 | 烟雾语义分割（轻量，<1M 参数） | **共同一作**（与 Kang Li，有印刷脚注），通讯明确是 Zhijun Fang。无 CRediT，两位共同一作的起草分工不明 |
| 12_CNN_Transformer_PR2023 | 2023 | Pattern Recognition 136 | 医学图像分割（CTC-Net） | 一作。主题混杂：医学。二作是其硕士生 |
| 13_BiDirectional_TIP2024 | 2024 | IEEE TIP 33 | 皮肤病灶分割（BiFBA-Net） | 一作，IEEE 脚注丢失。主题混杂：医学 |
| 05_NewtonInterpolation_PR2025 | 2025 | Pattern Recognition 159 | 烟雾语义分割（NINet） | 一作，通讯是其博士生 Guiqian Wang。**CRediT 明确 Writing–original draft 是 Wang**，正文按学生起草处理 |

## Tier A3｜权重 0.75（通讯但非一作）——3 篇

| Paper_ID | 年份 | Venue | 主题 | 备注 |
|---|---|---|---|---|
| 04_SAGINN_TIP2024 | 2024 | IEEE TIP 33 | 烟雾语义分割（GINL/PHSA + 烟雾感知损失） | 三作 + 明确通讯。共同一作是学生 Lin Zhang 与 Jing Wu，正文很可能由学生起草，主要用作"资深角色"证据 |
| 18_DualGuided_TMM2024 | 2024 | IEEE TMM 26 | 少样本语义分割（频域原型 + DCT 池化） | 四作 + 共同通讯。主导团队是 Wen/Huang/Ma，一手风格价值低。主题混杂：少样本分割 |
| 06_MIFNet_PR2025 | 2025 | Pattern Recognition 159 | 烟雾图像分割（Transformer + CNN 双编码器） | 二作 + 通讯。**CRediT 明确 Writing–original draft 是 Kang Li**，正文按学生起草处理 |

## Tier B｜权重 0.25（二作，只能佐证或反驳）——2 篇

| Paper_ID | 年份 | Venue | 主题 | 备注 |
|---|---|---|---|---|
| 10_FrequencySpace_TCE2025 | 2025 | IEEE TCE 71(2) | 轻量烟雾分割（傅里叶频空交互） | 二作，通讯标记丢失于栏序错乱。一作 Kang Li 主导，风格价值低 |
| 09_MultiStage_TIP2026 | 2026 | IEEE TIP 35 | 实时轻量烟雾分割（0.73M 参数） | 二作，IEEE 脚注丢失。若 PDF 证实通讯可升 A3。与 10 共享作者与参考文献，混杂风险高 |

## 建模优先级（P2–P4 直接照此取样）

**一级锚点（一手行文，优先取样）：** 21、20、36、31、07、17（17 仅取干净段落）
**二级（一作，可放心用但通讯未证实）：** 19、16、08、01、02、11、12、13、30、03
**三级（正文由学生起草，只看结构与组织，不当一手语言证据）：** 05、06、04、18
**佐证层（不得独立生成特征）：** 09、10

## 年代与主题分布（P4 去混杂用）

年代和方法范式是两条不同的轴，P4 要分开查。

**按年份切（2011–2019 共 8 篇 / 2020–2026 共 14 篇）**
- 前段：21(2011)、17(2012)、31(2016)、19(2016)、20(2017)、16(2018)、30(2019)、08(2019)
- 后段：01(2020)、11(2021)、07(2021)、02(2022)、03(2023)、12(2023)、04(2024)、13(2024)、18(2024)、05(2025)、06(2025)、36(2025)、10(2025)、09(2026)

**按方法范式切（手工特征 7 篇 / 深度学习 15 篇）**
- 手工特征：21、17、31、19、20、16、30
- 深度学习：08、01 起，及其后全部 15 篇
- 注意 08（2019）已是深度方法，所以年份分界点与范式分界点不重合，这个错位正好可以用来区分"年代语言趋势"和"方法范式带来的表述变化"。

**烟雾任务（17 篇）：** 21、17、31、19、20、16、30、08、01、07、02、03、04、05、06、10、09
**非烟雾任务（5 篇，天然对照组）：** 11（去雾）、12（医学分割）、13（皮肤病灶）、18（少样本）、36（超分）

**Venue 分布**
- IEEE TIP 5 篇：01、07、04、13、09
- Pattern Recognition 7 篇：17、11、02、03、12、05、06
- Information Sciences 2 篇：19、16
- KSII TIIS 2 篇：31、30
- IEEE TCE 2 篇：36、10
- IEEE Access 1 篇：20；IEEE TMM 1 篇：18；Neurocomputing 1 篇：08；Fire Safety Journal 1 篇：21

P4 判断"出版社模板效应"时的主对照轴是 **IEEE 系列 9 篇（01、07、04、13、09、36、10、20、18）对 Elsevier 系列 11 篇（17、11、02、03、12、05、06、19、16、08、21）**，KSII 2 篇作第三方参照。

**固定合作者线索：** Kang Li（03 共同一作、06 一作、09 一作、10 一作）、Xue Xia（02、11、16、19、30）、Jinting Shi（02、16、19、30）、Lin Zhang（02、07、16、04）、Zhijun Fang（03、12、19）、Chunmei Wang（06、09、10）。P4 必须检查 Kang Li 参与的 4 篇是否形成独立的写作簇。
