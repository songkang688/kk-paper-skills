<!--
FnyPro-1 Stage 00 Wave 3 Agent G clean corpus
Paper_ID: 12_CNN_Transformer_Complementary_PR2023_Medical_Segmentation
Source: /workspace/12_CNN_Transformer_Complementary_PR2023_Medical_Segmentation.md (bilingual reader, **Original:** blocks only)
Content policy: English original text only. Excluded: all Chinese, reader navigation/glossary/reading notes,
the venue/DOI line (S003), reference entries (S116/S121: reader states full bibliography is only in the PDF,
so nothing verbatim to keep), and table data rows (S081-S082, S088-S090, S103-S104, uncertain per reader notes).
Author biographies (S118-S120) are retained in an appendix because they appear verbatim (original OCR quirks intact).
Figure/table captions are segregated into a trailing appendix instead of interrupting body paragraphs.
Fixes applied: dual-column paragraph order in the Introduction (S009 moved before S008, following citation
order [1] -> [2]; moderate confidence); cross-page sentence joins (S013+S014, S028+S029, S036+S037,
S087+S091, S102+S105); section-title glue split (4.1.1, 4.1.2, 4.5.1, 4.5.2, 4.5.3); equations (1)-(7),
(10), (12)-(14) reassembled from fragmented blocks -- flagged below, verify against PDF.
Ligature artifacts (ffi rendered as garbled glyphs), "state-ofthe-art", "f eature", "var- ious", "de- coder",
"ImageNet- 22 K", "JFT-300 M" normalized. "CTC --Net" spacing normalized to "CTC-Net".
Authorial wording otherwise preserved verbatim, including recurring "long-rang", "an decoder",
"seft-attention", "Eq.s", "That's proofed that", "we also adopts", "To further enhancing".
-->

# An effective CNN and Transformer complementary network for medical image segmentation

Feiniu Yuan, Zhengxiao Zhang, Zhijun Fang

## Abstract

The Transformer network was originally proposed for natural language processing. Due to its powerful representation ability for long-range dependency, it has been extended for vision tasks in recent years. To fully utilize the advantages of Transformers and Convolutional Neural Networks (CNNs), we propose a CNN and Transformer Complementary Network (CTC-Net) for medical image segmentation. We first design two encoders by Swin Transformers and Residual CNNs to produce complementary features in Transformer and CNN domains, respectively. Then we cross-wisely concatenate these complementary features to propose a Cross-domain Fusion Block (CFB) for effectively blending them. In addition, we compute the correlation between features from the CNN and Transformer domains, and apply channel attention to the self-attention features by Transformers for capturing dual attention information. We incorporate cross-domain fusion, feature correlation and dual attention together to propose a Feature Complementary Module (FCM) for improving the representation ability of features. Finally, we design a Swin Transformer decoder to further improve the representation ability of long-range dependencies, and propose to use skip connections between the Transformer decoded features and the complementary features for extracting spatial details, contextual semantics and long-range information. Skip connections are performed in different levels for enhancing multi-scale invariance. Experimental results show that our CTC-Net significantly surpasses the state-of-the-art image segmentation models based on CNNs, Transformers, and even Transformer and CNN combined models designed for medical image segmentation. It achieves superior performance on different medical applications, including multi-organ segmentation and cardiac segmentation.

Keywords: Transformer; Medical image segmentation; Feature complementary module; Cross-domain fusion; Convolutional neural network

## 1. Introduction

<!-- Paragraph order below restores citation order [1] -> [2]; the reader emitted these two
paragraphs in swapped order (S008 before S009), a typical dual-column extraction artifact. -->

Medical images have different modalities [1] that reflect the internal structures of human bodies and are widely used for modern medical diagnosis. To better assist disease diagnosis professionals, medical image segmentation methods have been proposed to separate specific organs from others. Segmented organs play an important role in computer-aided clinical diagnosis. Medical image segmentation involves many clinical applications, such as multi-organ segmentation and cardiac segmentation. Accurate pixel-level classification of medical images for locating lesions is of great significance to clinical treatments, and it already serves as an important auxiliary diagnostic tool.

With the constant innovation of computing power and the rapid development of deep learning, Convolutional Neural Networks [2] (CNNs) have become the predominant backbone for vision models. In recent years, many CNN based methods have been proposed for medical image processing. Most methods adopt a general U-shaped architecture [3], which consists of an encoder and an decoder for medical image segmentation [4,5]. The encoder usually captures detailed texture information and contextual features through consecutive down-samplings, convolutions and normalizations. With the deepening of networks, receptive fields gradually enlarge and more semantic information is extracted. The decoder is responsible for gradually up-sampling feature maps to generate the output mask. Spatial details are inevitably lost during down-sampling, and lost information can be partially restored by using skip connections. Despite great successes of CNN based methods, long-rang dependency information has not been modelled well in most CNN based methods.

As an emerging model first thrived and widely used in various tasks of Natural Language Processing (NLP), the Transformer model [6] has achieved huge progresses and successes in the deep learning community. In recent years, more and more Transformer based methods [7,8] have been proposed for computer vision tasks. Compared to CNNs, Transformers are easier to make full use of self-attention mechanisms, which can compensate for CNNs' inherent limitations to long-range dependencies. Alexey et al. [9] proposed a Vision Transformer (ViT) for image classification, which is one of the most influential events in the vision research field. ViT [9] perfectly bridges the gap between natural language processing and computer vision. It is the first time for researchers to report that Transformers are used in vision tasks and also achieve the state-of-the-art performance for vision problems. Carion et al. [10] proposed a DEtection TRansformer (DETR) by utilizing an elegant design based on Transformers to build the first fully end-to-end object detection model. To improve image segmentation performance, Liu et al. [11] proposed a hierarchical vision Transformer using shifted windows (Swin Transformer). It not only applies the inductive bias of CNNs to a network structure with Transformers, but also exploits the advantages of self-attention mechanisms embedded in Transformers.

CNNs and Transformers focus on different aspects. On one hand, CNNs heavily adopt convolutions with strong inductive biases, leading to locality and translation invariance. This property allows CNNs to preferably extract local contextual information, but it inevitably brings a non-negligible difficulty that is a limited receptive field. There are many solutions that have been proposed to deal with the problem [12], such as Atrous convolution [13], enlarged kernel sizes [14], pyramid pooling [15] and non-local operations [16]. These methods alleviate this problem, but do not solve it completely. On the other hand, Transformers inherently adopt self-attention mechanisms for perfectly extracting global and long-range dependencies, but do not capture locality and translation invariance very well.

According to the above-mentioned analyses, Transformers and CNNs are naturally complementary to each other. From this perspective, we believe that combining these two kinds of CNNs and Transformers can overcome the weaknesses of two models and strengthen their advantages simultaneously. To obtain such a purpose, we propose a CNN and Transformer Complementary Network (CTC-Net) for medical image segmentation. In our CTC-Net, we first design a CNN based encoder branch by ResNet34 [17] mainly for extracting contextual features and another Transformer based encoder branch by Swin Transformer blocks [11] mainly for capturing long-range dependency information. Then, we specifically design a feature complementary module for cross-wisely enhancing features from two different domains. We compute the correlation between features from CNN and Transformer domains for further improving performance. In addition, we conduct channel attention on the Transformer self-attention features for capturing dual attention information. The main contributions of this paper are summarized as follows:

1) We design dual encoding paths that are CNN and Transformer encoders for producing complementary features. The CNN encoder implemented by ResNet34 [17] mainly focuses on extracting spatial and contextual features, while the Transformer one implemented by Swin Transformer [11] is mainly responsible for capturing long-range dependencies.

2) We propose an effective Feature Complementary Module (FCM) by cross-wisely fusing features from the transformation domains of CNN and Transformer. Our FCM adopts a cross-domain fusion manner for effectively combining CNN and Transformer features. In fact, we propose cross-domain correlation between CNN and Transformer features, and channel attention on the Transformer path.

3) We propose multi-scale skip connections of complementary features to effectively enhance the representation ability of the Swin Transformer decoder. Combining Transformer decoded features and complementary ones can jointly extract contextual and long-range information. In this way, we propose a CNN and Transformer Complementary Network (CTC-Net) for medical image segmentation.

The remainder of this paper is organized as follows. In Section II, we review related work on semantic segmentation by CNNs, Transformers and their combinations. Section III describes our method. Section IV presents experiments and analysis. Finally, we conclude this paper in Section V.

## 2. Related work

### 2.1. CNN based methods

Long et al. [2] proposed a Fully Convolution Network (FCN) for image segmentation, which has begun to become one of the mainstream networks for semantic segmentation. Inspired by the success of FCNs, more improvements have been made by adopting deeper, wider networks or more effective structures, such as VGG [18], ResNet [17], DenseNet [19], HRNet [20], GoogleNet [21]. Besides these classic networks, Ronneberger et al. [3] proposed a U-shaped Network (U-Net) for biomedical image segmentation, which is an encoder-decoder structure. After that, a set of U-Net based methods have been proposed, and have demonstrated outstanding performance beyond other kinds of models for medical image segmentation.

Although the U-shaped structure is very simple, it exhibits a powerful representation ability. Res-UNet [22] replaces each submodule of the standard U-Net with residual blocks and dense networks. Yuan et al. [23] stacked several encoders and decoders to form a Wave-shaped Network (W-Net), which specially uses skip connections between wave crests and troughs for improving segmentation performance. To obtain deep smoke segmentation, Yuan et al. [24] designed a two-path U-shaped architecture, where one deeper network is responsible for extracting global contexts and the other shallower one for obtaining fine-grained spatial details. Oktay et al. [25] proposed an attention U-Net by generating a gating signal that emphasizes the attention of features at different spatial locations. In addition, U-shaped structures can also be seen in the field of 3D medical image segmentation, such as 3D U-Net [26] and V-Net [27]. To improve accuracy of smoke segmentation, Yuan et al. [28] proposed cubic-cross convolutional and count prior attentions. The count prior attention globally supervises the overall classification errors of all pixels.

### 2.2. Transformer based methods

The model of Transformer [29] was originally designed for the task of machine translation. It uses self-attention mechanism, layer normalization, feed forward network and residual structures for achieving excellent performance, and it does not employ any convolutions. The elegant and powerful self-attention mechanism shortly allows Transformer based models to achieve the state-of-the-art performance in various tasks of natural language processing. Due to the powerful representation ability of long-rang dependencies, Transformer based models have achieved amazing accuracy in many NLP tasks.

Recently, many researchers have tried to introduce Transformers into the computer vision field for utilizing the advantage of long-range dependency. Alexey et al. [9] divided an input image into patches to replace words in NLP tasks, thus they first applied the standard Transformer to vision tasks. Experimental results validate that Transformers have the possibility to become a backbone network for vision tasks, and have outperformed many existing CNN based models trained on large datasets, such as ImageNet-22K and JFT-300M. Touvron et al. [30] used attention to enhance the applicability of vision Transformers by training data-efficient image transformers on smaller datasets, such as ImageNet-1k. They also used data augmentation and regularization strategies [31] for further improving performance. Srinivas et al. [32] proposed a Bottleneck Transformer Network (BoTNet) for visual recognition by only replacing 3 × 3 convolutions with multi-head self-attention blocks, but which achieves surprisingly good performance on the ImageNet.

The Swin Transformer [11] mainly adopts patch merging, patch expanding and seft-attention blocks to achieve image segmentation tasks that are often dominantly obtained by CNNs. It can not only use inductive biases of convolutions to networks with Transformers as the backbone of encoders and decoders, but also fully exploit the advantages of self-attention mechanisms itself. The method implements local attention in each window instead of global attention in the whole image, which is similarly equivalent to convolutions and reduces the computational complexity of Transformers to be from quadratic to linear. Shifted windows allow information flow through originally fixed windows, thus obtaining global interaction of different local windows. Through patch merging, Swin Transformer obtains multi-scale features as convolutions and further expands receptive fields. Inspired by the great success of Swin Transformers, we adopt Swin Transformer in both encoders and decoders.

### 2.3. CNN and Transformer combined methods

Combinative methods can keep individual benefits of different algorithms for final purposes [33]. Different from inserting self-attention mechanism blocks into CNN models [34,35], several works mainly make attempts to combine CNNs and Transformers for improving performance. Carion et al. [35] used CNNs to initially extract the preliminary features of objects, and then adopted Transformers to continue dealing with the extracted features. Valanarasu et al. [36] introduced an additional gating mechanism in the Transformer layer to reduce computational complexity and improve the segmentation capability of the model. There are also various combinations between these two structures in multi-modal brain tumor segmentation [37,38] and 3D medical image segmentation [12,39].

Fig. 1 shows the simplified structures of five typical methods for main framework comparisons, including two pure CNN methods, and three CNN and Transformer combined methods. For the sake of simplification and clearness, we do not draw some nondominant structures, such as skip connections, attention structures and loss functions. By the way, the CNN encoders and decoders, the Transformer encoders and decoders, and the fusion modules in Fig. 1 are totally different from each other.

As shown in Fig. 1a, it is the famous U-Net structure consisting of a CNN encoder and a CNN decoder, which has achieved excellent performance on medical images. Fig. 1b is our previous work [23] with two sets of CNN encoders and decoders for boosting soft segmentation accuracy. In this method, the first encoder is followed by the first decoder, then the results are fed into the second encoder for further improving feature representation, and finally the second decoder recovers the second encoded features to the input size. Thus, a Wave-shaped Network (W-Net [23]) is formed.

Fig. 1c shows TransUnet [40], which is the first method to adopt Transformers for medical image segmentation. Its core idea is rather simple by directly inserting a Transformer block between a CNN encoder and a CNN decoder. The CNN encoder is to extract high-resolution spatial details and contextual information, the Transformer block is responsible for further modeling long-range dependencies, and the CNN decoder is to recover features to the input size. However, this method fails to fully exploit the advantages brought by Transformers and neglect introducing Transformers into each scale of the feature maps.

As shown in Fig. 1d, TransFuse [41] has a CNN encoder, two CNN decoders, a Transformer decoder and a feature fusion module. The two encoders extract contextual and long-rang dependency features, and the first decoder is used for up-sampling features to be fused with Transformer features. Then the fused features are fed into the second decoder for generating the final output. However, this method does not use Transformers to decode features for further improving long-rang dependencies and fusing low-level spatial details.

To solve above-mentioned problems, we propose a CNN and Transformer Complementary Network (CTC-Net) for medical image segmentation, which has a CNN encoder, a Transformer encoder, a Transformer decoder and an effective feature fusion module, as shown in Fig. 1e. The CNN encoder is mainly responsible for capturing spatial contextual information, and the Transformer encoder focuses on extracting long-range dependency. These features are in two domains and complementary to each other. Therefore, we propose a cross-domain fusion module for enhancing. To further model long-range dependencies in different levels, we also propose a Transformer decoder with skip connections for multi-scale fusing and decoding.

## 3. The proposed methods

### 3.1. Architecture overview

Inspired by the powerful representation abilities of CNNs and Transformers, we propose a CNN and Transformer Complementary Network (CTC-Net). As shown in Fig. 2, our CTC-Net consists of four main branches, including a CNN encoder, a Transformer encoder, a Feature Complementary Module (FCM) and a Transformer decoder. The main differences of our method from existing architectures are that we design two different encoders to produce complementary features, and propose a cross-domain complementary fusion module.

Our motivation of using both CNN and Transformer encoders is that CNN encoders are mutually complementary to Transformer encoders. On the one hand, there are relatively small or thin organs in medical images, so deeper CNN architectures may result in severe loss of small or thin objects. It is very difficult for decoders to recover lost small and narrow objects, leading to failures in small and narrow objects. On the other hand, Transformer encoders can capture more dependencies between long and narrow organs in human bodies, such as TransUnet [40]. Long-range information is very useful for improving segmentation accuracy of long and narrow objects. Therefore, we specially propose the multi-scale Feature Complementary Module (FCM) for fusing features from both CNN and Transformer encoders.

Finally, we design the Transformer decoder, which directly accepts the feature maps from the Transformer encoder for progressively recovering feature maps. In addition, our FCM produces different level complementary information from CNN and Transformer decoders, which is also fed into the Transformer decoder by skip connections. The complementary features are very important for restoring small and narrow objects commonly existing in human bodies.

### 3.2. The Transformer encoder

Alexey et al. [9] proposed the Vision Transformer (ViT), which is the first Transformer model for vision tasks. In a standard Transformer, pixel values in each patch are concatenated to produce a token feature vector, which is required to calculate the attention with all other tokens in the whole image, directly leading to the quadratic computational complexity with respect to the image size. To solve this problem, the Swin Transformer [11] performs self-attention only in each local window, thus the computational complexity is linearly proportional to the image size.

We stack Swin Transformer Blocks (STB) and patch operations [11] to construct the main feature encoding path, named as Transformer encoder (Fig. 2c). Each Swin Transformer block (Fig. 2e) is composed of two successive sub-blocks. The first sub-block consists of Layer Normalization (LN), Window based Multi-head Self Attention (W-MSA), Multi-Layer Perceptron (MLP) and residual additions. The second one has almost the same operations, but replaces W-MSA with Shifted Window based MSA (SW-MSA) [11].

We also use patch merging [11] to down-sample feature maps. Common down-sampling methods used in CNNs are pooling and de-convolution. Similarly, Transformer based methods also need to perform down-sampling operations for aggregating contextual features. To obtain the same ability, Swin Transformer [11] merges adjacent 2 × 2 patches into a large patch by concatenating these 4 small patches along the channel direction. This procedure is called patch merging.

According to spatial resolutions, the Transformer encoder can be divided into four levels, as shown in Fig. 2c. The first level has a patch embedding layer and two Swin Transformer blocks for feature encoding. The second to fourth levels have a patch merging for down-sampling, and two Swin Transformer blocks for extracting long-range dependencies.

Suppose that the input RGB image x has the size of H × W × 3, and the output y of our CTC-Net is H × W × N where N is the category number for segmentation. The 2D outputs of the Transformer encoder in the four levels are denoted by g1, g2, g3, and g4, which have the sizes of (H/4 × W/4) × C, (H/8 × W/8) × 2C, (H/16 × W/16) × 4C, (H/32 × W/32) × 8C, respectively. According to the Swin Transformer [11], a RGB image patch with size of 4 × 4 is regarded as a token, so the feature dimension C of each token is equal to 4 × 4 × 3 = 48, i.e. C = 48.

### 3.3. The CNN encoder

To obtain contextual features and maintain certain spatial details by convolutional neural networks, we use the four encoding blocks of ResNet34 [17] to build a CNN encoder, as shown in Fig. 2a. The four blocks of ResNet34 [17] are denoted by Conv1x, Conv2x, Conv3x and Conv4x, each of which performs down-sampling operations by a rate of 2.

To make the feature map size of the CNN encoder to be exactly consistent with that of the transformer encoder, we adopt Conv1x and Conv2x to down-sample feature maps twice in Level 1. For the sake of consistency, the channel C of the 3D feature map f1 for Level 1 is set to 48. Hence, the CNN encoder generates an output feature map f1 with size of H/4 × W/4 × C for the first level, which has the same pixel number as the first level output of the Transformer encoder. For the second level, the Conv3x block is used to process f1 to generate another 3D feature map f2, which has the size of H/8 × W/8 × 2C. Next, we use Conv4x to filter f2 obtain the third 3D feature map f3 with H/16 × W/16 × 4C for Level 3. Our CNN encoder has only three levels to produce three feature maps. These three maps, i.e. f1, f2 and f3, contain abundant spatial details and contextual semantics for improving the representation of the Transformer decoder.

### 3.4. Feature complementary module

Transformer based methods originally proposed for NLPs are different from CNN based ones for vision tasks. These two kinds of methods have totally different feature extraction manners, and also have completely diverse purposes for applications. The features by the Transformer encoder and the CNN encoder are generated in different domains. To obtain mutually complementary information, we propose a feature complementary module by designing four blocks, as shown in Fig. 3.

The first block is called Cross-domain Fusion Block (CFB). Our CFB is responsible for cross-wisely fusing and enhancing features from two different domains of Transformer and CNN encoders. Specifically, the feature maps from the Transformer and CNN encoders are denoted by gi and fi, respectively. Suppose that the 2D feature map gi has the size of (h × w) × c, and the 3D CNN feature map has the size of h × w × c. To implement cross-domain fusion, we first apply Global Average Pooling (GAP) on these two maps to generate two feature vectors with size of (1 × 1) × c. Then, we concatenate the Transformer input gi with the globally pooled feature vector of the CNN input fi along the first axis for producing a larger 2D feature map g1i with size of (h × w + 1) × c. Then the concatenated map is fed into a Swin Transformer Block (STB) for feature fusion. Thus we can obtain a powerfully fused 2D feature map g2i with size of (h × w) × c, which is reshaped into its 3D version g3i with size of h × w × c. On the other hand, we also concatenate the CNN input fi with the pooled feature vector of the Transformer input gi along the first axis for producing another larger 2D feature map f1i with size of (h × w + 1) × c. Similarly, we use a Swin Transformer Block to process the concatenated feature map for producing another cross-domain fused feature map f2i, and reshape it to obtain a 3D feature map f3i. Finally, we concatenate the two cross-domain fused 3D feature maps and use a 1 × 1 convolution to generate a cross-domain fusion feature map si with size of h × w × c. The processing for our CFB is formulated as follows:

<!-- Equations (1)-(5) reassembled from fragmented blocks S047-S052; sub/superscripts inferred
from the prose above (g1i denotes g with superscript 1 and subscript i, etc.). Verify against PDF. -->

g1_i = cat(GAP(f_i), g_i), (1)

f1_i = cat(GAP(g_i), f_i), (2)

g3_i = reshape(STB(g1_i)), (3)

f3_i = reshape(STB(f1_i)), (4)

s_i = conv(cat(g3_i, f3_i)), (5)

where GAP, cat, STB, reshape and conv stand for Global Average Pooling, concatenation, Swin Transformer Block, reshaping, and convolutions, respectively.

Eq.s 1 and 2 perform the intensive cross-domain fusion of features from two different domains. In addition, the Swin Transformer Blocks in Eq.s 3 and 4 can further enhance the feature representation abilities of long-range dependencies. Eq. (5) finally fuses the features from two kinds of cross-wise ways.

The second block is the Correlation Enhancement Block (CEB). Our CEB is proposed to model the cross-domain correlation between features from two transformation domains of Transformer and CNN encoders. We first reshape the 2D Transformer feature map gi to obtain its 3D version g0i, and then point-wisely multiply g0i by fi to produce a cross-domain correlation feature map ei with size of h × w × c. In fact, our CEB is a special kind of attention mechanisms, which can enhance important information and suppress unremarkable features among the two feature maps. By using CEB, we extract mutually salient features in both CNN and Transformer branches for further improving accuracy.

The third one is the Channel Attention Block (CAB). The original Swin Transformer block has a built-in self-attention mechanism for modeling long-range dependency. To further enhancing attention features, we apply a channel attention [42] commonly used by CNNs to the Transformer features. In this way, we efficiently implement a mixture of channel and self-attention attentions to obtain a dual attention feature map ai with size of h × w × c. In other words, our CAB is factually a mixed attention mechanism.

The last one is Feature Fusion Block (FFB). We concatenate the cross-domain feature map si, the correlation feature map ei and the dual attention feature map ai to obtain a feature map m1i with size of h × w × 3c, and use residual and reshaping operations to generate the output feature map mi with size of h × w × c for our FCM, formulated as:

<!-- Equations (6)-(7) reassembled from fragmented blocks S056-S058; the residual form of (7)
is inferred from fragments "reshape conv" and "+ CBR(m1 ... m1" plus the prose "use residual and
reshaping operations". Verify against PDF. -->

m1_i = cat(s_i, e_i, a_i), (6)

m_i = reshape(conv(m1_i) + CBR(m1_i)), (7)

where CBR is a block with convolutions (Conv), batch normalization (BN) and rectified linear unit (ReLU) to fuse the concatenated features and reduce the number of parameters at the same time.

### 3.5. The Transformer decoder

Swin Transformer blocks have been proven quite qualified for serving as either encoders or decoders [8]. Just contrary to patch merging, patch expanding [11] is often used to up-sample feature maps. Following the idea of [11], we stack Swin Transformer blocks and patch expanding operations to create a four-level decoding path. To fuse features from both Transformer and CNN encoders, we also feed the cross-domain fused features from the Transformer and CNN encoders to the Swin Transformer block. As shown in Fig. 2d, our Transformer decoder has four levels. In each level, reinforced short connections between the Transformer decoder and the two encoders are proposed for compensating lost spatial details and long-range dependency information.

The fourth decoding level only adopts a patch expanding operation to up-sample feature maps at a rate of 2. In the third and second decoding levels, we first adopt two Swin Transformer blocks to fully fuse the cross-domain enhanced feature map from its corresponding feature complementary module and the up-sampled features from its adjacent high level, and then use patch expanding to up-sample the fused feature map. In the first decoding level, we also adopts two Swin Transformer block for feature fusion and extraction of long-range dependencies. Besides, we use a final patch expanding block to up-sample the feature map for generating the output mask with the same size as the input image. In the final patch expanding block, we use a patch expanding with a rate of 4 for recovering the size of the 2D feature map, a 1 × 1 convolution for adjusting its channel number to the category number N, and a reshaping operation to convert the 2D map into a 3D feature map that is just the output of our CTC-Net. According to the descriptions of Fig. 2d, the data processing in the Transformer decoder can be briefly formulated as follows:

v_k = STB(STB(u_k, m_k)), (8)

u_{k-1} = PE(v_k), (9)

where k is the level index, and STB and PE denote Swin Transformer and patch expanding blocks, respectively.

## 4. Experiments and discussion

### 4.1. Datasets

To evaluate the performance of our method for medical image segmentation, we compared our method with existing state-of-the-art networks on two widely used medical image datasets, which are the Synapse dataset (Synapse) and the Automatic Cardiac Diagnosis Challenge (ACDC) dataset. The Synapse and ACDC datasets are available via https://www.synapse.org/#!Synapse:syn3193805/wiki/217789, and https://www.creatis.insa-lyon.fr/Challenge/acdc/, respectively. More details about the two datasets are described as follows:

#### 4.1.1. Synapse

Synapse includes 30 CT scans on abdominal organs for multi-organ segmentation. Following TransUnet [40], we selected 18 cases as a training set, and regarded the rest 12 cases as a test set. We report the average Dice Similarity Coefficient (DSC) and the average Hausdorff Distance (HD) on 8 categories of 2211 2D slices extracted from the 3D volumes. The 8 classes are aorta, gallbladder, spleen, left kidney, right kidney, liver, pancreas, and stomach.

#### 4.1.2. ACDC

ACDC aims to evaluate the segmentation performance of left ventricle (LV), right ventricle (RV) and myocardium (MYO) for automated cardiac diagnosis. The dataset includes MRI images of 100 different patients. We divided the dataset into a training set with 70 samples, a validation one with 10 samples and a test one with 20 samples. We report the average DSC on the 3 classes mentioned above.

### 4.2. Implementation details

Our CTC-Net was implemented using Python 3.8 and Pytorch 1.7.1. All experiments were conducted on an Intel i9 PC with an Nvidia GTX 3090 of 24GB memory. We used the pre-trained weights of Swin Transformer on ImageNet to initialize the Transformer encoder and decoder our CTC-Net, and adopted a pre-trained ResNet34 to initialize the parameters of our CNN encoder. The batch size is set to 24, the maximum iteration number is set to 13,950, and the optimizer is SGD with basic learning rate 0.01, momentum 0.99 and weight decay 3e-5. The decay strategy of learning rate lr can be described as follows:

<!-- Equation (10) reassembled from fragmented blocks S069-S071. Verify against PDF. -->

lr = base_lr · (1 - iter_num / max_iterations)^0.9, (10)

where base_lr is a basic learning rate, max_iterations is a maximum iteration number, and iter_num is iteration index.

The overall loss of our model is defined as the weighted sum of a cross entropy loss and a dice loss. The two loss functions and the weight ratios between them can be described as follows:

L = (1 - α) ℓ_ce + α ℓ_dice, (11)

where ℓ_ce denotes the cross entropy loss, ℓ_dice stands for the dice loss, and α is a related importance weight empirically set to 0.6.

Human organs often have very smooth surfaces. To prevent the output results being noisy, we add a post-processing method on the segmentation results by our CTC-Net. There are several post-processing methods that can be adopted for removing noise, such as morphological operators and median filtering. For the sake of simplicity and computation efficiency, we use median filtering to obtain more smooth results. Subsequent experiments also validate that the results processed by median filtering are more accurate than the original results of our network. The reason may be that human organs have inherent smooth surfaces.

Two evaluation metrics are the average Dice Similarity Coefficient (DSC) and the average Hausdorff Distance (HD). They both indicate the similarity between a predicted segmentation and its ground truth. DSC is used to evaluate the overlapping degree between a segmentation prediction P and its corresponding ground truth G, and HD measures the overlapping quality of segmentation boundaries. The two metrics are defined as follows:

<!-- Equations (12)-(14) reassembled from fragmented blocks S076-S079. Verify against PDF. -->

DSC = 2|P ∩ G| / (|P| + |G|), (12)

HD(P, G) = max[D(P, G), D(G, P)], (13)

D(P, G) = max_{p∈P} min_{g∈G} ||p - g||, (14)

where ∩ stands for an intersection operator for two sets, p and g are coordinate vectors of two pixels, |S| is the pixel number of a set S, ||v|| is the l2 norm of a vector v, and P and G denote the coordinate sets of the segmentation prediction and the ground truth, respectively. A larger DSC or a smaller HD means a better segmentation.

Other detailed parameter settings of our CTC-Net are summarized in Table 1. As shown in Table 1, Depth_encoder and Depth_decoder denote the depth of each Swin Transformer layer in the Transformer encoder and decoder, Num_heads stands for the number of attention heads in the Transformer encoder and decoder, and Num_heads_FCM is the number of attention heads in FCM.

### 4.3. Experiments on Synapse

Table 2 lists the results of our method and twenty state-of-the-art CNN semantic segmentation models on the Synapse dataset. We compared our CTC-Net with these 20 methods, including pure Transformer based models, pure CNN based ones, and CNN and Transformer combined ones. We used the average Dice Similarity Coefficient (DSC) as our main evaluation metrics.

According to Table 2, experimental results demonstrate that our proposed CTC-Net achieves the highest average DSC of 78.41% among all the compared methods. Compared with any of the above models, our CTC-Net outperforms them on at least half of all the eight categories. All compared methods always achieve the comparatively low accuracies on pancreas segmentation due to the particularly large deformation of the pancreas from case to case and its blurred boundary. Thanks to the efficient combination of local details and global interactions in a cross-domain manner, our CTC-Net produces the best results on pancreas among all the methods. As for Kidney (R) and Kidney (L), our CTC-Net achieves the highest DSC and the second highest DSC among twenty-one methods, respectively. These existing methods have achieved state-of-the-art results, so it validates that our method is powerful.

For the sake of simplicity, Table 3 presents the average Hausdorff Distances (HDs) achieved by some of the excellent models in Table 2. Experimental results show that our CTC-Net achieves accurate segmentations on both large organs, and long and narrow ones, such as kidney and pancreas. Its CNN and Transformer encoders provide complementary features that are helpful for medical image segmentation. Our FCM can effectively fuse these two kinds of features in different scales. Due to effective fusion of complementary features, our CTC-Net has a powerful ability to extract robust feature representations for large, narrow or long-shaped organs, such as kidney, liver and pancreas. The long-range dependency of Transformer enables our network to segment large organs well, such as kidney and liver. The local details by CNNs make our network produce more accurate boundaries. The combination of CNN and Transformer features boosts the overall segmentation performance. Although our method only surpasses TransUNet by 1% in term of DSC, it improves nearly 10% in the HD metric and is well ahead of other models. According to Table 3, our CTC-Net obtains the best result among them. Furthermore, we even achieve a HD of 19.19% in our ablation studies, which is much better than our current architecture. Fig. 4 shows the visual comparisons between the results of our CTC-Net and compared methods. Our method achieves very pleasing segmented results.

### 4.4. Experiments on ACDC

<!-- Cross-page join: S087 (p.7) ends mid-sentence at "on two classes"; the continuation was
glued behind a Table 4 header row in S091 (p.9). Rejoined here. -->

To evaluate the generalization and robustness of our CNN and Transformer complementary model, we also performed related experiments on the ACDC dataset, which contains entirely different modalities and body parts. Table 4 presents the average DSC metric, and our method also achieves the highest average DSC on the ACDC dataset among these state-of-the-art methods. In addition, our method surpasses all the compared methods on two classes of right ventricle (RV) and left ventricle (LV). As for the category of myocardium (MYO), our method obtains the second highest DSC of 85.52%. These experiments effectively validate that our method outperforms the state-of-the-art methods of medical image segmentation.

### 4.5. Ablation studies

In order to prove the rationality of our CTC-Net and the interpretability of each module, we conducted ablation studies on the Synapse dataset.

#### 4.5.1. Evaluation of FCM

To validate the effectiveness of our FCM, we obtain several variants of our CTC-Net by replacing it with other existing modules or removing certain key blocks of FCM.

One straightforward idea is to simply concatenate two feature maps from the CNN and Transformer encoders, and adopt 1 × 1 convolutions to fuse them. In this way, we obtain the first variant of our CTC-Net for validating the importance of our FCM, denoted by "concat + conv".

Inspired by the success of [40], we replace the proposed FCM with a transformer decoder to perform the cross attention between the features from the CNN and Transformer encoders. The query matrix of the cross attention is from the CNN encoder, and the matrices of the key and value pair are generated based on the Transformer encoder. This is the case for one aspect. In the other aspect, the query matrix and the matrices of the key and value pair are reversely from the Transformer and CNN encoders, respectively. The final output is obtained by convolving the outputs from two aspects. Thus, the second variant is generated, and it is named as "cross attention".

The purpose of Channel Attention Block (CAB) is to emphasize channel related information for improving feature robustness. To validate the importance of CAB on the CNN branch, we add channel attention blocks in both CNN and Transformer paths to produce the third variant of our network, named as "Dual CAB". It seems reasonable that we would achieve better results by adding channel attentions in both CNN and Transformer branches. However, enabling channel attentions in both CNN and Transformer branches does not produce better results, as shown in Table 5.

In addition, we also performed three conventional ablation experiments to observe the performance of some blocks in our FCM. The fourth variant of our method is obtained by deleting the Channel Attention Block (CAB), and it is named as "without CAB". We remove the Cross-domain Fusion Block (CFB) from the FCM to produce the fifth variant of our method, named as "without CFB". Furthermore, we remove Correlation Enhancement Block (CEB) from our FCM to verify its effectiveness, named as "without CEB".

The experimental results for ablation studies are listed in Table 5. According to the average DSCs, our method can outperform the five variants by very large margins. In addition, our method achieves the highest DSCs on five categories among all variants. Although the second variant uses a cross attention method for cross-wisely fusing features from Transformers and CNNs, its DSC is far lower than that of our method. That's proofed that the FCM plays a very key role in our network.

#### 4.5.2. Evaluation of encoders

Our CTC-Net has two important encoders, which are Transformer and CNN ones. The Transformer encoder is the major branch for extracting long-range dependencies. The CNN encoder serves as an auxiliary branch to compensate for contextual features and spatial details. To explore the importance of the CNN encoder, we remove it to obtain a variant of our method, which is a pure transformer architecture. The variant has an encoder and a decoder, and both of them are composed of Swin Transformer blocks. The experimental results are shown in Table 6. Our method achieves the average DSC of 78.41%, which is significantly better than that of 76.38% by the variant. In addition, our method also obtains better results on six out of eight categories than the variant. It proves that the CNN encoder is a key branch in our network.

#### 4.5.3. Evaluation of decoders

Most of existing U-shaped networks have approximately symmetric structures. We know by intuition that symmetric networks may achieve excellent results. However, our CTC-Net has two encoders but one decoder, so it is obviously asymmetric. Why not design two decoders for our method?

<!-- Cross-page join: S102 (p.9) ends mid-sentence at "skip connections between"; continuation
found at S105 (p.10) starting "different levels of encoders and decoders". Rejoined here. -->

To answer the above question, we need to evaluate the symmetric variant of our method with two decoders, denoted by "CTC-Net with two decoders". We add a traditional CNN decoder widely used in U-shaped networks to our CTC-Net. The CNN decoder directly accepts feature maps from the CNN decoder of the original CTC-Net as the input, and adopts de-convolutions for gradually up-sampling the feature maps in a learnable manner. To improve spatial details, we also use skip connections between different levels of encoders and decoders. The variant produces two outputs by the Transformer and CNN decoders. Finally, we fuse the two outputs for the variant. As shown in Table 7, the symmetric variant cannot achieve better results than our asymmetric CTC-Net with only one decoder. Obviously, the results are contrary to our intuitions. There may be two main reasons for explaining the results. The first one is that adding a CNN decoder greatly increases network parameters, leading to possible overfitting. Another one is that the two decoders recover feature maps independently and they lack adequate information interchanging.

In addition, we replace the Swin Transformer Block with our self-designed Swin Transformer Decoder to produce another variant, named as "CTC-Net with cross attention". By the way, the cross attention [40] has achieved significant improvements for image segmentation. The variant only differs only in the part of attention calculation from our CTC-Net. We apply cross attention on features from skip connections and up-sampled features at each up-sampling stage, where the query matrix is from skip connection and the matrices of the key and value pair are the up-sampled features. The experimental results are shown in Table 7. The variant with cross attention achieves far better results than the variant with two decoders, but it cannot surpass our CTC-Net.

## 5. Conclusions

Since the Transformer has achieved great improvements in NLPs, it has been widely used in a variety of NLP tasks. In recent years, researchers have tried to exploit Transformer based methods for solving vision tasks, because Transformers have very powerful representation capability of long-range dependencies. Traditional Convolutional Neural Networks (CNNs) can effectively extract contextual information and spatial details, and CNNs have widely been used for vision tasks. However, CNNs are more difficult to extract long-range dependencies than Transformers. In the contrary side, Transformers are not good at extracting spatial related information and maintaining spatial details. To an extent, these two kinds of features by CNNs and Transformers are complementary to each other.

To efficiently compensate for shortcomings of CNNs and Transformers, we propose a CNN and Transformer Complementary Network (CTC-Net) for medical image segmentation. Our CTC-Net has two encoders that are a CNN one and a Transformer one, a feature fusion module, and a Transformer decoder. The CNN encoder is constructed by ResNet34 [17] for extracting features in the CNN domain, while the Transformer one is created by Swin Transformer blocks [11] for capturing long-range dependent features. The feature fusion module uses cross-domain concatenation, feature correlation and dual attention methods to effectively combine these features from CNN and Transformer domains. The Transformer decoder is created by Swin Transformer blocks for further improving long-range representation and recovering feature maps to the input size. Experiments show that our method achieves very good results, and it consistently outperforms the state-of-the-art segmentation networks for medical image segmentation. Although our method achieves pleasing segmented results, our limitation lies in the extraction of boundary details. The main reason may be that our CNN and Transformer encoders start to recover feature maps from the 4x down-sampled feature maps, which already lose detailed spatial information. In the future, we will explore novel networks without downsampling feature maps for maintaining high resolutions and abundant details.

## Declaration of Competing Interest

The authors declared that they have no conflicts of interest to this work. We declare that we do not have any commercial or associative interest that represents a conflict of interest in connection with the work submitted.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was partially supported by the National Natural Science Foundation of China (62272308), the Joint Key Fund of National Natural Science Foundation of China (U2033218), and the Major Project of New Generation Artificial Intelligence for Scientific and Technological Innovation 2030 (2020AAA0109300).

## References

<!-- Reference entries excluded: the reader block S121 states that full bibliographic entries
appear only in the PDF (reader-condensed summary, flagged uncertain). Consult the original PDF
(Pattern Recognition 136 (2023) 109228) for the verbatim reference list. -->

## Appendix: Author biographies (from pp. 11-12; OCR spacing "20 04" -> "2004" and Elsevier
"His-research"/"His-current" artifacts -> "His research"/"His current" fixed; otherwise verbatim)

Feiniu Yuan received his B.Eng. and M.E. degrees in mechanical engineering from Hefei University of Technology, Hefei, China, in 1998 and 2001, respectively, and his Ph.D. degree in pattern recognition and intelligence system from University of Science and Technology of China (USTC), Hefei, in 2004. From 2004 to 2006, he worked as a post-doctor with State Key Lab of Fire Science, USTC. From 2010 to 2012, he was a Senior Research Fellow with Singapore Bioimaging Consortium, Agency for Science, Technology and Research, Singapore. He is currently a professor, a PhD supervisor and a vice dean with College of Information, Mechanical and Electrical Engineering, Shanghai Normal University (SHNU), China. He is also with Key Innovation Group of Digital Humanities Resource and Research, SHNU, china. He is a senior member of IEEE and CCF. His research interests include deep learning, image segmentation, pattern recognition and 3D modeling.

Zhengxiao Zhang, born in 1997, received his B.Eng. degree in communication engineering from Shanghai Normal University, Shanghai, China, in 2020. Now, he is an M.E candidate with College of Information, Mechanical and Electrical Engineering, Shanghai Normal University. From 2020 to 2023, he studied in the Laboratory of Artificial Intelligence and Visual Perception at Shanghai Normal University. His research interests include deep learning and medical image segmentation.

Zhijun Fang is a professor and the dean of School of Computer Science and Technology, Donghua University. He obtained his PhD degree in Shanghai Jiaotong University and was a visiting scholar in University of Washington. He is a senior member of IEEE/ACM/CCF/CAAI/CSIG. His current research interests include image & video processing, machine vision, and intelligent data analysis.

## Appendix: Figure and table captions (segregated from body; numeric table content excluded,
see PDF for data rows)

Fig. 1. Comparisons of simplified frameworks. (a) U-Net with a CNN encoder and a CNN decoder. (b) W-Net with two CNN encoders and two CNN decoders. (c) TransUnet with a CNN encoder, a Transformer block and a CNN decoder. (d) TransFuse with a CNN encoder, two CNN decoders, a Transformer decoder and a fusion module. (e) Our CTC-Net with a CNN encoder, a Transformer encoder, a Transformer decoder and an effective feature fusion module.

Fig. 2. The overall architecture of our CTC-Net. (a) The CNN encoder. (b) The multi-scale Feature Complementary Module (FCM). (c) The Transformer encoder. (D) The Transformer decoder. (e) Swin Transformer Block (STB).

Fig. 3. The architecture of Feature Complementary Module (FCM). Our FCM consists of four blocks, which are Cross-domain Fusion Block (CFB), Correlation Enhancement Block (CEB), Channel Attention Block (CAB) and Feature Fusion Block (FFB). Yellow cuboids or rectangles represent the output features from the CNN encoder, while blue ones denote the output features from the Transformer encoder.

Fig. 4. The visualized comparison of different methods on Synapse datasets.

Table 1. Network configuration of CTC-Net.

Table 2. Experiments on Synapse (mean Dice Similarity Coefficients in %).

Table 3. Experiments on Synapse datasets (mean HD).

Table 4. Experiments on ACDC (mean DSC in %).

Table 5. Ablation experiment on FCM (mean Dice Similarity Coefficients in %).

Table 6. Ablation experiments for evaluating the importance of the CNN encoder (mean Dice Similarity Coefficients in %).

Table 7. Ablation experiments for evaluating decoders (mean Dice Similarity Coefficients in %).
