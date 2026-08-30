# Title Playbook（袁非牛）

证据基础：22 篇（Tier A 20 + Tier B 2），2011–2026，IEEE 9 篇 / Elsevier 11 篇 / KSII 2 篇。
标题全文清单见 `../corpus/tierA_list.md`；结构统计见 `../_work/p2_struct.txt`。

---

## T1｜机制在前、任务在后，用 "for" 铰接

- **When**：写任何方法类论文的标题。
- **Why**：他的标题一律先交代"用什么机制"，再交代"解决什么任务"，让读者在读完前半句时就知道技术贡献是什么。
- **Do**：`[机制/方法名词短语] + for + [任务名]`。任务名放在最后，不要把任务提到句首。
- **Language/Structure**：`A Gated Recurrent Network With Dual Classification Assistance **for** Smoke Semantic Segmentation`；`High-order local ternary patterns with locality preserving projection **for** smoke detection and image classification`。
- **Evidence**：20/22 篇用 "for" 作机制→任务的铰接（01、02、03、04、05、06、07、09、10、11、12、13、16、17、18、19、20、30、31、36）。17 号用了两个 "for"（`A double mapping framework for extraction of shape-invariant features ... for video smoke detection`）。
- **Counterexamples**：08 号 `Deep Smoke Segmentation`（三词极简，无机制）；21 号 `Video-based smoke detection with histogram sequence of LBP and LBPV pyramids`（任务在前，用 "with" 铰接）。两个反例都在 2011–2019 的早期。
- **Confidence**：high。跨年代、跨 venue、跨主题（去雾/医学/超分都成立）。
- **Avoid**：不要把任务提前写成 "Smoke Segmentation Using X"；语料里 0 篇用 "Using"。

## T2｜标题写机制的全称，缩写留给摘要

- **When**：论文提出了带缩写名的网络或模块。
- **Why**：缩写在标题里不可读，他一律把缩写的展开式写进标题，再在摘要里首次定义缩写。
- **Do**：标题写全称短语；摘要中用 `... to propose a Xxx Yyy Network (XYN)` 的形式首次定义。
- **Language/Structure**：01 号网络叫 W-Net，标题写 `A Wave-Shaped Deep Neural Network`；02 号叫 CCENet，标题写 `Cubic-cross convolutional attention and count prior embedding`；07 号叫 CGRNet，标题写 `A Gated Recurrent Network With Dual Classification Assistance`；13 号叫 BiFBA-Net，标题写 `A Bi-Directionally Fused Boundary Aware Network`。
- **Evidence**：22 篇标题中出现网络缩写的为 0 篇；而摘要里定义缩写的至少 12 篇。
- **Counterexamples**：无。但注意 04 号 `Smoke-Aware Global-Interactive Non-Local Network` 恰好首字母构成 SAGINN，属于反向设计缩写，不是把缩写写进标题。
- **Confidence**：high。
- **Avoid**：不要在标题里放 CCENet / W-Net 这类内部命名。

## T3｜机制槽位偏好"成对/双路"命名

- **When**：方法由两个互补分支、两个域或两次操作构成。
- **Why**：他的方法设计本身高频采用互补双路，标题直接把这种对偶性写出来当卖点。
- **Do**：用 `Dual-` / `Bi-` / `double` / `A and B complementary` / `X-Space Interaction` 这类显式对偶词。
- **Language/Structure**：`Dual-Encoded Features from Both Spatial and Curvelet Domains`（30）；`Dual-Guided Frequency Prototype Network`（18）；`A Bi-Directionally Fused Boundary Aware Network`（13）；`An effective CNN and Transformer complementary network`（12）；`A double mapping framework`（17）；`Cubic-cross convolutional attention and count prior embedding`（02）；`Frequency-Space Interaction With Hierarchical Aggregation Network`（10）；`Multi-Stage Group Interaction and Cross-Domain Fusion Network`（09）；`Learning multi-scale and multi-order features`（16）。
- **Evidence**：9/22 篇标题带显式对偶或双成分结构，跨 2012–2026、跨四个 venue、跨三种任务。
- **Counterexamples**：单机制标题也存在且不少（03 lightweight、11 confidence prior、36 comprehensive feature aggregation），所以这是偏好而非规则。
- **Confidence**：medium-high。作为倾向可用，不能当必须。
- **Avoid**：不要为了套这个模式硬造"双路"，方法本身没有对偶性就不要写。

## T4｜带评价性形容词的不定冠词开头是次要模式

- **When**：想在标题里就传达方法的定位（有效/轻量/高效/全面）。
- **Why**：他有一批标题用 `A/An + 评价形容词 + ...` 直接给方法定性。
- **Do**：`An effective ...` / `A lightweight ...` / `A Comprehensive ...`。
- **Language/Structure**：`A lightweight network for smoke semantic segmentation`（03）；`An effective multi-scale interactive fusion network ...`（06）；`An effective CNN and Transformer complementary network ...`（12）；`A Comprehensive Feature Aggregation Network for Efficient Image Super-Resolution`（36）。
- **Evidence**：9/22 以 `A/An` 开头，其中 4 篇紧跟评价形容词。`effective` 出现 2 次（06、12，均为 Elsevier PR）。
- **Counterexamples**：13/22 不用冠词开头，直接以机制名词开头（IEEE 系列尤其明显：04、07、09、10、13、18、20 全部无冠词）。
- **Confidence**：medium。**存在明显的 venue 相关性**：无冠词开头集中在 IEEE 期刊，`A/An` 开头集中在 Elsevier。这一条很可能部分是期刊排版惯例，不能当纯个人风格。
- **Avoid**：不要给 IEEE 稿件套 `An effective ...`；不要在同一投稿目标下混用两种开头。

## T5｜任务名用当前最精确的粒度，且粒度升级会被写进正文

- **When**：命名任务。
- **Why**：他对任务粒度非常敏感，标题里的任务名会随他自己推进的问题难度逐级升级，而且他会在 Introduction 里显式论证这个升级。
- **Do**：按 `detection → recognition → segmentation → density estimation` 的粒度谱选最精确的那个词，并在 Introduction 里说明为什么比上一级更难。
- **Language/Structure**：标题任务名演进：`smoke detection`（21/2011、17/2012、19/2016、31/2016、20/2017）→ `smoke recognition`（16/2018、30/2019）→ `smoke segmentation`（08/2019、02/2022、03/2023、09/2026）→ `smoke density estimation`（01/2020）。01 号 Introduction 里明确写 `Smoke density estimation provides more information than smoke segmentation, but it is far more challenging than smoke segmentation`。08 号写 `smoke segmentation is a far more difficult task than smoke recognition`。
- **Evidence**：粒度演进在 22 篇标题上单调可见；正文里的粒度论证在 01、08、20 三篇有直接原文。
- **Counterexamples**：非烟雾主题的四篇（11 去雾、12/13 医学分割、36 超分）不参与这条粒度谱，它们直接用领域标准任务名。
- **Confidence**：high（针对烟雾系列）／不适用（针对其他主题）。
- **Avoid**：不要用比实际贡献更强的任务名（例如只做了 patch 分类却写 segmentation）；这是他明确在正文里区分开的东西。

## T6｜长度与信息密度

- **When**：定稿标题。
- **Why**：他的标题长度集中在中等区间，极短和极长都是个别情况。
- **Do**：目标 9–14 个词，容纳"机制 + 任务"两个槽位即可，不要塞第三个槽位。
- **Language/Structure**：多数标题恰好一个机制短语 + 一个任务短语。
- **Evidence**：最短 3 词（08 `Deep Smoke Segmentation`），最长 20 词（17，塞了机制 + 中间产物 + 分类器 + 任务四个槽位），其余 20 篇集中在 8–16 词。
- **Counterexamples**：17 号（2012）是唯一的超长标题，同时也是他唯一独著的 PR 论文，可能反映早期未受审稿压缩。
- **Confidence**：medium。长度本身是弱信号，主要靠"槽位不超过两个"来控制。
- **Avoid**：不要把数据集名、参数量、性能数字写进标题；语料里 0 篇这样做（03 的 "<1M 参数" 只出现在摘要）。
