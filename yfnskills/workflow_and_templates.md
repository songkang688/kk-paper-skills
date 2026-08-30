# 操作流程与章节骨架模板

模板里的示意句全部是改写过的，可直接套用，但**必须替换全部内容词**。方括号 `[ ]` 内是需要用户提供的事实。

**本文件管单个章节怎么写**。要出整篇初稿或把中文稿重写成英文稿时，编排（问诊、事实包、五路分节 agent 并行、父节点融合、tex/pdf/docx 三格式）走 `draft_workflow.md`，各分节 agent 写作时仍回到本文件取对应章节的骨架模板。

---

## 一、从事实要点到成稿的六步流程

与用户的所有往来（要事实、报缺口、交代取舍）都用平常说话的方式，口吻参照 `review_voice.md`：说清缺了什么、缺了会怎么样、建议怎么补，不要发验收单式的表格问卷。

### 第 1 步：收集事实（不可跳过）
按 `SKILL.md` 第二节的表格向用户索取要写章节所需的事实。缺项就明确列出缺哪几项、缺了会导致什么，然后只写能写的部分，缺口标 `[TODO: 需要 X]`。**不用占位数字或编造的模块名填充。**

### 第 2 步：填推理链
```
Problem: [用户给的表面问题]
Representation Failure: [追问一层——哪类信息没被表示出来]
Design Principle: [从信息缺失抽象出的原则]
Module: [以被丢失的信息命名]
Ablation: [移除后掉多少]
Claim: [在什么数据集上比谁好多少]
```
链条填不满就回到第 1 步。**模块名必须包含 Representation Failure 里那类信息的名称**（见 `research_reasoning.md` RD1）。

### 第 3 步：确认适用条件
逐项检查带条件的规则是否适用：主题是不是烟雾/火灾类（决定 I2、T5、RS6）、论文是不是轻量或高效类（决定 RS8）、是不是深度学习方法（决定 M5）、是否借用了外部数学工具（决定 M7）、目标年代风格（决定 C5）。条件不满足就跳过该规则，**不要变形套用**。

### 第 4 步：按章节骨架起草
用下面的模板。起草时优先保证结构骨架（`SKILL.md` 第四节六条），句法细节可以第二遍再打磨。

### 第 5 步：过自检清单
`SKILL.md` 第九节的自检清单，逐项过。

### 第 6 步：回报缺口
把所有 `[TODO:]` 与 `[REF:]` 汇总列给用户，说明每一项缺了会影响哪条规则。

### 第 7 步：出 md 与 PDF 两份
把定稿写成 `.md`，然后转出同名 `.pdf`，两份放同一目录：

```bash
python md2pdf.py <文稿.md>       # 论文正文类加 --serif
```

跨平台，换电脑不用改。新机器上先跑 `python md2pdf.py --check` 确认三项依赖齐全。

只给 md 视为未完成。若环境缺 python、markdown 解析器或 PDF 渲染器，照常写出 md 并明确告知 PDF 未生成的原因与手动命令，不要静默跳过。详见 `SKILL.md` 第四点五节。

---

## 二、章节骨架模板

### Title
```
[Mechanism Full Name] for [Task Name]
```
可选前缀 `A / An`（Elsevier 稿件更常见）。机制槽位有对偶性时用 `Dual-` / `Bi-` / `A and B complementary`。9–14 词，槽位不超过两个。

### Abstract（180–260 词）
```
[对象] has [属性1] and [属性2], which leads to a challenging task of [任务].
To solve these problems, we propose a [Full Method Name] ([ABBR]) for [任务].
To [目的1], we first propose a [Module1] ([M1]) to [作用].
To [目的2], we design a [Module2] ([M2]), which [操作说明].
In addition, to [目的3], we present a [Module3] ([M3]) to [作用].
Finally, we [整合动作] to build our [ABBR].
Experiments on [数据集类型] show that our method outperforms existing state-of-the-art methods.
[可选次级结论句：额外数据集 / 额外任务 / 额外性质]
```
**结尾不给具体数值。**

### Introduction
```
段1（真实代价）：[任务] is important for [具体后果], since [原因]. [次级应用场景，可选].
段2（传统方案物理失效，限有非视觉替代方案的任务）：Traditional [旧方案] usually [工作原理]. However, [必须满足的物理前提] is required, so [在目标场景不成立]. Therefore, [旧方案] is not suitable in such cases.
段3（显式切分）：[领域] can be classified into [N] categories: [类1] and [类2]. 或 The general framework of [任务] mainly contains [N] steps, which are [A], [B], and [C], respectively.
段4（难点枚举）：It is a challenging task to [任务]. The reasons are [N] folds: 1) [属性1], 2) [属性2], ..., and N) [属性N].
段5（逐条评述）：[Author] et al. [n] proposed [方法], which [机制]. If [场景条件], the method may [失效方式]. [Author] et al. [n] used [方法]. However, [方法] depends greatly on [前提], which varies in [条件], so [后果].
段6（收敛到信息缺失）：Although [某类方法] works well, it discards / does not involve / loses [某类信息]. To capture [该信息], we propose [以该信息命名的模块].
段7（压缩解法，若有独立 RW）：The first way is to [路线1], but [缺陷]. Another way is to [路线2], hence [优点]. In our method, we follow the [第几] way.
段8（贡献列表）：The main contributions of this paper are summarized as follows:
1) We propose a [Module1] to [目的]. [1–3 句机制与有效性说明]
2) To [目的], we design a [Module2]. [说明]
3) By integrating [Module1], [Module2] and [Module3], we propose [Full Name] ([ABBR]) for [任务]. [整合说明]
段9（路线句，可选）：The rest of this paper is organized as follows. Section II reviews related work on [A], [B] and [C]. Section III details [方法名]. ...（路线句是全学科通用样板，写的时候换成自己的章节安排即可，不要整句照抄任何一篇的原文）
```

### Related Work
```
## [N]. Related work
### [N.1] [一般任务的技术谱系名]
[Author] et al. [n] proposed [方法], which [机制]. ... However, these methods [具体缺陷].
### [N.2] [本文具体任务名]
[早期手工方法综述]. With the rapid development of deep learning, [深度方法综述]. Yuan et al. [n] proposed [自己的前作], which [机制]. [中性评价或指出局限]
### [N.3] [本文贡献所在的机制谱系]
[该谱系的方法综述含缺陷从句]
[定位段] However, above-mentioned methods do not [缺陷]. Inspired by the recent successes of [某路线], we design [模块1] to [目的], [模块2] to [目的], and finally combine these modules to jointly solve [问题].
```

### Methods
```
## [N]. The proposed method
### [N.1] Architecture overview
Fig. [k] shows the overall framework of our [ABBR], consisting of [阶段列表]. Given an input image with the size of [H × W], [第一步]. Then, [第二步]. Finally, [输出说明].
### [N.2] [Module1 Name]
To [目的], we propose [Module1]. [前提事实], so [设计约束]. For an input feature tensor X ∈ R^{C×H×W}, we first [操作1] to produce [中间表示], then [操作2], and finally [操作3] so that the output keeps the same size as the input.
    [公式] (1)
where [符号] denotes [含义], [符号] is [含义], and [符号] is [含义].
### [N.3] [Module2 Name]
To [目的], we design [Module2]. ...
### [N.k] Loss function
Our objective function consists of [N] terms. [逐项说明各分量监督哪个输出与权重]
    [公式] (k)
where [符号定义]
```

### Results
```
## [N]. Experimental results
### [N.1] Datasets and implementation details
[数据集清单与规模]. [训练设置：优化器、学习率、batch、epoch、硬件]
### [N.2] Evaluation metrics
[指标定义与公式]
### [N.3] Ablation studies
To validate the effectiveness of [Module], we design a series of variants, as shown in Table [k].
As shown in Table [k], we find that removing [Module] degrades [指标] by [数值], so it means that [Module] plays an important role in [功能].
[The reason is that <可核验机制>.] 或 [The reason may be that <不可核验属性>.]
### [N.4] Comparisons with state-of-the-art methods
Table [k] lists quantitative comparison results on [数据集].
Our method achieves the highest [指标] of [数值] among compared methods while maintaining [代价指标].
[若有输掉的指标] [对手] achieves slightly higher [指标] than our method on [子集], but our [另一指标] is distinctly lower on all the [N] sets.
Fig. [k] shows [定性结果说明].
### [N.5] Experiments on real [对象] scenes（限烟雾类）
[定性结果与判断依据说明]
### [N.6] Real-time inference performance（限轻量类）
[参数量、FLOPs、FPS 与取舍陈述]
```

### Conclusion（150–250 词）
```
[对象] has [属性1], [属性2] and [属性3]. These properties lead to a challenging task of [任务].
In this paper, to [目的1], we propose a [Module1] to [作用]. To [目的2], we design a [Module2] that [机制]. To [目的3], we present a [Module3].
By integrating [模块列表], we propose [Full Name] ([ABBR]) for [任务].
Experimental results on [数据集] demonstrate that our method outperforms existing state-of-the-art methods.
[局限段，2023 年后风格] Although our method achieves [成绩], our limitation lies in [具体局限]. The main reason may be that [机制]. In the future, we will [具体技术方向].
```

### 图注
```
短档：Fig. [k]. [名词短语].
长档：Fig. [k]. [总述]. (a) [面板1]. (b) [面板2]. The results by (c) [方法1], (d) [方法2], ..., and ([末位]) our method. [颜色/线型语义说明]. [附加信息说明].
消融图：Fig. [k]. Ablation analysis. (a) [最简基线]; (b) [基线加一个组件]; (c) [再加一个]; (d) the proposed [ABBR] with all components.
表标题：TABLE [k] [Comparisons/Experiments] of [什么] on [哪个数据集]
```

---

## 三、改写现有草稿时的检查顺序

改写整篇草稿的完整流程（接稿问诊、目录约定、逐节顺序、验证闸门）在 `polish_workflow.md`；下面只是其中「检查什么先检查什么」的顺序，因为前面的改动会影响后面：

1. **结构层**：章节顺序、小节顺序（消融在前、损失在最后）、Related Work 是否以定位段收尾、是否误写了独立 Discussion
2. **闭环层**：每个模块是否有对应消融、模块名是否回指被诊断的信息缺失、贡献条数与模块数是否对应
3. **句法层**：目的从句是否都在模块之前、Results 里是否误用 `we propose`、过去时是否越界、表号是否越界
4. **措辞层**：输掉的指标是否用了 `slightly`、因果解释的 hedge 档位是否正确、有无 `has attracted increasing attention` 这类禁用句
5. **图注层**：our method 是否在末位、颜色语义是否逐图声明、有无 Elsevier 插入句
6. **事实层**：所有数值、公式、引用是否都有出处；缺口是否都标了 `[TODO:]` / `[REF:]`
