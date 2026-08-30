# 图表与图注风格

证据：22 篇共 419 条图表标题（11,605 词）。原文见 `_work/p3_captions/`；详细规则见 `playbook/figures_captions_playbook.md`。

**覆盖范围声明**：语料的表格内容在 PDF 提取时普遍丢失，只有图表标题存活（见 `corpus/cleaning_log.md`）。因此本文件只覆盖**图注写法**与**图的角色分工**，无法覆盖表格内部排版、字体、配色的实现层面。按 00 号规则，**不猜绘图软件与字体名**。

---

## 一、图注长度两档分化

| 档 | 适用图类 | 长度 | 写法 |
|---|---|---|---|
| 短档 | 架构图、流程图、算子示意图、曲线图 | 5–15 词 | 一个名词短语，靠正文解释 |
| 长档 | 定性比较图、消融图、失败案例图、难点示例图 | 30–60 词 | 总述 + 逐面板枚举 + 颜色语义说明 |

跨篇平均词/条从 7.2 到 44.7，差异主要由该篇是否有多面板定性比较图决定，不由年代决定。

**短档示意**：`Fig. 1. Imaging model of smoke particles.` / `Fig. 2. The overall framework of the proposed <Net>.` / `Fig. 9. Training error curve of the neural network.`

**长档结构**：`Fig. N. <总述>. (a) <面板>. (b) <面板>. The results by (c) <方法1>, (d) <方法2>, ..., and (x) our method. <颜色/线型语义说明>. <附加信息说明>.`

## 二、多面板顺序（零反例的硬规则）

```
(a) 输入图
(b) ground truth（真实数据无 GT 时跳过，(b) 直接进对比方法）
(c)…(x) 各对比方法（顺序必须与主比较表的行顺序一致）
最后一个面板 = our method
```

**our method 永远在末位。** 6 个多面板比较图无一例外，这是全语料唯一可机械校验且零反例的规则。

数据集分组时，组内顺序保持一致：`(a) 图像 (b) ground truth (c) 预测 / (d)–(f) 第二个数据集的同一三联 / (g)–(i) 第三个数据集的同一三联`。

## 三、颜色语义显式定义且逐图重复

在图注末尾加一句颜色或线型的语义约定，并在后续**每一张**用到该约定的图注里重复一遍。不写"颜色含义同上图"。

改写示意：`The blue outlines indicate the annotated regions, while the yellow ones show the predictions of each method.`

结构是：`The <颜色1> <线型名> <动词> <语义1>, and the <颜色2> ones <动词> <语义2>.`

主证据是 13 号在 Fig. 5、6、7、8、9 五张图注里逐一重复同一约定，措辞间有微小漂移（动词在 `are` 与 `denote` 之间互换、第五次省略了定冠词）——这个不一致本身是真实手写习惯的证据，但也意味着**不可作为模板机械复制**，复刻时自己保持措辞一致即可。

## 四、消融图用递进式面板

面板从最简基线开始，每个面板增加一个组件，图注逐条写出该面板包含什么。

示意：`Fig. N. Ablation analysis. (a) a plain encoder-decoder; (b) an encoder-decoder with short-cut connections; (c) <b 加一个组件>; (d) the proposed <Net> with all components.`

配套正文逐面板对应说明（`Fig. Na is just ... by removing ...` / `In Fig. Nc, we add ... to Fig. Nb, but we do not ...` / `Fig. Nd is the proposed ...`）。

**不要在一个消融图里同时改两个组件；图注的面板描述必须与消融表的变体名一致。**

## 五、表格标题

单行名词短语：`<Comparisons / Experiments> <of 什么> <on 哪个数据集>`。一行结束，不加解释从句，不写结论，不写指标定义。

大小写形式跟随目标期刊（IEEE 全大写 / IEEE 句首大写 / Elsevier 句首大写三种并存）——**这是 venue 模板，不是个人风格。**

## 六、图的角色分工七类，位置固定

| 角色 | 位置 | 图注档位 |
|---|---|---|
| 难点示例图 | Introduction | 长档 |
| 概念 / 成像模型图 | Methods 开头 | 短档 |
| 总体架构图 | Methods 总览小节 | 短档 |
| 模块细节图 | 各组件小节 | 中短档（含子图枚举） |
| 消融图 | Results 消融小节 | 长档，递进式面板 |
| 定性比较图 | Results 比较小节（合成与真实各一张） | 长档，our method 在末位 |
| 失败案例图 | Conclusion 局限段或 Results 末尾 | 长档 |

可选两类：
- **数据集样例图**：结构是 `Fig. N. <样例来源说明>: (a) <正类样例> and (b) <负类样例>.` 改写示意：`Fig. 6. Representative examples collected for training: (a) positive patches and (b) negative patches.`
- **精度-代价权衡散点图**：可作全文首图（36、03 都这样做），把精度与参数量的权衡放在最显眼位置

**失败案例图不得放在比较图之前。**

## 七、必须剔除的项

1. **Elsevier 插入句**：`(For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)` 是排版系统自动加的，不是作者写的。生成时不得复现。
2. **清洗标记**：`[NOTE: table contents not present in extracted text.]` 是语料清洗时加的，不是原文。
3. **正文中的图解读段不是图注**。以 `Fig. N shows / illustrates ...` 开头的段落属于"图的正文解读"，恰好印证了架构图靠正文解释这一点，但统计图注长度时应视为污染项。
