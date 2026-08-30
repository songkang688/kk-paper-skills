# Frequency-Space Interaction With Hierarchical Aggregation Network for Lightweight Smoke Image Segmentation

**Paper_ID:** 10_FrequencySpace_TCE2025_Lightweight_Smoke_Segmentation
**Authors:** Kang Li, Feiniu Yuan (Senior Member, IEEE), and Chunmei Wang
**Venue:** IEEE Transactions on Consumer Electronics (2025)

## Abstract

Many methods tend to adopt more complex modules to improve smoke segmentation accuracy, but complex methods cannot achieve required processing speeds in computation-limited devices. To address this challenge, we propose a lightweight model with greatly minimized parameters to achieve competitive smoke segmentation performance. Specifically, we leverage Fourier transforms to enable feature interaction between spatial and frequency domains, and design a Frequency-Spatial Interaction Block (FSIB) to accurately encode features and recover details. Additionally, considering morphological variations and diverse characteristics of smoke, we introduce a Group Multi-Dilated Fusion module (GMDF) between the encoder and decoder to expand receptive fields for capturing more details. Furthermore, we employ a hierarchical feature aggregation strategy to further improve the presentation ability of features. Based on these modules, we construct a Frequency-Spatial Interaction Hierarchical Aggregation Network (FSIHAN) for achieving efficient smoke segmentation. Extensive experiments on two benchmark smoke datasets demonstrate that our FSIHAN outperforms various lightweight architectures and smoke segmentation methods. On the SYN70K test set, our method achieves a 79.4% mIoU with only 1.77M parameters, reducing the parameter numbers by approximately 57x compared to the state-of-the-art SAGINN. The base model of FSIHAN has only 0.46M parameters, leading to a reduction of about 220x compared to SAGINN.

**Index Terms:** Smoke segmentation, frequency-space interaction, lightweight network, hierarchical aggregation.

## Introduction

### I. Introduction

Fire is one of the significant disasters that pose a threat to human life and property. In recent years, researchers have developed various fire detection systems [1] and have devoted substantial efforts to continuously optimize their performance [2] for preventing fires and minimizing losses. Smoke is a key indicator in the early stages of a fire, and the effectiveness of a fire early warning system relies on the accurate and rapid detection of smoke.

In the past, early fire detection systems primarily depend on physical sensors. Chen et al. [3] developed a novel fire detection system that integrates smoke and gas sensors. However, this approach encounters challenges when implemented in outdoor or open spaces. With technological advancements, many researchers have turned to machine learning and artificial feature classifiers for smoke detection [4], [5], which perform better than traditional physical sensors in large or open spaces. Nevertheless, smoke in complex environments exhibits significant variability, which leads to numerous challenges for models in practical applications. Traditional recognition models for smoke detection have high false alarm rates, poor generalization ability, and insufficient adaptability to different environments.

With the rapid development of deep learning models [6], [7], [8], [9], their powerful feature extraction capabilities have made manual feature designs unnecessary. Consequently, more and more researches have begun to adopt deep learning networks to tackle challenges of smoke detection. Luo et al. [10] combined smoke motion features and Convolutional Neural Networks (CNNs) to propose a fire smoke detection algorithm based on background dynamic updating and dark channel prior. Yin et al. [11] integrated deep CNNs with recurrent neural networks to propose a deep convolutional recurrent motion spatial network for smoke detection. DSS [12] effectively addresses the issue of limited smoke segmentation data by synthetically generating a large number of smoke images. Yuan et al. [13] proposed an end-to-end smoke density estimation method based on a fully convolutional network. Frizzi et al. [14] designed a convolutional neural network based on DSS [12] for semantic segmentation of smoke and fire. FoSp [15] introduced a bidirectional cascade focus module to fuse low-resolution and high-resolution features into medium resolution ones, thereby improving the accuracy of smoke location and reducing the missed detection rate. SmokeSeger [16] successfully implements smoke segmentation in urban scenes by combining CNNs with Transformers. SAGINN [17] improves smoke feature representation through a global interaction mechanism, effectively addressing the irregularity and diffusion characteristics of smoke.

However, high-accuracy segmentation models often come with large model parameters, which pose challenges for deployments on mobile and resource-constrained devices. Therefore, it is necessary to reduce computations without apparently influencing accuracy. As shown in Fig. 1, we provide a visual performance comparison between the variants of our model and existing smoke segmentation models on the SYN70K dataset, and our method achieves a good balance between speed and accuracy.

> Fig. 1. The visual comparison of performance on the SYN70K dataset. Horizontal and vertical axes represent parameter numbers and mean IoUs, respectively.

Although smoke detection models based on CNNs and Transformers have made significant progresses in accuracy, they still face challenges such as high computational resource requirements, complex structures, and large numbers of parameters, so it is challenging to meet the real-time response demands of fire early warning systems. To address these issues, we propose a Frequency-Space Interaction with Hierarchical Aggregation Network (FSIHAN) for lightweight smoke segmentation. Our FSIHAN can maintain high segmentation accuracy while reducing computational complexity and the number of parameters. We introduce a Frequency-Spatial Interaction Block (FSIB) to facilitate interaction learning between frequency and spatial domains. Through FSIB, we construct a smoke feature encoder capable of cross-domain feature fusion. Next, we develop a Group Multi-Dilated Fusion (GMDF) module, which serves as a connection between the encoder and the decoder. GMDF expands the receptive field of features. To further improve feature fusion, we implement a Hierarchical Feature Aggregation Module (HFAM) mechanism to integrate deep semantic information with local features for gradually optimizing feature reconstruction and improving segmentation accuracy. Experimental results demonstrate that our method shows significant advantages in both accuracy and computational efficiency, especially compared to larger models. This makes it suitable for resource-constrained environments and real-time smoke detection tasks.

The key contributions of this paper can be summarized as follows:

1) We propose an innovative Frequency-Space Interaction with Hierarchical Aggregation Network (FSIHAN) for smoke segmentation. FSIHAN effectively achieves a balanced trade-off between lightweight design and accuracy.

2) We design a novel Frequency-Space Interaction Block (FSIB) to facilitate effective interaction and learning of smoke features between frequency and spatial domains.

3) We introduce a Group Multi-Dilated Fusion (GMDF) mechanism to strengthen the connection between the encoder and decoder. Additionally, we propose a Hierarchical Feature Aggregation Module (HFAM) to progressively integrate deep semantic information with local features for enhancing performance.

The rest of this paper is structured as follows. Section II reviews related work. Section III details the proposed method. Section IV presents comprehensive experiments on benchmark smoke datasets to analyze the effectiveness of each component and validate the method's superiority. Section V concludes with key remarks and future research.

## RelatedWork

### II. Related Work

#### A. Smoke Segmentation Method

In early smoke detection and segmentation, researchers primarily relied on distinct and easily distinguishable features such as color [4], [18], texture [5] and swaying features [19]. These features are somewhat effective in identifying smoke. For example, Adam et al. [20] proposed a video image processing method for forest fire detection based on background subtraction, color space, wavelet transform, and support vector machines. Tian et al. [21] achieved high-precision smoke detection and separation based on convex optimization of the atmospheric scattering model and dual-dictionary sparse representation combined with image matting techniques. However, these methods highly depend on expert knowledge and perform poorly in practical applications.

Semantic segmentation [6], [7], [22] performs well in regular objects, but morphological variations and non-rigid characteristics of smoke make generic algorithms challenging for early smoke segmentation. To improve performance, DeepSmoke [23] adopts EfficientNet [24] for smoke detection and uses DeepLabv3+ [22] for smoke segmentation. Yan et al. [25] proposed a transmission-guided local coherence loss function to guide the network to learn local pixel relationships and constructed a mixed smoke segmentation dataset SMOKE5K. Wang et al. [26] proposed an attention-guided optical satellite video smoke segmentation method and incorporated physical constraints to optimize the loss function and enhance the model's performance. MIFNet [27] adopts a dual encoder structure combining Transformer and CNN to enhance smoke image segmentation performance by attention mechanisms and multi-scale fusion modules. VTrUNet [28] introduces Transformer to enhance the UNet [7] architecture for smoke segmentation in complex multi-spectral LandSat images.

The above-mentioned methods mainly focus on improving the segmentation accuracy of models, and often ignore the number of parameters and computational complexity. Therefore, our research aims to optimize the model's computational efficiency and storage requirements to achieve effective and reliable smoke segmentation.

#### B. Frequency-Based Model

The frequency domain plays a central role in signal analysis, and in recent years, an increasing number of studies have introduced it into the field of computer vision. For example, FCANet [29] enhances feature selection by incorporating frequency transformations into the channel attention network. SPANet [30] introduces a frequency-balancing token mixer that effectively solves the issue of balancing frequency components in visual features through spectral pooling aggregation modulation. Wang et al. [31] propose an innovative perspective from the frequency shortcut angle, suggesting that neural networks improve image classification performance by learning frequency features. Additionally, frequency-domain techniques have achieved notable success in tasks such as medical image segmentation [32], and camouflaged object detection [33]. This paper combines frequency-domain and spatial-domain features to explore their potential in smoke feature extraction and detection, aiming to provide new insights and methods for the field.

#### C. Lightweight Framework

The mainstream efficient segmentation methods are based on lightweight architectures. SegNet [34] restores spatial information by reusing the pooling indices from the encoder to improve segmentation accuracy while reducing computational complexity. ENet [35] achieves low-complexity and high-efficiency semantic segmentation by highly optimized model structures. MobileNets [36] employs a streamlined architecture and leverages depthwise separable convolutions to construct an efficient and lightweight deep neural network. BiSeNet [37] designs a bilateral network structure with spatial paths and context paths, achieving efficient real-time performance. BiSeNetv2 [38] processes spatial details and high-level semantics by detail branch and semantic branch respectively, and introduces guided aggregation layer and auxiliary training strategy, which realizes real-time semantic segmentation with high precision and efficiency. MALUNet [39] adopts a U-shaped architecture with four attention modules to reduce the number of channels, ensuring the model remains lightweight. LPS-Net [40] progressively expands a small network into a larger one by gradually increasing the number of convolutional blocks, the number of channels, or the input resolution, achieving an optimal tradeoff between speed and accuracy. SwiftFormer [41] optimizes the performance of real-time mobile vision applications based on Transformers by an efficient additive attention mechanism.

In contrast, there are relatively few research papers on lightweight smoke segmentation. Muhammad et al. [42] proposed an edge intelligence-assisted smoke detection method that effectively improves the accuracy and real-time performance of smoke detection in hazy environments. Li et al. [43] modified the dual-path way of BiSeNet [37] to introduce a pyramid pooling module and efficient channel attention to seek a balance between high precision and real-time performance. Almeida et al. [44] proposed a lightweight convolutional neural model (EdgeFireSmoke) for wildfire detection. Yuan et al. [45] constructed a Lightweight Smoke Segmentation Network (LSSNet) by designing multiple lightweight attention modules. MsFireD-Net [46] significantly reduces the complexity of CNN networks by reverse depthwise separable de-convolutions to improve the efficiency and accuracy of smoke segmentation.

Although the aforementioned methods effectively reduce the computational cost of attention, these methods mainly focus on spatial domain feature extraction and fail to fully address challenges such as irregular smoke shapes, local textures, and blurry edges. Therefore, we introduce Fourier Transform to analyze the frequency domain features of smoke and propose a highly efficient, low-complexity frequency-space interaction smoke segmentation network through the interaction of frequency and spatial domain features. The model has minimal parameters of only 0.12M.

## Methods

### III. Proposed Method

To enable early fire detection and timely alarm, we propose an innovative Frequency-Space Interaction with Hierarchical Aggregation Network (FSIHAN) for lightweight smoke segmentation. FSIHAN improves segmentation accuracy in smoke detection tasks and reduces the model's computational complexity.

#### A. The Whole FSIHAN Framework

Fig. 2 illustrates the overall architecture of the FSIHAN. FSIHAN consists of three core modules: Frequency-Spatial Interaction Block (FSIB), Group Multi-Dilated Fusion (GMDF) module, and Hierarchical Feature Aggregation Module (HFAM). In the encoder stage, we adopt a Transformer-Style to encode feature maps. The difference is that we use the downsampling of ENet [35] to obtain multi-scale feature representations. To enhance segmentation performance while ensuring the lightweight nature of the encoder, we apply different numbers of FSIBs at multiple downsampling stages to extract smoke features. Specifically, we configure 4 FSIBs in the third layer of the encoder, while the remaining layers use 2 FSIBs. The FSIB module learns features through the interaction between the spatial and frequency domains, which is crucial for analyzing the relationship between smoke targets and backgrounds across different domains. To enhance the receptive field of features and facilitate the information flow between the encoder and decoder, we introduce a GMDF module. GMDF captures the morphological features of smoke at multiple scales by applying depthwise separable convolutions with different dilation rates within groups, effectively handling smoke targets of varying shapes and sizes. In the decoder stage, we design the Hierarchical Feature Aggregation Module (HFAM) to refine the recovery of smoke features. Four HFAM modules are employed to aggregate deep semantic features with shallow local features, enhancing the decoding and segmentation capabilities for smoke. Finally, we use a 1×1 convolution layer to convert the multi-channel feature map into a single-channel output and apply bilinear interpolation to restore the original image size, generating a clear smoke segmentation map.

> Fig. 2. The overall structure of the proposed FSIHAN.

#### B. Frequency-Space Interaction Block

In image processing tasks, frequency domain information can effectively analyze the global energy distribution and texture features of images, which is particularly crucial for smoke segmentation tasks. Additionally, the diversity and non-rigidity of smoke often make it challenging for traditional methods to effectively extract features. To address this challenge, we design a Frequency-Space Interaction Module (FSIM) by combining 2D Fourier Transform and asymmetric convolutions. FSIM extracts the global frequency domain information of images through the Fourier Transform, which is integrated with local spatial features, thereby enhancing the model's ability to capture features in complex scenes.

The input feature map X ∈ R^(C×H×W) is split along the channel axis to obtain X1 ∈ R^(C/2×H×W) and X2 ∈ R^(C/2×H×W). In the X1 branch, we adopt two asymmetric convolution layers with convolution kernels of 3×1 and 1×3 to accurately capture local spatial features. These asymmetric convolutions extract local features from different directions, making them better suited to the diversity of smoke shapes and enhancing the model's ability to capture local details. The formal formula is as follows:

Xs = F_{1×3}(F_{3×1}(X1))    (1)

In the X2 branch, we extract the frequency domain features of the image through Fourier Transform. To enhance the model's ability to learn frequency domain features, we reshape the frequency features by the 2D Fast Fourier Transform (2D FFT) and introduce a 3×3 depthwise separable convolution (DwConv) to strengthen the frequency features. These enhanced features are then adjusted to accommodate the 2D Inverse Fast Fourier Transform (2D iFFT) for effectively transforming the frequency features into space ones. This process can be represented as follows:

FFT(u, v) = Σ_{h=0}^{H−1} Σ_{w=0}^{W−1} X2(h, w) e^(−j2π(uh/H + vw/W))    (2)

FFT′(u, v) = Re(DwConv(Re(FFT(u, v))))    (3)

iFFT(h, w) = (1/(HW)) Σ_{u=0}^{H−1} Σ_{v=0}^{W−1} FFT′(u, v) e^(j2π(uh/H + vw/W))    (4)

where Re(.) represents the reshape operation.

[NOTE: Eqs. (2) and (4) were fragmented at column breaks in the source ("H + vw −j2π X2(h, w)e ..."); the exponents and summation bounds have been reassembled following the standard 2D DFT/iDFT form. The exponent term "uh/H" was partially lost in the source fragments.]

Next, we use sigmoid to activate the features from the frequency domain and the spatial domain for generating weights or inverse weights. To achieve deeper feature complementarity and interaction between domains, we utilize these weights or inverse weights to interact with different domains. Finally, these fused features information are output by a 3×3 depth-wise separable convolution layer to improve the model's representation ability of multi-domain features. The specific implementation details are as follows:

Xsf = ϕ(Xs) · iFFT(h, w) + (1 − ϕ(Xs)) · X1    (5)

ξ = ϕ(iFFT(h, w))    (6)

Xfs = ξ · Xs + (1 − ξ) · X2    (7)

Xo = DwConv([Xsf, Xfs])    (8)

where Re(.) represents the reshape operation, ϕ(·) represents Sigmoid function, 1 − ϕ(·) generates inverse weights, and [,] means concatenation operation.

Inspired by the design of Transformer block, we propose an innovative Transformer-style Frequency-Space Interaction Block (FSIB). FSIB consists of two core modules: FSIM and Multi-Layer Perceptron (MLP) [47]. In the MLP, the default ratio of the hidden layer to the input dimension is 3. FSIM facilitates effective interaction between frequency and spatial domain features, while the MLP further strengthens feature representation through high-dimensional mapping and nonlinear transformations. The detailed structure of FSIB is shown in Fig. 3.

> Fig. 3. Frequency-Space Interaction Block.

#### C. Group Multi-Dilated Fusion

The Atrous Spatial Pyramid Pooling (ASPP) module [8] extracts multi-scale features by using dilated convolution kernels with different dilation rates. The dilated convolution is crucial for handling images with diverse scales, complex backgrounds, or varying object sizes. However, it comes with a higher computational overhead, since down-sampling is not used. To solve this problem, we design a Group Multi-Dilated Fusion module (GMDF). It reduces computational complexity by efficient feature processing methods while maintaining the ability to extract multi-scale features. The structure of GMDF is shown in Fig. 4.

> Fig. 4. Group Multi-Dilated Fusion.

Unlike ASPP, our GMDF introduces three key strategies: feature grouping, intra-group interaction, and inter-group fusion mechanisms. First, our GMDF divides the feature map into multiple groups and expands the receptive field of features by incorporating scale information with different dilation rates. Then, within each group, feature representations are strengthened through adaptive weighting and fusion. Next, our GMDF extracts a single-channel feature map from each group and merges these single-channel feature maps to complete the fusion of inter-group information. Finally, all the fused features are concatenated for further boosting the feature representation capability.

Specifically, given an input feature map X ∈ R^(C×H×W), we first use a channel separation method to divide X into four groups {Xi}_{i=1}^{4} ∈ R^(C/4×H×W). We use 3×3 depthwise separable convolutions with different dilation rates d = {1, 6, 12, 18} to extract multi-scale spatial information from each group, thereby achieving receptive field differences between groups. The processing procedure can be formulated as follows:

X′i = DDwConv(Xi), i = 1, 2, 3, 4    (9)

where DDwConv(·) represents the dilated depth-wise separable convolution operation.

Next, to enhance the presentation of features within each group, we generate scale coefficients for each group using the sigmoid activation function, which then are used to adaptively weight and fuse the features within each group. This process is represented explicitly as follows:

Yi = ϕ(X′i) × Xi + X′i    (10)

where ϕ(·) represents the sigmoid function.

[NOTE: Eq. (10) was scrambled in the source ("X′i × Xi + X′ (10) Yi = ϕ"); reassembled per the described adaptive weighting with residual.]

Unlike most methods that directly concatenate feature maps for fusion, our GMDF does not directly concatenate the features after group fusion. Instead, we perform single-channel extraction on each feature group to achieve more efficient inter-group feature fusion. The extracted single-channel features are then concatenated along the channel axis to form a 4-channel feature map containing rich spatial information. This process is repeated for each group until all channels are processed. To further enhance effective feature fusion, we introduce a shared 4-channel convolutional layer with a 3×3 kernel to integrate the features from different groups. Finally, the processed feature map undergoes a final integration by a 3×3 depthwise separable convolutional layer to produce a feature map with rich spatial information. We can describe the entire process using the following formulas:

Y^j_o = F^4_{3×3}([Y^j_1, Y^j_2, Y^j_3, Y^j_4]), j = 1, 2, . . . , C    (11)

Y_F = DwConv([Y^1_o, Y^2_o, Y^3_o, . . . , Y^j_o])    (12)

where DwConv(·) represents the depthwise separable convolutional layer.

[NOTE: Eqs. (11)–(12) were fragmented across column breaks ("1, Yj 2, Yj 3, Yj 4 ... o = F3×3 4 (11) ..."); reassembled per the described per-channel group extraction and shared 4-channel convolution.]

#### D. Hierarchical Feature Aggregation Module

In the decoding stage, the traditional UNet [7] typically uses simple concatenation and de-convolution operations to integrate deep semantic information with shallow local features. However, this fusion strategy has limitations in terms of modeling mutual relationships between global semantics and local details. Therefore, we propose a Hierarchical Feature Aggregation Module (HFAM), as shown in Fig. 5.

> Fig. 5. Hierarchical Feature Aggregation Module.

In HFAM, deep semantic features and shallow spatial details are first aligned in spatial dimensions, and then concatenated during the initial stage to achieve basic-level fusion. Subsequently, we apply a convolution followed by a Sigmoid activation to the basically fused features to generate adaptive fusion coefficients. Positive and inverse weights are produced to enable dynamic modulation between global semantic information and local detailed features. On this basis, we use element-by-element multiplications to realize the secondary fusion of deep and shallow features for further strengthening the complementary feature information. Finally, a 3×3 depthwise separable convolution is adopted to mitigate feature aliasing effects and improve representation ability. The computation flow of HFAM is described as:

F′_h = Conv_{1×1}(F_h)    (13)

σ = ϕ(Conv_{1×1}([F′_h, F_l]))    (14)

F_o = DwConv(σ · F′_h + (1 − σ) · F_l)    (15)

where Conv_{1×1} denotes a 1×1 convolution used to adjust channels.

[NOTE: Eqs. (13)–(15) were fragmented across column breaks; reassembled per the described gated fusion of deep features F_h and shallow features F_l.]

The hierarchical structure of HFAM is mainly reflected in its multi-level integration of both deep and shallow features, as well as its iterative integration within the decoder architecture. Overall, HFAM explicitly divides the feature fusion process into a "primary guidance stage" and a "fine-grained conditioning stage" to achieve dynamic coordination and adaptive weighting between semantic and detailed information. This design uses channel concatenation and additive operations to provide both channel and spatial information increments for decoding features.

#### E. Loss Function

The smoke segmentation task is a typical pixel-wise binary classification task. In this task, the Binary Cross-Entropy (BCE) is widely adopted as the loss function for models. However, the BCE loss is easy to ignore the global structural information, which limits the improvement of model performance to some extent. Therefore, we introduce the weighted loss of Intersection over Union (ℓ^ω_IoU) and BCE (ℓ^ω_BCE) [48]. The ℓ^ω_IoU loss assigns different weights to each pixel by calculating the differences between central pixels and their boundaries, enabling the network to pay more attention to pixels that are difficult to classify correctly.

The weight (ω) calculation formula is as follows:

ω = 1 + ε · |AP_{31×31}(G) − G|    (16)

where G represents the ground truth. AP_{31×31}(·) represents average pooling with a kernel size of 31×31 to compute the mean of local regions for labels. The parameter ε with a default value of 5 is used to control the degree of weight enhancement for boundary regions. The addition of 1 is to prevent the weights in certain regions from approaching zero.

The ℓ^ω_BCE loss function is defined as:

ℓ^ω_BCE = − Σ_{h=1}^{H} Σ_{w=1}^{W} ω · [G · log(P) + (1 − G) · log(1 − P)]    (17)

where P is the predicted map.

The ℓ^ω_IoU loss function is defined as:

ℓ^ω_IoU = 1 − ( Σ_{h=1}^{H} Σ_{w=1}^{W} ω · P · G ) / ( Σ_{h=1}^{H} Σ_{w=1}^{W} [ω · (P + G) − ω · P · G] )    (18)

The final loss function is expressed as:

ℓ_total = α · ℓ^ω_BCE + β · ℓ^ω_IoU    (19)

where α and β control the relative weights of the two losses, and their default values is set to 1.

## Results

### IV. Experiments and Results

#### A. Experimental Datasets

The dynamic characteristics of smoke, including its varying shapes and indistinct boundaries, make pixel-level accurate annotation of real smoke images extremely challenging. To address this issue, the synthetic smoke dataset SYN70K [12] was introduced and has been widely used in [14], [15], [16], and [17]. SYN70K consists of approximately 70,000 images, each with a resolution of 256×256 pixels. We divide these images into training and validation sets in an 8:2 ratio. The test set includes the DS01, DS02, and DS03 subsets of SYN70K, totaling 3,000 images. We combined DS01, DS02, and DS03 for consistent evaluation into a unified SSS test set.

SMOKE5K [25] is a mixed smoke dataset comprising 5,400 images, which include 4,000 synthetic smoke images obtained from SYN70K and 1,400 real-world smoke images. Among them, 5,000 images are designated for training, while 400 images are reserved for testing. The real smoke images in this dataset face several challenges, such as sparse smoke, small targets, and similar backgrounds, which make the smoke segmentation task particularly difficult. In the examples shown in Fig. 6, we have highlighted the smoke regions with red boxes. To ensure consistency in processing, we resize each image to 480×480 pixel.

> Fig. 6. Smoke examples. (a) Synthetic smoke images. (b) Real smoke images.

#### B. Experimental Settings

All training, validation, and testing experiments were conducted on a system equipped with a single NVIDIA 2080Ti GPU, and under the PyTorch [49] framework. During the training process, we employed the standard AdamW optimizer and adopted the CosineAnnealingLR [50] scheduler to adjust the learning rate, and used a maximum of 50 iterations and a minimum learning rate 1e-5.

For the SYN70K dataset, the initial learning rate and the batch size were set to 2e-3 and 32, respectively. The model was trained for 50 epochs. For the SMOKE5K dataset, the initial learning rate and the batch size were set to 1e-3 and 6, respectively. The model was trained for 100 epochs.

#### C. Evaluation Metrics

To evaluate the proposed method's performance, we selected Intersection over Union (IoU) as the primary metric for segmentation accuracy. We measured the overall performance of the model by calculating the mean IoU (mIoU) over the test dataset. Additionally, we conducted a comparative analysis of the parameter numbers for each model and compared their Floating Point Operations (FLOPs) to assess computational complexity.

For the SMOKE5K dataset, we adopted the same performance metrics [15] and [25], including Mean Square Error (MSE) and F-Measure (Fβ), to ensure the consistency and comparability. The MSE calculates the average of the squared differences between predicted values and true labels. The formula for calculating MSE is as follows:

MSE = (1/N) Σ_{i=0}^{N−1} (y_i − ŷ_i)^2    (20)

where y_i represents the ground truth, ŷ_i represents the predicted value, and N is the total number of pixels. In practical testing, we calculate the average of MSE for all test data to obtain the mean Mean-square error (mMse). The mMse reflects the model's overall performance.

The Fβ serves as a supplementary metric to the mMse, and it is the mean of precision and recall for effectively balancing the evaluation of both accuracy and recall.

#### D. Ablation Experiments

We conducted ablation experiments on the SSS test set of SYN70K, with the input image resolution set to 256×256 pixels for FLOPs evaluation.

To explore the impact of the channel dimension on model performance, we constructed five models of different scales by adjusting the channel width: FSIHAN-Tiny (T), FSIHAN-Small (S), FSIHAN-Base (B), FSIHAN-Middle (M), and FSIHAN-Large (L). These experiments systematically analyze the specific impact of different architectural scales on task performance. The related experimental results are presented in TABLE I.

> TABLE I. Performance under different channel configurations. [NOTE: table contents not present in extracted text.]

According to the results presented in TABLE I, an increase in channel dimension leads to a significant rise in both the number of parameters and FLOPs. While the performance metric (mIoU) also improves accordingly, the increasing gains are relatively modest. Based on this observation, we focus our analysis on the performance of FSIHAN-T, FSIHAN-B, and FSIHAN-L variants. FSIHAN-T contains 0.12M parameters and requires 0.11G FLOPs, and it achieves a mIoU of 76.62%. With the smallest number of channels and parameters, FSIHAN-T offers high computational efficiency, making it suitable for resource-constrained devices. FSIHAN-B, with 0.46M parameters and 0.39G FLOPs, achieves an improved mIoU of 78.58%. Compared to the Tiny variant, the Base model significantly enhances performance by increasing channel width, and this demonstrates the effectiveness of channel expansion. FSIHAN-L reaches the highest performance with 1.77M parameters, 1.46G FLOPs, and a mIoU of 79.38%, indicating further gains from broader channel configurations.

In summary, FSIHAN-T represents a lightweight setup focused on efficiency, FSIHAN-B serves as the balanced baseline with a trade-off between accuracy and complexity, and FSIHAN-L corresponds to the full-scale configuration for offering optimal performance when computational resources are sufficient.

To accelerate experimental validation, we selected an encoder configuration with channel combinations {16, 32, 64, 128} as the baseline model, which was subsequently used for ablation studies. To validate the effectiveness of the network constructed with Frequency-Space Interaction Block (FSIB), Group Multi-Dilated Fusion (GMDF) and Hierarchical Feature Aggregation Module (HFAM), we progressively added the proposed modules to the baseline model, resulting in six variant models. The experimental setups and results are detailed in TABLE II.

> TABLE II. Segmentation performance of different components on the SSS test set. [NOTE: table contents not present in extracted text.]

According to the experimental results in TABLE II, the baseline model achieves a mIoU of 76.41% with only 0.378M parameters and 0.316 GFLOPs, effectively demonstrating the efficacy of FSIB in smoke feature extraction while maintaining a low-complexity encoder design. As GMDF and HFAM modules are progressively introduced, the model's segmentation performance significantly improves. These results indicate that each module contributes positively to performance enhancement, validating the effectiveness of our model design. On the other hand, from the baseline model to Variant 6, mIoU steadily increases from 76.41% to 78.58%. Although the number of modules leads to a slight increase in computational complexity and parameters, the performance improvement far outweighs the additional computational cost, making it negligible. Therefore, the model effectively balances computational complexity and segmentation performance.

To further investigate the specific contributions of the proposed modules, particularly in terms of the model's attention regions and feature extraction, we conducted a heatmap analysis of the results from each variant. The heatmaps in Fig. 7 illustrate the differences in the model's attention when processing the same input. For instance, in the second image of Fig. 7, the baseline model successfully extracts smoke features and localizes them well, due to FSIB. However, the heatmap indicates that the model overly focuses on the wheel region, resulting in mis-segmentation. After incorporating GMDF, this issue is mitigated by expanding the receptive field of features by the multi-dilated structure. Further improvements are observed with the addition of HFAM. The mis-segmentation in the wheel area is reduced, and the heat intensity significantly decreases. Ultimately, as we stack additional layers of HFAM, the mis-segmentation in the wheel region is satisfactorily resolved.

> Fig. 7. Heat map visualizations of some samples in the SSS test sets. (a) Images; outputs of (b) Variant 1, (c) Variant 2, (d) Variant 3, (e) Variant 4, (f) Variant 5, and (g) Variant 6.

To verify the effectiveness of the GMDF module, we conducted comparative experiments with ASPP in terms of parameters, computational complexity, and segmentation performance. The experimental results are shown in TABLE III.

> TABLE III. Ablation study of ASPP and GMDF. [NOTE: table contents not present in extracted text.]

The results demonstrate that GMDF outperforms ASPP in several aspects: the GMDF's parameters are reduced by 50%, effectively lowering memory consumption; computational complexity is decreased by 0.13 GFLOPs, significantly improving the model's computational efficiency; and mIoU is increased by 0.46%, indicating that GMDF has a clear advantage in fine-grained feature extraction and segmentation accuracy.

#### E. Comparisons With State-of-the-Art Methods

In the subsequent comparative experiments, we selected three representative models from the FSIHAN family (FSIHAN-T, FSIHAN-B, and FSIHAN-L) to evaluate their performance against current SOTA methods. The selection of models is mainly based on two considerations. The first one is to ensure the conciseness of tables and highlighting key comparative results. The second one is to evaluate models of different scales to comprehensively validate the adaptability and effectiveness of the proposed method under various computational resource constraints.

To fully evaluate the proposed method, we conducted systematic comparisons between our model and several mainstream lightweight approaches on two widely adopted benchmark datasets for smoke segmentation, including SYN70K and SMOKE5K. The compared methods include UNet [7], BiseNetV2 [38], MALUNet [39], LPS-Net [40], SwiftFormer [41], PIDNet [51], and ULite [52].

To ensure the fairness and comparability of results, we conducted reproducibility experiments on mainstream lightweight models under the same experimental environment. All models were trained from scratch on the SYN70K and SMOKE5K datasets, with strict consistency in parameter settings and training procedures. The input resolution is 256×256 for SYN70K and 480×480 for SMOKE5K to test FOLPs. TABLE IV presents the quantitative analysis of results by different lightweight models.

> TABLE IV. Segmentation results of different lightweight method. [NOTE: table contents not present in extracted text.]

Based on the experimental results presented in TABLE IV, the proposed method demonstrates optimal performance. We performed a detailed comparative analysis on the SYN70K dataset. As a classic encoder-decoder architecture, UNet performs well in segmentation tasks. However, UNet has high computational complexity with 13.68G FLOPs. In contrast, FSIHAN-T, an extremely lightweight model, has a computational complexity of only 0.11G, which is approximately 1/124 of UNet's FLOPs, and the mIoU of FSIHAN-T is 76.62% that is 0.03% higher than that of UNet. This substantial reduction in computational overhead makes FSIHAN-T an efficient solution for real-time or resource-constrained environments. The segmentation performance of FSIHAN-B is comparable to that of PIDNet, but the former has significantly reduced parameters and FLOPs compared to the latter. As for FSIHAN-L with only 1.77M parameters, it is much smaller than most other models (except for ULite). FSIHAN-L achieves a mIoU of 79.38%, making it suitable for high-precision application scenarios. Its performance on the SMOKE5K dataset is similar to that on SYN70K, validating the consistency of our proposed model across different datasets. These experimental results highlight the advantages of our method in optimizing segmentation performance and resource consumption, making it an ideal choice for real-time segmentation tasks in resource-constrained environments.

In addition, to further validate the quantitative analysis presented in TABLE IV, we conducted a qualitative evaluation of the performance of different segmentation methods on the SYN70K and SMOKE5K datasets. We selected representative samples for visual demonstration, as shown in Fig. 8 and Fig. 9.

> Fig. 8. Visualization comparisons with different lightweight methods on SYN70K dataset. The green and red curves represent the ground truth and prediction mask, respectively.

> Fig. 9. Visualization comparison with different lightweight methods on SMOKE5K dataset.

In the visual comparison, we chose FSIHAN-B for our analysis. To facilitate intuitive comparison, we used red curves to mark the regions of predicted segmentation and green ones to denote the ground truth. This approach allows for a clear evaluation of the model's segmentation performance. Compared to the other seven methods, our approach demonstrates the best segmentation results on synthetic smoke images, with the predicted contours closely matching the ground truth. For instance, in the second image of Fig. 8, the appearance of smoke and background objects are highly similar. Although other methods can identify and locate the smoke region, they exhibit significant over-segmentation. In contrast, our method delineates the shape of smoke and effectively avoids mis-segmentation, showcasing higher accuracy.

Fig. 9 demonstrates the segmentation results on the SMOKE5K dataset, where we conduct a qualitative analysis on the more challenging real images. Consistent with its performance on synthetic images, FSIHAN-B further exhibits significant advantages on real images. In addition to achieving better localization accuracy and boundary details, FSIHAN-B also delivers more impressive results in tasks involving distant and small smoke. As shown in the third and fourth images in Fig. 9, even in the presence of complex background interference, our model can accurately segment the smoke, including details that are difficult for the human eye to distinguish.

On the other hand, we conducted a comparative analysis of our model against the current SOTA smoke segmentation models on the SYN70K and SMOKE5K datasets. These models include DSS [12], W-Net [13], Frizzi [14], TANet [53], LSSNet [45], SmokeSeger [16], FoSp [15], SAGINN [17], MIFNet [27], and Trans-BVM [25], most of which have large parameter sizes and complex network architectures.

To ensure the optimal performance of compared methods, the segmentation results are from their original papers, as shown in TABLE V and TABLE VI. It is particularly important to note that the segmentation results in TABLE V represent the average mIoU score across the three test sets, DS01, DS02, and DS03, i.e., (mIoU_DS01 + mIoU_DS02 + mIoU_DS03)/3.

> TABLE V. Results on SYN70K with different smoke segmentation method. [NOTE: table contents not present in extracted text.]

TABLE V indicates that the FSIHAN variants demonstrate significant competitive advantages over current SOTA smoke segmentation methods in terms of both parameter efficiency and segmentation performance. Specifically, FSIHAN-T, the most lightweight variant in the FSIHAN family, achieves a segmentation accuracy of 76.6% with only 0.12M parameters. Compared to SmokeSeger, FSIHAN-T not only achieves higher segmentation accuracy but also utilizes over 280 times fewer parameters, demonstrating exceptional efficiency under extreme resource constraints. FSIHAN-B further improves performance, i.e., achieving 78.6% mIoU with just 0.46M parameters.

LSSNet, a lightweight smoke segmentation model, achieves a mIoU of only 73.2% while utilizing 0.88M parameters. These results indicate that FSIHAN-B outperforms LSSNet in segmentation accuracy and model compactness, underscoring the effectiveness of our architectural design. FSIHAN-L, the largest model in the FSIHAN series, obtains a 79.4% mIoU with only 1.77M parameters. FSIHAN-L performs competitively with SAGINN*, which achieves a 79.9% mIoU without classification assistance but relies on a heavy ResNeXt 101 [56] backbone. Compared to SAGINN (101.1M parameters), FSIHAN-L achieves comparable performance with approximately 57x fewer parameters. Moreover, compared to other recent high-performing models, such as FoSp and MIFNet, FSIHAN-L still exhibits clear advantages in parameters. FoSp achieves an 82.5% mIoU but requires 47.5M parameters, while MIFNet achieves an 81.6% mIoU with 24.6M. Although these models slightly outperform FSIHAN-L in accuracy, their parameters are 13x to 27x larger.

We conducted a comparative evaluation of existing state-of-the-art models for smoke segmentation, including methods such as Trans-BVM, FoSp, and SAGINN. Detailed quantitative results are shown in TABLE VI.

> TABLE VI. Segmentation results on the test set of SMOKE5K. [NOTE: table contents not present in extracted text.]

Compared to FoSp, FSIHAN-L reduces the number of parameters approximately 27x, while only showing a marginal difference of 0.001 in mMse and 0.002 in Fβ. Overall, our model significantly reduces the parameters, and maintains the accuracy nearly identical to FoSp. Our FSIHAN-L overtakes SAGINN in Fβ metric. These results demonstrate that FSIHAN-L achieves performance comparable to SOTA methods while maintaining high efficiency.

#### F. Experimental Results in Real-World Scenarios

To address the complex variations across different real-world scenarios, we collected three types of smoke videos: dense smoke, diffuse smoke, and translucent smoke. We provided the test results of several existing lightweight models, including UNet [7], BiseNetV2 [38], MALUNet [39], LPS-Net [40], and PIDNet [51], as well as the proposed FSIHAN-B.

As illustrated in Fig. 10, our proposed method achieves the best overall performance in smoke segmentation across three different types of test videos. In scenarios involving dense smoke, most models produce satisfactory segmentation results. However, when these models process diffused and semi-transparent smoke, the results are less than satisfactory. Although BiseNetV2, PIDNet, and our FSIHAN model demonstrate comparable performance, FSIHAN exhibits superior capability in capturing fine-grained edge details, significantly outperforming other methods. In addition, we find that pure white smoke (as illustrated in the second and third rows) poses a significant challenge to most models.

> Fig. 10. Visual segmentation results of different lightweight models on three types of real-world smoke videos.

To evaluate the real-time inference performance in realistic smoke video scenarios, we selected the first 100 frames from a video. We measured the total inference time and the number of frames per second (FPS). All input frames were resized to a resolution of 480×480.

> TABLE VII. Real-time performance evaluation on real smoke video. [NOTE: table contents not present in extracted text.]

Based on TABLE VII, the proposed FSIHAN variants demonstrate significant compactness advantages in terms of parameter count and model size. Specifically, the lightweight FSIHAN-T contains only 0.12M parameters and requires only 0.60 MB of storage, which is substantially smaller than all baseline models, highlighting its large advantage in model size and resource consumption. Combined with the quantitative analysis results on the SYN70K and SMOKE5K datasets in TABLE IV, the FSIHAN models achieve a good trade-off between segmentation accuracy and resource usage.

In particular, FSIHAN-T, the smallest model, achieves 54.1 FPS, so it sufficiently meets the demands of most real-time applications, although it is still slower than LPS-Net (97.1 FPS) and BiseNetV2 (82.1 FPS). As the model size increases, FSIHAN-B and FSIHAN-L show further improvements in segmentation accuracy, but the inference latency also increases, reaching 24.4 ms (41.0 FPS) and 33.8 ms (29.6 FPS), respectively.

## Conclusion

### V. Conclusion

Semantic segmentation has increasingly become the preferred technique for smoke detection. However, existing smoke segmentation models often suffer from high complexity and limited representational capacity. Therefore, developing an efficient and lightweight smoke segmentation framework is crucial for computation-limited devices. In response to this challenge, we propose a lightweight smoke segmentation method called FSIHAN. This approach introduces the Frequency-Space Interaction Module (FSIM) to facilitate efficient cross-domain feature fusion. The FSIM is integrated into the FSIB block along with a Multi-Layer Perceptron (MLP) to enhance the extraction of smoke-related features.

Additionally, during the transition from encoding to decoding, we introduce the Group Multi-Dilated Fusion (GMDF) module, which improves the efficiency of feature information propagation and fusion. In the decoding stage, we employ the Hierarchical Feature Aggregation Module (HFAM) module to enable fine-grained decoding across successive layers. Experimental results demonstrate that FSIHAN outperforms current state-of-the-art semantic segmentation algorithms on the SYN70K, SMOKE5K, and various real-world smoke image tests.

The FSIHAN models achieve a good balance between model size and segmentation performance, and particularly excel in edge detail preservation and complex smoke scenarios. However, our method remains a limitation of processing speed. In future work, we explore methods to further reduce computational latency, which is an ongoing challenge that needs to be addressed.

## References

[NOTE: References [3]–[56] were printed in two interleaved columns and further interleaved with body text (real-time performance paragraphs) in the source; each entry below has been reassembled from its split fragments.]

1. [1] K. Muhammad, J. Ahmad, and S. W. Baik, "Early fire detection using convolutional neural networks during surveillance for effective disaster management," Neurocomputing, vol. 288, pp. 30–42, May 2018.
2. [2] K. Muhammad, J. Ahmad, Z. Lv, P. Bellavista, P. Yang, and S. W. Baik, "Efficient deep CNN-based fire detection and localization in video surveillance applications," IEEE Trans. Syst., Man, Cybern., Syst., vol. 49, no. 7, pp. 1419–1434, Jul. 2019.
3. [3] S.-J. Chen, D. C. Hovde, K. A. Peterson, and A. W. Marshall, "Fire detection using smoke and gas sensors," Fire Saf. J., vol. 42, no. 8, pp. 507–515, 2007.
4. [4] A. Garg, S. Nath, and P. Nagrath, "Smoke detection in digital frames," Int. Res. J. Eng. Technol., vol. 5, no. 4, pp. 3843–3846, 2018.
5. [5] W. Ye, J. Zhao, S. Wang, Y. Wang, D. Zhang, and Z. Yuan, "Dynamic texture based smoke detection using surfacelet transform and HMT model," Fire Safety J., vol. 73, pp. 91–101, Apr. 2015.
6. [6] E. Shelhamer, J. Long, and T. Darrell, "Fully convolutional networks for semantic segmentation," IEEE Trans. Pattern Anal. Mach. Intell., vol. 39, no. 4, pp. 640–651, Apr. 2017.
7. [7] O. Ronneberger, P. Fischer, and T. Brox, "U-Net: Convolutional networks for biomedical image segmentation," in Proc. Int. Conf. Med. Image Comput. Comput.-Assist. Intervention, pp. 234–241, 2015.
8. [8] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille, "DeepLab: Semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected CRFs," IEEE Trans. Pattern Anal. Mach. Intell., vol. 40, no. 4, pp. 834–848, Apr. 2018.
9. [9] Z. Liu et al., "Swin transformer: Hierarchical vision transformer using shifted windows," Proc. IEEE Int. Conf. Comput. Vis., 2021, pp. 10012–10022.
10. [10] Y. Luo, L. Zhao, P. Liu, and D. Huang, "Fire smoke detection algorithm based on motion characteristic and convolutional neural networks," Multimedia Tools Appl., vol. 77, pp. 15075–15092, Jun. 2018.
11. [11] M. Yin, C. Lang, Z. Li, S. Feng, and T. Wang, "Recurrent convolutional network for video-based smoke detection," Multimedia Tools Appl., vol. 78, pp. 237–256, Jan. 2019.
12. [12] F. Yuan, L. Zhang, X. Xia, B. Wan, Q. Huang, and X. Li, "Deep smoke segmentation," Neurocomputing, vol. 357, pp. 248–260, Sep. 2019.
13. [13] F. Yuan, L. Zhang, X. Xia, Q. Huang, and X. Li, "A wave-shaped deep neural network for smoke density estimation," IEEE Trans. Image Process., vol. 29, pp. 2301–2313, 2020.
14. [14] S. Frizzi, M. Bouchouicha, G. Jean-Marc, E. Moreau, and M. Sayadi, "Convolutional neural network for smoke and fire semantic segmentation," IET Image Process., vol. 15, no. 6, pp. 634–647, 2021.
15. [15] L. Yao, H. Zhao, J. Peng, Z. Wang, and K. Zhao, "FoSp: Focus and separation network for early smoke segmentation," in Proc. AAAI Conf. Artif. Intell., vol. 38, 2024, pp. 6621–6629.
16. [16] T. Jing, Q. Meng, and H. Hou, "SmokeSeger: A transformer-CNN coupled model for urban scene smoke segmentation," IEEE Trans. Ind. Informat., vol. 20, no. 2, pp. 1385–1396, Feb. 2024.
17. [17] L. Zhang, J. Wu, F. Yuan, and Y. Fang, "Smoke-aware global-interactive non-local network for smoke semantic segmentation," IEEE Trans. Image Process., vol. 33, pp. 1175–1187, 2024.
18. [18] D. Xing, Y. Zhongming, W. Lin, and L. Jinlan, "Smoke image segmentation based on color model," J. Innov. Sustain. RISUS, vol. 6, no. 2, pp. 130–138, 2015.
19. [19] S. Wang, Y. He, J. Zou, D. Zhou, and J. Wang, "Early smoke detection in video using swaying and diffusion feature," J. Intell. Fuzzy Syst., vol. 26, no. 1, pp. 267–275, 2014.
20. [20] M. Adam, I. Mahmoud, and H. Ren, "Forest fire detection and identification using image processing and SVM," J. Inf. Process. Syst., vol. 15, no. 1, pp. 159–168, 2019.
21. [21] H. Tian, W. Li, P. O. Ogunbona, and L. Wang, "Detection and separation of smoke from single image frames," IEEE Trans. Image Process., vol. 27, no. 3, pp. 1164–1177, Mar. 2018.
22. [22] L. Chen, Y. Zhu, G. Papandreou, F. Schroff, and H. Adam, "Encoder-decoder with atrous separable convolution for semantic image segmentation," in Proc. Eur. Conf. Comput. Vis. (ECCV), 2018, pp. 801–818.
23. [23] S. Khan et al., "DeepSmoke: Deep learning model for smoke detection and segmentation in outdoor environments," Expert Syst. Appl., vol. 182, Nov. 2021, Art. no. 115125.
24. [24] M. Tan and Q. Le, "EfficientNet: Rethinking model scaling for convolutional neural networks," in Proc. Int. Conf. Mach. Learn., 2019, pp. 10578–11247. [NOTE: page range as printed in source.]
25. [25] S. Yan, J. Zhang, and N. Barnes, "Transmission-guided Bayesian generative model for smoke segmentation," in Proc. Assoc. Adv. Artif. Intell., 2022, pp. 1–9.
26. [26] T. Wang et al., "AOSVSSNet: Attention-guided optical satellite video smoke segmentation network," IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens., vol. 15, pp. 8552–8566, 2022.
27. [27] K. Li, F. Yuan, C. Wang, "An effective multi-scale interactive fusion network with hybrid Transformer and CNN for smoke image segmentation," Pattern Recognit., vol. 159, 2025, Art. no. 111177.
28. [28] J. Liu, J. Li, S. Peters, and L. Zhao, "A transformer boosted UNet for smoke segmentation in complex backgrounds in multispectral LandSat imagery," Remote Sens. Appl. Soc. Environ., vol. 36, Nov. 2024, Art. no. 101283.
29. [29] Z. Qin, P. Zhang, F. Wu, and X. Li, "FCANet: Frequency channel attention networks," in Proc. IEEE Int. Conf. Comput. Vis., 2021, pp. 783–792.
30. [30] G. Yun, J. Yoo, K. Kim, J. Lee, and D. Kim, "SPANet: Frequency-balancing token mixer using spectral pooling aggregation modulation," in Proc. IEEE Int. Conf. Comput. Vis., 2023, pp. 6113–6124.
31. [31] S. Wang, R. Veldhuis, C. Brune, and N. Strisciuglio, "What do neural networks learn in image classification? A frequency shortcut perspective," in Proc. IEEE Int. Conf. Comput. Vis., 2023, pp. 1433–1442.
32. [32] Z. Zhou, A. He, Y. Wu, R. Yao, X. Xie, and T. Li, "Spatial-frequency dual domain attention network for medical image segmentation," in Proc. IEEE Int. Conf. Bioinform. Biomed. (BIBM), 2024, pp. 4076–4081.
33. [33] Y. Sun, C. Xu, J. Yang, H. Xuan, and L. Luo, "Frequency-spatial entanglement learning for camouflaged object detection," in Proc. IEEE Int. Conf. Comput. Vis., 2025, pp. 343–360.
34. [34] V. Badrinarayanan, A. Kendall, and R. Cipolla, "SegNet: A deep convolutional encoder-decoder architecture for image segmentation," IEEE Trans. Pattern Anal. Mach. Intell., vol. 39, no. 12, pp. 2481–2495, Dec. 2017.
35. [35] A. Paszke, A. Chaurasia, S. Kim, and E. Culurciello, "ENet: A deep neural network architecture for real-time semantic segmentation," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016, pp. 1–10.
36. [36] A. Howard et al., "MobileNets: Efficient convolutional neural networks for Mobile vision applications," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), 2017, pp. 1–9.
37. [37] C. Yu, J. Wang, C. Peng, C. X. Gao, G. Yu, and N. Sang, "BiSeNet: Bilateral segmentation network for real-time semantic segmentation," in Proc. Eur. Conf. Comput. Vis., 2018, pp. 1–17.
38. [38] C. Yu, C. Gao, J. Wang, G. Yu, C. Shen, and N. Sang, "BiSeNet V2: Bilateral network with guided aggregation for real-time semantic segmentation," Int. J. Comput. Vis., vol. 129, pp. 3051–3068, Sep. 2021.
39. [39] J. Ruan, S. Xiang, M. Xie, T. Liu, and Y. Fu, "MALUNet: A multi-attention and light-weight UNet for skin lesion segmentation," in Proc. IEEE Int. Conf. Bioinform. Biomed., 2022, pp. 1150–1156.
40. [40] Y. Zhang, T. Yao, Z. Qiu, and T. Mei, "Lightweight and progressively-scalable networks for semantic segmentation," Int. J. Comput. Vis., vol. 131, pp. 2153–2171, May 2023.
41. [41] A. Shaker, M. Maaz, H. Rasheed, S. Khan, M. Yang, and F. Khan, "SwiftFormer: Efficient additive attention for Transformer-based realtime mobile vision applications," in Proc. IEEE Int. Conf. Comput. Vis., 2023, pp. 17379–17390.
42. [42] K. Muhammad, S. Khan, V. Palade, I. Mehmood, and V. H. C. de Albuquerque, "Edge intelligence-assisted smoke detection in foggy surveillance environments," IEEE Trans. Ind. Informat., vol. 16, no. 2, pp. 1067–1075, Feb. 2020.
43. [43] Y. Li, W. Zhang, Y. Liu, and X. Shao, "A lightweight network for real-time smoke semantic segmentation based on dual paths," Neurocomputing, vol. 501, pp. 258–269, Aug. 2022.
44. [44] J. S. Almeida, C. Huang, F. G. Nogueira, S. Bhatia, and V. H. C. de Albuquerque, "EdgeFireSmoke: A novel lightweight CNN model for real-time video fire-smoke detection," IEEE Trans. Ind. Informat., vol. 18, no. 11, pp. 7889–7898, Nov. 2022.
45. [45] F. Yuan, K. Li, C. Wang, and Z. Fang, "A lightweight network for smoke semantic segmentation," Pattern Recognit., vol. 137, May 2023, Art. no. 109289.
46. [46] F. M. A. Hossain and Y. Zhang, "MsFireD-Net: A lightweight and efficient convolutional neural network for flame and smoke segmentation," J. Autom. Intell., vol. 2, no. 3, pp. 130–138, 2023.
47. [47] A. Dosovitskiy et al., "An image is worth 16x16 words: Transformers for image recognition at scale," in Proc. Int. Conf. Learn. Reinforcement, 2021, pp. 1–22. [NOTE: venue name as printed in source; presumably Int. Conf. Learn. Represent. (ICLR).]
48. [48] J. Wei, S. H. Wang, and Q. M. Huang, "F3Net: Fusion, feedback and focus for salient object detection," in Proc. Assoc. Adv. Artif. Intell., 2020, pp. 1–8.
49. [49] A. Paszke et al., "PyTorch: An imperative style, high-performance deep learning library," in Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019, pp. 1–12.
50. [50] I. Loshchilov and F. Hutter, "Decoupled weight decay regularization," in Proc. Int. Conf. Learning Represent., 2018, pp. 1–19.
51. [51] J. Xu, Z. Xiong, and S. P. Bhattacharyya, "PIDNet: A real-time semantic segmentation network inspired by PID controllers," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), 2023, pp. 19529–19539.
52. [52] B. Dinh, T. Nguyen, T. Tran, and V. Pham, "1M parameters are enough? A lightweight CNN-based model for medical image segmentation," in Proc. Asia Pacific Signal Inf. Process. Assoc. Annu. Summit Conf., 2023, pp. 1279–1284.
53. [53] X. Xia, K. Zhan, Y. Peng, and Y. Fang, "Texture-aware network for smoke density estimation," Proc. IEEE Int. Conf. Visual Commun. Image Process., Suzhou, China, 2022, pp. 1–5.
54. [54] K. Simonyan and A. Zisserman, "Very deep convolutional networks for large-scale image recognition," in Proc. Int. Conf. Learn. Represent. (ICLR), 2015, pp. 1–21.
55. [55] E. Xie, W. Wang, Z. Yu, A. Anandkumar, J. Alvarez, and P. Luo, "SegFormer: Simple and efficient design for semantic segmentation with transformers," in Proc. Adv. Neural Inf. Process. Syst. (NIPS), vol. 34, 2021, pp. 12077–12090.
56. [56] S. Xie, R. Girshick, P. Dollár, Z. Tu, and K. He, "Aggregated residual transformations for deep neural networks," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017, pp. 5987–5995.

## Other

### Author Affiliations (first-page footnote)

Kang Li is with the College of Mathematics and Science, Shanghai Normal University, Shanghai 200234, China (e-mail: 1647872686@qq.com).

[NOTE: only Kang Li's affiliation footnote survived in the extracted text; footnotes for the other authors were not present. The source also contained a duplicated copy of the first Introduction paragraph glued to this footnote (first-page header/footer artifact), which was removed.]
