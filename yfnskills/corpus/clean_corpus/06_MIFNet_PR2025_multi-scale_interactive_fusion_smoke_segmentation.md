# 06_MIFNet_PR2025_multi-scale_interactive_fusion_smoke_segmentation — Clean English Corpus

<!-- Stage 00 Wave 3 Agent H. English **Original:** blocks only; no Chinese content.
     Source: /workspace/06_MIFNet_PR2025_multi-scale_interactive_fusion_smoke_segmentation.md (bilingual reader).
     Anchors in comments (SXXX/CXXX) refer to reader block ids.
     Authorship context (do not re-derive): Tier A3, weight 0.75; CRediT: Kang Li wrote original draft, Yuan review & editing — body prose is NOT Yuan first-draft prose.
     Table numeric rows (S067, S068, S075, S083, S084, S085, S089, S090, S095) excluded as non-prose table debris. -->

## Title

<!-- src: S001, S003, S005, S002 -->
An effective multi-scale interactive fusion network with hybrid Transformer and CNN for smoke image segmentation

Kang Li (a), Feiniu Yuan (b,a,*), Chunmei Wang (b)

(a) College of Mathematics and Science, Shanghai Normal University, Shanghai, 200234, China. (b) College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, Shanghai 201418, China.

Pattern Recognition 159 (2025) 111177. DOI: 10.1016/j.patcog.2024.111177

## Abstract

<!-- src: S006 -->
Smoke has visually elusive appearances, especially in low-light conditions, so it is quite difficult to quickly and accurately detect smoke from images. To address these challenges, we design a dual-encoder structure of Transformer and Convolutional Neural Network (CNN) to propose an effective Multi-scale Interactive Fusion Network (MIFNet) for smoke image segmentation. To improve the presentation of features, we propose a Local Feature Enhancement Propagation (LFEP) module to enhance spatial details. To optimize global and local features for efficient fusion, we integrate LFEP into the original Transformer to replace the traditional multi-head self-attention mechanism. Then, we propose a Multi-level Attention Coupled Module (MACM) to fuse Transformer and CNN features of the dual-encoder. MACM can flexibly focus on information interaction between different levels of two encoding paths. Finally, we design a Prior-guided Multi-scale Fusion Decoder (PMFD), which combines prior knowledge with a multi-scale feature fusion strategy to improve the performance of segmentation. Experimental results demonstrate that MIFNet substantially outperforms the state-of-the-art methods. MIFNet achieves a mean Intersection over Union (mIoU) of 81.6 % on the synthetic smoke (SYN70K) dataset, and a remarkable accuracy of 98.3 % on the forest smoke dataset.

## Introduction

<!-- original heading: "1. Introduction" (S008) -->

<!-- src: S009 -->
Smoke detection and segmentation is an important research area in computer vision and image processing, with applications in fire safety, industrial automation, and surveillance [1]. Smoke is often the first visible sign of a fire or gas leak, and if not detected early, can lead to catastrophic consequences. Therefore, the ability to accurately segment smoke from the surrounding environment is crucial, especially as video surveillance systems become increasingly prevalent in urban and forest areas [2].

<!-- src: S010; dropped dangling column-break fragment "In" at block end -->
Traditional smoke detection methods rely on physical sensors, such as photoelectric smoke detectors and ionization smoke detectors, which detect smoke particles through changes in light intensity or current. These systems are effective for early smoke detection, but have limited ability to provide detailed information about the distribution and concentration of smoke. However, these methods may also be limited by the range of the sensors and are generally ineffective in large open environments. On the other hand, due to factors such as lighting conditions, background, and type of combustion material, the shape or color of smoke is not deterministic and its appearance can vary greatly.

<!-- src: S011 -->
In addition, smoke is easily confused with fog, clouds, or other similar targets, making it difficult for traditional image segmentation methods to accurately distinguish them. Some classic methods mainly use color spaces [3], such as HSV (hue and saturation), where smoke is usually represented by specific ranges of values in each color channel. By comparing the color histograms of smoke regions and non-smoke regions, these methods can detect the presence of smoke in an image or video frame, but their application scenarios are limited.

<!-- src: S012 -->
Early researchers manually designed visual features of smoke, such as shape and texture, for extraction. However, due to the ever-changing appearance of smoke, relying solely on the designer's experience resulted in unsatisfactory segmentation results. With the advancement of computer vision technology, smoke detection based on deep convolutional neural networks has become a viable alternative. It allows for the analysis of visual data to detect the presence of smoke in a larger range, and can provide additional information such as the volume, direction of spread, and source location of the smoke. These statistics and advanced semantic information about smoke are particularly relevant to firefighting and gas leak response.

<!-- src: S013 -->
Smoke segmentation is one of key applications in semantic segmentation. In recent years, deep learning techniques have widely been adopted in smoke segmentation. From convolutional neural networks (CNN) [4,5] to Transformer models [6–8], end-to-end trained deep segmentation networks have outperformed methods relying on traditional handcrafted features, greatly improving the accuracy of semantic segmentation algorithms. Some CNN-based models have been successfully applied to smoke segmentation tasks and achieved good results on specific smoke datasets [9–12]. To improve semantic segmentation performance, worldwide researchers have increasingly used large models with huge parameters, and also have combined some high computational methods, such as, merging features of different scales [13], embedding features within recurrent neural networks (RNNs), and adding classification auxiliary tasks [12]. SmokeSeger [14] introduces a two-branch concurrent structure of CNNs and Transformers for smoke segmentation. However, this simple addition operation is not sufficient to fully integrate the information of CNN and Transformer.

<!-- src: S014 -->
Considering the above challenges, although CNN-based smoke detection methods have achieved good performance, there are certain segmentation defects in identifying some smoke details or small targets. In addition, achieving higher precision while maintaining low computational complexity is another key challenge in developing smoke detection and segmentation systems. To overcome these challenges, we propose a new multi-scale interactive fusion network based on a hybrid architecture of Transformer and CNN for smoke image segmentation, named MIFNet. By leveraging the advantages of Transformer and CNN, our MIFNet achieves precise segmentations for smoke images. Its Transformer encoder focuses on mining contextual information, which is crucial for understanding the complexity and dynamics of smoke. Its CNN encoder is dedicated to capturing local features, which are indispensable for presenting fine textures in smoke images. Therefore, we propose a Multi-level Attention Coupled Module (MACM) to achieve effective interaction between features of Transformer and CNN encoders. Additionally, we introduce Local Feature Enhancement Propagation (LFEP) to modify the Transformer encoder. LFEP replaces the matrix multiplication operations in traditional multi-head self-attention with addition and subtraction operations between different pooling methods, significantly reducing model complexity and enhancing model performance. In decoding stage, we construct a Prior-guided Multi-scale Fusion Decoder (PMFD). The PMFD utilizes the output maps from different levels of MACM, gradually merging them by upsampling and addition operations. A large number of experiments show that our method achieves state-of-the-art performance on synthetic and real smoke image datasets. The main contributions of this method are summarized as follows:

<!-- src: S015; re-split enumerated contribution list -->
1) We propose a Local Feature Enhancement Propagation (LFEP) to replace the multi-head self-attention for re-constructing the Transformer encoder. The quadratic matrix multiplication of the traditional Transformer is replaced by the linear addition and subtraction between different pooled features, so LFEP can significantly reduce computational complexity.

2) We propose a Multi-level Attention Coupled Module (MACM) to facilitate fusion of features between Transformer and CNN encoders. MACM enhances the model's ability to capture subtle smoke appearances by using deep interaction of cross-domain features at different levels.

3) We propose a Prior-guided Multi-scale Fusion Decoder (PMFD). PMFD gradually utilizes high-level information to generate low-resolution feature maps with more spatial details. Thus we implement gradual integration of low-resolution and high-resolution information for aggregating multi-scale features.

<!-- src: S016; final sentence truncated in extraction (likely "…Section 5 offers conclusions.") -->
The remainder of this paper is organized as follows. Section 2 briefly summarizes the related work on image segmentation. Section 3 provides a detailed introduction to the proposed network. Section 4 describes experimental configuration and analysis results, and Section 5 offers [sentence truncated in extraction].

## RelatedWork

<!-- original heading: "2. Related works" (S017) -->

### Semantic segmentation methods

<!-- original heading: "2.1. Semantic segmentation methods" (S018) -->

<!-- src: S019; fixed stray periods after citation brackets -->
Compared with traditional semantic segmentation methods, deep learning models show significant advantages. This model can learn image features and perform end-to-end classification by itself, which significantly improves the accuracy of semantic segmentation. Chen et al. [15,16] solved the problem of resolution reduction in deep convolutional neural networks by using atrous convolution, and improved the model's ability to capture fine details by using a conditional random field. WideSegNeXt [17] addresses the shortcomings of the fully convolutional network by incorporating NeXt Dilated Units into residual blocks. It can capture multi-scale spatial context information, and effectively recognize small objects. DeepIGeoS [18] proposes an interactive segmentation method based on deep learning to improve the results obtained by automatic CNN and reduce user interaction during refinement for higher accuracy. Qi et al. [19] proposed a remote sensing image segmentation method based on implicit three-dimensional scene representation, which uses limited annotation information to generate segmentation results of arbitrary views. And the method adopts a two-stage training strategy. Kirillov et al. [20] proposed the PointRend neural network module based on point rendering, which performs point-based segmentation prediction at adaptively selected locations based on iterative subdivision. STLNet [21] analyzes the distribution of low-level information and proposes quantization and counting operators to describe texture information.

<!-- src: S020 -->
Vaswani et al. [22] proposed a new sequence-to-sequence model that completely abandons the traditional RNN and CNN architectures, instead using attention mechanisms to process sequential data. Unlike convolution's local operation, self-attention has been proven to capture long-range dependencies. ViT [23] applies the Transformer architecture from natural language processing to computer vision tasks and achieves remarkable results. SETR [8] is the first representative model for semantic segmentation based on ViT, which replaces the CNN encoder with a pure Transformer structure. Subsequently, researchers extended ViT to semantic segmentation, resulting in many excellent models. For example, SegFormer [7] introduces the Transformer encoder to capture long-range dependencies between pixels, and designs a new Transformer-based architecture for image segmentation tasks. SeaFormer [24] uses a squeeze-enhanced axial Transformer to improve accuracy and reduce latency. Swin Transformer [25] combines hierarchical structures and local ideas to enable the model to better handle image features of different scales.

### Smoke segmentation methods

<!-- original heading: "2.2. Smoke segmentation methods" (S021) -->

<!-- src: S022 -->
The technology for smoke detection in video and images based on machine vision has become a core research focus, because it offers advantages, such as rapid response time, strong anti-interference capabilities, and low cost. CNNs can automatically learn hierarchical features from raw pixel values without the need for manual feature selection. Frizzi [26] was the first to use CNN to classify the presence of fire and smoke in the video stream. Subsequently, ARGNet [27] is a smoke detection network based on a recursive feature pyramid with deconvolution, dilated convolution and global optimal non-maximum suppression for high-precision detection of forest fire smoke. However, the localization of fire or smoke areas within these tasks lacks precision, only offering approximate regional features delineated by bounding boxes.

<!-- src: S023 + S024 (merged across p2→p3 page break); fixed "[30]]" and stray periods after brackets -->
With the application of methods based on FCN [4] to semantic segmentation, the accuracy of semantic segmentation algorithms has been greatly improved. AFSNet [28] proposed an adaptive frame selection network to enhance the performance of video smoke detection methods through augmented extended convolution. W-Net [10] designed a waveform architecture with an encoder-decoder structure stack. It is actually a soft segmentation method for smoke. To solve the problem of interference from non-smoke objects, CGRNet [12] combines gated recurrent networks with classification assistance, and uses smoke classification results to adjust and refine smoke segmentation results. Wang et al. [29] introduced a parallel dual attention mechanism network and spatial pyramid pooling to process and fuse feature maps in parallel, and proposed an innovative fire and smoke recognition method. Cao et al. [30] used CNNs to generate feature foreground from intermediate layers for guiding the temporal modeling process of smoke objects. They proposed a feature foreground module to promote the learning of smoke temporal representation. Tao et al. [31] proposed a pixel-level supervised neural network to learn discriminative feature representation for forest smoke recognition. Yuan et al. [32] proposed a lightweight encoder-decoder network based on ResNet-Style architecture for smoke segmentation, and achieve good results. Xia et al. [33] proposed a texture-aware network to capture the internal transparency of smoke components for pixel-wise smoke density estimation. Wen et al. [13] proposed a dense multi-scale context and asymmetric pooling embedding network for smoke segmentation. DeepSmoke [11] used two different networks for smoke detection and segmentation.

### Transformer and CNN combined methods

<!-- original heading: "2.3. Transformer and CNN combined methods" (S025) -->

<!-- src: S026 -->
Transformers have excellent global modeling capabilities, while CNNs are good at modeling local information. Therefore, researchers have empirically improved model performance by combining the advantages of CNN and Transformer. There are two main fusion types that are internal and external. Specifically, internal fusion involves the substitution of certain components of Transformers with CNN layers, and vice versa. For instance, SwiftFormer [34] proposes an additive attention mechanism that replaces the quadratic matrix multiplication in traditional self-attention mechanisms, and achieves key-value interaction replacement through linear element-wise multiplication. ConViT [35] is the first method to apply the inductive bias of CNNs to Transformers, creating a gating position self-attention mechanism. External fusion methods mainly achieve high-performance models by mixing CNNs and Transformers. Conformer [36] employs a dual structure that leverages the advantages of convolutional operations and self-attention mechanisms to maximize the preservation of local details and global dependencies, thereby enhancing representational learning. CoAtNet [37] effectively improves its generalization ability by stacking convolutional and self-attention layers vertically. Yuan et al. [38] proposed a CNN and Transformer Complementary Network (CTC–Net) for medical image segmentation by designing a cross-domain fusion block. SmokeSeger [14] designs a dual-branch smoke segmentation model that combines Transformer and CNN branches to enhance representation of global and local features.

<!-- src: S027 -->
Inspired by the successes of Transformer and CNN combined methods, we propose a new smoke image segmentation network that utilizes a hybrid architecture of Transformers and CNNs. Different from existing methods, we propose a multi-scale interaction strategy for effectively fusing cross-domain features, and design a prior-guided decoder for gradually generating final results. Our method essentially combines both internal and external fusion.

## Methods

<!-- original heading: "3. The proposed method" (S028) -->

### Dual-path encoder

<!-- original heading: "3.1. Dual-path encoder" (S029) -->

<!-- src: S030 + S031 (merged; removed duplicated column-break fragment "To address" at end of S030) -->
In challenging segmentation tasks such as smoke segmentation, due to large-scale distribution, irregular shape changes, and blurred boundaries, there is a lack of excellent feature extraction ability from local features to global long-range dependencies, resulting in inaccurate differentiation between target pixels and background pixels. To address this problem, we design a dual-encoder with Transformer and CNN, as shown in Fig. 1. We first leverage the Local Feature Enhancement Propagation (LFEP) technique to construct the LFE-Former encoder, significantly enhancing the Transformer's local perception capabilities. Subsequently, we utilize the unique advantages of the Multi-level Attention Coupled Module (MACM) to deeply integrate the features from each layer of the LFE-Former and CNN encoders. This process not only obtains a hybrid representation of global and local features, but also successfully captures rich information at four different scales (F4~F1).

#### LFE-Former encoder

<!-- original heading: "3.1.1. LFE-Former encoder" (glued to body in S032; unglued) -->

<!-- src: S032 -->
Traditional Transformer encoders typically generate single-scale feature maps of fixed resolution, which is less efficient in dealing with multi-scale smoke objects. To overcome this limitation, we propose a Local Feature Enhancement Transformer (LFE-Former) for encoding. As shown on the left of Fig. 1, LFE-Former generates multi-scale features with 1/2, 1/4, 1/8, and 1/16 of the input size.

<!-- src: S033 -->
Transformer is good at handling contextual information, but it is bad at capturing local details. Due to the semi-transparent nature of smoke, it is quite hard to accurately distinguish smoke from various backgrounds. Moreover, traditional Multi-head Self-Attention (MSA) mechanisms involve quadratic matrix multiplication operations, leading to high computational complexity. To address these issues, we propose a Local Feature Enhancement Propagation (LFEP) module to replace MSA. LFEP effectively reduces computational costs by adopting a hybrid pooling strategy of maximum and average poolings, and combines addition and subtraction with linear operations for enhancing features, as shown in Fig. 2(b). Specifically, the Maximum Pooling (MP) retains significant features by selecting the maximum value within a local region, while the Average Pooling (AP) reduces noise by calculating the average value within a local area.

<!-- src: S034 + S035 (merged across column break; overlap "on input features to" / "Maximum pooling is used to highlight" resolved conservatively — see cleaning log) -->
In LFEP, we first use a 3 × 3 average pooling for information communication, then perform subtraction between input feature and its pooled one. This approach helps restore or emphasize high-frequency details that might be lost during average pooling, which is crucial for identifying smoke edges or textures. Additionally, in another branch, we perform maximum pooling with a 3 × 3 kernel on input features to highlight significant components and reduce noise. Finally, the results of these two paths are fused to produce an enhanced representation of objects. The specific formula is as follows:

LFEP_o = {x_i − AP{x_i}} + MP{x_i}   (1)

<!-- src: S036 -->
Our LFEP module has potential advantages in analyzing local feature variations. On the one hand, it can reduce the interference from background information. On the other hand, it can extract main textures from images, and reduce the number of model parameters and the risk of overfitting.

#### CNN encoder

<!-- original heading: "3.1.2. CNN encoder" (glued to body in S037; unglued) -->

<!-- src: S037 -->
In computer vision tasks, previous work has relied heavily on powerful encoders, such as ResNet50 [39], ResNet101 and others. These encoders extract higher-level features by stacking multiple convolutional layers and residual blocks. Although this approach achieved a significant improvement in performance, it also resulted in a substantial increase in the number of parameters. This may cause some difficulties in the training and deployment of the model.

<!-- src: S038 -->
To circumvent this issue, our CNN encoder is only used to extract local information. This implies that we do not require an overly complex backbone network to capture global contextual information. Instead, we utilize a standard pretrained ResNet18 [39] encoder to extract local features. As a result, our CNN encoder has a faster convergence rate during training. At the same time, our dual-encoder demonstrates better stability and accuracy in the task of smoke segmentation.

### Multi-level attention coupled module

<!-- original heading: "3.2. Multi-level attention coupled module" (S039) -->

<!-- src: S040 -->
To fully mine and utilize both global and local feature information, we meticulously design a Multi-level Attention Coupled Module (MACM), as shown in the Fig. 3. MACM is not only able to focus on deep information within a single encoder, but also interact with cross-encoder information. This unique design allows MACM to more comprehensively understand and integrate multi-dimensional data from different encoders, thereby outputting features with rich hierarchies and scales.

<!-- src: S041; Eq. (2) garbled in PDF text layer, flagged -->
As shown in Fig. 3, we introduce attention heat maps into the main units of MACM to visually demonstrate its performance and exceptional ability in integrating global and local information. By observing these visualized heat maps, we can clearly see how MACM captures and fuses global and local information from different encoders, thereby gaining a deeper understanding of its advantages in complex tasks. MACM primarily consists of three key steps. Initially, we employ the feature maps from the LFE-Former encoder as query vectors and those from the CNN layer as key vectors, executing an attention mechanism to facilitate dynamic interaction between features. The mathematical expression for this step can be represented as: [Eq. (2) garbled in extraction: Att_i = Conv3×3(EC_i × Softmax(…)); see PDF] where EC_i and ET_i represent the feature maps of the ith layer of CNN and LFE-Former encoder.

<!-- src: S042; Eq. (3) garbled in PDF text layer, flagged -->
Next, we apply a max pooling operation in the CNN layer to capture the local texture information of the smoke. To enhance the influence of these texture details on the attention map, we generate texture coefficients using the sigmoid function. This process can be formalized as: [Eq. (3) garbled in extraction: …_i = Sigmoid(Mp(…)) × Att_i; see PDF] where Mp(⋅) represents the 3 × 3 max pooling.

<!-- src: S043; Eq. (4) truncated in PDF text layer, flagged -->
Finally, we combine the feature map from the transformer layer with the texture-enhanced guided attention map, integrating these two sources of information through a summation operation. This results in a composite feature map that incorporates both the global features from the LFE-Former encoder and the local texture information from the CNN encoder. The mathematical expression for this step can be written as: [Eq. (4) truncated in extraction: F_i = Conv3×3(…); see PDF] where Conv3×3(⋅) represents a 3 × 3 convolution with single channel. By limiting the output to a single channel, we can force the model to focus more on spatial details and complex structures.

### Prior-guided multi-scale fusion decoder

<!-- original heading: "3.3. Prior-guided multi-scale fusion decoder" (S044) -->

<!-- src: S045 -->
Variability and irregularity of smoke require segmentation methods to have excellent multi-scale adaptability. Additionally, contextual information also greatly influence the accuracy of smoke segmentation methods, such as contrast between smoke and background, internal structure of smoke. To address these issues, we design a new Prior-guided Multi-scale Fusion Decoder (PMFD) that is based on Feature Pyramid Network (FPN) [40], shown in Fig. 4.

<!-- src: S046 + S047 (merged across p4→p5 break; junction "…we mainly perform feature | PMFD emphasizes…" is a column-break seam, joined without invented text — see cleaning log); Eq. (5) partly readable -->
Our PMFD can handle multi-scale information from both local details and global overviews. Specifically, we upsample and element-wisely add the multi-scale features (F4, F3, F2, F1) from different levels of MACM in a bottom to up manner, thus we can integrate global semantic information with local spatial details. This process not only preserves the uniqueness of multi-level features, but also achieves the complementarity and enhancement of information. Notably, we adjust the channel number of F1, F2, F3 and F4 to one. This means that we mainly perform feature [column-break seam] PMFD emphasizes integration and interaction in spatial dimensions rather than the channel dimension. This process is important for smoke segmentation, because features at different levels can provide complementary and rich information, which helps improve the model's segmentation accuracy. This process can be represented by the following formula: [Eq. (5), partially garbled in extraction: F̃_{i−1} = Up(F_i) ⊕ F_{i−1}, i = 4, 3, 2; see PDF]

<!-- src: S048 -->
To further refine the fused feature map, we employ a 3 × 3 convolution with shared weights to reduce potential aliasing effects. This step helps in smoothing out the boundaries and reducing noise in the final prediction. Additionally, we upsample the feature map to match the size of F1 to ensure consistency across different scales. Next, we concatenate the segmentation results from different scales to create a more comprehensive representation of features. Finally, the concatenated features are passed through additional convolutional layers and upsampling operations to refine the predictions.

<!-- src: S049 -->
Although our PMFD and FPN [40] focus on integrating multi-scale features, our PMFD is greatly different from FPN. The first difference is input sources. FPN obtains input from the backbone and relies on convolutions to adjust channel dimensions during the layer-by-layer fusion process. In contrast, PMFD directly obtains input from MACM, avoiding the need for additional convolutions. The second one is feature processing mechanisms. FPN directly makes predictions after fusing features at each level. PMFD first fuses global and local information. Then, to achieve complementarity and enhancement of feature information, shared-weight convolution, upsampling, concatenation operations are designed to generate the hybrid features of different scales.

### Multiple objective function

<!-- original heading: "3.4. Multiple objective function" (S050) -->

<!-- src: S051; Eq. (6) glued mid-sentence in PDF text layer, flagged -->
The smoke segmentation is a typical pixel-level binary classification problem. In this task, the Binary Cross-Entropy (BCE) loss function is widely adopted as the standard method for loss computation. Although the BCE loss function is simple and commonly used, it ignores the global structural information of images. To address this shortcoming, F3Net [41] further improved these two loss functions by introducing Weighted BCE [sentence interrupted by equation in extraction] L(P, G) = ℓω_BCE(P, G) + ℓω_IoU(P, G)   (6), where P and G represent the prediction result and ground truth.

## Results

<!-- original heading: "4. Experiments and results" (S052) -->

### Datasets and implementation

<!-- original heading: "4.1. Datasets and implementation" (S053) -->

#### Experimental datasets

<!-- original heading: "4.1.1. Experimental datasets" (glued to body in S054; unglued) -->

<!-- src: S054; "SYN70 K" spacing artifact normalized to "SYN70K" throughout -->
The dynamic nature of smoke, such as its variable shapes and blurry boundaries, makes precise pixel-level manual annotation of real smoke images extremely challenging. In view of this, we employed the synthetic smoke dataset SYN70K [9] as our training dataset. It is worth mentioning that in the process of model training, we divided the SYN70K dataset into a training dataset and a validation dataset at a ratio of 4:1. This division aimed to ensure that the model learned sufficient generalization ability from a large amount of data, while also effectively assessing its performance through a single validation dataset.

<!-- src: S055 -->
To comprehensively evaluate the generalization capability of our MIFNet, we use synthetic and real smoke images as test datasets. Specifically, the synthetic image test dataset consisted of the DS01, DS02, and DS03 subsets from the SYN70K dataset, each containing 1000 RGB smoke images of size 256 × 256. The real smoke image is from the forest smoke dataset (FSD) taken by Tower Line [13]. Some sample images from these datasets are displayed in Fig. 5. With such a configuration of the test dataset, we can thoroughly evaluate the performance of our MIFNet under different conditions.

#### Implementation details

<!-- original heading: "4.1.2. Implementation details" (glued to body in S056; unglued) -->

<!-- src: S056 -->
In the process of model training, we implement a series of data augmentation techniques to prevent model overfitting. Specifically, we apply random rotations (including 90, 180, and 270°) and horizontal flips to the training data. In terms of optimization algorithm selection, we use the Stochastic Gradient Descent (SGD) optimizer with momentum, setting the β value to 0.9 to promote faster convergence and a more stable learning process. The initial learning rate was set to 1e-2, and we employed a cosine annealing strategy to adjust the learning rate. Moreover, we set the batch size to 16 to achieve higher computational efficiency under hardware resource constraints. Our MIFNet undergo a total of 100 epochs to ensure that it could fully learn the complex features of smoke images.

<!-- src: S057 -->
All training, validation, and testing were completed under the PyTorch deep learning framework, with the experimental environment being a computer equipped with a single NVIDIA 2080Ti 11G GPU. We uniformly adjust the resolution of the SYN70K training, validation, and test images to 224 × 224. Meanwhile, on the FSD dataset, we maintain high-resolution images for training and testing to capture more detailed information, which is crucial for enhancing the model's performance in real-world smoke detection tasks.

### Evaluation metrics

<!-- original heading: "4.2. Evaluation metrics" (S058) -->

<!-- src: S059 + S060 (merged across p5→p6 page break; duplicated word "Higher" removed) -->
We employ three widely-used metrics to evaluate our method, including Dice coefficient (Dice), Intersection over Union (IoU) and Accuracy (Acc). In order to facilitate comparisons, we calculate the mean IoU (mIoU) and mean Dice (mDice) of all images in the DS01, DS02 and DS03 subsets of SYN70K dataset. Higher scores of mIoU and mDice mean better performance. In addition, we choose sensitivity (SE) to reflect the prediction accuracy of each pixel in the FSD dataset. A higher SE score indicates that the model can effectively identify most positive samples, reducing the possibility of missing key objects.

### Ablation experiments

<!-- original heading: "4.3. Ablation experiments" (S061) -->

#### Ablation study of transformer blocks

<!-- original heading: "4.3.1. Ablation study of transformer blocks" (glued to body in S062; unglued) -->

<!-- src: S062 -->
To further evaluate each component of our MIFNet. We conducted a series of ablation experiments to deeply analyze the two key elements: model structure and training strategy.

<!-- src: S063 -->
Firstly, we use the classic Multi-head Self-attention (MSA) [23] and Efficient Additive Attention (EAA) [34] to replace the core component LFEP of the LFE-Former encoder, and compared its influence on the segmentation results. Results are shown in Table 1.

<!-- src: S064; restored missing period after "2.45 G" -->
Our LFEP achieves significant performance improvements. Compared to MSA and EAA, LFEP mIoU increases by 1.13 % and 0.73 %, respectively. Additionally, LFEP also has significant advantages in the number of parameters and computational complexity. Our LFEP reduces the number of parameters by about 4 M and FLOPs by 2.45 G. This is primarily due to addition and subtraction operations between pooled features in LFEP. Obviously, it avoids complex computations and are more efficient than complex matrix operations in MSA and EAA.

<!-- src: S065 -->
To provide a more intuitive comparison of the performance differences between LFEP, MSA, and EAA, we conducted visual comparisons of results. As shown in Fig. 6, purple denotes predicted background regions, and highlight color marks smoke ones. Combining visual results in Fig. 6 with quantitative analysis results in Table 1, it is evident that LFEP achieves the best performance for smoke segmentation. LFEP significantly enhances its ability to capture detailed information by local feature enhancement mechanism. This optimization is particularly reflected in the precise identification of smoke boundaries, allowing LFEP to achieve higher accuracy in smoke segmentation applications.

#### Ablation study of the MACM module

<!-- original heading: "4.3.2. Ablation study of the MACM module" (glued to body in S066; unglued) -->

<!-- src: S066; dropped dangling column-break fragment '"1 (H/2 × W/2)"' duplicated at start of S069 -->
MACM effectively integrates LFE-Former and CNN encoder feature information. To validate the effectiveness of MACM, we design a series of variant experiments, as shown in Table 2. We do not use MACM and gradually increase the number of MACM. "None" means to replace all MACMs with element-wise addition operations.

<!-- src: S069 -->
Here, "1 (H/2 × W/2)" indicates that only MACM with the scale of (H/2 × W/2) is retained, and features of other scales are fused by element-wise addition. As the number of MACMs increases, the segmentation performance of the model is gradually improved. The reason is that MACM can facilitate more extensive interactions between global and local information for capturing richer spatial details.

<!-- src: S070 + S071 (merged across p6→p7 page break) -->
To validate the segmentation performance of MACM, we conducted visual comparisons, as shown in Fig. 7. As the number of MACM increases, the smoke segmentation performance steadily improves. In the case of zero or one MACM, smoke boundaries of segmented results are not precise enough, leading to false segmentation of backgrounds as smoke. As the number of MACM goes up to 2 or 3, erroneous segmentations are significantly mitigated and the outlines of smoke regions boundaries become clearer. For the number of MACM reaching 4, segmented smoke boundaries become very accurate.

<!-- src: S072 -->
Table 2 and Fig. 7 effectively validate the performance of MACM by segmentation results. To demonstrate the interactivity of the MACM module, we visualize the heat maps from the internal layers of MACM to show the fusion process of global and local information, as shown in Fig. 8. We selected smoke images of different scales and densities as analytical examples. Fig. 8(b) and (c) are the inputs to MACM, while Fig. 8(d) represents the middle results of MACM, and Fig. 8(e) shows the final output feature map. Interaction of global and local features in the encoder by MACM makes the contours of smoke objects clearly visible. This directly proves the effectiveness of our MACM.

#### Ablation study of decoder

<!-- original heading: "4.3.3. Ablation study of decoder" (glued to body in S073; unglued) -->

<!-- src: S073 -->
PMFD is another significant contribution, dedicated to the effective fusion of features from different modalities or processing paths to reconstruct smoke details and generate accurate prediction maps. To highlight the advantages of PMFD, we conducted comparative experiments by replacing PMFD with other similar decoder architectures, including FPN [40] and Mixer Layer Aggregation (MLA) [14]. These alternatives are labeled as Model 1 and Model 2, respectively. Table 3 provides detailed quantitative results, while Fig. 9 shows visual comparison results.

<!-- src: S074 + S076 (merged across table/caption interruption on p7) -->
We conducted comprehensive tests on the performance of FPN, MLA and PMFD using three evaluation metrics of mDice, mIoU and Acc. According to Table 3, our PMFD outperforms Model 1 and Model 2 on all metrics, demonstrating its superior performance. In the mIoU evaluation metric, our PMFD achieves performance improvements of 1.19 % and 0.99 % over Model 1 and Model 2, respectively. The main reason for this significant improvement is that we complement and enhance feature information by concatenating hybrid feature maps of different scales. FPN and MLA have not the unique advantage.

<!-- src: S077 -->
Fig. 9 visually demonstrates the performance of different decoders in smoke segmentation tasks. We selected smoke images of varying scales and with multi-object characteristics for validation experiments. In terms of detail handling, our PMFD shows significant superiority. Specifically, looking at the second row of image segmentation results, FPN and MLA suffer from under-segmentation and over-segmentation, whereas our PMFD is able to accurately locate and segment the object areas without errors. These comparisons not only highlight our advantages in scale adaptability but also demonstrate the significant effectiveness of our method in foreground enhancement.

#### Ablation study of different losses

<!-- original heading: "4.3.4. Ablation study of different losses" (glued to body in S078; unglued) -->

<!-- src: S078 -->
To further explore the application of loss function in our smoke segmentation network, we conduct ablation experiments to understand the specific impact of multi-objective loss function. For comparative analysis, we select single IoU and BCE loss functions as reference benchmarks to evaluate the practical utility of the combined BCE+IoU loss function. The results as shown in Table 4.

<!-- src: S079 -->
Through experimental comparison, we find that on the three test sets, our network using BCE and IoU shows excellent segmentation performance. In contrast, the model using only the BCE loss function performs the least satisfactorily, while the model using the IoU loss alone has an intermediate performance. The specific reason may be that the BCE loss is susceptible to interference from background classes, while the IoU loss is inherently suitable for dealing with small targets. In our design of the multi-objective loss function, by assigning different weights to BCE and IoU losses, we are able to differentially weight pixels in various locations. This strategy effectively enhances the segmentation of small target smoke, alleviates the problem of class imbalance, refines edge detection accuracy, and thereby improves the overall generalization capability of the model. Therefore, when dealing with complex smoke segmentation tasks, our method demonstrates higher performance and better results.

### Performance evaluation

<!-- original heading: "4.4. Performance evaluation" (S080) -->

#### Experiments on SYN70K dataset

<!-- original heading: "4.4.1. Experiments on SYN70K dataset" (glued to body in S081; unglued) -->

<!-- src: S081; fixed "types:1)" spacing -->
To comprehensively validate the performance of our MIFNet, we conducted quantitative comparative experiments by different methods. Our comparison include the most advanced methods, which can be broadly categorized into two main types: 1) Methods based on Deep Convolutional Neural Networks (DCNN), including but not limited to DANet [42], DMNet [43], PointRend [20] and EANet [44]; 2) Methods based on Transformer models, including Segmenter [6], SegFormer [7], Conformer [36], FAT-Net [45], and Swiftformer [34]; 3) Some methods of smoke segmentation, including SmokeSeger [14], Frizz [26], W-Net [10], TANet [33], CGRNet [12], DMAENet [13] and SAGINN [46].

<!-- src: S082 + S086 (merged across table interruption; duplicated lead-in "Table 5 reports" removed) -->
Table 5 details the comparison results of model performance, including model parameters, floating point operations (FLOPs), and mIoU. It is clear from Table 5 that our MIFNet achieved outstanding results on the comprehensive smoke segmentation dataset SSS (DS01, DS02, and DS03), demonstrating its superior performance. Notably, MIFNet surpassed the SmokeSeger in the smoke segmentation task while being smaller in model scale, mIoU is over 6 %. These achievements not only highlight the high efficiency of MIFNet in processing smoke image segmentation, but also validate the validity of our proposed Trans-CNN coupling structure. With these structures, MIFNet achieves higher accuracy with lower computational costs, which is important for deployment and resource management in real-world application scenarios.

<!-- src: S087 -->
As can be seen from the data comparison in Table 6, among the different smoke segmentation networks evaluated on the SYN70K dataset, our MIFNet has achieved outstanding results on the mIoU evaluation metric. MIFNet shows the following significant advantages: 1) Parameter efficiency: MIFNet has 24.6 M parameters, which is significantly less than SAGINN's 101.1 M parameters, with only a slight drop in performance. This characteristic indicates that MIFNet can provide high-performance capabilities while maintaining reasonable computational costs. 2) Higher mIoU scores: On three different datasets (DS01, DS02, and DS03), MIFNet's mIoU scores are 81.8 %, 81.0 %, and 81.9 %. These results are close to or even rival those of the larger parameter SAGINN (83.3 %, 82.7 %, and 82.9 %), demonstrating that MIFNet can achieve comparable performance levels even with fewer parameters. 3) Without classification module: MIFNet outperforms versions of the CGRNet and SAGINN that do not use classification auxiliary (results marked with * in the Table 6). This suggests that MIFNet may be more effective at mining and utilizing the intrinsic structural information of the data, thus achieving excellent segmentation results without the need for additional classification guidance. In summary, MIFNet has demonstrated efficiency and competitiveness in the smoke segmentation task, and its effectiveness and practicality have been fully validated.

<!-- src: S088 + S091 (merged across p8→p9 page break) -->
Fig. 10 illustrates the comparison of segmentation effects of different networks on the SYN70K dataset. It is evident from the results that most networks can effectively handle large smoke areas in images, benefiting from their ability to capture salient object abstract features. However, when facing complex or ambiguous smoke scenes, our MIFNet demonstrates superior performance. Taking the fourth and fifth samples as examples, our MIFNet shows a clear advantage in edge detail processing; our method produces clearer smoke regions, and its segmentation results not only have smoother edges but also adhere more closely to the ground truth. In contrast, DMNet, DANet, Segmenter, SegFormer, and CGRNet* exhibit varying degrees of under-detection or mis-segmentation issues. They either misclassify backgrounds similar to smoke or fail to accurately identify thin smoke areas. Although SAGINN* and DMAENet have a comparable overall visual performance to MIFNet, there are still differences in detail handling, which are particularly noticeable in the first, second, and third samples. We highlight these differences with red boxes.

#### Experiments on FSD dataset

<!-- original heading: "4.4.2. Experiments on FSD dataset" (glued to body in S092; unglued) -->

<!-- src: S092 -->
To highlight the exceptional performance of our MIFNet in real-world applications, we fine-tuned it on the forest smoke dataset (FSD). Additionally, we compared our method with several different methods for smoke segmentation on the FSD dataset. The quantitative results are provided in Table 7, while Fig. 11 offers visual comparisons, further proving the superiority of our method.

<!-- src: S093 -->
Similar to the performance results on the synthetic smoke dataset, our MIFNet also demonstrates outstanding performance on the FSD dataset. It achieves remarkable results on all evaluation metrics, with an accuracy rate as high as 98.3 %. Fig. 11 further illustrates the performance disparities between various methods through visual results. MIFNet shows significant advantages in smoke localization, boundary recognition, and dealing with small and thin smoke in images. Particularly, in handling images with invisible smoke or smoke-like objects, as seen in the second and third rows of Fig. 11, MIFNet is able to achieve more precise segmentation than other algorithms. Moreover, even in situations where smoke is occluded, MIFNet can accurately localize and segment it.

#### Results of other scenarios

<!-- original heading: "4.4.3. Results of other scenarios" (glued to body in S094; unglued) -->

<!-- src: S094 + S096 (merged across table interruption; overlap "we thoroughly verify the" / "These results verify the robustness of our model." resolved conservatively — see cleaning log) -->
To assess the model's resistance to noise or outliers in training data, we specifically selected fire and smoke images from complex scenes for testing. Through diversified data testing, we thoroughly verify the robustness of our model. These experimental results ensure that our model maintains stable and reliable performance in the face of various interference factors that may exist in the real world. The experimental results are shown in Fig. 12.

<!-- src: S097 -->
In experiments of flame and smoke images, we did not fine-tune our model. We directly tested flame and smoke images with our model pre-trained on the SYN70K dataset. To visually demonstrate the reliability of segmentation results, we overlay original images with a mask. As shown in Fig. 12, our MIFNet performs well in complex fire scenes, successfully avoiding interference from flames. In addition, our method can precisely locate and segment the sparse smoke areas.

## Discussion

<!-- No standalone Discussion section in this paper; discussion content is embedded in Section 4 (Results) and Section 5 (Conclusions). -->

(No standalone Discussion section in the source paper.)

## Conclusion

<!-- original heading: "5. Conclusions" (S098) -->

<!-- src: S099 -->
In this study, we propose MIFNet, an innovative smoke image segmentation method that employs a synergistic combination of Transformer and CNN branches. This dual-encoder architecture significantly enhances the model's robustness and predictive accuracy by reducing background interference. To address the semi-transparent nature of smoke and its weak differentiation from the background, we design an LFE-Former encoder based on the Local Feature Enhancement Propagation (LFEP) mechanism to enhance the foreground feature representation of smoke. Moreover, to fully integrate global and local information, we design a Multi-level Attention Coupled Module (MACM) that facilitates the interaction of feature information between different encoders, effectively output multi-scale feature. We also design a Prior-guided Multi-scale Fusion Decoder (PMFD), which combines prior knowledge with a multi-scale feature fusion strategy to further improve the accuracy of model in complex scenes. Through extensive qualitative and quantitative analysis, MIFNet has proven its superiority, particularly excelling in handling edge details and generating smoother and more precise edges. Future work will explore the application of MIFNet in real surveillance systems to enhance the capability of early detection of fires and gas leaks.

## Acknowledgments

<!-- original heading: "Acknowledgments" (glued to body in S104; unglued) -->

<!-- src: S104 -->
This work was partially supported by the National Natural Science Foundation of China (62272308) and the Capacity Construction Project of Shanghai Local Colleges (23010504100).

## References

<!-- original heading: "References" (glued to first entry in S106; unglued). src: S106–S118.
     Reader notes: references condensed with medium confidence; hyphenation/line-break splits repaired; entries re-separated one per line. -->

[1] K. Muhammad, T. Hussain, M. Tanveer, G. Sannino, V. de Albuquerque, Cost-effective video summarization using deep CNN with hierarchical weighted fusion for IoT surveillance networks, IEEE Int. Things J. 7 (5) (2020) 4455–4463.
[2] F. Cui, Deployment and integration of smart sensors with IoT devices detecting fire disasters in huge forest environment, Comput. Commun. 150 (2020) 818–827.
[3] T. Nguyen-Ti, T. Nguyen-Phuc, T. Do-Hong, Fire detection based on video processing method, in: International Conference on Advanced Technologies for Communications, 2014, pp. 106–110.
[4] E. Shelhamer, J. Long, T. Darrell, Fully convolutional networks for semantic segmentation, IEEE Trans. Pattern Anal. Mach. Intell. 39 (4) (2016) 640–651.
[5] F. Yuan, K. Li, C. Wang, J. Shi, Y. Zhu, Fully extracting feature correlation between and within stages for semantic segmentation, Digit. Signal Process. 127 (2022).
[6] R. Strudel, R. Garcia, I. Laptev, C. Schmid, Segmenter: Transformer for semantic segmentation, in: Proc. Int. Conf. Comput. Vis, 2021, pp. 7262–7272.
[7] E. Xie, W. Wang, Z. Yu, A. Anandkumar, J.M. Alvarez, P. Luo, Segformer: simple and efficient design for semantic segmentation with transformers, Adv. Neural Inf. Process. Syst. 34 (2021) 12077–12090.
[8] S. Zheng, et al., Rethinking semantic segmentation from a sequence-to-sequence perspective with transformers, in: Proc. IEEE Conf. Comput. Vis. Pattern Recognit, 2021, pp. 6881–6890.
[9] F. Yuan, L. Zhang, X. Xia, B. Wan, Q. Huang, X. Li, Deep smoke segmentation, Neurocomputing 357 (2019) 248–260.
[10] F. Yuan, L. Zhang, X. Xia, Q. Huang, X. Li, A wave-shaped deep neural network for smoke density estimation, IEEE Trans. Image Process. 29 (2020) 2301–2313.
[11] S. Khan, et al., Deepsmoke: deep learning model for smoke detection and segmentation in outdoor environments, Expert Syst. Appl. 182 (2021).
[12] F. Yuan, L. Zhang, X. Xia, Q. Huang, X. Li, A gated recurrent network with dual classification assistance for smoke semantic segmentation, IEEE Trans. Image Process. 30 (2021) 4409–4422.
[13] G. Wen, et al., A dense multi-scale context and asymmetric pooling embedding network for smoke segmentation, IET Comput. Vis. (2023) 1–11.
[14] T. Jing, Q. Meng, H. Hou, SmokeSeger: a Transformer-CNN coupled model for urban scene smoke segmentation, IEEE Trans. Ind. Inf. 20 (2) (2024) 1385–1396.
[15] L. Chen, G. Papandreou, I. Kokkinos, K. Murphy, A.L. Yuille, Semantic image segmentation with deep convolutional nets and fully connected CRFs, in: Proc. Int. Conf. Learn. Represent, 2015, pp. 1–14.
[16] L. Chen, et al., Semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected CRFs, IEEE Trans. Pattern Anal. Mach. Intell. 40 (4) (2018) 834–848.
[17] Y. Nakayama, H. Lu, Y. Li, T. Kamiya, WideSegNeXt: semantic image segmentation using wide residual network and NeXt Dilated Unit, In IEEE Sensors Journal 21 (10) (2021) 11427–11434.
[18] G. Wang, et al., DeepIGeoS: a deep interactive geodesic framework for medical image segmentation, IEEE Trans. Pattern Anal. Mach. Intell. 41 (7) (2019) 1559–1572.
[19] Z. Qi, Z. Zou, H. Chen, Z. Shi, Remote-Sensing Image Segmentation Based on Implicit 3-D Scene Representation, IEEE Geosci. Remote Sens. Lett. 19 (2022) 1–5.
[20] A. Kirillov, Y. Wu, K. He, R. Girshick, Pointrend: Image segmentation as rendering, in: Proc. IEEE Conf. Comput. Vis. Pattern Recognit, 2020, pp. 9799–9808.
[21] L. Zhu, D. Ji, S. Zhu, W. Gan, W. Wu, J. Yan, Learning statistical texture for semantic segmentation, in: IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2021, pp. 12532–12541.
[22] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. Gomez, L. Kaiser, I. Polosukhin, Attention is all you need, Advances in Neural Information Processing Systems, Curran Associates, Inc., 2017, pp. 5998–6008.
[23] A. Dosovitskiy et al., An image is worth 16x16 words: transformers for image recognition at scale, 2020. [Online]. Available: https://arxiv.org/abs/2010.11929.
[24] Q. Wan, Z. Huang, J. Lu, G. Yu, L. Zhang, SeaFormer: squeeze-enhanced axial Transformer for mobile semantic segmentation, in: International Conference on Learning Representations (ICLR), 2023.
[25] Z. Liu, et al., Swin transformer: hierarchical vision transformer using shifted windows, in: Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021, pp. 9992–10002.
[26] S. Frizzi, et al., Convolutional neural network for video fire and smoke detection, Conference of the IEEE Industrial Electronics Society 34 (2016) 877–882.
[27] J. Zhan, Y. Hu, G. Zhou, Y. Wang, W. Cai, L. Li, A high-precision forest fire smoke detection approach based on ARGNet, Comput. Electron. Agric. 196 (2022).
[28] H. Tao, Q. Duan, An adaptive frame selection network with enhanced dilated convolution for video smoke recognition, Expert Systems with Application (2023).
[29] Y. Wang, Z. Luo, D. Chen and Y. Li, Semantic segmentation of fire and smoke images based on dual attention mechanism, 2022 4th International Conference on Frontiers Technology of Information and Computer (ICFTIC), 2022, pp. 185–190.
[30] Y. Cao, Q. Tang, X. Wu, X. Lu, EFFNet: enhanced Feature Foreground Network for Video Smoke Source Prediction and Detection, in: IEEE Transactions on Circuits and Systems for Video Technology 32, 2022, pp. 1820–1833.
[31] H. Tao, Q. Duan, M. Lu, Z. Hu, Learning discriminative feature representation with pixel-level supervision for forest smoke recognition, Pattern Recognit. 143 (2023).
[32] F. Yuan, K. Li, C. Wang, Z. Fang, A lightweight network for smoke semantic segmentation, Pattern Recognit. 137 (2023).
[33] X. Xia, K. Zhan, Y. Peng, Y. Fang, Texture-aware network for smoke density estimation, in: IEEE International Conference on Visual Communications and Image Processing, 2022, pp. 1–5.
[34] A. Shaker, M. Maaz, H. Rasheed, S. Khan, M. Yang, F. Khan, SwiftFormer: efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications, in: 2023 IEEE/CVF International Conference on Computer Vision, 2023, pp. 17379–17390.
[35] S. Ascoli, H. Touvron, M. Leavitt, A. Morcos, G. Biroli, L. Sagun, Convit: improving vision transformers with soft convolutional inductive biases, In Int. Conf. Mach. Learn. PMLR (2021) 2286–2296.
[36] Z. Peng, et al., Conformer: local features coupling global representations for recognition and detection, IEEE Trans. Pattern Anal. Mach. Intell. 45 (8) (2023) 9454–9468.
[37] A. Srinivas, T. Lin, N. Parmar, J. Shlens, P. Abbeel, A. Vaswani, Bottleneck transformers for visual recognition, in: Proceedings IEEE Conference on Computer Vision and Pattern Recognition, 2021, pp. 16519–16529.
[38] F. Yuan, Z. Zhang, Z. Fang, An Effective CNN and Transformer Complementary Network for Medical Image Segmentation, Pattern Recognit. 136 (Apr. 2023) 109228.
[39] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, in: IEEE Conference on Computer Vision and Pattern Recognition, 2016, pp. 770–778.
[40] T.-Y. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan, S. Belongie, Feature pyramid networks for object detection, in: Proceedings IEEE Conference on Computer Vision and Pattern Recognition, 2017, pp. 936–944.
[41] J. Wei, S.H. Wang, Q.M. Huang, F3Net: fusion, feedback and focus for salient object detection, in: Proceedings of the AAAI Conference on Artificial Intelligence 34, 2020, pp. 12321–12328.
[42] J. Fu, J. Liu, H. Tian, Y. Li, Y. Bao, Z. Fang, H. Lu, Dual attention network for scene segmentation, in: Proceedings IEEE Conference on Computer Vision and Pattern Recognition, 2019, pp. 3141–3149.
[43] J. He, Z. Deng, Y. Qiao, Dynamic multi-scale filters for semantic segmentation, in: Proceedings of the IEEE/CVF International Conference on Computer Vision, 2019.
[44] M. Guo, et al., Beyond self-attention: external attention using two linear layers for visual tasks, IEEE Trans. Pattern Anal. Mach. Intell. 45 (5) (2023) 5436–5447.
[45] H. Wu, S. Chen, G. Chen, W. Wang, B. Lei, Z. Wen, Fat-net: feature adaptive transformers for automated skin lesion segmentation, Med. Image Anal. 76 (2022).
[46] L. Zhang, J. Wu, F. Yuan, Y. Fang, Smoke-aware global-interactive non-local network for smoke semantic segmentation, IEEE Trans. Image Process. 33 (2024) 1175–1187.

## Other

### Keywords

<!-- src: S007; duplicate keyword fragment glued into affiliation block S005 dropped -->
Keywords: Smoke segmentation; Attention coupled module; Hybrid network; Foreground enhancement

### CRediT authorship contribution statement

<!-- src: S100, S101 -->
Kang Li: Writing – original draft, Visualization, Validation, Software, Methodology. Feiniu Yuan: Writing – review & editing, Validation, Funding acquisition, Conceptualization. Chunmei Wang: Writing – review & editing, Validation, Supervision.

### Declaration of competing interest

<!-- original heading glued to body in S102; unglued. src: S102, S103 -->
The authors declare the following financial interests/personal relationships which may be considered as potential competing interests: Feiniu Yuan reports financial support was provided by National Natural Science Foundation of China. If there are other authors, they declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Data availability

<!-- original heading glued to body in S105; unglued. src: S105 -->
Data will be made available on request.

### Figure and table captions

<!-- src: C001–C019; "Fig. N. ." double-period artifacts fixed; separated from body text -->
Fig. 1. The overview framework of the dual-path encoder in our MIFNet.
Fig. 2. Local Feature Enhancement Transformer (LFE-Former). (a) Detailed structure of LFE-Former. (b) The structure of Local Feature Enhancement Propagation (LFEP).
Fig. 3. Multi-level attention coupled module (MACM).
Fig. 4. Prior-guided Multi-scale Fusion Decoder (PMFD).
Fig. 5. Some examples. (a) Synthetic smoke images. (b) Forest smoke images.
Fig. 6. Visualization of different Transformer block. (a) Image. Results of (b) MSA, (c) EEA, (d) ours LFEP.
Fig. 7. Results with different MACM numbers. (a) Input images, (b) Ground truths, (c) no MACM, (d) one MACM, (e) two MACM, (f) three MACM, and (g) four MACM.
Fig. 8. Visualized features in MACM interaction process. (a) Smoke images; the results of (b) LFE-Former encoder, (c) CNN encoder, (d) MACM middle layer, and (e) MACM output.
Fig. 9. Segmentation results with different decoder. (a) Input images; (b) Ground truth; (c) Model 1; (d) Model 2; (e) Our method.
Fig. 10. Results on SYN70K dataset. (a) Images, (b) Ground truth. Segmentation results of (c) DMNet, (d) DANet, (e) Segmenter, (f) SegFormer, (g) CGRNet*, (h) DMAENet, (i) SAGINN*, (j) Our MIFNet. Best viewed in red.
Fig. 11. Results on FSD dataset. (a) Images, (b) Labels. Segmentation results of (c) FAT-Net, (d) EANet, (e) Swiftformer, (f) DMAENet, (g) Ours method. Best viewed in blue.
Fig. 12. Results of our MIFNet on fire and smoke images. (a) Original images, (b) prediction maps, and (c) mixed images.
Table 1. Comparisons of different Transformer block.
Table 2. Ablation study of MACM.
Table 3. Ablation study of the decoder on DS01 test dataset.
Table 4. Ablation study of the loss function.
Table 5. Smoke segmentation results on the SSS dataset.
Table 6. Results of different smoke segmentation networks on the SYN70K dataset.
Table 7. Smoke segmentation results on the FSD dataset.
