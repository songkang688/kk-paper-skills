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
