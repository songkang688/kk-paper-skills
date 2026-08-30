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
