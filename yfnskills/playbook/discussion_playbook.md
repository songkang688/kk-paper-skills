# Discussion Playbook（袁非牛）— 有限证据倾向，不是稳定规律

## 先看证据量：这一节的样本量是 1（外加 2 个替代形态）

P3 开工第一步是数 Tier A 里到底有几篇真有独立 Discussion。结果如下（依据 `../corpus/section_coverage.csv` 与 `../_work/p3_struct.txt` 的词数统计）：

| Paper_ID | 状态 | 有效词数 | 能否作证据 |
|---|---|---|---|
| 21_LBP_LBPV_FireSafety2011（A1，独著） | **真正独立成节**，且与 Conclusion 分开（`6. Discussion` + `7. Conclusions`） | 148 | **可以，是唯一一篇** |
| 08_Deep_Smoke_Segmentation_2019（A2） | 作者写的 `F. Limitations of our method` 子节，位于 Results 内部 | 约 210 | 可以，但属"局限性子节"形态 |
| 12_CNN_Transformer_PR2023（A2） | 作者把标题写成 `4. Experiments and discussion`，Results 与 Discussion 合并 | 无法分离 | 只能作"合并写法"的证据 |
| 11_Confidence_Prior_PR2021（A2） | **清洗者按规范拆出，原文没有这一节** | 261 | **不可作证据（P1 审计已标记）** |
| 其余 18 篇 | 无此节，相关内容散在 Results 与 Conclusion | 0 | 不可 |

**结论：Discussion 的独立写法在这个语料里几乎不存在。本 playbook 全部规则的 confidence 上限为 low–medium，且必须标注"有限证据倾向"。生成时的默认策略应当是不写独立 Discussion，而是按 D4 把内容分配到 Results 与 Conclusion。**

---

## D1｜唯一的真实样本（21 号）显示：Discussion 用来交代系统级限制，不用来复述结果

- **When**：仅当目标期刊要求独立 Discussion，或论文有系统级适用范围问题需要单独交代。
- **Why**：21 号的 Discussion 一句结果都没复述，全篇在讲"这个系统在什么条件下不管用"。
- **Do**：按"速度实测 → 是否达到实时门槛 → 对训练集的依赖 → 未知场景下的性能不可知 → 明确说出能力下限 → 给出解决方向"的顺序写，全部用陈述句，不做辩解。
- **Language/Structure**（21 号原文顺序，全节仅 148 词）：
  1. 速度事实：`The algorithm can detect the presence of smoke in a video with the size of 320×240 at about 10 frames per second (fps).`
  2. 与门槛比较：`It cannot obtain real time processing frame rates (above 25 fps).`
  3. 依赖前提：`The algorithm needs a training image set. In fact, the positive and negative images used in the algorithm are impossible to cover all kinds of smoke and non-smoke objects. Therefore, detection and false alarm rates of the system highly depend on the training image set.`
  4. 条件式失效：`If a video contains too many objects which are not included in the training set, the system performance will drop obviously.`
  5. **承认不可知**：`So we do not know the performance on unknown videos. That is the lower limit of smoke detection of the video system.`
  6. 解决方向：`Solution to the above mentioned problems is to create a representative image database and improve the algorithm itself.`
- **Evidence**：1 篇（21，Tier A1，独著，2011）。
- **Counterexamples**：无可比对象。
- **Confidence**：**low（单篇依赖）**。但值得注意的是第 5 步 `So we do not know the performance on unknown videos` 这种直接承认认知边界的写法，在全语料其他位置也能找到同源的坦诚式限定（19 号结论 `However, LPP is not compulsory, so we may not apply LPP if we do not care about dimensions and computation time`；19 号 Introduction `Our experiments validate that feature combination truly improves performance, but it is difficult for us to theoretically prove it`）。**这个"坦诚度"是跨章节可确认的倾向，confidence 可提到 medium；但"用独立 Discussion 承载它"的做法只有单篇证据。**
- **Avoid**：不要在 Discussion 里重复 Results 的数字；不要用 Discussion 做研究意义升华。

## D2｜替代形态一：局限性子节放在 Results 末尾（08 号）

- **When**：不想单开一章，但要交代局限。
- **Why**：08 号把局限做成 Results 的最后一个子节，用一个显式小节标题隔开，从而既不破坏 Results 的观察节奏，也不占用 Conclusion 篇幅。
- **Do**：命名为 `F. Limitations of our method`，先给总判断，再用 `The main reasons are as follows. First, ... Second, ... Third, ...` 枚举，每一条都归因到对象属性；最后补一条工程性局限（速度）。
- **Language/Structure**：`Although our method has achieved good results, there is a long way to reach perfect effects. The main reasons are as follows. First, smoke has very large variations of features: texture, shape, color, etc. ... Second, the edge of smoke is very blurry compared to other objects ... Third, many objects, such as fog and clouds, share the same visual appearance as smoke. ... Therefore, another limitation of our method is that the test speed needs to be further improved.`
- **注意**：这一段的三条归因与该论文 Introduction 的难点枚举同源（都是半透明、边界模糊、类烟物体），也就是**局限性被写成"任务固有难点尚未被完全解决"，而不是"我们的方法有缺陷"**。这是一个可复用的修辞策略，但也要意识到它有回避自身缺陷的风险。
- **Evidence**：1 篇（08，Tier A2，2019）。
- **Confidence**：low（单篇依赖）。
- **Avoid**：不要把全部局限都归到任务难度上；08 号最后那句速度局限是唯一指向自身的，比例过低。

## D3｜替代形态二：直接把标题写成 "Experiments and discussion"（12 号）

- **When**：解释与观察高度交织，拆开会造成重复。
- **Why**：12 号在标题层面就宣告合并，避免了内容混用被读者当成结构错误。
- **Do**：把 Results 小节标题写成 `Experiments and discussion`，在小节内部允许观察句后紧跟机制解释（用 RS3 的 hedge 句式），但**局限与未来工作仍然放到 Conclusion**。
- **Evidence**：1 篇（12，Tier A2，2023）。该篇的局限确实放在 Conclusion：`Although our method achieves pleasing segmented results, our limitation lies in the extraction of boundary details. The main reason may be that our CNN and Transformer encoders start to recover feature maps from the 4x down-sampled feature maps, which already lose detailed spatial information.`
- **Confidence**：low（单篇依赖），但作为"合并时要在标题上声明"的操作规则是安全的。
- **Avoid**：不要在没有标题声明的情况下把 Discussion 内容混进 Results。

## D4｜默认策略：不写独立 Discussion，把内容三分

- **When**：绝大多数情况（22 篇里 18 篇如此）。
- **Why**：这是他的实际主流做法，而不是遗漏。
- **Do**：把通常属于 Discussion 的内容按功能拆到三处：
  1. **机制解释** → 放进 Results，紧跟对应的观察句，用 `The main reason may be that ...`（见 `results_playbook.md` RS3）。
  2. **局限与未来工作** → 放进 Conclusion 的最后一段（见 `conclusion_playbook.md` C5）。
  3. **与文献的对比性判断** → 放进 Related Work 的定位段（见 `related_work_playbook.md` R5），或放进 Results 的比较小节。
- **Evidence**：18/22 篇采用此分配。其中局限性出现在 Conclusion 的有 05、06、09、10、12、13、16、18、36 共 9 篇；机制解释出现在 Results 的有 01、02、05、06、12、13、16、30、31 共 9 篇。
- **Confidence**：**high（作为默认策略）**。这一条的证据量与其他 Discussion 规则是反过来的——"不写独立 Discussion"才是有 18 篇支撑的规律。
- **Avoid**：不要为了凑章节完整性硬造一个 Discussion；不要把同一条解释同时写进 Results 和 Conclusion。

## D5｜若必须写独立 Discussion，可用的最小骨架

综合 21、08、12 三种形态的可迁移部分，给出一个骨架，但必须标注它是**推断而非观察**：

1. 一句总判断，用让步式开头（`Although our method achieves ..., there is a long way to ...` / `Although our confidence prior achieves excellent results, there are still some common problems to be solved.`）
2. 枚举局限，用 `First / Second / Third` 或 `Firstly / Secondly / Thirdly`，每条给出机制而不只是现象
3. 区分两类局限：任务固有难点 vs 方法自身缺陷，且后者不能缺席
4. 工程性代价（速度、内存、超参依赖）单列一条
5. 收尾给解决方向，用 `Solution to the above mentioned problems is to ...` 或 `We can ... in the future`
6. 全节不复述定量结果，不做意义升华

- **Confidence**：**low，且明确标注为推断骨架**。第 1、2、5 步有原文支撑（08 与 11 的让步开头、08 的枚举、21 的收尾）；第 3、4、6 步是从跨章节习惯反推的，没有独立 Discussion 的直接证据。
- **重要提醒**：11 号那段"Firstly/Secondly/Thirdly 枚举超参依赖、残余雾、夜间场景落后"的文字读起来非常像这个骨架，但**它是清洗者从 Results 尾部与 Conclusion 拆出来重组的，不是作者写的独立 Discussion**，不得引用为证据。P5 审计时必须核对这一点。
