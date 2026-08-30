# 九章节写作指令（精简可执行版）

本文件是 `playbook/` 下九份详细 playbook 的合一精简版。每节只保留可直接执行的指令。
需要证据与反例时查 `evidence_register.csv`（按 Rule_ID 检索）或 `playbook/` 的原始文件。

**每节开头的"先确认"是硬性前置条件，缺项必须先问用户。**

---

## §1 Title

**先确认**：机制名、任务名、是否有缩写命名。

1. 结构写成 `[机制名词短语] + for + [任务名]`。任务名在最后，不要提到句首。不用 `Using`。〔T1〕
2. 标题写机制的**全称**，缩写留到摘要首次定义。不要在标题放 `W-Net` / `CCENet` 这类内部命名。〔T2〕
3. 方法有互补双路或两次操作时，用 `Dual-` / `Bi-` / `double` / `A and B complementary` 显式写出对偶性。方法没有对偶性就不要套。〔T3〕
4. 任务名取当前最精确的粒度。烟雾类按 `detection → recognition → segmentation → density estimation` 选，并在 Introduction 论证为什么比上一级更难。〔T5，限烟雾〕
5. 长度 9–14 词，槽位不超过两个。不写数据集名、参数量、性能数字。〔T6〕
6. **不要**用 `A/An + 评价形容词` 开头当风格标识——那是 venue 相关的。〔黑名单〕

## §2 Abstract

**先确认**：难点属性、总方法名与缩写、各模块名称与用途、实验结论方向与强度。

目标 180–260 词。move 序列：

1. **首句**给难点，归因到**对象的物理或视觉属性**（半透明、边界模糊、形状纹理颜色变化大、非刚性）。不要归因到缺数据集、指标不统一、算力不足。〔A1〕
2. **第二句**钩连并首次定义缩写：`To solve these problems / Aiming at solving these problems, we propose a <Full Name> (<ABBR>) for <task>.` 必须显式回指第一句的难点。〔A2〕
3. **主体**逐模块巡览，每个模块写成 `To <purpose>, we <propose/design/present/adopt> <Module (ABBR)>`，用 `first → then → Afterwards / In addition → Finally` 串联。一句一个模块，不要合并。〔A3〕
4. **结尾** `Experiments / Experimental results / Extensive experiments (on <数据集类型>) show / demonstrate / validate that our method outperforms ...` 需要时补一句次级结论（额外数据集、额外任务、额外性质）。〔A4〕
5. **结尾不给具体数值。** 21/22 篇如此。〔A4〕
6. 强度词按结果实际强弱选：压倒优势 `significantly outperforms`；一般优势 `outperforms`；接近或有限 `competitive` / `good` / `satisfying` / `better than most existing methods`。不要一律用 `significantly`。〔A5〕
7. 长度增长花在模块数上，不要用超过 2 句写领域重要性。〔A6〕

## §3 Introduction

**先确认**：应用场景与失败代价、传统替代方案及其物理限制、领域技术路线切分、难点清单、被诊断为缺失的信息、各模块与该信息的对应、贡献条目。

move 序列（第 2 步限烟雾/火灾主题）：

1. **首段落在真实世界代价上**：任务失败会导致什么损失、谁受益。不写 `has attracted increasing attention`。〔I1〕
2. **传统方案物理前提失效式过渡**（限有非视觉替代方案的任务）：旧方案原理 → 它必须满足的物理前提 → 该前提在目标场景不成立 → 因此需要视觉方法。不要写成"旧方案精度低"。〔I2〕
3. **显式给切分**：`... can be classified / divided / categorized into N categories: A and B.` 或 `... consists of N steps, which are A, B, and C, respectively.` 每一类都要命名。〔I3〕
4. **难点枚举**：`The reasons are N folds: 1) ..., 2) ..., 3) ...` 或 `The main reason(s) may be A, B, C, and D.` 每一项都是对象的一个属性。用 `may` 做 hedge，不要写成断言。〔I4〕
5. **逐条评述现有方法**，缺陷写成**条件式失效**：`If / Once <场景条件>, the method may give false alarms.` 或 `X depends greatly on Y, which varies in <条件>, so ...` 不写 `performs poorly`。〔I5〕
6. **收敛到信息缺失**：`Although X works well, it discards / does not involve / loses <某类信息>.` 紧接 `To capture <该信息>, we propose <以该信息命名的模块>.`〔I6/X2〕
7. **压缩解法为 RW 留展开空间**（若有独立 Related Work）：`The first way is ... Another way is ...` 每条一句，不点具体方法名。可以表明自己选哪条：`In our method, we follow the second way.`〔I6〕
8. **贡献列表**：引导句 `The main contributions of this paper are summarized as follows:` + 3 项（必要时 2–5）。每项首句 `We propose/design <模块>` 或 `To <目的>, we <动作>`，随后 1–3 句解释机制与为什么有效。**末项把前面模块整合成整个网络。** 不要把实验结果写成贡献。〔I7〕
9. **章节路线句**（可选，8/22 篇没有）。若写，展开到小节级：`Related work on <A> is given in Section II-A, <B> in Section II-B, and <C> in Section II-C.`〔I9〕
10. **不要**用 `at least N contributions`——那是 2011–2017 的年代标记。〔黑名单〕

## §4 Related Work

**先确认**：小节数与各小节技术谱系名、每小节点评哪些工作及其缺陷、本文贡献属于哪条谱系。

1. 分小节，**按技术谱系或任务命名**，不用"早期方法/近期方法"这类时间轴。3 个小节为众数。〔R1〕
2. 小节排序：`[一般任务] → [本文的具体任务] → [本文贡献所在的机制]`，**让机制小节收尾**。〔R2〕
3. 小节内部一句一方法：`<第一作者姓> et al. [n] proposed / presented / used / adopted / designed <方法>, which <一句机制说明>.` 不要把三四个工作合并成一句。〔R3，节奏可用但不作风格标识〕
4. **缺陷从句紧贴方法句**：方法句后直接加 `but / however <具体缺陷>`。小节末尾再用一句把这批缺陷归并成一类信息缺失。〔R4〕
5. 引用自己的前作用**第三人称**：`Yuan et al. [n] <过去时动词> <方法>`，与相邻他人句式一致，不加自我背书。自引后的评价可以是中性或指出其局限。〔R7〕
6. **必须以定位段收尾**（19/19 篇无例外）。两种开头任选：
   - 肯定式：`Inspired by <某成功路线>, we also <动作>.`
   - 否定式：`However, above-mentioned methods do not <缺陷>.`
   段内必须有一句显式差异化陈述（`Different from previous ... approaches, our method is built on ...`）。〔R5〕
7. 与 Introduction 的重叠用**抽象层级差**控制：Introduction 给路线不点名，Related Work 展开成小节逐篇点名。〔R8〕
8. 方法是两条既有路线的结合时，可加一句合法性依据。结构是"结合类方法能保留各条路线各自的长处"，改写示例：`Hybrid designs are able to retain the respective strengths of the two kinds of representations.`〔R9〕

## §5 Methods

**先确认**：整体数据流、每模块的输入输出尺寸与操作、每模块解决前文哪个问题、损失各分量及监督对象、公式与符号。

小节骨架：`总览 → 组件（逐个）→ 损失/优化`，深度 2–3 层，5–6 个小节为众数。

1. **第一小节给总览**，命名 `Architecture Overview` / `The Overall Structure` / `Overall Pipeline of Our Network`。内容含输入尺寸、经过哪些阶段、每阶段交给哪个模块、如何输出。**总览里不给公式。**〔M1〕
2. **每个组件小节首句先重述问题**：`To address this problem / To overcome this limitation, we propose <模块>.` 然后才给操作与公式。一个小节不引入两个新模块。〔M2/X1〕
3. **模块内部按输入→操作→中间表示→输出推进**，尺寸与通道数显式写出。变换链用 `first ... then ... finally` 一句写完。主动交代通道数守恒与尺寸复原。不写"经过若干卷积后"。〔M3〕
4. **公式后紧跟 `where`** 逐符号定义，一句定义完全部新符号，多个同类符号用 `respectively` 串联。不把定义拆到后文。不用 `obviously` / `it is easy to see` 跳过推导。〔M4〕
5. **损失函数是最后一个小节**，命名 `Loss Function` / `Joint Loss Function` / `Training Loss` / `Deep Supervisions`。逐项列出分量损失与权重，说明每项监督哪个模块的输出。手工特征类论文的等价位置是分类器小节。〔M5〕
6. **前提在前、后果在后**：`<可核验前提>, so <设计后果或约束>.` 不倒写成 `Therefore we design X because Y`。注意主形式是逗号 + `so`，**不是 `so that`**。〔M6〕
7. **借用外部数学工具时先复述**（LBP、LTP、Curvelet、KPCA、GPR、插值理论等）：专设一个小节讲清该工具含公式，再用后续小节讲自己的改动。复述小节里不夹自己的改动。〔M7〕

## §6 Results

**先确认**：数据集清单、指标定义、消融变体与掉分数值、主比较表的方法顺序与数值、输掉的指标、代价指标。

小节序列：`数据集 → 实现细节/设置 → 评价指标 → 消融 → 与 SOTA 比较 → 真实场景/视频 →（复杂度或实时性）`

1. **消融放在比较之前。** 不要把消融拆散插在各比较小节之间。〔RS1〕
2. **每个观察挂显式锚点**：`Table N lists <什么>.` 独立成句，或 `As shown in Table N, we find that <观察>.` 合写。不写无出处的结论。〔RS2/X6〕
3. **因果解释分两档**：
   - 可核验的架构或数据事实（自己为什么赢、对手的已知架构缺陷、数据集规模、消融的结构性后果）→ `The (main) reason is that ...`
   - 不可核验的属性或不利结果（自己为什么输、模块为什么没增益、数据分布、对象外观、图像质量）→ `The (main) reason may be that ...`
   不用 `This is obviously because` / `It is clear that`。〔RS3〕
4. **次优结果用非对称让步**：先如实承认 `<对手> achieves slightly higher <指标> than our method`，紧接 `but / although ... our method is obviously / distinctly lower/better in <另一指标>`。**`slightly` 只用于对手优势或自身劣势；`obviously / distinctly / nearly` 只用于自身优势。** 输了要给精确数字。〔RS4〕
5. **消融与模块一一对应**，用递进式变体（基线 → 加一个 → 再加一个）。每个变体给出掉多少并说明该模块负责什么：`..., so it means that <模块> plays an important role in <功能>.` 不要出现 Methods 有但消融没测的模块。〔RS5〕
   **若用户根本没有做消融实验**：写 `[TODO: 消融实验缺失]`，不要编造变体或数值。告知使用者闭环无法满足及其后果，并可建议最小消融方案（每个模块各删一次）。语料里 21、30、31、17 四篇没有消融小节，靠理论论证支撑模块合法性——这是真实存在但更弱的选项。
   **若结果条目极少**：不要注水。Results 篇幅应与实际证据量成正比，不补未做过的数据集、未测过的指标或无数据支撑的定性描述。宁可写短，并如实说明证据范围。
6. **真实场景与视频单列小节**（限烟雾类），以定性图为主。不把真实场景结果混进主比较表；无 ground truth 的真实图不报定量指标。〔RS6〕
7. **只做观察与机制解释，不做意义升华。** 不写 future work，不写"这对消防安全有重要价值"。〔RS7〕
8. **代价维度单列**（限轻量或高效类）：报参数量、FLOPs、FPS，用倍数表达优势（`approximately 57× fewer parameters`）。不用"很快"这类无数值表述。〔RS8〕

## §7 Discussion

**默认不写。** 22 篇里 18 篇没有独立 Discussion，这是主流做法而非遗漏。〔D4〕

把内容三分：
- **机制解释** → Results，紧跟对应观察句，用 §6 第 3 条的两档 hedge
- **局限与未来工作** → Conclusion 最后一段，见 §8 第 5 条
- **与文献的对比性判断** → Related Work 的定位段，见 §4 第 6 条

**只有在目标期刊明确要求时才写独立 Discussion。** 此时用下面的骨架，并注意它是从三种单篇形态反推的推断骨架（`overgeneralization_blacklist.md` 第四类已留档）：

1. 让步式总判断：`Although our method achieves ..., there is a long way to ...`
2. 枚举局限，`First / Second / Third`，每条给机制不只给现象
3. 区分任务固有难点与方法自身缺陷，**后者不能缺席**
4. 工程性代价（速度、内存、超参依赖）单列一条
5. 收尾给解决方向
6. 全节不复述定量结果，不做意义升华

另有两种替代形态：局限性子节放 Results 末尾并命名 `F. Limitations of our method`；或把 Results 标题直接写成 `Experiments and discussion` 在标题层声明合并。

## §8 Conclusion

**先确认**：上述全部 + 局限及其机制 + 未来方向的具体技术。

目标 150–250 词，允许 1–2 个长段（每段 150–200 词）。

1. **开头重述难点**，比摘要写得更具体，可用 1–3 句展开。不引入摘要与 Introduction 都没提过的新难点。〔C1〕
2. **模块复述保留目的从句**：`To <目的>, we <propose/introduce/adopt> <模块>.` 措辞与摘要不同但结构保留。〔C2/X1〕
3. **与摘要的信息差**：增加难点展开、模块机制细节、局限与未来工作；保持结论强度不变；**不增加新数字、不引入新对比对象**。〔C3〕
4. **时态**：方法现在时主动（`we propose`），实验过去时（`We performed experiments on ...`）。**不要刻意写被动**——那是年代特征。〔C4〕
5. **局限与未来工作段**（2023 年后风格）：单独一段，局限给机制（可用 `The main reason may be that ...`），未来方向指向具体技术而非"进一步改进"。可引用失败案例图。〔C5〕
6. **句子控制在 25 词以内**，主体段落不 hedge、不用 `, so` 因果尾句、不放表号图号。〔MS1/MS3/X5〕
7. **坦诚式限定**（可选）：某组件其实可选或某论断无法证明时，主动单句说出，不加辩解。例如 `However, <模块> is not compulsory, so we may not apply it if we do not care about <代价>.`〔C6〕

## §9 Figures / Tables / Captions

**先确认**：每张图的角色类型、面板数与内容、颜色或线型的语义约定。

1. **图注分两档**：架构图、流程图、算子示意图用一个名词短语（5–15 词）；定性比较图、消融图、失败案例图用长枚举（30–60 词）。〔V1〕
2. **多面板顺序固定**：`(a) 输入 → (b) ground truth → (c)…(x) 对比方法（顺序与主比较表一致）→ 最后一个面板 = our method`。**our method 永远在末位，零例外。**〔V2〕
3. **颜色语义在图注显式定义**，并在后续每张用到该约定的图注里重复一遍。不写"颜色含义同上图"。〔V3〕
4. **消融图用递进式面板**，每个面板比前一个多一个组件，图注逐条写出该面板包含什么。〔V4〕
5. **表格标题是单行名词短语**：`<Comparisons/Experiments> <of 什么> <on 哪个数据集>`，一行结束，不加解释从句，不写结论。大小写跟随目标期刊。〔V5〕
6. **图的角色分工七类，位置固定**：
   - 难点示例图 → Introduction
   - 概念/成像模型图 → Methods 开头
   - 总体架构图 → Methods 总览小节
   - 模块细节图 → 各组件小节
   - 消融图 → Results 消融小节
   - 定性比较图 → Results 比较小节（合成数据与真实数据各一张）
   - 失败案例图 → Conclusion 局限段或 Results 末尾
   可选：数据集样例图、精度-代价权衡散点图（可作首图）。〔V6〕
7. **不生成出版社插入句**：`(For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)` 是 Elsevier 排版系统自动加的，不是作者写的。〔V7〕
8. **不猜绘图软件与字体名。** 语料的表格内容在提取时普遍丢失，本 Skill 无法覆盖表格内部排版与配色的实现层面。
