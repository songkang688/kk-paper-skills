# 按章节的微观语言特征（袁非牛）

数据来源：22 篇 × 4 个章节块 = 88 条记录，逐项脚本统计。原始数据 `../_work/p4_micro_raw.csv`，分组报告 `../_work/p4_micro_report.txt`。
所有密度指标单位为"每千词次数"（记作 /k）。表中数值为 22 篇的**中位数**，不是均值，以免被个别篇目拉偏。

**方法学说明（必读）**：被动语态、时态、名词化三项是正则近似而非句法分析。被动 = `be 动词 + 3 字符以上的 -ed/-en 分词`；名词化 = `以 -tion/-sion/-ment/-ness/-ity/-ance/-ence 结尾的 4 字符以上词`。这些指标可用于**同一语料内部的跨章节与跨分组比较**，不适合与外部文献的绝对值对照。

---

## 一、总表

| 指标 | Front（Title/Abstract/Intro/RW） | Methods | Results | Conclusion |
|---|---|---|---|---|
| 句长均值（词） | 20.8 | **21.9** | **19.1** | 21.1 |
| 句长中位数 | 19 | 20 | **17** | 20 |
| 超长句占比（>40 词，%） | 2.9 | **6.4** | 2.7 | **0** |
| 段落长度均值（词） | 126.5 | **81.6** | 85.2 | **164** |
| 被动语态 /k | 9.2 | **11.4** | 8.1 | **6.5** |
| we /k | 8.3 | 15.1 | 13.8 | **18.8** |
| our /k | **2.5** | 4.5 | **17.4** | 9.8 |
| we + propose/design/... /k | 5.6 | 6.5 | **1.3** | **13.0** |
| we + 过去时实验动词 /k | **0** | **0** | **2.8** | **0** |
| hedge 词 /k | 2.7 | 2.5 | 2.2 | **0** |
| booster 词 /k | 2.4 | 1.1 | 2.6 | **0** |
| 连接词 /k | 5.1 | 4.1 | 5.0 | **6.2** |
| 名词化 /k | 85.8 | 61.4 | **51.2** | **91.8** |
| 缩写 /k | **29.4** | 32.2 | **56.4** | 43.2 |
| 目的从句 /k | 3.5 | 3.1 | 3.0 | **5.6** |
| `, so/thus` 因果尾句 /k | 1.2 | 1.2 | 1.0 | **0** |
| `As shown in ...` 证据锚点 /k | **0** | 2.7 | 2.6 | **0** |

## 二、从数据里读出来的七条特征

### MS1｜句长在四个章节之间几乎不变，这本身就是特征

句长均值 19.1–21.9，中位数 17–20，四节的极差不到 3 个词。也就是说他**不用句长来区分章节功能**。唯一的分化在超长句：Methods 有 6.4% 的句子超过 40 词（因为要在一句里写完"转置→卷积→转置回"这类变换链），而 Conclusion 的超长句占比是 **0%**。

- **Do**：目标句长 17–22 词。Methods 允许少量长句承载完整变换链；Conclusion 严格控制在 25 词以内，一句一件事。
- **Confidence**：high（跨 22 篇的中位数稳定）。

### MS2｜段落长度才是区分章节的手段，Conclusion 是 Methods 的两倍

段落长度中位数：Conclusion 164 词 → Front 126.5 → Results 85.2 → Methods 81.6。

Methods 和 Results 用**短段落**（一段一个模块 / 一段一个观察），Conclusion 用**长整段**（把方法整体压成一段密集复述）。

- **Do**：Methods/Results 每段 80–90 词，一段只处理一个模块或一个证据锚点；Conclusion 允许 150–200 词的单一长段。
- **Confidence**：high。

### MS3｜`our` 在 Results 里暴涨 7 倍，`we propose` 在 Conclusion 里达到峰值

`our` 密度：Front 2.5 → Methods 4.5 → **Results 17.4** → Conclusion 9.8。
`we + propose/design/...` 密度：Front 5.6 → Methods 6.5 → **Results 1.3** → **Conclusion 13.0**。

两条曲线正好相反。Results 里几乎不说"我们提出"，而是反复说"our method / our CSSAM / our BiFBA-Net"——因为该节的主语是**被比较的对象**而不是**提出的动作**。Conclusion 则回到"我们提出"，密度是全文最高，比 Methods 还高一倍。

- **Do**：Results 用 `our method / our <模块名>` 作主语做比较；Conclusion 用 `we propose` 重新宣告一遍每个模块。不要在 Results 里写 `we propose`。
- **Confidence**：high。这是全表里最干净的一组反向对照。

### MS4｜时态纪律严格：过去时被完全限制在 Results

`we + 过去时实验动词`（conducted / performed / implemented / compared / tested / trained / evaluated）密度：Front **0** → Methods **0** → Results **2.8** → Conclusion **0**。

方法陈述一律现在时，实验陈述一律过去时，而且过去时**只出现在 Results**。Conclusion 里回顾实验时也用过去时，但密度低到中位数为 0（只有 08、17 等个别篇目有 `We performed experiments` / `Several experiments were performed`）。

- **Do**：方法与模块一律现在时；只在 Results 里用过去时描述做过的实验；Conclusion 里回顾实验优先用现在时的结论陈述（`Experiments show that ...`）而不是过去时的过程陈述。
- **Confidence**：high。

### MS5｜Conclusion 不 hedge、不用因果尾句、不用证据锚点

Conclusion 的 hedge 中位数 **0**、booster 中位数 **0**、`, so/thus` 中位数 **0**、`As shown in` 中位数 **0**。四项同时为零。

这不代表 Conclusion 没有不确定性表达——局限性是**单独一段**处理的（见 `../playbook/conclusion_playbook.md` C5），而不是散在句子里的 hedge 词。同时 Conclusion 的连接词密度是全文最高（6.2/k），说明它靠连接词而不是靠 hedge 来组织。

- **Do**：Conclusion 的主体段落用无 hedge 的陈述句；把所有不确定性集中到最后的局限段；不要在 Conclusion 里放表号图号。
- **Confidence**：high。

### MS6｜名词化和缩写密度反向分布，Results 最"动词化"

名词化密度：Conclusion 91.8 → Front 85.8 → Methods 61.4 → **Results 51.2**。
缩写密度：**Results 56.4** → Conclusion 43.2 → Methods 32.2 → Front 29.4。

Results 是名词化最低、缩写最高的一节——因为它满是方法名、数据集名、指标缩写，同时句子结构最简单直接（句长中位数也是最低的 17 词）。Front 与 Conclusion 则是高名词化、低缩写的抽象论述。

- **Do**：Front 与 Conclusion 用抽象名词化表述（`the representation ability of features`、`the interdependence between channels`）；Results 换成短句 + 缩写 + 具体数值。
- **Confidence**：medium-high（名词化为正则近似）。

### MS7｜目的从句在四节都存在，Conclusion 密度最高

目的从句（`To <purpose>, ...` / `In order to ...`）密度：Conclusion **5.6** → Front 3.5 → Methods 3.1 → Results 3.0。四节全部大于 3.0/k，没有一节缺失。

这是 P2/P3 定性发现的量化确认：**"目的在前、机制在后"是贯穿全文的句法习惯，且在 Conclusion 里最密集**。同时它在 Results 里的密度（3.0）主要来自实验设计目的（`To validate the effectiveness of MACM, we design a series of variant experiments`）而不是模块目的。

- **Do**：全文保持 3/k 以上的目的从句密度；Conclusion 提到 5/k 以上。Results 里的目的从句用于交代实验设计意图。
- **Confidence**：high。见 `sentence_patterns.md` S1 的完整处理。

## 三、证据锚点的边界

`As shown in / as listed in / as illustrated in` 密度在 Front 与 Conclusion 都是 **0**，在 Methods 2.7、Results 2.6。

也就是说**表号图号严格限制在 Methods 与 Results**。Introduction 里提到图（如 07 号的 `Some challenging examples for smoke segmentation are shown in Fig. 1`）是极少数例外，Conclusion 里引用图注只有 13 号一例（局限段引用失败案例图 Fig. 9）。

- **Do**：不要在摘要、Introduction 主体或 Conclusion 主体里放表号；难点示例图可在 Introduction 引用一次；失败案例图允许在 Conclusion 的局限段引用。
- **Confidence**：high。
