# Smoke-Aware Global-Interactive Non-Local Network for Smoke Semantic Segmentation

**Paper_ID:** 04_SAGINN_TIP2024_Smoke_Semantic_Segmentation
**Authors:** Lin Zhang, Jing Wu, Feiniu Yuan (Senior Member, IEEE), and Yuming Fang (Senior Member, IEEE). (Lin Zhang and Jing Wu are co-first authors; corresponding author: Feiniu Yuan.)
**Venue:** IEEE Transactions on Image Processing (2024); manuscript received 9 May 2023; revised 14 November 2023 and 4 January 2024; accepted 7 January 2024; date of publication 5 February 2024.

## Abstract

Compared with other objects, smoke semantic segmentation (SSS) is more difficult and challenging due to some special characteristics of smoke, such as non-rigid, translucency, variable mode and so on. To achieve accurate positioning of smoke in real complex scenes and promote the development of intelligent fire detection, we propose a Smoke-Aware Global-Interactive Non-local Network (SAGINN) for SSS, which harness the power of both convolution and transformer to capture local and global information simultaneously. Non-local is a powerful means for modeling long-range context dependencies, however, friendliness to single-scale low-resolution features limits its potential to produce high-quality representations. Therefore, we propose a Global-Interactive Non-local (GINL) module, leveraging global interaction between multi-scale key information to improve the robustness of feature representations. To solve the interference of smoke-like objects, a Pyramid High-level Semantic Aggregation (PHSA) module is designed, where the learned high-level category semantics from classification aids model by providing additional guidance to correct the wrong information in segmentation representations at the image level and alleviate the inter-class similarity problem. Besides, we further propose a novel loss function, termed Smoke-aware loss (SAL), by assigning different weights to different objects contingent on their importance. We evaluate our SAGINN on extensive synthetic and real data to verify its generalization ability. Experimental results show that SAGINN achieves 83% average mIoU on the three testing datasets (83.33%, 82.72% and 82.94%) of SYN70K with an accuracy improvement of about 0.5%, 0.002 mMse and 0.805 Fβ on SMOKE5K, which can obtain more accurate location and finer boundaries of smoke, achieving satisfactory results on smoke-like objects.

**Index Terms:** Smoke semantic segmentation, global-interactive non-local, pyramid high-level semantic, smoke-aware loss.

## Introduction

### I. Introduction

Fire is one of the most frequent disasters, which seriously threatens life and social public safety, and causes extremely irreversible damage to the ecological environment. Since fires are usually accompanied by smoke first, and smoke is more observable than flame, some scholars proposed smoke-based fire detection as early as 1979 [1]. Though traditional fire detector has high precision, it has strict limitation on space, easily causing alarm delay in many inapplicable scenes. Therefore, fire detection based on computer vision (CV) has become the mainstream. Smoke semantic segmentation (SSS) is a full-image pixel-by-pixel recognition task, which can provide richer information by separating the smoke and its fine boundaries from the image, while the characteristics of smoke, such as semi-transparent, non-rigid, fuzzy boundary, bring greater challenges. Compared with other objects, smoke will have a lot of particularity and uncertainty with the change of time and environment. For example, smoke is prone to produce intra-class heterogeneity (Fig. 1(a)). Many objects and backgrounds with similar shapes and textures to smoke can cause serious inter-class similarity (Fig. 1(b)). Notices that the camera's observation distance and the different stage of fire will make the smoke exhibit characteristics with variable scale (Fig. 1(c)). The boundary of smoke is very vague, which is even hard for human eyes to distinguish (Fig. 1(d)).

> Fig. 1. Some samples of smoke image.

To deal with these challenges, various models were proposed [2], [3], [4], [5], [6], which basically follow the classification-like network structure based on DCNNs. What these methods have in common is that they progressively down-sample the inputs to feature maps with different scales, propose various ways to encode powerful representations by multi-scale feature fusion and variant of attention, then directly feed them to the decoder of the downstream task. Nonetheless, such topologies always lack sufficient cross-scale interactions to obtain high-quality (HQ) and high-resolution (HR) representations with rich semantic information. Long-range global relationships and local spatial information are the key to generate HQ and HR representations, but the contradiction between them leads to the undesirable result. Recently, transformer [7], as an effective way to capture long-range dependencies, has made remarkable achievements in CV. However, pure transformers of CV (ViT) have several problems, e.g., the ability to extract local information is obvious insufficient, larger sequence length than natural language processing causes higher computational complexity, and it relies on pre-training on large datasets.

Many variants of ViT propose various means to enhance the locality, such as transformer-in-transformer [8], shifted window partitioning [9], [10], the spatial shuffle operation [11], [12], local and global layer-by-layer fusion [13]. Although the above operations can reinforce the locality to a certain extent, they increase the complexity of the model. Therefore, a more straightforward and effective way is to combine the transformer and convolution. Non-local network [14] falls into this type of method, which pioneers the use of self-attention in CV and gets a series of developments [15], [16], [17]. These methods, however, are biased towards local interactions and ignores global interactions. To reduce the computational cost, introducing the pooling operation into the transformer is feasible. For Multi-Head Self-Attention (MHSA) [7], a single pooling operation is weak, which only model token-to-region relationship, but disregard token-to-token relationship [18]. Here, multi-size parallel pooling maybe a more powerful strategy.

Additionally, the existing methods usually treat all objects in an image equally and ignore that distinct classes of objects should have different levels of importance in specific task. As required, fire-detection should pay more attention to the fire-related objects such as smoke and flame than those useless for the task, like cloud, sky etc. That is to say, SSS model should segment smoke as the most major object with the highest possible precision and the accuracy of other objects can be treated as secondary, which is not considered in the current approach because of the use of the binary cross-entropy loss (BCE). In this case, the most urgent task is to identify the importance of different objects to distinguish precisely between these confusing categories. One possible approach is to assign different weights to different objects to reduce model's attention on non-smoke objects. Based on this notion, we propose a novel loss function termed "Smoke-Aware Loss" (SAL). As shown in Fig. 2, we notice that the results produced by three models using BCE as loss function are incomplete, missing some parts of smoke. However, training model with our SAL can correct segmentation errors to a certain extent.

> Fig. 2. (a) Input image; (b) DANet+BCE; (c) DANet+SAL; (d) CCNet+BCE; (e) CCNet+SAL; (f) SAGINN+BCE; (g) SAGINN+SAL.

Inspired by the above methods, we propose a model combining the transformer and convolution with a novel loss function specifically optimized for SSS, termed Smoke-Aware Global-Interactive Non-local Network (SAGINN). SAGINN can bridge the gap of local and global information meanwhile shrinking the need for training data, ensure powerful contextual features while decreasing resource consumption by designing a Global-Interactive Non-local (GINL) instead of MHSA, regulate the segmentation representation for further refinement by introducing pyramid high-level semantic information and focus more on the segmentation of smoke meanwhile alleviating the problem of inter-class similarity by SAL. Overall, the key contributions of this paper are as follows:

(1) We propose a model SAGINN, which promotes model to learn semantically-rich and spatially-precise representations by integrating multi-scale DCNN with transformer.

(2) To undergird the learning ability of model for HQ representations, we propose a GINL module, which can encourage global interactions between high-level and low-level features through converging key information K-V pairs. And we encapsulate a Pyramid Pooling Reshape (PPR) module to GINL to dwindle computational cost of attention.

(3) To further incorporate global and local features, a Pyramid High-level Semantic Aggregation (PHSA) module is proposed, which extracts three-scale features rich in semantics from classification to guide the amendment of segmentation features by non-overlap depthwise convolution. To our knowledge, we are the first to explore classification features to directly promote segmentation representations.

(4) We propose a SAL to highlight the status of smoke in the scene, which could urge the model to concentrate on the smoke object and reduce the interference from other irrelevant objects by taking advantage of the important semantic information in data labels.

## RelatedWork

### II. Related Work

#### A. Attention Mechanism in Vision Architectures

It is there for all to see the startling achievement attention mechanism harvested since it was first applied in neural networks for image classification [19]. Reference [20] proposes a SENet to extract channel adaptability, which has continuously been proven essential for visual tasks in [22], [23], [24], [25]. Self-attention mechanism stemming from NLP, as an instantiation of spatial attention, has gone virus in recent transformer-based [7] models for its excellent properties in capturing long-range dependence. As the prelude of self-attention to be used in CV, Non-local [14] can easily plug into lots of models and earn the outperformance. As the further ameliorate of the non-local, DANet [15] achieves a promising segmentation result through combining long-range dependence in spatial with channel adaptability seized by self-attention. CCNet [17] designs a sparse attention to aggregate long-range dependence in both horizonal and vertical directions. Afterwards, the ViT [25] accomplishes better performance on the image classification compared with DCNNs by introducing standard transformer. To extend the ViT from the classification to semantic segmentation, SETR [26] grafts three different kinds of decoders onto the ViT encoder. Segmenter [27] proposes a Mask transformer, introducing learnable classification label into decoder to generate class mask. However, transformer-based methods bring the quadratic complexity for HR images, causing slower reasoning speed, which are not conducive to actual application. Therefore, Segformer [28] and Twins-SVT [13] avoid excessive computing costs via embracing efficient self-attention and spatially separable self-attention. Moreover, to compensate the lack of locality, Swin [9] and Cswin [10] design shifted window partitioning while Twins [13] adopts hierarchical network, but these means complicate the network, erode the global receptive field and ignore channel adaptability.

#### B. Hybrid Framework of DCNN and Self-Attention

A model with a lightweight attention implementation, which concerts both efficiency and performance while has the local receptive field of DCNN and the global context dependence of self-attention, is demanded for much more vision tasks. References [29], [30], and [31] have proven that the combination of transformer and convolution as a hybrid architecture avails the network absorbing the strengths of both. Reference [32] enhances locality while modeling long-range dependence by integrating DCNN and transformer, accompanied with a LeFF layer to promote the correlation of adjacent tokens. Mobile-ViT [33] and Mobile-Former [34] interact the locality of MobileNet [36], [37], [38] with the long-range contextual information of ViT. CoaT [38] designs a co-scale and conv-attentional mechanism, allowing the representations to learn between different scales and completes relative position embedding in a convolution-like ways. CPVT [39], so does the Twins-PCPVT [13], leverages convolution to form implicit positional encoding, alleviating the awkward impact of changing image resolution resulting in accuracy faltering. To solve the deficiency of ViT in addressing locality, [40] adopts spatial prior to model local spatial contexts by convolutions and then the context interaction with a ViT is made in spatial feature injector module. Moreover, CMT [29] dwindles the computing cost of MHSA by convolutions, in which the local perception unit and the inverted residual feed-forward network are embedded to enhance locality. SegNeXt [41] displaces all self-attention modules with MSCA, balancing the efficient and performance. References [31] and [42] show that the MHSAs and convolutions are equipped with complementary capacity to capture high-level semantics and low-level details.

#### C. Smoke Semantic Segmentation

Traditional methods mainly design a variety of distinguishable features of smoke, such as color [44], [45], [46], [47], shape [47], motion [48], [49]. Further, [50] and [51] introduce roughness histogram on this basis. References [48] and [52] use the Gaussian Model to shrink background modeling time and consider salience map. Kalman filter is adopted to describe the boundary of smoke in [53]. Tian et al. [54] uses dictionary technique to model foreground smoke and background non-smoke on the foundation of the atmospheric scattering theory. However, the biggest limitation of traditional methods is over reliant on artificially picked characteristics of smoke.

With the rapid development of deep learning, SSS is more self-completed by deep neural networks. Earlier methods [55], [56] usually adopt simple fully convolutional neural network, resulting in a lack of multi-scale features. Therefore, [2] and [3] propose two types of encoder-decoder network to inject the spatial details of low-level features into high-level representations to complement each other. DeepSmoke [57] employs the EfficientNet and Deeplab v3+ for outdoor smoke detection and segmentation. FoSp [58] employs a bidirectional cascade to fuse features of three resolutions while designing a domain fusion module to integrate the distinctive features. And a Multi-scale Residual Module [59] is designed to fuse multiscale features. Nevertheless, the attention mechanism provides another effective way to improve the performance. Like, [60] introduces a multi-scale residual group attention in U-Net. CCENet [4] designs a cubic-cross convolutional attention, extracting the long-range dependencies in three dimensions. Reference [5] designs a 3D attention to fuse attention maps along three axes, accompanied with a multi-scale channel attention. CGRNet [6] designs an improved GRU to capture the spatial correlation of 2D features to learn long-range context dependence. Li et al. [61] proposes a lightweight ECA channel attention to reduce the complexity. Specially, Yan et al. [62] introduces Bayesian generative model while leveraging the proposed transmission-guided local coherence loss to predict smoke mask. And Ma et al. [63] improves TSDPC to find the optimal double truncation distance and determine clustering centers.

The above methods effectively verify the feasibility of intelligent fire detection using SSS. However, we find that compared with other objects, the research enthusiasm of SSS is obviously less, which is mainly pinned on the lack of real smoke datasets, and some characteristics of smoke also surge the difficulty of segmentation. Furthermore, all the method in status quo can scarcely keep a promising performance while shrinking the scale of model. Therefore, our method takes both efficiency and performance into account, providing an alternative for smoke detection in realistic complex environment.

## Methods

### III. The Proposed Method

SSS aims at understanding all smoke objects in an image, which assign a semantic label belonging to smoke or background to each pixel of image. There is a strong internal association between semantic segmentation and classification, which is an important reason for many semantic segmentation methods to take classification model as backbone. However, existing methods mostly deal with them separately, in this paper, we further explore the potential relationship between semantic segmentation and classification task. Particularly, object classification can provide complementary cues to assist object semantic segmentation, to bridge the gap between two tasks, we propose SAGINN, which fuses two models together by sharing the same backbone. In addition to the clues provided by classification branch, we also propose a series of modules to promote the improvement of prediction accuracy. For this purpose, we first introduce the overall framework of SAGINN, then give a detailed description of each key elements, containing GINL, PHSA and SAL function. Finally, we present specific prediction details.

> Fig. 3. The overall framework of SAGINN.

#### A. Architecture Overview

As illustrated in Fig. 3, SAGINN is a typical two-branch structure, which can accomplish semantic segmentation and classification simultaneously. Given a natural color image X as input, ResNeXt 101 [64] is used as the backbone to extract multi-scale feature maps, mainly because it has achieved an excellent 82.9% and 96.3% accuracy on top1 and top5, respectively, with relatively few parameters (83.5M). Compared to most DCNNs, it has superior feature representation ability imbued with relative smaller model size. For the segmentation, the most important purpose of the encoding stage is to embed rich scene semantic information into the feature maps, which can be achieved by adopting various methods to fuse multiscale features. Therefore, we propose an improved module GINL based on non-local, which is an important basis for building segmentation branch to generate finer mask. And for the classification, 8 × 8 feature maps successively get through a series of operations such as convolution, pooling and fully-connected to generate the highest-level feature representations. In this way, the intrinsic relationship between segmentation and classification in feature space is facilitated more tightly due to the joint supervision of the shared backbone by both tasks.

To generate more powerful representation, we stack several GINLs to construct segmentation branch. Due to its high cost, excessively stacking of GINL will literally affect the efficiency of method. To balance performance and efficiency, the 8 × 8 features passing through non-local are fed into three parallel GINLs simultaneously to iteratively aggregate the key information (K-V pairs) from multiple feature pairs with different scales. The outputs of three GINLs are fused in a bottom-to-up manner by a feature fusion module. To further establish the bond between two tasks, PHSA is added to explicitly improve segmentation representations, which can dynamically aggregate the high-level semantics learned from the classification branch into the features derived from the fusion of GINLs. By definitely supervising the classification, PHSA can collects rich categories semantic information, which can assist the model to make better decision by rectifying segmentation errors caused by smoke-like objects. Finally, the feature representations produced by DW-Channel Attention Block (DCA) and Decoder module in series will be used for final prediction of SSS. Specially, we introduce dropout in DCA as regularization to mitigate the overfitting. Our model has stronger generalization ability by introducing pyramid high-level information guidance from classification into segmentation. All the elements of SAGINN are tightly coupled, so the model allows end-to-end multi-task joint optimization with a simple loss function.

#### B. Global-Interactive Non-Local

Although the context fusion helps to capture objects with different scales, it cannot consider and leverage the relationship between objects in a global view. It has been proven that transformer excels in building object global relationships, namely long-range dependencies. As the earliest transformer variant used in CV, non-local also shows great potential for a variety of tasks. However, the original non-local is better suited for handling single-scale and low-resolution representations, which is disadvantageous for semantic segmentation. Therefore, it is urgent to extend the topology design of original non-local to generate HQ HR representation. Low-level features usually have high resolution but lack semantic, whereas high-level features have low resolution but rich semantics. To give full play to the advantages of these cross-scale features, we delve into global interaction learning of the multi-scale representation in non-local to integrate key information across multiple level, to unleash the potential of transformer to learn both long-range global relationships and local spatial information.

GINL is designed for global interaction of key information by aggregating 8×8 high-level semantic features with different scale features. The 8 × 8 feature maps are of low resolution, but often include abundant scene semantic information, which can provide stable semantic supplement for low-level features. Therefore, in the interaction process, GINL extracts the key information (K-V pairs) of the 8 × 8 features as guidance of global interaction. Taking the performance and efficiency into account, we design GINL with several key optimizations, whose detailed structure is shown in Fig. 4. Firstly, we map high-level features f1 to K′1, V′1 and low-level features f2 to Q′2, K′2, V′2, following the self-attention in non-local [14]. In order to pursue the improvement of efficiency in computing the attention map, especially the high-resolution feature, inspired by P2T [18], we adopt PPR module to reduce spatial dimension of K and V produced from the low-level features. As shown in Fig. 4, GINL aggregates the key information from high-level feature into low-level feature by concatenating corresponding K-V pairs to produce K′ and V′. The details of global interaction self-attention GISA(f1, f2) can be described as:

K′ = Concat(Reshape(W_K1 f1), PPR(W_K2 f2))  (1)

V′ = Concat(Reshape(W_V1 f1), PPR(W_V2 f2))  (2)

Q′2 = Reshape(W_Q2 f2)  (3)

GISA(f1, f2) = Add(f2, Reshape(softmax(Q′2 K′ᵀ) V′))  (4)

where W_Ki, W_Vi (i = 1, 2) and W_Q2 are the learnable weights of 1×1 convolutional layer, Concat(·) is concatenation along with channel, Reshape(·) transforms the input size into the corresponding size, Add(·) performs element-wise sum.

> Fig. 4. The detailed structure of GINL.

> Fig. 5. Pyramid pooling reshape (PPR).

The K and V from higher resolution features passing through PPR shown in Fig. 5 highly summarizes the contextual information of the input, which can therefore be regarded as a powerful substitute for the input in computing the attention map. The PPR can be depicted as:

f1 = Reshape(AvgPool(f, 2))  (5)

f2 = Reshape(AvgPool(f, 4))  (6)

f3 = Reshape(AvgPool(f, 8))  (7)

f4 = Reshape(GlobalAvgPool(f))  (8)

f′ = Concat(f1, f2, f3, f4)  (9)

where Reshape(·) can convert the input from 3D to 2D, AvgPool(·) and GlobalAvgPool(·) represent the average pooling with different pool kernel and global average pooling respectively, Concat(·) is the concatenation operation.

By introducing 8×8 high-level semantics, GINL effectively completes the bottom-to-up feedforward process through the global interaction between high-level information and that of other scales. High-level information enhances GINL's ability to integrate key and determined information in features, and can simultaneously learn long-range global relationships and local spatial information in a coarse-to-fine manner, which makes the decoded low-level features also can provide credibly sufficient high-resolution semantic information.

#### C. Pyramid High-Level Semantic Aggregation

Accurate recognition of task-related regions in images is very important for semantic segmentation. However, there are many obstacles to accurately identify the object regions in SSS. Among them, the interference of smoke-like objects, such as clouds, fog, etc., is a common challenge. It will exert a quite negative impact on accurately locating smoke area and seriously harm the segmentation performance to lead to high errors in fire detection, which is usually due to the lack of sufficient global context priors. An effective way is to adopt the precise class semantic information in high-level features to rectify the misclassified pixels in segmentation features. To sufficiently harvest the merits of classification task, we propose a PHSA to fine-tune the segmentation representation to attempt to reduce the adverse effects of interfering elements.

As shown in Fig. 6, Pyramid High-level Semantics (PHS) is from the middle layer of classification branch, from which we select three groups of features in 8 × 8, 4 × 4 and 2 × 2 respectively. PHS learned from a series of feature generators containing a conv block and an average pooling with 2 × 2 kernel, where conv block is a combination of 3 × 3 convolution, ReLu and BN. To obtain the highest-level global semantic to complete high precision classification, the last feature generator is structured slightly different in that it uses the convolution kernel with the same size as the feature maps to perform depthwise convolution instead of average pooling, transforming the feature maps from 2×2×c to 1×1×c by channel-by-channel addition.

> Fig. 6. The framework of PHSA.

PHS have the same number of channels as the outputs of the feature fusion module in Fig. 3. To make full use of category information to achieve feature enhancement, PHSA first carries out softmax nonlinear mapping on PHS, which is to highlight the importance of different positions in the feature, and then adopts non-overlap depthwise convolution and pixel-wise addition to obtain more robust and distinguishable feature representations, which can be formulated as:

fre = DWC(fs, softmax(F8×8)) + DWC(fs, softmax(F4×4)) + DWC(fs, softmax(F2×2))  (10)

where F8×8, F4×4 and F2×2 are PHS, fs represents the outputs of feature fusion module in segmentation branch, fre represents the refined features obtained after PHSA, DWC(·) is the non-overlap depthwise convolution shown in Fig. 7.

> Fig. 7. Details of non-overlap depthwise convolution.

The fre is a more powerful representation to distinguish among various categories than fs by fusing high-level semantics under three pyramid scales. PHS can provide multiple effective receptive fields, which can collect semantic information of sub-regions with variable sizes to form feature representation of different locations. With the introduction of semantic class cues by PHSA, our model can further explore the inherent semantic relations of the fused features and learn the spatial dependence between different features, which can encourage model to pay more attention to the smoke regions.

#### D. Smoke-Aware Loss

Apparently, high segmentation accuracy in fire detection will make the model more focus on smoke objects thus greatly reduce the probability of fire alarm delay. SSS is a binary-classification problem, which divides the image into foreground smoke and background non-smoke. However, most of the existing SSS algorithm cannot provide reliable segmentation mask, where the most common mis-segmentation often occurs on smoke-like objects, owing to similar appearance and equivalent status to the smoke. We conjecture that one of the main reasons is the use of BCE in the training phase, which treats the errors generated by all pixels equally and assigns the same weight to their losses. Nevertheless, compared to other objects, the smoke should receive the highest level of attention in SSS and be allocated with distinct weight. That is, smoke ought to be the most critical hierarchy segmentation object when we establish the SSS model.

In order to distinguish the importance of different objects and excavate the key information of smoke, we propose a novel loss function SAL that specifically places emphasis on the smoke. In supervised learning, the information carried by labels is the most directional. According to our prior knowledge, in SSS, those pixels with the largest value in the labels are all belonging to sematic class of smoke, which can credibly show the importance of objects. Therefore, when designing SAL, we take labels as guidance to reflect what semantic class model ought to pay more attention. Based on this idea, we define f as an important factor which can be computed by:

f = ‖(P′ − Y) ⊙ (Y + E)‖_F  (11)

P′ = P ⊙ Y  (12)

where P and Y are the predicted mask and the corresponding mask label respectively, E is an all-one matrix, ⊙ is the element-wise product.

In our task, foreground smoke loss is multiplied by important factor f due to its highest importance. On the contrary, background non-smoke loss has the lowest important level without any weighting. Therefore, the SAL is the sum of foreground and background losses, which is designed to be:

Lossseg = f · Is + Ib  (13)

Ic = −Σ_c y_c log(p_c), c ∈ {s, b}  (14)

Instead of setting a fixed weight for the foreground smoke, we dynamically adjust the weight based on each prediction mask and corresponding label, which can reflect the accuracy of results more directly. By analyzing (11), we find that SAL encourages the model to pay more attention to the foreground smoke. When the prediction mask of smoke is gradually close to the label, the supervision degree of foreground regions will decrease accordingly, which can better prevent the model from falling into the suboptimal solution and is obviously superior to the fixed weight manually handpicked.

#### E. Prediction Heads

Two set of prediction results are generated by different heads respectively. The segment head outputs the smoke mask, which is reconstructed to predict by the corresponding decoder and supervised by SAL. The class head uses classification label to restrict the back-propagation of BCE. Therefore, the whole model is optimized by a multi-task jointly training loss function, which can be described as:

L = Lossseg + α Losscla + β ‖W‖²₂  (15)

where Lossseg and Losscla represent SAL and BCE, α is a constant for controlling the importance of each loss, β is a weight decay coefficient. Through experiments, α is set as 0.25 in our model.

## Results

### IV. Experimental Results

#### A. Datasets and Implementation Details

Some special properties of smoke, such as changeable shape, blurred boundary, etc., make it very difficult to manually label real smoke images at pixel-level, therefore, we use the synthetic smoke dataset SYN70K proposed in [2] as the training dataset, which contains 70632 fully annotated 256 × 256 RGB smoke images. With different color, shape, texture, etc., all augmenting pure smoke images generated by computer graphics and volume rendering covers a wide variate of smoke patterns. As we combine them with various backgrounds, synthetic images are rich in diversity, which is very friendly to model training. To verify the generalization of SAGINN, synthetic smoke images, real smoke images and videos are embraced as testing datasets. The synthetic images, also from SYN70K, are divided into three datasets named DS01, DS02 and DS03, each of which contains 1000 256×256 RGB smoke images, the real smoke images and videos are from several publicly available datasets, including dataset-1 [70], dataset-2 [71], SMOKE5K [62] and two smoke videos [72]. Some samples of datasets are exhibited in Fig. 8.

> Fig. 8. Samples of (a) Synthetic image, (b) Real image, and (c) Real video.

For a start we implement the SAGINN using the PyTorch [65] on a single NVIDIA GeForce RTX4090 with 24GB memory. For fair comparison, we handpick a set of hyper-parameters to train SAGINN and then use the same to all ablation experiments. For the difficulty of generating high-resolution smoke images, the input size of image is 256×256. Specially, we adopt the ResNeXt101 pre-trained on ImageNet 1k [66] as our backbone and the Stochastic Gradient Descent (SGD) as optimizer while the momentum and weight decay coefficients β are set as 0.9 and 1e-5, respectively. Inspired by [67], we employ the warm-up and cosine annealing learning rate policy:

Warm-up: LR = (Epnow / Epwarm) × LRmax + LRmin  (16)

Cosine annealing: LR = LRmax × (1 + cos((Epnow − Epwarm) / (Epmax − Epwarm))) / 2  (17)

where Epnow is the current training epoch, Epwarm is the total epochs with warm-up we set to 10 and Epmax represents the total training epochs. The model is trained for 50 epochs with batch size of 8. We set LRmin and LRmax to 1e-5 and 0.01. This training strategy can sufficiently prevent the interference bring up by noisy data in the early stage of training through a tiny learning rate, whose dwindling learning rate based on cosine annealing also efficiently avoid fluctuations of performance in the terminal training phase. SAGINN takes about 50mins to train for each epoch, and 8s to process each testing dataset of SYN70K, including the time for image loading and inference.

#### B. Evaluation Metrics

We evaluate our method from multiple perspectives using a variety of metrics. IoU and Dice are commonly used evaluation indicators in semantic segmentation, which can measure the overlap between two samples. For convenient comparison, the mean IoU (mIoU) and Dice (mDice) of all images in DS01, DS02 and DS03 of SYN70K are taken as the final comparison result, the higher mIoU means the better performance, and the same goes for mDice. In addition, we select the mean Mse (mMse), reflecting the predictive accuracy of each pixel, and the mean F-measure (Fβ), obtained according to the prediction and recall values, as evaluation metrics on SMOKE5K, a lower mMse and a higher Fβ indicates a superior algorithm.

#### C. Ablation Studies

In this subsection, we further conduct comprehensive studies on each proposed component according to a series of ablation experiments, which are proceeded from three aspects: model structure, loss function, and training strategy.

Firstly, as shown in Table I, we compare the effect of different backbone. With similar number of parameters, our model with ResNeXt101 achieves the better results, improve mIoU by about 2% over the model with ResNet101. Such results demonstrate the more powerful feature representation ability of ResNeXt101.

By removing or replacing different modules in our model, we conduct the following ablation studies in terms of model structure. One major contribution of SAGINN is to propose GINL to effectively learn HQ representations. Table II and Table III display ablation studies on GINL variants by (1) changing the number of stacked GINL through replacing them with non-local. Here, we gradually increase GINL from scratch, from single scale to multiple scales. The 0 in Table II means that all three GINLs in Fig. 3 are replaced by nonlocal, the 1 (64 × 64) means that only the GINL of 64 × 64 feature is retained and the others are replaced by nonlocal, and so on, (2) removing PPR from GINL.

> Table II. Ablation study of GINL.

> Table III. Ablation study of PPR.

From the results, we observe that as the number of GINLs increases, the prediction accuracy is obviously improved, especially 32 × 32 and 16 × 16, with each improvement reaching more than 1%. This indicates that GINL can jointly extract both global and local representations by aggregating multi-level attention and generate more HQ features for enhancing the robustness of model. Incorporating GINL into segmentation branch could largely promote the global interactions between features, further improving the performance. What's more, the introduction of PPR produces the increase of about 1.6% in mIoU, accompanies with a reduction in computational complexity of attention map without additional parameters.

The PHSA is another main contribution, which is designed to establish the intrinsic relationship between segmentation and classification. The PHSA contains three different scales of high-level semantic information: 8×8, 4×4 and 2×2. We study the effect of PHSA from a variety of perspectives, including semantic information of different scales, feature fusion modes and nonlinear activation, the results are shown in Table IV–VI.

> Table IV. Results of different high-level semantics.

> Table V. Results of different fusion modes.

> Table VI. Ablation study of softmax.

When we completely remove PHSA from segmentation branch, corresponding to the None in Table IV, the performance decreases by average 3% mIoU, which clearly demonstrates the importance role of PHSA. Moreover, we observe that the performance is further improved by gradually adding high-level semantics at different scales to PHSA, in which 4 × 4 semantic information brings the most obvious precision enhancement, generally more than 2.5%. The results of different feature fusion modes in PHSA are given in Table V. Adopting concatenation instead of addition results in a performance decline of about 2%, indicating that the addition is more skilled in aggregating multi-level attention, which makes the model perform better in segmenting objects with large scale variations. The results on whether the semantics is nonlinear activated by softmax are shown in Table VI. The PHSA including softmax obtains better accuracy, achieving an improvement of about 0.6%, which may because softmax can more effectively highlight the importance of different locations of semantic features, providing more specific betterment to segmentation features. Such results highlight the merit of PHSA, whose semantic features from classification can effectively aggregate higher-level semantics to refine the segmentation features. This further verifies that, benefiting from the good generalization of PHSA, classification information is helpful for improving semantic learning of segmentation features. By using PHSA to explicitly model the relationship between segmentation and classification, we can make better use of classification information to improve segmentation accuracy.

To fully understand PHSA, we visualize the learned spatial attention maps by method Grad-CAM [68], showing which parts of the image receives more attention from model. In Fig. 9, the 2nd and 3rd row respectively show that the learned attention maps before and after the signal enters PHSA. By comparison, it can be found that the attention map of PHSA output has significantly increased the focus area of smoke. And Fig. 10 shows the attention maps formed by the output of PHSA of all the variants in Table IV. The observations reveal that in tandem with multi-scale semantics, the model gradually realizes the modification of segmentation expression, enhancing the attention to the smoke region, while decreasing that of the background area. The results indicate that PHSA can better focus on semantically meaningful foreground smoke regions, learn a more explicit structure information to help fine-tune the feature quality and further demonstrate that global information introduced by PHSA can provide more correct semantic guidance to help model better understand complex context, meanwhile, PHSA is powerful on learning discriminative features to obtain more accuracy results.

> Fig. 9. Visualization of spatial attention maps. (a) Image, (b) input of PHSA in SAGINN, (c) output of PHSA in SAGINN. Best viewed in color.

> Fig. 10. Spatial attention maps of the output of PHSA. (a) Image, (b) None, (c) 8 × 8, (d) 4 × 4 and 8 × 8, (e) 2 × 2, 4 × 4 and 8 × 8 (SAGINN). Best viewed in color.

In the following we show how the SAL further improve the performance. In Table VII, we display results given by two nonlocal-based methods and our model with different loss, BCE and SAL. And in Fig. 2, we show the corresponding smoke segmentation masks. We find that by embedding SAL, mIoU achieves varying degrees of improvement, especially our model, increasing about 2%, and the visualization is highly consistent with this. While SAL is induced, the model strengthens smoke-related attention and optimizes the missing parts of smoke when using BCE. The above results fully demonstrate that the model equipped with SAL can provide more confident prediction from multiple perspectives, which can be observed by the raising mIoU and more compact smoke segmentation area.

> Table VII. Comparisons of three methods with different loss.

Table VIII illustrates the results of different loss function. Single-loss-A and single-loss-B only supervise the segmentation with SAL, but the difference lies in that the former completely removes the classification branch in the model, while the latter just cancels the supervision of classification without making any changes on the architecture. We observe that multi-task joint training can achieve better performance, which is higher than single-loss by about 3%. Another finding is that with the same structure, the performance of multi-loss is significantly better than that of single-loss, which contributes to 1.2∼1.5% improvement. This verifies the common belief that effective classification supervision can help PHSA learn more excellent high-level semantics to assist the model to make better decisions.

Furthermore, we discuss the choice of hyper-parameter α in training process. Since segmentation is the main task, which should receive more attention, it is more appropriate to set α between 0 and 1. The mIoU under different α are exhibited in Table IX, showing that α achieves the best performance at 0.25, which also indicates that compared to segmentation, giving relatively little focus on classification is more conducive to achieving the predicted masks with higher confidence.

> Table IX. Ablation study of different α.

In addition, we analyze the influence of different training strategies. We train SAGINN at three different kinds of learning rate (lr), and the results are displayed in Table X. Fixed lr means the lr is set to 0.01 in the training process, and decaying lr initiates the lr as 0.01 with decaying by 0.9 every 10 epochs. By contrast, adopting warm-up and cosine annealing lr achieves the best performance, getting about 1∼2% mIoU promotion over others. Meanwhile, fixed lr performs the worst, which implies that a small lr is a better choice in later training stage, while maintaining a high lr will easily lead to the model missing the optimal solutions and falling into sub-optimal solutions.

> Table X. Results of different training strategies.

#### D. Comparison With SOTA

To validate the performance of our model, we present quantitative comparison with the SOTA methods on SYN70K and SMOKE5K, which could be roughly grouped into the following categories: 1) the method based on DCNN, including PSPNet [69], DSS [2], W-Net [3], CCENet [4], CMNet [5], and CGRNet [6] where the last five models are proposed for smoke, 2) the method of introducing self-attention to DCNN, containing DANet [16] and CCNet [18], 3) Vision transformer models, which include Segmenter [28], SegFormer [29], Twins [13], Swin [9] and FoSp [59], 4) others, Trans-BVM [62]. As listed in Table XI and Table XII, the results demonstrate that our method consistently deliver outstanding performance on SSS, which achieves around 83% mIoU and 90.7% mDice on SYN70K, 0.002 mMse and 0.805 Fβ on SMOKE5K, superior to all comparison methods with a large margin.

> Table XI. Smoke segmentation performance on SYN70K.

> Table XII. Smoke segmentation performance on SMOKE5K.

The overall results reveal the following findings. First, the effective acquisition of long-range contextual dependence is very beneficial to improving performance. For example, PPM-based PSPNet, GRU-based CGRNet, nonlocal-based DANet and CCNet have gained significant performance increase on mIoU. Second, ViT series models don't display absolute advantage in SSS. According to our analysis, the main reasons are: (1) due to the large number of parameters, ViT series models are completely less dominant than DCNN-based methods on small training dataset (our training dataset only has 70632 images), (2) DCNN is more inclined to learn features such as texture and color, which happens to be more consistent with the characteristics of smoke. Therefore, as the results shown, our methods can make full use of the strengths of both DCNN and transformer, which significantly improve the performance on SSS. In addition, we report the relevant results about efficiency in Table XII, which show that our model achieves relatively better speed-accuracy trade-offs: in case not equipped with the lowest parameters and FLOPs, SAGINN achieves competitive FPS and a-list accuracy, especially compared to ViT series models, indicating that the strategy we adopted is more conducive to improving the learning ability of model without greatly increasing the computing complexity. Interestingly, by analyzing the results, we find that ViT series models generally have lower FLOPs, but FPS is not ideal, which does not occur in the networks with DCNN as the backbone, such as DANet, CCNet and our method. We suspect the main reason is that the operations in transformer, albeit with lower computing cost, bring more time-consuming feature transforming tactics compared to convolution in inference.

Figure 11 provides some typical qualitative results of synthetic smoke images, which can support quantitative findings by visually assessing the predictions of compared methods. To highlight the difference between segmentation masks, we mark the samples with different lines, in which the solid blue line reflects the accuracy of edge prediction, and the dotted red line displays the segmentation ability on the difficult smoke area. We have the following observations. Firstly, most method can achieve better results on smoke occupying large area in the images, which mainly because most methods have a bias to capture abstract information about salient objects. Secondly, our model still consistently outperforms other methods for different smoke patterns and a variety of complex scenes. For example, for the second and third samples, our method shows absolute superiority in edge prediction, which is not only smoother, but also closer to corresponding GT. Thirdly, as for challenging smoke, most methods have more obvious incorrect segmentation except for our model, like the first, fourth and fifth samples, many methods either misclassify similar backgrounds as smoke or miss areas of thin smoke, which accredit to both the strong generalization ability of the model, and the priority of SAL-induced parameters modification. Figure 12 and 13 depict segmentation results of real images and videos, which are basically consistent with the synthetic images, and SAGINN further shows evident advantage. In addition to getting more accurate positioning and more detailed boundaries, SAGINN achieves more impressive results on challenging objects, such as the last example in Fig. 12 and the white smoke video in Fig. 13.

> Fig. 11. Results on synthetic images. (a) Test images, (b) GT. Segmentation results of (c) Deeplab v1, (d) PSPNet, (e) DSS, (f) CMNet, (g) CGRNet, (h) DANet, (i) CCNet, (j) Segmenter, (k) Segformer, (l) Twins, (m) Swin, (n) our SAGINN. Best viewed in color.

> Fig. 12. Results on real images. (a) Test images. Segmentation results of (b) Deeplab v1, (c) PSPNet, (d) DSS, (e) CMNet, (f) CGRNet, (g) DANet, (h) CCNet, (i) Segmenter, (j) Segformer, (k) Twins, (l) Swin, (m) our SAGINN.

> Fig. 13. Results on real videos: white smoke and black smoke. (a) Test frames. Segmentation results of (b) Deeplab v1, (c) PSPNet, (d) DSS, (e) CMNet, (f) CGRNet, (g) DANet, (h) CCNet, (i) Segmenter, (j) Segformer, (k) Twins, (l) Swin, (m) our SAGINN. Best viewed in color.

#### E. Inter-Class Similarity Analysis

In this section, we further test the ability of SAGINN to solve inter-class similarity. Segmentation results of some samples with typical inter-class similarity, including smoke and non-smoke images, are presented in Fig. 14. Based on the observation, we can find: firstly, for smoke image, that is, the first four samples, while accurately segmenting the smoke, our method avoids the interference of smoke-like objects to the greatest extent, and basically does not identify them as smoke. However, other algorithms have more or less false segmentation on these samples, especially the first and fourth samples, where the many identify the helicopter's spray in the first sample as white smoke and fail to accurately locate the smoke due to the inference of large clouds in the background of the fourth sample. Secondly, for non-smoke image, our results achieve zero error. It is evident from the results that our method has better scalability to confused categories. We think the main reasons are twofold. On one hand, the semantic information generated by supervised classification contains global abstract information of the image which can effectively promote feature self-adjustment, moreover, the probability of containing smoke object in non-smoke images should be close to 0, which can further correct misclassification in segmentation features. On the other hand, SAL assigns different weights to the foreground and background by adopting explicit position information of smoke contained in GT, which can further reduce the interference of smoke-like objects by weakening the model's focus on the background.

> Fig. 14. Results on real images. (a) Test images. Segmentation results of (b) Deeplab v1, (c) PSPNet, (d) DSS, (e) CMNet, (f) CGRNet, (g) DANet, (h) CCNet, (i) Segmenter, (j) Segformer, (k) Twins, (l) Swin, (m) our SAGINN.

## Conclusion

### V. Conclusion

In this paper, we propose a method, termed SAGINN, to deal with challenging SSS in complex scenes. To take into account both local and global information, we integrate convolution structures and self-attention mechanisms, and further design a GINL to encourage global interaction between multi-scale key information. To improve the robustness of network representation and alleviate inter-class similarity, based on the close internal relationship between segmentation and classification, we propose a PHSA to use higher-level semantic category information to guide the modification of segmentation representation. In addition, semantic segmentation in smoke detection is quite different from traditional semantic segmentation, which should treat smoke as the most important object. Based on this knowledge, we propose a SAL that forces the model to pay more attention to foreground smoke by assigning different weights to foreground and background losses. A large number of quantitative and qualitative experiments prove that our method can achieve more accurate location and more precise boundary segmentation. Meanwhile, SAGINN also exhibits great advantage in dealing with inter-class similarity, and there is basically no false segmentation in the smoke-like object.

## Acknowledgments

This work was supported in part by the National Natural Science Foundation of China under Grant 62262027, in part by the Jiangxi Provincial Natural Science Foundation under Grant 20212BAB202012, and in part by the Key Science and Technology Project of Jiangxi Provincial Department of Education under Grant GJJ2201311. The associate editor coordinating the review of this manuscript and approving it for publication was Dr. Nikolaos Mitianoudis.

## References

[1] D. A. Robinson, "Smoke detection: Critical element of a university residential fire safety program," J. Amer. College Health Assoc., vol. 27, no. 5, pp. 265–266, 1979.
[2] F. Yuan, L. Zhang, X. Xia, B. Wan, Q. Huang, and X. Li, "Deep smoke segmentation," Neurocomputing, vol. 357, pp. 248–260, Sep. 2019.
[3] F. Yuan, L. Zhang, X. Xia, Q. Huang, and X. Li, "A wave-shaped deep neural network for smoke density estimation," IEEE Trans. Image Process., vol. 29, pp. 2301–2313, 2020.
[4] F. Yuan, Z. Dong, L. Zhang, X. Xia, and J. Shi, "Cubic-cross convolutional attention and count prior embedding for smoke segmentation," Pattern Recognit., vol. 131, Nov. 2022, Art. no. 108902.
[5] F. Yuan, Y. Shi, L. Zhang, and Y. Fang, "A cross-scale mixed attention network for smoke segmentation," Digit. Signal Process., vol. 134, Apr. 2023, Art. no. 103924.
[6] F. Yuan, L. Zhang, X. Xia, Q. Huang, and X. Li, "A gated recurrent network with dual classification assistance for smoke semantic segmentation," IEEE Trans. Image Process., vol. 30, pp. 4409–4422, 2021.
[7] A. Vaswani, N. Shazeer, and N. Parmar, "Attention is all you need," in Proc. Adv. Neural Inf. Process. Syst., Long Beach, CA, USA, 2017, pp. 6000–6010.
[8] K. Han, A. Xiao, E. Wu, J. Guo, C. Xu, and Y. Wang, "Transformer in transformer," in Proc. Adv. Neural Inf. Process. Syst., 2021, pp. 15908–15919.
[9] Z. Liu et al., "Swin transformer: Hierarchical vision transformer using shifted windows," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 9992–10002.
[10] X. Dong et al., "CSWin transformer: A general vision transformer backbone with cross-shaped windows," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 12114–12124.
[11] Z. Huang, Y. Ben, and G. Luo, "Shuffle transformer: Rethinking spatial shuffle for vision transformer," 2021, arXiv:2106.03650.
[12] J. Fang, L. Xie, X. Wang, X. Zhang, W. Liu, and Q. Tian, "MSG-transformer: Exchanging local spatial information by manipulating messenger tokens," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), New Orleans, LA, USA, Jun. 2022, pp. 12053–12062.
[13] X. Chu, Z. Tian, and Y. Wang, "Twins: Revisiting the design of spatial attention in vision transformers," in Proc. Adv. Neural Inf. Process. Syst., vol. 34, 2021, pp. 9355–9366.
[14] X. Wang, R. Girshick, A. Gupta, and K. He, "Non-local neural networks," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Salt Lake City, UT, USA, Jun. 2018, pp. 7794–7803.
[15] J. Fu et al., "Dual attention network for scene segmentation," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Long Beach, CA, USA, Jun. 2019, pp. 3141–3149.
[16] L. Ye, M. Rochan, Z. Liu, and Y. Wang, "Cross-modal self-attention network for referring image segmentation," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Long Beach, CA, USA, Jun. 2019, pp. 10494–10503.
[17] Z. Huang et al., "CCNet: Criss-cross attention for semantic segmentation," IEEE Trans. Pattern Anal. Mach. Intell., vol. 45, no. 6, pp. 6896–6908, Jun. 2023.
[18] Y.-H. Wu, Y. Liu, X. Zhan, and M.-M. Cheng, "P2T: Pyramid pooling transformer for scene understanding," IEEE Trans. Pattern Anal. Mach. Intell., vol. 45, no. 11, pp. 12760–12771, May 2023.
[19] V. Mnih, N. Heess, and A. Graves, "Recurrent models of visual attention," in Proc. Adv. Neural Inf. Process. Syst. (NIPS), Montreal, QC, Canada, 2014, pp. 2204–2212.
[20] J. Hu, L. Shen, and G. Sun, "Squeeze-and-Excitation networks," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Salt Lake City, UT, USA, Jun. 2018, pp. 7132–7141.
[21] L. Chen et al., "SCA-CNN: Spatial and channel-wise attention in convolutional networks for image captioning," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Honolulu, HI, USA, Jul. 2017, pp. 6298–6306.
[22] Z. Qin, P. Zhang, F. Wu, and X. Li, "FcaNet: Frequency channel attention networks," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 763–772.
[23] X. Hu, K. Yang, L. Fei, and K. Wang, "ACNET: Attention based network to exploit complementary features for RGBD semantic segmentation," in Proc. IEEE Int. Conf. Image Process. (ICIP), Sep. 2019, pp. 1440–1444.
[24] S. Woo, J. Park, J. Lee, and I. Kweon, "CBAM: Convolutional block attention module," in Proc. Eur. Conf. Comput. Vis. (ECCV), Munich, Germany, 2018, pp. 3–19.
[25] A. Dosovitskiy, L. Beyer, and A. Kolesnikov, "An image is worth 16×16 words: Transformers for image recognition at scale," in Proc. Int. Conf. Learn. Represent. (ICLR), vol. 3013, 2021, pp. 1–21.
[26] S. Zheng et al., "Rethinking semantic segmentation from a sequence-to-sequence perspective with transformers," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2021, pp. 6877–6886.
[27] R. Strudel, R. Garcia, I. Laptev, and C. Schmid, "Segmenter: Transformer for semantic segmentation," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 7242–7252.
[28] E. Xie, W. Wang, and Z. Yu, "Segformer: Simple and efficient design for semantic segmentation with transformers," in Proc. Adv. Neural Inf. Process. Syst. (NIPS), vol. 34, 2021, pp. 12077–12090.
[29] J. Guo et al., "CMT: Convolutional neural networks meet vision transformers," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), New Orleans, LA, USA, Jun. 2022, pp. 12165–12175.
[30] H. Wu et al., "CvT: Introducing convolutions to vision transformers," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 22–31.
[31] J. Li, X. Xia, and W. Li, "Next-ViT: Next generation vision transformer for efficient deployment in realistic industrial scenarios," 2022, arXiv:2207.05501.
[32] K. Yuan, S. Guo, Z. Liu, A. Zhou, F. Yu, and W. Wu, "Incorporating convolution designs into visual transformers," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 559–568.
[33] S. Mehta and M. Rastegari, "MobileViT: Light-weight, general-purpose, and mobile-friendly vision transformer," in Proc. Int. Conf. Learn. Represent. (ICLR), vol. 6230, 2022, pp. 1–26.
[34] Y. Chen et al., "Mobile-former: Bridging MobileNet and transformer," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), New Orleans, LA, USA, Jun. 2022, pp. 5260–5269.
[35] A. Howard et al., "Searching for MobileNetV3," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 1314–1324.
[36] A. G. Howard et al., "MobileNets: Efficient convolutional neural networks for mobile vision applications," 2017, arXiv:1704.04861.
[37] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen, "MobileNetV2: Inverted residuals and linear bottlenecks," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Salt Lake City, UT, USA, Jun. 2018, pp. 4510–4520.
[38] W. Xu, Y. Xu, T. Chang, and Z. Tu, "Co-scale conv-attentional image transformers," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 9961–9970.
[39] X. Chu et al., "Conditional positional encodings for vision transformers," in Proc. Int. Conf. Learn. Represent. (ICLR), vol. 488, Kigali, Rwanda, 2023, pp. 1–19.
[40] Z. Chen, Y. Duan, and W. Wang, "Vision transformer adapter for dense predictions," in Proc. IEEE Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 12159–12168.
[41] M. Guo, C. Lu, and Q. Hou, "SegNeXt: Rethinking convolutional attention design for semantic segmentation," in Proc. Adv. Neural Inf. Process. Syst. (NIPS), vol. 35, New Orleans, LA, USA, 2022, pp. 1140–1156.
[42] N. Park and S. Kim, "How do vision transformers work?" in Proc. Int. Conf. Learn. Represent. (ICLR), vol. 6017, 2022, pp. 1–26.
[43] C. Yuan, Z. Liu, and Y. Zhang, "Learning-based smoke detection for unmanned aerial vehicles applied to forest fire surveillance," J. Intell. Robot. Syst., vol. 93, nos. 1–2, pp. 337–349, Feb. 2019.
[44] A. Garg, S. Nath, and P. Nagrath, "Smoke detection in digital frames," Int. Res. J. Eng. Technol., vol. 5, no. 4, pp. 3843–3846, 2018.
[45] M. Mahmoud and H. Ren, "Forest fire detection and identification using image processing and SVM," J. Inf. Process. Syst., vol. 15, no. 1, pp. 159–168, 2019.
[46] K. Dimitropoulos, P. Barmpoutis, and N. Grammalidis, "Higher order linear dynamical systems for smoke detection in video surveillance applications," IEEE Trans. Circuits Syst. Video Technol., vol. 27, no. 5, pp. 1143–1154, May 2017.
[47] A. Filonenko, D. C. Hernández, and K.-H. Jo, "Fast smoke detection for video surveillance using CUDA," IEEE Trans. Ind. Informat., vol. 14, no. 2, pp. 725–733, Feb. 2018.
[48] Y. Jia, G. Lin, J. Wang, J. Fang, and Y. Zhang, "Early video smoke segmentation algorithm based on significance detection and Gaussian mixture model," Comput. Eng., vol. 42, no. 2, pp. 206–209, 2016.
[49] Y. Luo, L. Zhao, P. Liu, and D. Huang, "Fire smoke detection algorithm based on motion characteristic and convolutional neural networks," Multimedia Tools Appl., vol. 77, no. 12, pp. 15075–15092, Jun. 2018.
[50] Y. Zhao, "Candidate smoke region segmentation of fire video based on rough set theory," J. Electr. Comput. Eng., vol. 2015, pp. 1–8, Feb. 2015.
[51] N. Zhang et al., "Rough set and region growing smoke image segmentation algorithm," Comput. Sci. Explor., vol. 11, no. 8, pp. 1296–1299, 2017.
[52] Y. Hu, H. Wang, and Z. Ma, "Adaptive smoke image segmentation algorithm based on improved hybrid Gaussian model," J. Comput. Aided Des. Comput. Graph., vol. 28, no. 7, pp. 1138–1145, 2016.
[53] Z. Lin, H. H. T. Liu, and M. Wotton, "Kalman filter-based large-scale wildfire monitoring with a system of UAVs," IEEE Trans. Ind. Electron., vol. 66, no. 1, pp. 606–615, Jan. 2019.
[54] H. Tian, W. Li, P. O. Ogunbona, and L. Wang, "Detection and separation of smoke from single image frames," IEEE Trans. Image Process., vol. 27, no. 3, pp. 1164–1177, Mar. 2018.
[55] R. Kaabi, M. Sayadi, M. Bouchouicha, F. Fnaiech, E. Moreau, and J. M. Ginoux, "Early smoke detection of forest wildfire video using deep belief network," in Proc. 4th Int. Conf. Adv. Technol. Signal Image Process. (ATSIP), Sousse, Tunisia, Mar. 2018, pp. 1–6.
[56] X. Li, Z. Chen, Q. M. J. Wu, and C. Liu, "3D parallel fully convolutional networks for real-time video wildfire smoke detection," IEEE Trans. Circuits Syst. Video Technol., vol. 30, no. 1, pp. 89–103, Jan. 2020.
[57] S. Khan et al., "DeepSmoke: Deep learning model for smoke detection and segmentation in outdoor environments," Expert Syst. Appl., vol. 182, Nov. 2021, Art. no. 115125.
[58] L. Yao, H. Zhao, J. Peng, Z. Wang, and K. Zhao, "FoSp: Focus and separation network for early smoke segmentation," 2023, arXiv:2306.04474.
[59] F. Yuan, L. Zhang, and X. Xia, "Smoke semantic segmentation with multi-scale residual paths and weighted middle surveillances," Multimedia Tools Appl., vol. 2023, pp. 1–26, Oct. 2023.
[60] Y. Zheng, Z. Wang, B. Xu, and Y. Niu, "Multi-scale semantic segmentation for fire smoke image based on global information and U-Net," Electronics, vol. 11, no. 17, p. 2718, Aug. 2022.
[61] Y. Li, W. Zhang, Y. Liu, and X. Shao, "A lightweight network for real-time smoke semantic segmentation based on dual paths," Neurocomputing, vol. 501, pp. 258–269, Aug. 2022.
[62] S. Yan, J. Zhang, and N. Barnes, "Transmission-guided Bayesian generative model for smoke segmentation," in Proc. AAAI Conf. Artif. Intell. (AAAI), 2022, pp. 3009–3017.
[63] Z. Ma, Y. Cao, L. Song, F. Hao, and J. Zhao, "A new smoke segmentation method based on improved adaptive density peak clustering," Appl. Sci., vol. 13, no. 3, p. 1281, Jan. 2023.
[64] S. Xie, R. Girshick, P. Dollár, Z. Tu, and K. He, "Aggregated residual transformations for deep neural networks," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017, pp. 5987–5995.
[65] A. Paszke, S. Gross, and S. Chintala, "Automatic differentiation in PyTorch," in Proc. Adv. Neural Inf. Process. Syst., vol. 31, 2017, pp. 1–4.
[66] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, "ImageNet: A large-scale hierarchical image database," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2009, pp. 248–255.
[67] I. Loshchilov and F. Hutter, "SGDR: Stochastic gradient descent with warm restarts," in Proc. Int. Conf. Learn. Represent. (ICLR), Toulon, France, 2017, pp. 1–16.
[68] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, "Grad-CAM: Visual explanations from deep networks via gradient-based localization," in Proc. IEEE Int. Conf. Comput. Vis. (ICCV), Venice, Italy, Oct. 2017, pp. 618–626.
[69] H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia, "Pyramid scene parsing network," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017, pp. 6230–6239.
[70] Smoke-Semantic-Segmentation. Accessed: Nov. 12, 2023. [Online]. Available: https://github.com/rekon/Smoke-semantic-segmentation
[71] Unet-Smoke. Accessed: Nov. 12, 2023. [Online]. Available: https://github.com/sonvbhp199/Unet-Smoke
[72] Video Smoke Detection. Accessed: Nov. 12, 2023. [Online]. Available: http://staff.ustc.edu.cn/~yfn/vsd.html

## Other

### Front matter

Lin Zhang and Jing Wu are with the School of Big Data Science, Jiangxi Science and Technology Normal University, Nanchang, Jiangxi 330038, China (e-mail: zymm_nc@163.com; 2484773973@qq.com). Feiniu Yuan is with the College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, Shanghai 201418, China (e-mail: yfn@ustc.edu). Yuming Fang is with the School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, Jiangxi 330032, China (e-mail: leo.fangyuming@foxmail.com).

### Author biographies

Lin Zhang received the B.E. degree in computer science and technology from East China Jiaotong University, Nanchang, China, in 2004, and the M.E. degree in computer science and the Ph.D. degree in management engineering from the Jiangxi University of Finance and Economics, Nanchang, in 2007 and 2020, respectively. She is currently an Associate Professor with the School of Big Data Science, Jiangxi Science and Technology Normal University, Nanchang. Her research interests include image processing and pattern recognition.

Jing Wu is currently pursuing the B.Eng. degree in computer science and technology with the Jiangxi Science and Technology Normal University, Nanchang, China. His research interests include image processing and image segmentation.

Feiniu Yuan (Senior Member, IEEE) received the B.Eng. and M.E. degrees in mechanical engineering from the Hefei University of Technology, Hefei, China, in 1998 and 2001, respectively, and the Ph.D. degree in pattern recognition and intelligence systems from the University of Science and Technology of China (USTC), Hefei, in 2004. From 2004 to 2006, he was a Postdoctoral Researcher with the State Key Laboratory of Fire Science, USTC. From 2010 to 2012, he was a Senior Research Fellow with the Singapore Bioimaging Consortium, Agency for Science, Technology and Research (A∗STAR), Singapore. He is currently a Professor, a Ph.D. Supervisor, and the Vice Dean with the College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, China. His research interests include deep learning, image segmentation, pattern recognition, and 3D modeling.

Yuming Fang (Senior Member, IEEE) received the B.E. degree from Sichuan University, Chengdu, China, the M.S. degree from the Beijing University of Technology, Beijing, China, and the Ph.D. degree from Nanyang Technological University, Singapore. He is currently a Professor with the School of Information Management, Jiangxi University of Finance and Economics, Nanchang, China. His research interests include visual attention modeling, visual quality assessment, computer vision, and 3D image/video processing. He serves on the editorial board for IEEE TRANSACTIONS ON MULTIMEDIA and Signal Processing: Image Communication.
