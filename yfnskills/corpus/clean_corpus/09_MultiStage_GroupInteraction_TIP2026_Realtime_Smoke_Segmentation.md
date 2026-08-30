# Multi-Stage Group Interaction and Cross-Domain Fusion Network for Real-Time Smoke Segmentation

**Paper_ID:** 09_MultiStage_GroupInteraction_TIP2026_Realtime_Smoke_Segmentation
**Authors:** Kang Li, Feiniu Yuan (Senior Member, IEEE), Chunmei Wang, and Chunli Meng
**Venue:** IEEE Transactions on Image Processing (2026)

## Abstract

Lightweight smoke image segmentation is essential for fire warning systems, particularly on mobile devices. In recent years, although numerous high-precision, large-scale smoke segmentation models have been developed, there are few lightweight solutions specifically designed for mobile applications. Therefore, we propose a Multi-stage Group Interaction and Cross-domain Fusion Network (MGICFN) with low computational complexity for real-time smoke segmentation. To improve the model's ability to effectively analyze smoke features, we incorporate a Cross-domain Interaction Attention Module (CIAM) to merge spatial and frequency domain features for creating a lightweight smoke encoder. To alleviate the loss of critical information from small smoke objects during downsampling, we design a Multi-stage Group Interaction Module (MGIM). The MGIM calibrates the information discrepancies between high and low-dimensional features. To enhance the boundary information of smoke targets, we introduce an Edge Enhancement Module (EEM), which utilizes predicted target boundaries as advanced guidance to refine lower-level smoke features. Furthermore, we implement a Group Convolutional Block Attention Module (GCBAM) and a Group Fusion Module (GFM) to connect the encoder and decoder efficiently. Experimental results demonstrate that MGICFN achieves an 88.70% Dice coefficient (Dice), an 81.16% mean Intersection over Union (mIoU), and a 91.93% accuracy (Acc) on the SFS3K dataset. It also achieves an 87.30% Dice, a 78.68% mIoU, and a 92.95% Acc on the SYN70K test dataset. Our MGICFN model has 0.73M parameters and requires 0.3G FLOPs.

**Index Terms:** Real-time smoke segmentation, lightweight network, cross-domain fusion, group interaction.

## Introduction

### I. Introduction

Smoke image segmentation is a vital area of semantic segmentation that plays an essential role in fire early warning systems. This process involves separating smoke objects from the background of images with pixel-level accuracy. With the rapid advancement of deep learning, a series of high-precision smoke detection models have been proposed, including DSS [...]. [NOTE: source text truncated here at a column break; the enumeration of models following "including DSS" is missing from the extracted text.]

Despite significant progress in lightweight smoke detection networks, these methods still encounter inherent challenges. The first challenge is poor adaptability to various environments. Existing models lacks robustness under varying illumination conditions and complicated occlusions. The second one is decreased performance in extreme scenarios. The detection accuracy drops significantly in cases of thin smoke or distant objects. The last one is difficulty in capturing irregular shapes. Accurately segmenting smoke boundary is quiet difficult. Therefore, how to achieve efficient and high-precision lightweight smoke image segmentation in complex environments is a critical issue to be solved urgently.

A critical issue is the scarcity of high-quality and large-scale datasets for smoke segmentation. The real smoke image segmentation dataset [18] contains only 143 images, so it is insufficient for training and validating advanced models.

DSS [1] uses synthetic methods to create a large-scale smoke image dataset (SYN70K), but SYN70K contains considerable redundant information, as illustrated in Fig. 1 (a). Moreover, there exist notable domain differences between synthetic and real data. Models trained on synthetic data often have poor performance on real data. Therefore, it is essential to develop a more diverse real smoke dataset that is closer to practical applications.

> Fig. 1. Samples of two smoke datasets from (a) SYN70K and (b) SFS3K.

To address the aforementioned challenges, we systematically investigate methods from both data and modeling perspectives. First, we construct a real-world smoke and fire segmentation dataset named SFS3K. Thus, we can mitigate issues such as limited scales, lack of real data, and insufficient diversity for smoke segmentation. Second, we propose a Multi-stage Group Interaction and Cross-domain Fusion Network (MGICFN) to overcome the deficiencies of adaptability in complex environments and poor performance under extreme scenarios.

Our SFS3K dataset comprises 3760 real-world images of smoke and fire with 224×224 pixels. It covers a wide variety of smoke objects, including indoor and outdoor scenes, urban streets, small smoke, low contrast, and forest fire scenarios. We split the dataset into a subset of 3008 images for training and another one of 752 for testing. As shown in Fig. 1 (b), SFS3K contains visually diverse realistic examples. In contrast to existing datasets, SFS3K not only emphasizes smoke segmentation but also incorporates fire-related information, offering a more comprehensive and semantically rich annotation schema.

Our MGICFN is designed to achieve efficient and accurate smoke segmentation under constrained computational resources. It facilitates multi-stage feature interaction and cross-domain integration to enhance feature representation and maintain low computational complexity. Specifically, we propose a Cross-domain Interaction Attention Module (CIAM) to capture complementary information from both spatial and frequency domains. In CIAM, we design an Asymmetric Pooling Spatial Attention Unit (SAU) to emphasize salient spatial regions, and a Spectral Transfer Unit (STU) based on discrete Fourier transform to extract discriminative frequency components. To further refine feature fusion, a Group Fusion Module (GFM) and an Edge Enhancement Module (EEM) are incorporated in the decoder to improve segmentation accuracy and boundary clarity. Additionally, a group-enhanced Convolution Block Attention Module (CBAM) [16] is employed as a feature refinement bridge between the encoder and decoder. Moreover, conventional skip connections in UNet [17] are replaced with a novel Multi-Stage Group Interaction Module (MGIM) to promote efficient multi-scale feature aggregation across different network stages. These architectural innovations collectively enable MGICFN to achieve robust performance in complex and variable smoke detection scenarios.

We summarize the key contributions of this paper as follows:

1) We propose a Cross-domain Interaction Attention Module (CIAM) to construct the smoke encoder. The CIAM combines asymmetric pooling and discrete Fourier transform techniques to facilitate information interaction between spatial and frequency domain, effectively enhancing the encoding capability of smoke features.

2) We develop a Group Convolution Block Attention Module (GCBAM) based on CBAM [16] to bridge encoder and decoder features. It employs a grouping strategy to independently process smoke features and efficiently extract critical information by a shared CBAM module.

3) We propose a Multi-Stage Group Interaction Module (MGIM) and a Group Fusion Module (GFM) to integrate multi-dimensional feature information. MGIM executes three-stage feature interactions to deeply explore and integrate multi-level feature correlations, while the GFM completes feature fusion in two stages.

4) We design an Edge Enhancement Module (EEM) to improve the decoding performance of smoke features. The EEM enhances the extraction and representation of edge information, effectively improving the detection ability of smoke edges.

5) We propose a Multi-stage Group Interaction and Cross-domain Fusion Network (MGICFN) for smoke segmentation. Our MGICFN achieves state-of-the-art performance on the SFS3K dataset, with a Dice coefficient of 88.70%, mean IoU of 81.16%, and accuracy of 91.93%, while maintaining low computational complexity of only 0.30 GFLOPs.

The remainder of this paper is organized as follows. In Section II, we review related work on smoke detection, segmentation and lightweight networks. Section III presents our method in details, and Section IV describes experiments. At last, we make conclusions in Section V.

## RelatedWork

### II. Related Work

#### A. Smoke Detection

Early smoke detection methods primarily depend on traditional image processing techniques. These methods detect smoke from images by analyzing color, motion and texture features. For instance, Calderara et al. [19] combined wavelet transforms, color information, and Bayesian methods to achieve rapid smoke detection. Morerio et al. [20] proposed to combine motion detection, color information and regional dynamics, and used a multi-path MLP fusion output to detect fire and smoke in video surveillance. Dimitropoulos et al. [21] developed a high-order LDS (h-LDS) descriptor for dynamic texture analysis and applied it to video smoke detection. The method improves detection accuracy by multidimensional dynamic texture analysis and spatiotemporal modeling.

With the development of machine learning technology, Appana et al. [22] constructed an effective video smoke detection framework by integrating optical characteristic and spatiotemporal energy analyses with Gabor filtering of temporal features, and used Support Vector Machine (SVM) as the classifier. Yuan et al. [23] designed fuzzy logic rules and combined them with extended Kalman filtering to improve the accuracy of early forest fire detection. However, traditional machine learning methods are often constrained by the quality of hand-designed features and limited cross-scene generalization capabilities. In recent years, deep learning, especially Convolutional Neural Networks (CNNs), has made significant progress in image processing, providing new ideas for addressing above challenges. For example, Chen et al. [24] designed an Adaptive Feature Aggregation (SAFA) network to improve the accuracy of smoke detection in remote sensing images through adaptive fusion between global information and local salient features. Li et al. [25] investigated attention mechanisms to optimize DenseNet [26], and they achieved efficient flame and smoke detection by employing pruning techniques to reduce computational overhead. AANet [27] effectively enhances the detection accuracy of industrial smoke by introducing a video attribute information decoding module and a spatiotemporal context information aggregation mechanism. Lin et al. [28] proposed a context interaction enhancement network for smoke detection by using large convolutional kernels to expand the receptive field of smoke feature extraction.

#### B. Smoke Segmentation

Smoke detection methods primarily aim to identify the presence of smoke in images or videos, typically marking smoke regions with bounding boxes. In contrast, smoke segmentation methods classify each pixel to precisely delineate smoke regions, providing detailed information about its boundaries and exact location. By offering a more accurate representation of smoke regions, segmentation methods enable better assessment of fire locations and scales.

Tian et al. [29] designed sparse representations to separate smoke from backgrounds by combining an atmospheric scattering based imaging model with dual-dictionary convex optimization techniques. Jia et al. [30] developed an innovative conditional generative adversarial network to automatically segment smoke regions from videos. Xu et al. [31] integrated pixel-level and object-level saliency convolutional neural networks to extract information-rich smoke saliency maps, resulting in effective end-to-end smoke detection. Yuan et al. [1] implemented high-quality smoke segmentation by using an end-to-end structure that combines coarse and fine paths. Frizzi et al. [9] designed a convolutional neural network for semantic segmentation of smoke and fire. DeepSmoke [32] focuses on detecting and segmenting smoke in complex outdoor environments through a convolutional neural network. Wang et al. [33] proposed an attention mechanism-based optical satellite video smoke segmentation network (AOSVSSNet). VTrUNet [34] introduces a Transformer to enhance the UNet architecture [17], effectively segmenting smoke in complex multi-spectral LandSat images. FoSp [4] uses a bidirectional cascade Focus module to integrate features from lower and higher resolutions into medium-resolution representations, enabling accurate localization of smoke regions and effectively reducing the rate of missed detections. Jing et al. [5] enhanced the identification capability of smoke regions in complex backgrounds by combining the advantages of Transformer and convolutional neural networks. SAGINN [6] introduces several advanced techniques, including a global-interactive non-local module, a pyramid high-level semantic aggregation module, smoke-aware loss, and classification assistance to achieve high-precision smoke segmentation.

However, these models primarily focus on achieving high accuracy, often overlooking the constraints of computational resources and the requirements of specific application scenarios. As a result, they tend to exhibit high computational complexity and limited real-time performance, leading to delayed responses in fire warning systems. To address these limitations, we propose a lightweight smoke segmentation method designed to maintain high efficiency while keeping computational complexity low.

#### C. Lightweight Framework

Mainstream efficient segmentation methods primarily rely on lightweight network architectures to achieve high performance with reduced computational cost. For instance, ENet [35] achieves low complexity and high efficiency in semantic segmentation through highly optimized structures. BiSeNet [15] adopts a bilateral architecture incorporating spatial and context paths to achieve efficient real-time performance. BiseNetv2 [36] extracts spatial details and high-level semantics through a detail branch and a semantic branch, respectively. By introducing a guided aggregation layer and an auxiliary training strategy, it achieves real-time semantic segmentation with high precision. Similarly, FBSNet [37] also designs a dual branch of semantic and spatial information extraction to achieve real-time semantic segmentation performance. SeaFormer [38] introduces a novel squeeze-enhanced axial transformer method for semantic segmentation on mobile devices. MALUNet [39] constructs a U-shaped architecture that utilizes four attention modules, effectively reducing the number of channels. EIU-Net [40] incorporates inverted residual blocks, efficient pyramid squeeze attention blocks, atrous spatial pyramid pooling and multi-layer fusion modules to improve performance. SwiftFormer [41] uses an efficient additive attention mechanism to optimize the performance of real-time mobile vision applications. MsFireD-Net [42] significantly reduces the complexity of CNN networks through reverse depth-wise separable deconvolution. Additionally, EdgeFireSmoke [43] designs a lightweight convolutional neural model for visual wildfire detection.

Although existing methods aim to reduce computational cost, they still suffer from high computational complexity. To address this challenge, we propose a lightweight Multi-stage Group Interaction and Cross-domain Fusion Network (MGICFN) for real-time smoke segmentation. MGICFN enables efficient deployment on mobile devices by significantly reducing computational complexity while maintaining high segmentation accuracy.

## Methods

### III. The Proposed Method

Fig. 2 illustrates the architecture of the Multi-stage Group Interaction and Cross-domain Fusion Network (MGICFN). The proposed MGICFN consists of five core modules: CIAM, GCBAM, MGIM, GFM, and EEM. These modules work collaboratively to form a lightweight network with low computational complexity, specifically designed for smoke segmentation. MGICFN effectively addresses challenges such as the loss of light smoke and blurred segmentation boundaries, enhancing overall segmentation performance.

> Fig. 2. Overall framework of our MGIFN. [NOTE: "MGIFN" appears as printed in the source caption; presumably MGICFN.]

#### A. Overall Framework of the Network

To meet the demands of high efficiency and accuracy in real-world scenarios simultaneously, we introduce a lightweight architecture composed of several carefully designed modules integrated into an encoder-decoder structure. The encoder incorporates an efficient Downsampling Unit (DU) [35] and a novel Cross-domain Interaction Attention Module (CIAM), which is constructed through the interaction of a Spatial Attention Unit (SAU) and a Spectral Transfer Unit (STU). This combination enhances feature representation capabilities and maintains low computational overhead. In the decoder, the Group Fusion Module (GFM) and the Edge Enhancement Module (EEM) are adopted to progressively recover spatial details and improve boundary prediction. The encoder and decoder are connected via a Group Convolution Block Attention Module (GCBAM), thus we facilitate multi-scale feature refinement. Furthermore, we replace the standard skip connections [17] with a Multi-Stage Group Interaction Module (MGIM) to enable more effective fusion of features across different stages. The final segmentation prediction maps are generated by several convolutional and upsampling layers.

#### B. Cross-Domain Interaction Attention Module

In the task of smoke segmentation, it is a significant challenge to extract the diverse features of smoke, especially thin and small smoke clusters in distant scenes. As shown in Fig. 3, we design the Cross-domain Interaction Attention Module (CIAM) to replace traditional convolutional blocks to address this issue more effectively. The CIAM mainly comprises the Spatial Attention Unit (SAU), Spectral Transfer Unit (STU), and Feature Fusion Module (FFM). In the final stage of CIAM, we introduce an Inverted Residual Block (IRB) to enrich the propagation of smoke features.

> Fig. 3. Details of cross-domain interaction attention module.

The input feature X ∈ R^(C×H×W) is processed by a channel split operation to obtain X1 ∈ R^(C/2×H×W) and X2 ∈ R^(C/2×H×W). In one branch, we introduce a Spatial Attention Unit (SAU). The implementation details of the SAU are illustrated in the upper part of Fig. 3. To effectively capture the spatial feature distribution of smoke, we replace standard pooling and convolution operations with Global Average Pooling (GAP) and asymmetric convolutions, and apply them to the smoke feature maps in horizontal or vertical direction. After this, we expand the compressed feature map to match the input size. Finally, the feature distributions from different directions are aggregated by element-wise addition. The details of the SAU can be described as follows:

X_SAU = F_{3×1}(H_gap(X1)) + F_{1×3}(V_gap(X1))    (1)

where F_{1×3}(·) and F_{3×1}(·) represent asymmetric convolutions.

In another branch, we introduce the Spectral Transfer Unit (STU), illustrated at the bottom of Fig. 3. The STU transforms smoke features from the spatial domain to the frequency domain, allowing for the effective capture of characteristics such as texture that might be difficult to detect in the spatial domain. Specifically, we apply 1D Fast Fourier Transform (FFT) and Inverse Fast Fourier Transform (iFFT) in the horizontal and vertical directions of the smoke feature maps, respectively. To further emphasize the key frequency components of the smoke features, we introduce a learnable factor ω that modifies the relationship between the 1D FFT and iFFT. Finally, we aggregate the feature information from different components through element-wise addition. These processes can be expressed with the following formulas:

FFT_H(u) = Σ_{h=0}^{H−1} X2(h) e^(−2πj·uh/H)    (2)

iFFT_H(h) = (1/H) Σ_{u=0}^{H−1} (ω · FFT_H(u)) e^(2πj·uh/H)    (3)

FFT_W(v) = Σ_{w=0}^{W−1} X2(w) e^(−2πj·vw/W)    (4)

iFFT_W(w) = (1/W) Σ_{v=0}^{W−1} (ω · FFT_W(v)) e^(2πj·vw/W)    (5)

X_STU = iFFT_H(h) + iFFT_W(w)    (6)

[NOTE: Eqs. (2)–(5) were fragmented across column breaks in the source; summation bounds, exponents and normalization factors have been reassembled from the recovered fragments following the standard 1D DFT/iDFT form. The normalization denominators (1/H, 1/W) in Eqs. (3) and (5) appeared only as a bare "1" in the extracted text.]

Our CIAM achieves interaction between the spatial and frequency domain branches by the Feature Fusion Module (FFM). We firstly concatenate the feature information from both domains and process it with a convolutional layer to eliminate potential aliasing artifacts. Next, these cross-domain information are fed into a sigmoid function to generate Cross-domain Attention Coefficients (CACs). We utilize these CACs to reweight the input feature of each branch and then re-concatenate them, thereby enriching the feature representation. Afterward, the concatenated features undergo a depth-wise separable convolution layer, and a residual connection is established between the output and the input. These entire processes can be summarized as follows:

δ1 = ϕ(Conv_{1×1}([X_STU, X_SAU]))    (7)

X_FFM = F_{3×3}([(δ1 · X1), (δ1 · X2)]) + X    (8)

where F_{3×3}(·) represents depth-wise separable convolution layer. [, ] means concatenation. ϕ(·) means Sigmoid function.

Finally, we feed the interacted multi-domain features into an Inverted Residual Block (IRB). The IRB can further refine and enrich the smoke image's details to improve the segmentation's accuracy. The final process can be described as:

X_CIAM = Conv_{λC→C}(Conv_{C→λC}(X_FFM))    (9)

where λ represents expand ration. C indicates the number of channels. We set the λ to 3.

#### C. Group Convolutional Block Attention Module

To ensure a smooth transition between the encoder and decoder, we design a Group Convolutional Block Attention Module (GCBAM) as a mediator. Fig. 4 illustrates the structure of the GCBAM, which is an enhanced version of the Convolutional Block Attention Module (CBAM) [16]. The GCBAM is also a lightweight and efficient attention module that combines channel attention and spatial attention to help the model capture and leverage critical information in the data.

> Fig. 4. Group convolutional block attention module.

Unlike the original CBAM, our GCBAM utilizes a group strategy, where smoke features are grouped and fed into a shared CBAM module for processing. This approach allows GCBAM to explore and enrich the representation of smoke features more thoroughly, thereby improving the model's feature representation capabilities. The group-enhanced features are then fused through a concatenation operation and further refined using a depth-wise separable convolution layer to generate the final output. Our GCBAM enhances the feature representation diversity while reducing the number of parameters.

#### D. Multi-Stage Group Interaction Module

During the extraction of smoke features, excessive downsampling may lead to the loss of critical information, especially small smoke objects within high-dimensional features. Conversely, low-dimensional features may lack sufficient semantic information. To overcome this challenge, we propose a new Multi-stage Group Interaction Module (MGIM). As shown in Fig. 5, MGIM adaptively selects the most suitable features for fusion through interactions between features at different stages. This process effectively captures object information at various scales. Moreover, MGIM can effectively calibrate the information discrepancies between high and low dimensional features, significantly enhancing the model's ability to recognize smoke features.

> Fig. 5. Multi-stage group interaction module.

The MGIM first aligns the high-dimensional features X_high ∈ R^(Hh×Wh×Ch), low-dimensional features X_low ∈ R^(Hl×Wl×Cl), and intermediate layer features X_mid ∈ R^(H×W×C) through operations such as convolution, interpolation, and down-sampling. The down-sampling operation consists of a 2×2 average pooling layer with a stride of 2, combined with a 1×1 convolution. After aligning the features, we divide them into four equal parts based on the channel, denoted as {X^i_mid}_{i=1}^{4} ∈ R^(H×W×C/4), {X^i_high}_{i=1}^{4} ∈ R^(H×W×C/4), and {X^i_low}_{i=1}^{4} ∈ R^(H×W×C/4). Next, we input X^i_high, X^i_mid, and X^i_low into interaction units to achieve group interactions. Finally, we concatenate the interaction feature maps from different groups and process them with depth-wise separable convolution. The computational process for this part is as follows:

δ^i_2 = ϕ(BN(X^i_high + X^i_mid + X^i_low))    (10)

I^i = δ^i_2 · X^i_high + (1 − δ^i_2) · X^i_low    (11)

X_MGIM = DCBR([I^1, I^2, I^3, I^4])    (12)

We aggregate information from three different scales and process it through an activation function to obtain the values {δ^i_2}_{i=1}^{4} ∈ R^(H×W×C/4). Next, we use δ^i_2 to weigh and fuse high-dimensional and low-dimensional features to form an intermediate feature representation {I^i}_{i=1}^{4} ∈ R^(H×W×C/4). Then, we merge I^i on the channel dimension and generate the final output X_MGIM by a depth-wise separable convolution layer. On the other hand, we dynamically adjust the weights of the high-dimensional and low-dimensional features. If δ^i_2 ≥ 0.5, we assign higher weights to the high-dimensional features. Conversely, if δ^i_2 < 0.5, we increase the weights of the low-dimensional features to strengthen boundary features. Our group interaction reduces model complexity and flexibly achieves selective distribution of weights.

#### E. Group Fusion Module

In the design of our network, to efficiently integrate feature information from two different stages in the decoding process, we introduce a Group Fusion Module (GFM) instead of the direct concatenation. Fig. 6 shows the details of our GFM.

> Fig. 6. Group fusion module.

In simple terms, our GFM continues the group strategy of MGIM. GFM combines specific features from different groups and utilizes a shared convolutional layer to capture the same smoke features in different locations. Ultimately, the output generated by the GFM, through concatenation and depth-separable convolution operations, significantly enhances the efficiency of integrating high and low dimensional features. The formal formula for GFM is as follows:

G^i = Conv([X^i_high, X^i_mid])    (13)

F_O = DCBR([G^1, G^2, G^3, G^4])    (14)

#### F. Edge Enhancement Module

Traditional decoders [17] recover spatial information by simple skip connections and transposed convolutions. Although these methods are effective, they often lead to blurred boundaries due to the direct concatenation of coarse high-level semantics with fine-grained, low-level features. Transformers can model global contexts but incur high computational complexity, so they are less suitable for real-time deployment. To overcome these limitations, we propose an Edge Enhancement Module (EEM) as a core component of our decoder. It acts as a lightweight and adaptive fusion gate between higher-resolution and lower-resolution features. Instead of simple concatenation or computationally expensive attention, the EEM employs a learnable gating mechanism to dynamically balance high-resolution edge information and low-resolution contextual information. The structure of our EEM is shown in Fig. 7.

> Fig. 7. Edge enhancement module.

The EEM has three inputs: M_i ∈ R^(Hi×Wi×Ci), M_{i+1} ∈ R^(Hi/2×Wi/2×2Ci), and D_i ∈ R^(Hi/2×Wi/2×2Ci) (i = {3, 2, 1}). First, we fuse decoder features D_i and encoder features M_{i+1} by element-wise addition, and use convolution and up-sampling to process fused features for preliminarily obtaining initially enhanced features F^i_MD, formulated as follows:

F^i_MD = Up(Conv(D_i + M_{i+1}))    (15)

Next, we combine the initially enhanced features F^i_MD with the high-resolution features M_i. The combined features are passed through a Batch Normalization layer and a sigmoid function to generate a set of adaptive gating weights δ^i_3:

δ^i_3 = ϕ(BN(F^i_MD + M_i))    (16)

Gating weights determine the relative importance of details and contexts to be preserved at each location. Weights greater than 0.5 emphasize more contextual information, while ones less than 0.5 underline more spatial details.

Finally, we use a weighted element-wise addition of context features F^i_MD and detail features M_i to generate the output guided by the gating weights δ^i_3:

D_{i−1} = δ^i_3 · F^i_MD + (1 − δ^i_3) · M_i    (17)

In contrast to direct concatenation, our EEM employs a dynamic gating mechanism to adaptively recalibrate and enhance features. To unequivocally demonstrate this adaptive fusion process, we provide Grad-CAM [44] visualizations that trace the key information flow within the EEM aligned with the architecture in Fig. 7.

#### G. Joint Loss Function

The Binary Cross-Entropy (BCE) loss is widely adopted in pixel-wise binary classification tasks such as smoke segmentation. It often fails to capture global structural consistency, thereby limiting model performance. To address this problem, we introduce a composite loss function that integrates a weighted Intersection over Union (IoU) loss (l^ω_IoU) with a weighted BCE loss (l^ω_BCE) [45] to focus on ambiguous regions and boundary pixels.

The boundary-aware weight map ω is formulated as:

ω = 1 + ε · |AP_{31×31}(G) − G|    (18)

where G denotes the ground truth, AP_{31×31} represents an average pooling operation with a kernel size of 31 × 31 to compute the local mean of annotations. The coefficient ε (5 by default) controls the emphasis on boundary disparity. The addition of 1 ensures that the weight values remain non-zero.

The weighted BCE loss is defined over the spatial domain:

l^ω_BCE = ( Σ_{i,j}^{H,W} W_{i,j} · l_BCE(P_{i,j}, G_{i,j}) ) / ( Σ_{i,j}^{H,W} W_{i,j} )    (19)

where P is the predicted map and the standard BCE loss is defined as:

l_BCE(P, G) = −[G · log(P) + (1 − G) · log(1 − P)]    (20)

The weighted IoU loss is expressed as:

l^ω_IoU = 1 − ( Σ_{i,j}^{H,W} W_{i,j} · P_{i,j} · G_{i,j} + 1 ) / ( Σ_{i,j}^{H,W} W_{i,j} · (P_{i,j} + G_{i,j}) − Σ_{i,j}^{H,W} W_{i,j} · P_{i,j} · G_{i,j} + 1 )    (21)

The overall training objective loss is formulated as:

l_total = l^ω_BCE + l^ω_IoU    (22)

This joint loss improves segmentation accuracy by simultaneously enforcing pixel-wise classification correctness and promoting structural coherence in prediction.

## Results

### IV. Experiments and Results

#### A. Experimental Datasets

Smoke has some dynamic natures, such as its constantly changing shape and ambiguous boundary. These natures make pixel-level manual annotation of real smoke images extremely challenging. Consequently, many researchers have turned to synthetic smoke datasets for model training. For example, the SYN70K dataset used in [1], [3], [6], and [46] generates diverse and realistic smoke samples, providing valuable support for training and evaluation. In this study, we conducted relevant experiments on synthetic datasets (SYN70K) and our newly constructed real-world Smoke and Fire Segmentation dataset (SFS3K). To facilitate further research in smoke and fire segmentation, we will publicly release the SFS3K dataset at https://github.com/KL0319/SFS3K. Some examples of the SFS3K datasets as shown in Fig. 8.

> Fig. 8. Some examples from our SFS3K. (a) Images, (b) Labels.

#### B. Experimental Settings

All experiments were conducted on a workstation equipped with an Intel i9-10900K CPU and an NVIDIA GeForce RTX 2080Ti 11GB GPU. Models were implemented using the PyTorch [47] deep learning framework. We trained the models with a batch size of 32 for 100 epochs, and used the AdamW [48] optimizer with an initial learning rate of 0.002.

#### C. Evaluation Metrics

To comprehensively evaluate the performance of the smoke segmentation method, we adopt several key metrics: Accuracy (Acc), Dice coefficient (Dice), and Intersection over Union (IoU). Accuracy measures the proportion of correctly predicted pixels relative to the total number of pixels, reflecting the model's overall classification performance. Dice coefficients quantify the overlap similarity between the predicted segmentation and the ground truth annotations. IoU calculates the ratio of the intersection to the union between the predicted and true regions, providing a robust measure of spatial alignment. In addition to segmentation accuracy, we evaluated the efficiency of compared models using the following metrics: the number of parameters, Floating Point Operations (FLOPs in G), and Frames Per Second (FPS).

#### D. Ablation Experiments

In this paper, we adopt a UNet [17] architecture with channel configurations of [16, 32, 64, 128, 256] as the baseline for our ablation experiments. We modify key components, such as the encoder, decoder and skip connections, to investigate the impact of our proposed modules on model performance in smoke segmentation. TABLE I provides detailed descriptions of the various model variants, while TABLE II presents a comparative analysis of their segmentation performance on the SFS3K and SYN70K datasets.

> TABLE I. Details of different variants. [NOTE: table contents not present in extracted text.]

> TABLE II. Segmentation results of various variants on different datasets. [NOTE: table contents not present in extracted text.]

As shown in TABLE II, replacing the baseline encoder with our proposed encoder (Model 1) results in only a marginal increase of 0.03M parameters (from 1.94 M to 1.97 M). However, it achieves a significant reduction in computational cost, with FLOPs decreasing from 2.63G to 0.74G. Importantly, this modification also improves segmentation accuracy, with mIoU increasing by 2.25% on SFS3K and 2.28% on SYN70K. When the standard convolutions in the short connection path of UNet are replaced with GCBAM (Model 2), the number of parameters drops by 0.55 M, and FLOPs are further reduced to 0.71G, while segmentation performance improves notably. Next, we replaced the skip connection of UNet with GFM or MGIM (Model 3) for substantially reducing parameters to 0.91M and FLOPs to 0.62G. It is nearly an order of magnitude smaller than the original. This modification significantly reduces computational overhead while preserves high segmentation accuracy. Finally, replacing the U-Net decoder with EEM (Model 4) yields the best overall performance. The model achieves the lowest complexity with only 0.73M parameters and 0.30G FLOPs. Compared to the baseline, mIoU increases by 3.58% on SFS3K and 3.44% on SYN70K, demonstrating superior efficiency and segmentation capability.

By incrementally refining individual components within the UNet architecture, we systematically reduced both the number of parameters and computational complexity, and simultaneously improve segmentation performance. Among all evaluated variants of our model, our final model (Model 4) achieves an optimal trade-off between model scale and accuracy.

Fig. 9 shows visualized segmentation comparisons of different variants on the SFS3K dataset (images 1, 2, and 3) and the SYN70K dataset (images 4, 5, and 6). The baseline model exhibits several limitations: (1) insufficient refinement of edge details, particularly evident in images 1 and 3; (2) poor discrimination between foreground smoke and background regions, observed in images 2, 4, and 6; and (3) significant segmentation errors, as seen in image 5. To address these issues, we progressively optimize the encoder, decoder, and skip connections, resulting in four variant models (Model 1 to Model 4). Notably, our model (Model 4) achieves the best overall performance.

> Fig. 9. Visualization of different variants on the SFS3K and SYN70K test sets. (a) Smoke images, (b) Labels, (c) Baseline, (d) Model 1, (e) Model 2, (f) Model 3, and (g) Model 4 (Ours).

We conducted an ablation experiment to evaluate the effectiveness of GCBAM by replacing it with CBAM. As shown in TABLE III, our GCBAM reduces the parameter number by 0.01M compared to the CBAM. This reduction is attributed to its grouping strategy and the shared CBAM design, which together optimizes the model structure. Although the computational complexity (FLOPs) remains comparable, GCBAM demonstrates superior performance in key metrics such as mIoU. Specifically, on the SFS3K dataset, GCBAM improves mIoU from 80.48% (with CBAM) to 81.16%, an increase of 0.68%. On the SYN70K dataset, the mIoU increases from 78.04% to 78.68%, representing a 0.64% improvement. These improvements indicate that GCBAM enhances feature modeling capability and reduces redundant computation, significantly boosting model performance without incurring additional computational cost.

> TABLE III. Ablation study of CBAM and GCBAM. [NOTE: table contents not present in extracted text.]

To evaluate the effectiveness of the joint loss function, we conducted experiments with models, which were trained using the weighted Binary Cross-Entropy loss (l^ω_BCE), the weighted Intersection over Union loss (l^ω_IoU), and their combination, respectively.

As shown in TABLE IV, the two loss functions yield the comparable mIoU performance on the two smoke segmentation datasets. In contrast, the joint function of the two losses significantly improves the model's performance. Specifically, its mIoU reaches 81.16% on the SFS3K dataset, which outperforms the best result of two single losses by 0.48%. Similarly, its mIoU increases to 78.68% on the SYN70K dataset, leading to a gain of 0.54% compared to the best result.

> TABLE IV. Ablation study of different loss function. [NOTE: table contents not present in extracted text.]

The superior performance of the joint loss can be attributed to its complementary optimization effects. l^ω_BCE ensures pixel-wise classification accuracy, while l^ω_IoU enhances global structural consistency. Their combination promotes a balance between local detail and global information, leading to more robust segmentation performance across diverse datasets.

#### E. Comparison With State-of-the-Art Methods

To validate the State-Of-The-Art performance of our MGICFN in lightweight smoke segmentation tasks, we conducted extensive comparative experiments with several mainstream lightweight architectures on the SFS3K and SYN70K datasets. These architectures include UNet [17], BiSeNet V2 [36], MALUNet [39], EIUNet [40], SwiftFormer [41], PIDNet [49], and ULite [50].

> TABLE V. Segmentation results of different lightweight method. [NOTE: table contents not present in extracted text.]

According to the results in TABLE V, our MGICFN achieves outstanding segmentation accuracy across both datasets. On the SYN70K dataset, our MGICFN attains a Dice score of 87.30%, an accuracy of 92.95%, and a highly competitive mIoU of 78.68%. Similarly, our method obtains a Dice score of 88.70%, an mIoU of 81.16%, and an accuracy of 91.93% on the SFS3K dataset. In addition, our MGICFN exhibits a remarkable advantage in terms of parameters and computational complexity. With only 0.73M parameters, it is the most lightweight model among all compared methods. In terms of computational cost, our method requires only 0.30G FLOPs, which is merely 1/35 of that required by UNet (10.48G FLOPs). Our method also achieves an excellent balance between segmentation performance and computational efficiency. Although ULite also has a low parameters and computational load, our method outperforms it across all key metrics, particularly mIoU and accuracy.

To crossly verify the quantitative analysis results, we further conducted qualitative comparisons of mainstream lightweight models on the synthetic smoke dataset (SYN70K) and the real-world smoke dataset (SFS3K). The visualized results are shown in Fig. 10 and Fig. 11.

> Fig. 10. Visualization of different lightweight methods on the SYN70K test sets. (a) Smoke images, (b) Ground truth, (c) UNet, (d) BiSeNet V2, (e) MALUNet, (f) EIUNet, (g) SwiftFormer, (h) PIDNet, (i) ULite, and (j) MGICFN (Our method).

> Fig. 11. Visualization of different lightweight methods on the SFS3K test sets. (a) Smoke images, (b) Ground truth, (c) UNet, (d) BiSeNet V2, (e) MALUNet, (f) EIUNet, (g) SwiftFormer, (h) PIDNet, (i) ULite, and (j) MGICFN (Our method).

By analyzing visualized results, we find some important observations. Most methods exhibit commendable performance in the case of large smoke objects. It shows they have good adaptation to large objects. The major reason is their ability to capture abstract information about prominent objects. Our method has the advantage in complex scenarios and diverse smoke patterns, because it exhibits more stable and superior performance than others. Taking the second and fourth samples in Fig. 10 as examples, our method considerably reduces the proportion of false positive regions, and achieves a higher accuracy of predicted edge details under challenging conditions where smoke regions are significantly sparse or low in concentration.

As shown in the third and fourth samples of Fig. 11 with small or visually less salient smoke, existing methods commonly suffer from missed detection, but our method still accurately identifies these regions. Specifically, in the fifth sample with thin smoke in a forest scenario, our MGICFN is able to segment smoke contours that are more complete than other models. In the sixth sample with a low-light environment complicated by fire, our method obtains satisfactory segmentation. Although minor false segmentation occurs in the sky region, our error level is significantly lower than that of other comparative methods, and it remains within an acceptable range.

In addition, we report the total training time of several models using a batch size of 32 and 100 epochs on the SYN70K dataset. As shown in the "Time (h)" column of TABLE V, our method requires 11.5 hours, which represents a significant advantage compared to UNet (19.5 hours). Compared to some of lightweight methods, our MGICFN spends the relatively longer training time on training. The primary reason is the computational cost associated with the Fourier transform in the encoder. This can maintain higher initial feature resolutions to improve segmentation accuracy, particularly for capturing subtle and structural details in smoke regions. Despite the additional time cost, our MGICFN offers superior performance with the lowest parameter count and FLOPs among all compared methods.

On the other hand, we compared state-of-the-arts smoke segmentation methods on the SYN70K dataset in recent years, including DSS [1], W-Net [46], Fizzi [9], TANet [3], LSSNet [10], SmokeSeger [5], FoSp [4], and SAGINN [6].

> TABLE VI. Comparative results on SYN70K with different smoke segmentation methods. [NOTE: caption reconstructed; source text was garbled as "COMPARATIVE RESULTS ON SYN70K WITH DIFFERENT SSmoke SEGMEN...TATION METHOD". Table contents not present in extracted text.]

TABLE VI shows the performance comparison results of different methods. SAGINN achieves an mIoU of 83%, but it has significantly larger model size with 101.1M. In contrast, our MGICFN obtains an mIoU of 78.7% while maintaining an extremely lightweight architecture with only 0.73 million parameters that are 138× fewer parameters than SAGINN. Notably, when the classification auxiliary branch is removed from SAGINN, its mIoU drops to 79.9%, which is only marginally higher than our model's performance, highlighting MGICFN's strong efficiency-accuracy trade-off. LSSNet is another lightweight method for smoke segmentation. Our MGICFN shows more obvious advantages. MGICFN not only reduces parameters by 0.15M, but also increases mIoU by 5.5%.

#### F. Real-Time Inference Performance

To evaluate the inference efficiency of our method in real-world scenarios, we compared several lightweight methods on a smoke video dataset. These methods include UNet [17], MALUNet [39], PIDNet [49], LSSNet [10], and our MGICFN. For the sake of comparisons, all evaluations were conducted under consistent conditions using a 480 × 480 resolution, and the performance metrics including average FPS and latency were evaluated on the first 100 frames of the same video.

> TABLE VII. Real-time performance evaluation results. [NOTE: table contents not present in extracted text.]

According to TABLE VII, our method achieves competitive performance with only 0.73M parameters and 1.35G FLOPs. It demonstrates significantly higher efficiency than other methods. Our method obtains a frame rate of 57.4 FPS. Although our frame rate is slightly lower than other methods, our method has higher resolutions and accuracy than others. Unlike most methods using 1/4 original resolutions in early stages, our MGICFN maintains 1/2 original resolutions to preserve spatial details. This strategy slightly reduces throughput, but it significantly improves segmentation accuracy for thin and semi-transparent smoke. In addition, our method uses the Fourier transform to improve accuracy, but it incurs substantial computational cost at high resolutions.

As shown in Fig. 12, we randomly selected three samples from video frames for visual comparisons, and predicted regions are annotated with red contours. It can be observed that our method significantly outperforms UNet and MALUNet in terms of foreground awareness. Specifically, in the upper-left region of the video sequence, our method effectively avoids erroneous segmentation artifacts present in other approaches. Compared to PIDNet and LSSNet, our method demonstrates noticeably superior segmentation performance, exhibiting more consistent and clearer boundary depiction. Although PIDNet achieves slightly better segmentation results in the second sample, our method shows higher overall performance and greater robustness in the other two samples than others.

> Fig. 12. Segmentation of different lightweight models on a real-world smoke video. (a) UNet, (b) MALUNet, (c) PIDNet, (d) LSSNet, and (e) our MGICFN.

## Conclusion

### V. Conclusion

To improve the performance of real-time smoke segmentation, we propose a Multi-stage Group Interaction and Cross-domain Fusion Network (MGICFN). We propose several novel modules to build our network, including the Cross-domain Interaction Attention Module (CIAM), Group Convolutional Block Attention Module (GCBAM), Multi-Stage Group Interaction Module (MGIM), Group Fusion Module (GFM), and Edge Enhancement Module (EEM). These modules together enhance feature representation, inter-scale interaction, and boundary refinement. Our MGICFN achieves significant improvements in computational cost and segmentation accuracy. Experimental results demonstrate that our MGICFN achieves state-of-the-art performance on the synthetic SYN70K and real-world SFS3K datasets and maintains a lightweight architecture simultaneously.

Notably, its inference speed is constrained by its high-initial-resolution design and the computational overhead of frequency-domain processing. In future work, we will focus on optimizing these components to improve computational efficiency, and also plan to expand the SFS3K dataset with more real-world scenarios and extend our MGICFN to related tasks such as joint fire and smoke detection.

## References

[NOTE: References [12]–[50] were printed in two interleaved columns in the source; each entry below has been reassembled from its split fragments.]

1. [1] F. Yuan, L. Zhang, X. Xia, B. Wan, Q. Huang, and X. Li, "Deep smoke segmentation," Neurocomputing, vol. 357, pp. 248–260, Sep. 2019.
2. [2] Y. Cao, Q. Tang, X. Wu, and X. Lu, "EFFNet: Enhanced feature foreground network for video smoke source prediction and detection," IEEE Trans. Circuits Syst. Video Technol., vol. 32, no. 4, pp. 1820–1833, Apr. 2022.
3. [3] X. Xia, K. Zhan, Y. Peng, and Y. Fang, "Texture-aware network for smoke density estimation," in Proc. IEEE Int. Conf. Vis. Commun. Image Process. (VCIP), Suzhou, China, Dec. 2022, pp. 1–5.
4. [4] L. Yao, H. Zhao, J. Peng, Z. Wang, and K. Zhao, "FoSp: Focus and separation network for early smoke segmentation," in Proc. AAAI Conf. Artif. Intell., 2024, vol. 38, no. 7, pp. 6621–6629.
5. [5] T. Jing, Q.-H. Meng, and H.-R. Hou, "SmokeSeger: A transformer-CNN coupled model for urban scene smoke segmentation," IEEE Trans. Ind. Informat., vol. 20, no. 2, pp. 1385–1396, Feb. 2024.
6. [6] L. Zhang, J. Wu, F. Yuan, and Y. Fang, "Smoke-aware global-interactive non-local network for smoke semantic segmentation," IEEE Trans. Image Process., vol. 33, pp. 1175–1187, 2024.
7. [7] K. Muhammad, S. Khan, V. Palade, I. Mehmood, and V. H. C. de Albuquerque, "Edge intelligence-assisted smoke detection in foggy surveillance environments," IEEE Trans. Ind. Informat., vol. 16, no. 2, pp. 1067–1075, Feb. 2020.
8. [8] X. Li, Z. Chen, Q. M. J. Wu, and C. Liu, "3D parallel fully convolutional networks for real-time video wildfire smoke detection," IEEE Trans. Circuits Syst. Video Technol., vol. 30, no. 1, pp. 89–103, Jan. 2020.
9. [9] S. Frizzi, M. Bouchouicha, J.-M. Ginoux, E. Moreau, and M. Sayadi, "Convolutional neural network for smoke and fire semantic segmentation," IET Image Process., vol. 15, no. 3, pp. 634–647, Feb. 2021.
10. [10] F. Yuan, K. Li, C. Wang, and Z. Fang, "A lightweight network for smoke semantic segmentation," Pattern Recognit., vol. 137, May 2023, Art. no. 109289.
11. [11] Y. Hu and X. Lu, "Real-time video fire smoke detection by utilizing spatial–temporal ConvNet features," Multimedia Tools Appl., vol. 77, no. 22, pp. 29283–29301, Nov. 2018.
12. [12] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen, "MobileNetV2: Inverted residuals and linear bottlenecks," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Jun. 2018, pp. 4510–4520.
13. [13] Y. Cao, Q. Tang, and X. Lu, "STCNet: Spatiotemporal cross network for industrial smoke detection," Multimedia Tools Appl., vol. 81, no. 7, pp. 10261–10277, Mar. 2022.
14. [14] Y. Li, W. Zhang, Y. Liu, and X. Shao, "A lightweight network for real-time smoke semantic segmentation based on dual paths," Neurocomputing, vol. 501, pp. 258–269, Aug. 2022. [NOTE: title reassembled from split fragments; the seam between refs [14] and [34] was ambiguous in the source.]
15. [15] C. Yu, J. Wang, C. Peng, C. Gao, G. Yu, and N. Sang, "BiSeNet: Bilateral segmentation network for real-time semantic segmentation," in Proc. ECCV, 2018, pp. 325–341.
16. [16] S. Woo, J. Park, J. Lee, and I. S. Kweon, "CBAM: Convolutional block attention module," in Proc. Eur. Conf. Comput. Vis., 2018, pp. 3–19.
17. [17] O. Ronneberger, P. Fischer, and T. Brox, "U-Net: Convolutional networks for biomedical image segmentation," in Proc. Int. Conf. Med. Image Comput. Comput.-Assisted Intervent., 2015, pp. 234–241.
18. [18] Smoke Semantic Segmentation. Accessed: Feb. 2, 2021. [Online]. Available: https://github.com/rekon/Smoke-semantic-segmentation
19. [19] S. Calderara, P. Piccinini, and R. Cucchiara, "Vision based smoke detection system using image energy and color information," Mach. Vis. Appl., vol. 22, no. 4, pp. 705–719, Jul. 2011.
20. [20] P. Morerio, L. Marcenaro, C. S. Regazzoni, and G. Gera, "Early fire and smoke detection based on colour features and motion analysis," in Proc. 19th IEEE Int. Conf. Image Process., Sep. 2012, pp. 1041–1044.
21. [21] K. Dimitropoulos, P. Barmpoutis, and N. Grammalidis, "Higher order linear dynamical systems for smoke detection in video surveillance applications," IEEE Trans. Circuits Syst. Video Technol., vol. 27, no. 5, pp. 1143–1154, May 2017.
22. [22] D. K. Appana, R. Islam, S. A. Khan, and J.-M. Kim, "A video-based smoke detection using smoke flow pattern and spatial–temporal energy analyses for alarm systems," Inf. Sci., vols. 418–419, pp. 91–101, Dec. 2017.
23. [23] C. Yuan, Z. Liu, and Y. Zhang, "Learning-based smoke detection for unmanned aerial vehicles applied to forest fire surveillance," J. Intell. Robotic Syst., vol. 93, nos. 1–2, pp. 337–349, Feb. 2019.
24. [24] S. Chen, Y. Cao, X. Feng, and X. Lu, "Global2Salient: Self-adaptive feature aggregation for remote sensing smoke detection," Neurocomputing, vol. 466, pp. 202–220, Nov. 2021.
25. [25] H. Li, Z. Ma, S.-H. Xiong, Q. Sun, and Z.-S. Chen, "Image-based fire detection using an attention mechanism and pruned dense network transfer learning," Inf. Sci., vol. 670, Jun. 2024, Art. no. 120633.
26. [26] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, "Densely connected convolutional networks," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017, pp. 2261–2269.
27. [27] H. Tao, M. Lu, Z. Hu, Z. Xin, and J. Wang, "Attention-aggregated attribute-aware network with redundancy reduction convolution for video-based industrial smoke emission recognition," IEEE Trans. Ind. Informat., vol. 18, no. 11, pp. 7653–7664, Nov. 2022.
28. [28] J. Lin, C. Fu, Q. Huang, and Y. Zhu, "Contextual interaction enhancement network for smoke detection," in Proc. IEEE Int. Conf. Multimedia Expo (ICME), Jul. 2024, pp. 1–6.
29. [29] H. Tian, W. Li, P. O. Ogunbona, and L. Wang, "Detection and separation of smoke from single image frames," IEEE Trans. Image Process., vol. 27, no. 3, pp. 1164–1177, Mar. 2018.
30. [30] Y. Jia et al., "Automatic early smoke segmentation based on conditional generative adversarial networks," Optik, vol. 193, Sep. 2019, Art. no. 162879.
31. [31] G. Xu et al., "Video smoke detection based on deep saliency network," Fire Saf. J., vol. 105, pp. 277–285, Apr. 2019.
32. [32] S. Khan et al., "DeepSmoke: Deep learning model for smoke detection and segmentation in outdoor environments," Expert Syst. Appl., vol. 182, Nov. 2021, Art. no. 115125.
33. [33] T. Wang et al., "AOSVSSNet: Attention-guided optical satellite video smoke segmentation network," IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens., vol. 15, pp. 8552–8566, 2022.
34. [34] J. Liu, J. Li, S. Peters, and L. Zhao, "A transformer boosted UNet for smoke segmentation in complex backgrounds in multispectral LandSat imagery," Remote Sens. Applications: Soc. Environ., vol. 36, Nov. 2024, Art. no. 101283.
35. [35] A. Paszke, A. Chaurasia, S. Kim, and E. Culurciello, "ENet: A deep neural network architecture for real-time semantic segmentation," in Proc. CVPR, Jun. 2016. [NOTE: venue as reassembled from fragments; ENet is commonly cited as an arXiv preprint (Jun. 2016), so the "Proc. CVPR" fragment attachment is uncertain.]
36. [36] C. Yu, C. Gao, J. Wang, G. Yu, C. Shen, and N. Sang, "BiSeNet v2: Bilateral network with guided aggregation for real-time semantic segmentation," Int. J. Comput. Vis., vol. 129, no. 11, pp. 3051–3068, Nov. 2021.
37. [37] G. Gao, G. Xu, J. Li, Y. Yu, H. Lu, and J. Yang, "FBSNet: A fast bilateral symmetrical network for real-time semantic segmentation," IEEE Trans. Multimedia, vol. 25, pp. 3273–3283, 2023.
38. [38] Q. Wan, Z. Huang, J. Lu, G. Yu, and L. Zhang, "SeaFormer: Squeeze-enhanced axial transformer for mobile semantic segmentation," in Proc. Int. Conf. Learn. Represent., 2023.
39. [39] J. Ruan, S. Xiang, M. Xie, T. Liu, and Y. Fu, "MALUNet: A multi-attention and light-weight UNet for skin lesion segmentation," in Proc. IEEE Int. Conf. Bioinf. Biomed., Dec. 2022, pp. 1150–1156.
40. [40] Z. Yu, L. Yu, W. Zheng, and S. Wang, "EIU-Net: Enhanced feature extraction and improved skip connections in U-Net for skin lesion segmentation," Comput. Biol. Med., vol. 162, Aug. 2023, Art. no. 107081.
41. [41] A. Shaker, M. Maaz, H. Rasheed, S. Khan, M.-H. Yang, and F. S. Khan, "SwiftFormer: Efficient additive attention for transformer-based real-time mobile vision applications," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2023, pp. 17379–17390.
42. [42] F. M. A. Hossain and Y. Zhang, "MsFireD-Net: A lightweight and efficient convolutional neural network for flame and smoke segmentation," J. Autom. Intell., vol. 2, no. 3, pp. 130–138, Aug. 2023.
43. [43] J. S. Almeida, C. Huang, F. G. Nogueira, S. Bhatia, and V. H. C. de Albuquerque, "EdgeFireSmoke: A novel lightweight CNN model for real-time video fire–smoke detection," IEEE Trans. Ind. Informat., vol. 18, no. 11, pp. 7889–7898, Nov. 2022.
44. [44] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, "Grad-CAM: Visual explanations from deep networks via gradient-based localization," in Proc. IEEE Int. Conf. Comput. Vis. (ICCV), Venice, Italy, Oct. 2017, pp. 618–626.
45. [45] J. Wei, S. Wang, and Q. Huang, "F3Net: Fusion, feedback and focus for salient object detection," in Proc. AAAI Conf. Artif. Intell., Apr. 2020, vol. 34, no. 7, pp. 12321–12328.
46. [46] F. Yuan, L. Zhang, X. Xia, Q. Huang, and X. Li, "A wave-shaped deep neural network for smoke density estimation," IEEE Trans. Image Process., vol. 29, pp. 2301–2313, 2020.
47. [47] A. Paszke et al., "Automatic differentiation in PyTorch," in Proc. Adv. Neural Inf. Process. Syst., 2017, pp. 1–4.
48. [48] I. Loshchilov and F. Hutter, "Decoupled weight decay regularization," in Proc. Int. Conf. Learn. Represent., 2017.
49. [49] J. Xu, Z. Xiong, and S. P. Bhattacharyya, "PIDNet: A real-time semantic segmentation network inspired by PID controllers," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2023, pp. 19529–19539.
50. [50] B.-D. Dinh, T.-T. Nguyen, T.-T. Tran, and V.-T. Pham, "1M parameters are enough? A lightweight CNN-based model for medical image segmentation," in Proc. Asia–Pacific Signal Inf. Process. Assoc. Annu. Summit Conf. (APSIPA ASC), Oct. 2023, pp. 1279–1284.
