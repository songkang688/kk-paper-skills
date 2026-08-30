# 微观语言画像

数据：22 篇 × 4 个章节块 = 88 条记录，脚本统计。密度单位为每千词次数（/k），表中数值为 22 篇的**中位数**。
原始数据 `_work/p4_micro_raw.csv`，分组报告 `_work/p4_micro_report.txt`。

**方法学说明**：被动语态、时态、名词化三项是正则近似而非句法分析。这些指标可用于**同一语料内部的跨章节与跨分组比较**，不适合与外部文献的绝对值对照。

---

## 一、总表

| 指标 | Front | Methods | Results | Conclusion |
|---|---|---|---|---|
| 句长均值（词） | 20.8 | **21.9** | **19.1** | 21.1 |
| 句长中位数 | 19 | 20 | **17** | 20 |
| 超长句占比（>40 词，%） | 2.9 | **6.4** | 2.7 | **0** |
| 段落长度均值（词） | 126.5 | **81.6** | 85.2 | **164** |
| 被动语态 /k | 9.2 | 11.4 | 8.1 | 6.5 |
| we /k | 8.3 | 15.1 | 13.8 | **18.8** |
| our /k | **2.5** | 4.5 | **17.4** | 9.8 |
| we + propose/design /k | 5.6 | 6.5 | **1.3** | **13.0** |
| we + 过去时实验动词 /k | **0** | **0** | **2.8** | **0** |
| hedge 词 /k | 2.7 | 2.5 | 2.2 | **0** |
| booster 词 /k | 2.4 | 1.1 | 2.6 | **0** |
| 连接词 /k | 5.1 | 4.1 | 5.0 | **6.2** |
| 名词化 /k | 85.8 | 61.4 | **51.2** | **91.8** |
| 缩写 /k | **29.4** | 32.2 | **56.4** | 43.2 |
| 目的从句 /k | 3.5 | 3.1 | 3.0 | **5.6** |
| 逗号 + so 因果尾句 /k | 1.2 | 1.2 | 1.0 | **0** |
| `As shown in` 锚点 /k | **0** | 2.7 | 2.6 | **0** |

## 二、可执行结论

1. **句长目标 17–22 词，四节几乎不变。** 他不用句长区分章节功能。Methods 允许少量超长句承载完整变换链（超 40 词占 6.4%）；**Conclusion 严格控制在 25 词内**（超长句占比 0%）。
2. **段落长度才是区分章节的手段。** Methods/Results 每段 80–90 词，一段只处理一个模块或一个证据锚点；Conclusion 允许 150–200 词的单一长段。
3. **`our` 在 Results 暴涨 7 倍，`we propose` 在 Conclusion 达峰。** Results 里不写 `we propose`；Conclusion 里把每个模块重新宣告一遍。
4. **过去时只在 Results。** 方法与模块一律现在时。Conclusion 回顾实验优先用现在时的结论陈述（`Experiments show that ...`）而不是过去时的过程陈述。
5. **Conclusion 主体不 hedge、不用因果尾句、不用证据锚点**（四项中位数同时为 0）。不确定性集中到最后的局限段，靠连接词而非 hedge 组织（连接词密度全文最高 6.2/k）。
6. **名词化与缩写反向分布。** Front 与 Conclusion 用抽象名词化表述；Results 换短句 + 缩写 + 具体数值（名词化最低 51.2、缩写最高 56.4、句长最短 17）。**名词化的绝对水平是主题词汇效应，已剔除；只保留章节间落差。**
7. **表号图号严格限制在 Methods 与 Results。**
8. **目的从句在四节都 > 3/k，Conclusion 最高。** 不给密度目标，只要求每个模块前面都有。

## 三、七种句子功能转移

完整版含示意句与反例见 `dna/sentence_patterns.md`。

| ID | 转移 | 模板 |
|---|---|---|
| S1 | 方法 → 目的 | `To <purpose>, we <propose/design/adopt> <Module (ABBR)>.` 变体：`In order to ...` / `For the sake of ...` / `Aiming at solving this problem, ...` / `Motivated by ...` / `Inspired by ..., we also ...` |
| S2 | 现状 → 缺陷 | `Although X <能做到什么>, it discards / does not involve / loses <某类信息>.` |
| S3 | 前提 → 后果 | `<可核验前提>, so <设计后果或约束>.` |
| S4 | 操作 → 解释 | 公式编号后 `where <符号> is <含义>, ..., and <符号> is ...`；同类符号用 `respectively` 串联 |
| S5 | 证据锚点 → 观察 | 分离式 `Table N lists <什么>.` 或合写式 `As shown in Table N, we find that <观察>.` |
| S6 | 观察 → 比较 | `<对手> achieves slightly higher <指标> than ours, but our <另一指标> is distinctly lower.` |
| S7 | 比较 → 结论或限定 | 可核验 → `The (main) reason is that ...`；不可核验或不利 → `The (main) reason may be that ...` |
| S8 | 段尾 → 承接 | 定位式 `Inspired by ..., we also ...`；消融结论式 `..., so it means that <模块> plays an important role in <功能>.`；前提后果式见 S3 |

## 四、四个已量化的构式

| 构式 | 全语料次数 | 分布 | 用法 |
|---|---|---|---|
| `not only ... but also ...` | 35（最高频） | Front 11 / Methods 9 / Results 11 / Conclusion 4 | 把两个价值点绑在一句里，常用于贡献陈述与结果陈述 |
| `we (can) find that` | 30 | Results 23 | 与证据锚点合写 |
| `above-mentioned / aforementioned` | 29 | Front 18 | 集合回指。**通用学术英语，不作风格标识。** 03 号同篇内拼写不统一，复刻时统一用带连字符形式 |
| `slightly` | 20 | Results 18 | 非对称让步的关键副词 |
| `so that` | **6** | 4 次集中在 16 号一篇 | **不是习惯，不要使用作为风格标识** |

## 五、明确不作为语言特征的项

- `we propose` 高频 —— 纯通用
- `Experiments show that ...` —— 通用学术英语（22/22 出现只证明遵守惯例）
- 一句一方法的 `Author et al. [n] proposed` 综述节奏 —— 计算机视觉综述领域惯例
- 公式后 `where` 逐符号定义 —— 学术写作通行规范
- 名词化整体偏高 —— 主题词汇效应（烟雾术语本身多 -tion/-ity）
- 被动语态密度 —— 纯年代效应（详见 `overgeneralization_blacklist.md` 第三类）
- 缩写密度 —— venue 效应（IEEE 的 Conclusion 是 Elsevier 的 2.4 倍）
