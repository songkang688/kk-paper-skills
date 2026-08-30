# 36_FeatureAggregation_TCE2025_SuperResolution — Clean English Corpus

<!-- Stage 00 Wave 3 Agent H. English **Original:** blocks only; no Chinese content.
     Source: /workspace/36_FeatureAggregation_TCE2025_SuperResolution.md (bilingual reader).
     Anchors in comments (SXXX/CXXX) refer to reader block ids.
     Authorship context (do not re-derive): Tier A1, weight 1.00; Yuan first author AND sole corresponding.
     Extraction quality: HIGH for prose (reading order, equations pre-normalized inline (1)-(20)).
     Reader anchor anomaly: the "I. INTRODUCTION" heading and the first Introduction paragraph BOTH
     carry anchor S007 (S006 skipped in reader numbering).
     Reference list arrived glued (several entries per block, S056-S065); split into [1]-[61] below.
     Citation-number mismatches exist in the SOURCE text vs the reference list (see Results/References
     notes); preserved as printed. -->

## Title

<!-- src: S001, S002, S011 (metadata portion) -->
A Comprehensive Feature Aggregation Network for Efficient Image Super-Resolution

Feiniu Yuan, Senior Member, IEEE, Changhong Xie, and Biao Xiang

Shanghai Normal University, Shanghai 200234, China. IEEE Transactions on Consumer Electronics, 2025. DOI: 10.1109/TCE.2025.3605068

## Abstract

<!-- src: S004; "Extensive experiential results" preserved as printed — suspected source typo for
     "experimental" -->
Deep learning based models have achieved remarkable reconstruction performance in single image Super-Resolution. However, these models often involve high computational costs and substantial memory usage, which limits their practical deployment on consumer devices. To overcome these challenges, we propose a novel Comprehensive Feature Aggregation Network (CFAN) for efficient image reconstruction. Specifically, we first propose a Hybrid Pixel Attention (HPA) block to capture both local and non-local information at a low computational cost. To further exploit channel information, we design a Multi-Scale Channel Attention (MSCA) block to comprehensively model pixel interactions across spatial and channel dimensions. Finally, we adopt an Adaptive Feature Fusion (AFF) module, which can enhance the preservation of low-frequency structural information. Extensive experiential results demonstrate that our proposed method achieves competitive performance in terms of accuracy with fewer network parameters compared to state-of-the-art methods.

<!-- src: S005 -->
Index Terms—Super-resolution, attention mechanism, multi-scale feature fusion.

## Introduction

<!-- original heading: "I. INTRODUCTION" (S007 — heading and first paragraph share this anchor) -->

<!-- src: S007 (paragraph) -->
Single image Super-Resolution (SISR) aims to reconstruct a high-resolution (HR) image from its Low-Resolution (LR) version. Traditional interpolation methods, such as bilinear and bicubic resampling, provide a basic solution to image super-resolution, but they often produce over-smoothed edges and fail to recover high-frequency details. Inspired by the great successes of deep learning, many deep methods have been proposed to improve the performance of image super-resolution [1], [2], [3]. Convolutional Neural Networks (CNN) [4] are widely used to implement image super-resolution by learning end-to-end non-linear mappings between LR and HR images. Despite the superiority of deep methods over conventional ones in generating photorealistic details, CNN-based approaches face inherent limitations. Convolutional operations usually produce receptive fields with limited sizes, which hinder effective modeling of long-range dependencies and non-local features. Consequently, CNN-based methods often suffer from inconsistent textures or distorted structures in complex scenarios. To achieve larger receptive fields, some methods [5] employ deeper networks or larger convolutional kernels. However, these techniques increase computational costs and memory consumption, leading to the problem of deployments in real-time scenes. It is challenging to design efficient and high-quality SR networks.

<!-- src: S008 -->
Attention mechanisms have achieved considerable successes [6], [7], [8] in image super-resolution. Attention adaptively emphasizes crucial information for detail restoration, and suppresses non-significant one for noise removal. There are several types of attention mechanisms [9], including self-attention, spatial attention, channel attention, and pixel attention. Self-attention is a key component of the Transformer model. It adopts matrix multiplication to capture global dependencies and significantly extend receptive fields. Transformer-based methods have demonstrated exceptional performance in various vision tasks [10], [11], significantly surpassing CNN-based models. However, self-attention has a quadratic computation complexity that leads to high memory consumption and computational cost. Other attention mechanisms with lower computation complexity are more suitable for lightweight models [12], but they often have smaller receptive fields, limiting their ability to capture rich contextual information.

<!-- src: S009 -->
To alleviate computational burden, various lightweight networks have been proposed [13], [14], [15], [16] for image super-resolution. These networks mainly focus on two strategies of inference time reduction and lightweight structure. The former often incorporates techniques such as knowledge distillation [17], structural re-parameterization [18], and model quantization [19]. The latter strategy typically employs group convolutions [20], parameter sharing [21], and recursive architectures [3]. These techniques facilitate model deployments on resource-constrained devices. However, some techniques obviously reduce the capability of capturing rich spatial contexts because of their limited receptive fields in feature extraction. Hence, balancing between reconstruction accuracy and model complexity still remains an unresolved challenge in efficient SR designs.

<!-- src: S010 -->
To address aforementioned issues, we design a novel lightweight SR network, called Comprehensive Feature Aggregation Network (CFAN). Our network achieves a favorable trade-off between performance and efficiency using small-kernel convolutions and linear layers. Inspired by the success of shifted window self-attention mechanism, we develop a lightweight yet effective Hybrid Pixel Attention block (HPA) that captures both local and non-local features for improved image reconstruction. To complement the spatial-only modeling of HPA, we introduce a Multi-Scale Channel Attention (MSCA) block that captures the interaction between spatial and channel dimensions. Furthermore, we adopt an Adaptive Feature Fusion (AFF) module to dynamically combine basic image features with deep features. Thus, we preserve structural coherence and recover spatial details. The proposed CFAN achieves an optimal trade-off between model complexity and reconstruction accuracy, as illustrated in Fig. 1.

<!-- src: S012; enumerated contribution list re-split (glued in extraction) -->
The main contributions of our work are summarized as follows:

(1) We design a Hybrid Pixel Attention block (HPA) to refine spatial features and improve the model's ability to capture contextual dependencies.

(2) We propose a Multi-Scale Channel Attention (MSCA) module to comprehensively implement pixel interactions across spatial and channel dimensions.

(3) We combine an Adaptive Feature Fusion (AFF) module with HPA and MSCA to propose a novel Comprehensive Feature Aggregation Network (CFAN) for efficient and high-quality image reconstruction, which achieves outstanding performance on super-resolution tasks with fewer parameters and FLOPs.

## RelatedWork

<!-- original heading: "II. RELATED WORK" (S013) -->

### A. CNN-Based SR Methods

<!-- original heading: "A. CNN-Based SR Methods" (S014) -->

<!-- src: S015 -->
In the past few years, applying CNNs to super-resolution tasks has achieved substantial progress. Dong et al. [1] introduced the first CNN-based framework for SISR. Building upon this work, VDSR [22] adopts a deeper network with residual connections to improve reconstruction accuracy. ESPCN [16] uses a sub-pixel convolution layer in the reconstruction stage, and outperforms earlier methods using de-convolution layers. Afterwards, sub-pixel convolutions have become one of mainstream techniques in super-resolution models. To extract multi-scale information, LapSRN [23] introduces a Laplacian pyramid structure for progressive image reconstruction. DRCN [3] has a deeply recursive structure that reuses the same convolutional filters repeatedly. This strategy allows the network to implement a deep architecture without increasing the number of parameters significantly. EDSR [24] removes batch normalization and further deepens the network to establish a new benchmark in SR. RDN [25] integrates dense connections with residual ones to extract multi-scale contextual features across multiple layers. This technique enables robust feature fusion, and improves detail preservation and structure consistency in reconstructed images. Deeper networks have achieved remarkable successes in SR tasks, but deepening layers increases computational complexity and constrains their deployment on mobile devices.

### B. Attention Mechanisms for SR

<!-- original heading: "B. Attention Mechanisms for SR" (S016) -->

<!-- src: S017 -->
Attention mechanisms have been extensively explored in the single image super-resolution task. RCAN [6] adopts a residual channel attention framework to refine features across multiple levels for effectively enhancing high-frequency information. PAN [8] focuses on pixel-level attention, which allows the model to selectively emphasize informative spatial regions. HAN [26] further integrates multiple attention types with each other, including channel and spatial attention, to comprehensively capture hierarchical dependencies in feature representations. Due to the powerful representation ability of Transformers, recent methods have shifted towards utilizing Transformers to improve the performance of SISR. SwinIR [27] leverages a Transformer-based architecture with shifted windows to capture both local and global dependencies for enabling effective feature interaction. Building upon this, ELAN [28] adopts shifted convolutions to efficiently extract local structural information, and designs a group-wise self-attention (GMSA) module to effectively capture long-range dependency. Omni-SR [29] uses an omni-dimension feature aggregation scheme and a multi-scale hierarchical aggregation scheme, and achieves a state-of-the-art SR. Furthermore, RGT [30] introduces recursive generalization self-attention with linear complexity to model global dependencies, and combines it with local self-attention to effectively exploit global and local contexts. Li et al. [31] proposed a Transformer-Style lightweight model for SR.

### C. Efficient SR Models

<!-- original heading: "C. Efficient SR Models" (S018) -->

<!-- src: S019 -->
Efficient super-resolution models adopt lightweight networks to reduce computation and memory requirements, and they are suitable for real-time applications and mobile devices. In recent years, a variety of approaches have been proposed to improve computational efficiency of image super-resolution. FSRCNN [32] utilizes a post-upsampling technique to reduce computational overhead. CARN [21] adopts cascading residual blocks with grouped convolutions to achieve competitive SR results, and it maintains a lightweight design. IMDN [33] and RFDN [34] use multi-distillation blocks to extract and fuse features at different scales, achieving impressive results with fewer parameters. BSRN [20] employs blueprint-separable convolutions to optimize convolutional operations, and introduces two effective attention modules to enhance the model ability. The method won the first place in the model complexity track of the NTIRE 2022 Efficient SR Challenge. SAFMN [35] uses a feature pyramid and attention maps to dynamically modulate features based on spatial relevance, balancing reconstruction performance with resource consumption. FMP [37] introduces a Flexible Meta Pruning (FMP) technique for accelerating computations. It combines structured pruning with unstructured pruning during model training. Zheng et al. [38] proposed a lightweight self-modulation feature aggregation network for SR. Although some achievements have been made by existing methods, there remain some improvements to be achieved, such as better balances between reconstruction accuracy and efficiency.

## Methods

<!-- original heading: "III. THE PROPOSED METHOD" (S020) -->

### A. Overall Pipeline of Our Network

<!-- original heading: "A. Overall Pipeline of Our Network" (S021) -->

<!-- src: S022; equations pre-normalized inline in the reader -->
As illustrated in Fig. 2, the proposed Comprehensive Feature Aggregation Network (CFAN) has three sequential processing stages: shallow feature extraction, deep feature extraction based on Omni-Domain Feature Modulation (ODFM), and HR image reconstruction. Among them, ODFM consists of a Hybrid Pixel Attention (HPA) block and a Multi-Scale Channel Attention (MSCA) block. Specifically, given a low-resolution input image I_LR ∈ R^{3×H×W} with height H and width W, we first duplicate the input image four times, and concatenate them to extract shallow features: X_LR = Concat([I_LR, I_LR, I_LR, I_LR]) (1), X_0 = H_SF(X_LR) (2), where H_SF(·) denotes a convolution layer to extract a shallow feature map X_0. The convolutional layer offers an efficient method to map the input image to a high-dimensional feature space.

<!-- src: S023 -->
Next, X_0 is fed into k stacked ODFMs to extract deeper features containing non-local and contextual information: X_i = H_i(X_{i−1}), i = 1, . . . , k (3), where H_i(·) denotes the i-th ODFM, X_i ∈ R^{C×H×W}. To further enhance deep features and refine texture details, we individually fuse the outputs from the subsequent n stacked ODFMs with the shallow feature map X_s ∈ R^{C×H×W}: X_s = φ(W_p(X_LR)) (4), X_i = H_f(H_i(X_{i−1}), X_s), i = k, . . . , k+n (5), where W_p(·) is a 1×1 point-wise convolution, φ(·) is GELU [39], and H_f(·) is the adaptive feature fusion module. In our implementation, k=4 and n=4.

<!-- src: S024 -->
Finally, we apply a 3×3 convolution to smooth feature maps, and use a residual connection with the shallow feature map X_0 to stabilize network training. The final high-resolution image is reconstructed by I_HR = H_RC(Conv_{3×3}(X_{k+n}) + X_0) (6), where Conv_{3×3} represents a 3×3 convolution, and H_RC is a reconstruction module consisting of a 3×3 standard convolution and a pixel-shuffle layer. Following previous works [22], [23], [25], the model is optimized by minimizing the pixel-wise loss L1 between a ground-truth HR image I_HR and its prediction I_SR: L1 = ∥I_HR − I_SR∥_1 (7).

### B. Hybrid Pixel-Attention

<!-- original heading: "B. Hybrid Pixel-Attention" (S025) -->

<!-- src: S026 -->
The pixel attention mechanism enhances feature representation through dynamic pixel-wise weight allocation. Compared to channel and spatial attention mechanisms, it achieves finer-grained modulation by adaptively adjusting receptive fields via attention branches. This capability is particularly valuable for super-resolution, where non-local contextual correlations between image regions assist in recovering lost spatial details during upsampling. While traditional approaches expand receptive fields through larger kernels, deeper architectures, or global self-attention, they incur substantial computational and parametric costs. Swin Transformer [10] alleviates this via local-window self-attention with cross-window shifting, which balances long-range modeling and computational complexity. However, its computational overhead remains prohibitive for high-resolution super-resolution tasks.

<!-- src: S027 -->
Motivated by the success of window-shifting strategy in Swin Transformers, we propose a Hybrid Pixel Attention (HPA) block. As illustrated in Fig. 3, the HPA block sequentially processes the input feature through three complementary components: Local Pixel Attention (LPA), Dense Pixel Attention (DPA), and Sparse Pixel Attention (SPA). Among them, the LPA module employs simple convolutions to extract local spatial patterns. Both DPA and SPA modules are inspired by [7], [40], [41]. Specifically, DPA uses multiple non-overlapping windows to extract features, and employs a fully connected layer to model feature interactions within each window. Subsequently, SPA performs sparse sampling to generate multiple subsets and applies a fully connected layer to capture feature interactions from sparsely sampled regions. By adopting this window expansion strategy, HPA effectively enlarges receptive fields with relatively low computational overhead, enabling the capture of non-local dependencies in images. These three components mainly differ in feature extraction branches.

<!-- src: S028 -->
The general architecture of the pixel attention module is illustrated in Fig. 3. Specifically, given an input feature X ∈ R^{C_in×H×W}, we first apply a 1×1 convolution followed by a GELU activation function to adjust channels dimensions. The transformed features are then split into two groups along the channel dimensions: X_a and X_b. X_a is fed into the feature extraction branch to generate a spatial attention map X_atten, which modulates X_b via element-wise multiplication. A subsequent 1×1 convolution restores the channel dimension to match the original input. To address potential gradient instability caused by repeated element-wise modulation in deeper layers, we introduce layer normalization [42] and residual connection to stabilize training. The complete process can be formalized as: [X_a, X_b] = φ(W_p(X)) (8), X_atten = H_atten(X_a) (9), Y = LN(W_p(X_atten ⊙ X_b)) + X (10), where H_atten(·) represents the attention feature extraction branch.

<!-- src: S029; "undergone the same operations" preserved as printed -->
The processed feature map is then restored to its original shape R^{C×H×W} and combined with the input via a residual connection. These operations enable each pixel to interact with others. In contrast, the SPA module partitions X_a into a regular S×S grid, where each cell corresponds to a spatial region of size H/S×W/S. The resulting tensor is reshaped into dimensions S^2×C×HW/S^2 and undergone the same operations as in the DPA module. This sparse sampling approach allows each pixel to interact with others at distant locations, effectively compensating for the loss of non-local information. Together, these three modules progressively expand the effective receptive field, facilitating comprehensive spatial feature extraction from local textures to non-local contextual information. The operations by the feature extraction branches of the three modules can be formulated as: A_LPA = DWConv_{5×5}(DWConv_{3×3}(X_a)) (11), A_DPA = FC(LN(R_DPA(X_a))) + X_a (12), A_SPA = FC(LN(R_SPA(X_a))) + X_a (13), where DWConv denotes depth-wise convolutions, R_DPA/R_SPA are reshaping operations, and FC is the fully connected operation.

### C. Multi-Scale Channel Attention

<!-- original heading: "C. Multi-Scale Channel Attention" (S030) -->

<!-- src: S031 -->
As network depth increases, critical information tends to become increasingly dispersed along the channel dimension, leading to attenuation of key feature response. To mitigate this issue during the progressive expansion of receptive fields, it is necessary to recalibrate channel-wise information. We adopt an aggregated interaction strategy [43] to promote effective information propagation and fusion between spatial and channel dimensions with low computational overhead. This strategy first performs channel-wise reweighting on multi-scale features obtained through downsampling, and then aggregates the reweighted features with input features to enhance cross-dimensional feature interaction.

<!-- src: S032 -->
The detailed structure of the proposed MSCA module is depicted in Fig. 4. Specifically, given a feature map X ∈ R^{C×H×W} output by the HPA block, we first use a 1×1 point-wise convolution to expand its feature channels, producing an intermediate feature map X_1 ∈ R^{2C×H×W}. Next, we divide X_1 into two parts, denoted as Z and Q. Z is used to aggregate contextual information across spatial and channel dimensions, while Q serves as the query features to interact with the aggregated features. In the feature aggregation process, we first adopt the TokenLearner [44] module to compress the spatial information of Z, generating three sets of channel-wise importance weights corresponding to different scales. These weights guide the model to emphasize informative channels across multiple scales. Subsequently, a series of 3×3 depthwise convolutions and average pooling operations are applied to Z for extracting hierarchical multi-scale features: {A^C_0, A^C_1, A^C_2} = H_TL(Z) (14), Z_0 = W_d(Z) (15), Z_1 = W_d(Pool(Z_0)), Z_2 = W_d(Pool(Z_1)) (16), where H_TL is TokenLearner, W_d is a 3×3 depthwise convolution, and Pool denotes average pooling.

<!-- src: S033 -->
The multi-scale features, after channel-wise re-weighting guided by the importance weights, are upsampled to the original resolution and fused via element-wise summation. The aggregated feature map is then passed through a 1×1 convolution to integrate cross-channel information, generating a modulation feature P. Finally, an element-wise multiplication between Q and P facilitates cross-dimensional information interaction. These processing operations can be formulated as: Z_out = Σ_{i=0}^{2} A^C_i ⊙ UP(Z_i) (17), Y = X ⊙ W_p(Z_out) (18), where UP represents upsampling efficiently implemented by nearest-neighbor interpolation, and W_p presents a 1×1 point-wise convolution. The aggregated features then interact with the query features Q to produce the final output of MSCA, which is further fused with the input via a residual connection to preserve information and stabilize training.

### D. Adaptive Feature Fusion

<!-- original heading: "D. Adaptive Feature Fusion" (S034) -->

<!-- src: S035 -->
In image SR tasks, high-frequency details are recovered to mitigate blurring artifacts, and low-frequency information is preserved to avoid geometric distortions. Hence, we need to design a SR model that can extract high-frequency and low-frequency signals simultaneously for optimizing super-resolution. Decoding branches often use upsampling or concatenation to restore high-frequency information lost during the downsampling process of high-resolution images. However, overemphasis on high-frequency recovery may reduce the network's ability to retain low-frequency structural coherence, leading to suboptimal reconstructions. To make an optimized trade-off, traditional SR frameworks typically employ long-skip connections [48], which primarily assist in gradient flow stabilization and low-frequency component preservation. Combining deep features with shallow ones can enhance the network's ability to retain low-frequency structures. Inspired by PIDNet [49], we adopt an Adaptive Feature Fusion (AFF) module to balance high-frequency details and low-frequency structural information. The structure of AFF is shown in Fig. 2. Let X_d and X_0 respectively represent deep and basic features, the fusion process can be expressed as: α = sigmoid(φ(W_p(X_0))) ⊙ φ(W_p(X_d)) (19), X_out = X_0 · (1 − α) + X_d · α (20), where α is used to enhance semantic information of deep features, and (1−α) is adopted to supplement edge details. Obviously, semantic features and spatial details are complementary to each other.

## Results

<!-- original heading: "IV. EXPERIMENTS" (S036).
     Experimental setup (A. Implementation Details) is a separate subsection in the source and kept
     distinct from ablations/comparisons below. -->

### A. Implementation Details

<!-- original heading: "A. Implementation Details" (S037) -->

<!-- src: S038 -->
1) Datasets and Metrics: Following prior studies [22], [30], [50], we used DIV2K [51] and Flickr2K [24] as the training datasets. For evaluation, we used five widely recognized benchmark datasets, which are Set5 [52], Set14 [53], BSD100 [54], Urban100 [55], and Manga109 [56]. The performance is assessed using the Peak Signal to Noise Ratio (PSNR) and the Structural Similarity Index Measure (SSIM). All PSNR and SSIM values were computed on the Y channel of restored images.

<!-- src: S039; text cites "Adam [57]" and "Cosine Annealing scheme [58]" but the reference list has
     [57]=SGDR (cosine annealing) and [58]=Adam — the two citation numbers appear swapped in the
     source; preserved as printed -->
2) Implementation Details: The proposed CFAN consists of 8 ODFMs and 4 AFFs, and the number of channels is set to 48. To increase training samples, we adopted some data augmentation techniques, including random rotations of 90°, 180° and 270°, as well as horizontal flips. In addition, the mini-batch size is set to 32 and the patch size of each LR input is set to 48×48 pixels. The model was optimized using the Adam [57] optimizer with β1=0.9 and β2=0.99. The initial learning rate is set to 1×10^{-3} and is progressively reduced to a minimum of 1×10^{-7} using the Cosine Annealing scheme [58]. The L1 loss function is used for optimization over a total of 1×10^6 iterations.

### B. Ablation Study and Analysis

<!-- original heading: "B. Ablation Study and Analysis" (S040) -->

<!-- src: S041 -->
To deeply understand the key components of CFAN, we conducted comprehensive ablation studies to evaluate the contributions of HPA, MSCA and AFF. The corresponding results are presented in TABLE I.

<!-- src: S042; source numbering irregularity: this item has no "1)" prefix while the following two
     are "2)" and "3)" — preserved as printed -->
Effectiveness of HPA: The HPA block adopts a sequential structure, where three sub-modules are connected in series. To verify the effectiveness of capturing both local and non-local information, we further performed ablations on these two parts. Removing the LPA module leads to a PSNR drop of 0.12dB on the Urban100 and 0.25dB on the Manga109, while removing both the DPA and SPA modules causes a drop of 0.14dB on Urban100 and 0.19dB on the Manga109. These results demonstrate that relying solely on local or non-local features is insufficient for accurate detail reconstruction.

<!-- src: S043 -->
To further validate the effectiveness of the serial designs involving LPA, DPA, and SPA, we conducted two more ablation studies. In one variant, we rearrange the module order to LPA-SPA-DPA, and in the other we adopt a parallel structure. On the Manga109 dataset, the PSNR decreases by 0.10dB and 0.18dB, respectively. These findings suggest that the original serial design facilitates more effective spatial feature extraction. Furthermore, to investigate the impact of specific operations within the feature extraction branches of the DPA and SPA modules, we performed three additional ablation studies: removing Layer Normalization (LN), replacing LN with Softmax, and substituting linear layers with convolutional layers. As a result, PSNR drops by 0.24dB, 0.25dB, and 0.27dB on the Manga109, respectively. These results indicate that fully connected layers are more effective than convolutions for restoring structural details, and that LN contributes to stabilizing gradient flow during training.

<!-- src: S044 -->
Subsequently, we adjust the window sizes of the DPA and SPA modules, and the experimental results are presented in TABLE II. With the window size increasing from 4 to 6, the PSNR is consistently improved due to expanded receptive fields. However, the window size beyond 6 leads to a significant rise in parameter count, and also causes unstable training and a decline in reconstruction performance. Finally, we employed Local Attribution Map (LAM) and Diffusion Index (DI) to analyze the extent information utilized by different models during reconstruction. Generally, more information usage correlates with better reconstruction performance. As illustrated in Fig. 5, our CFAN demonstrates a denser distribution of activated features within the same patch size during the reconstruction process. These analyses validate that the HPA block enables CFAN to capture more comprehensive spatial information for optimizing its detail recovery capabilities.

<!-- src: S045; "which result in" preserved as printed -->
2) Effectiveness of MSCA: The MSCA module adopts an aggregated interaction strategy to model the latent correlations between spatial and channel dimensions. To verify its effectiveness, we conducted four ablation studies while keeping the overall model parameters comparable across variants. The results are presented in TABLE I. In the first experiment, we remove the MSCA module, which result in PSNR reductions of 0.12dB and 0.26dB on Urban100 and Manga109 datasets, respectively. This validates the critical role of the MSCA module in reconstruction accuracy. In the second experiment, we remove the TokenLearner module responsible for generating adaptive channel-wise weights. This leads to a reduction of 0.23dB in PSNR on the Manga109, underscoring the importance of dynamic multi-scale reweighting in capturing discriminative features. The third experiment removes the interaction operation between the aggregated features and the query features, which is crucial for cross-dimensional information exchange. As a result, PSNR drops by 0.06dB, 0.05dB, 0.05dB, and 0.16dB on the four datasets, respectively, indicating that this interaction operation effectively enhances cross-dimensional information exchange. Finally, we replace the MSCA module with a conventional channel attention module [34]. It results in significant performance degradation, particularly on Urban100 and Manga109, with PSNR reductions of 0.24dB and 0.50dB, respectively. This finding suggests that relying solely on channel attention may weaken the network's generalization ability.

<!-- src: S046 -->
3) Effectiveness of AFF: The core idea of this module is to fuse low-frequency structural information and contextual semantic features. To validate the effectiveness of AFF, we conduct an ablation study by removing it from the proposed network. As shown in TABLE I, removing AFF reduces the number of network parameters by only 8%, but the average PSNR decreases by 0.16dB. Furthermore, we integrated the AFF module into other networks with varying architectures. The experimental results in TABLE III demonstrate that adding the AFF module introduces approximately 10K extra parameters and achieves a PSNR improvement of nearly 0.04dB on the DIV2K validation set. These findings highlight the capability of AFF to enhance the performance with minimal impact on model complexity.

### C. Comparisons With State-of-the-Art Methods

<!-- original heading: "C. Comparisons With State-of-the-Art Methods" (S047) -->

<!-- src: S048; NOTE source-level citation-number mismatches: "IMDN [13]" (IMDN is [33] in the list;
     [13] is the vast-receptive-field attention paper) and "RLFN [42]" (RLFN is [46]; [42] is Layer
     normalization). Preserved as printed. "state-of-art" preserved as printed. -->
We compared CFAN with several state-of-art lightweight SR methods, including VDSR [22], IMDN [13], RFDN [34], SMSR [45], ShuffleMixer [47], RLFN [42], SAFMN [35], HAFRN [14], OSFFNet [36] and FMP [37].

<!-- src: S049 -->
1) Quantitative comparisons: TABLE IV presents the quantitative comparison results on benchmark datasets with the upscaling factors of ×2, ×3 and ×4. PSNR/SSIM values are computed on the Y-channel for each dataset. Params represents the number of parameters, and FLOPs refers to the number of floating-point operations. We measured them on an HR image with a resolution of 1280×720 pixels. Taking the ×4 SR task as an example, the CFAN achieves notable efficiency improvements with only 73% and 56% of the parameters of RLFN and IMDN, respectively, and also obtains superior PSNR improvements of 0.2 dB and 0.29 dB on the Urban100 dataset. Compared with FMP, our model requires approximately 55% fewer parameters yet achieves comparable performance across five benchmark datasets. In addition, when compared with OSFFNet, CFAN achieves similar or even better results while utilizing only 72% of its parameters. Notably, the CFAN exhibits a remarkable performance improvement on the Manga109 dataset. The dataset consists of manga-style images that differ considerably from the training set. These results show the strong generalization ability of the CFAN.

<!-- src: S050; "RLFN [42]" mismatch as above, preserved -->
To further evaluate the efficiency of our approach, we conducted comparisons with five representative methods, which are RLFN [42], ShuffleMixer [47], SAFMN [35], BSRN [20], and HAFRN [14]. Efficiency metrics are GPU memory usage (#GPU Mem.) and average inference time (#Avg. Time) for ×4 SR tasks. The GPU memory usage is measured as the peak usage during inference. The average inference time is calculated over 50 test images with a resolution of 320×180 pixels using an NVIDIA RTX 3060 GPU. As detailed in TABLE V, the proposed method demonstrates substantial advantages over state-of-the-art techniques. Compared with BSRN and ShuffleMixer, the CFAN achieves comparable inference speed and significantly reduces memory consumption. Although SAFMN shows lower memory and faster inference speed than CFAN, it suffers from significant performance degradation. All comparisons in TABLE IV and TABLE V indicate that the proposed CFAN achieves an effective balance between model complexity and reconstruction accuracy.

<!-- src: S051; NOTE "SAFMN [7]" is another source-level mismatch (SAFMN is [35]; [7] is the attention
     retractable transformer paper). "these compared approaches" preserved as printed. -->
2) Qualitative comparisons: We performed qualitative comparisons of the CFAN model with five representative lightweight SR models, including VDSR [22], IMDN [13], SAFMN [7], ShuffleMixer [47], and RFDN [34]. The visual results by these methods are illustrated in Fig. 6. Compared with these compared approaches, the CFAN model is capable of reconstructing sharper and more precise edges as well as repetitive patterns. The edge contours of floor tiles and the densely aligned railings are clearer than other methods. These comparisons clearly demonstrate the effectiveness of the CFAN in recovering structural details and high-frequency information from low-resolution inputs.

## Discussion

<!-- No standalone Discussion section in this paper. Discussion-style analysis is embedded in
     IV.B/IV.C (ablation interpretation and comparison analysis, S042-S046, S049-S051) and the
     future-work paragraph of the Conclusion (S054). -->

## Conclusion

<!-- original heading: "V. CONCLUSION" (S052) -->

<!-- src: S053 -->
To reduce computational complexity and memory consumption, we propose a Comprehensive Feature Aggregation Network (CFAN) for efficient image super-resolution. The proposed CFAN mainly consists of several cascaded Omni-Domain Feature Modulation (ODFM) blocks. Each ODFM includes an effective Hybrid Pixel Attention block (HPA), consisting of Local Pixel Attention (LPA), Dense Pixel Attention (DPA) and Sparse Pixel Attention (SPA). The hybrid attention provides larger receptive fields but with low computational complexity. To further enhance spatial details in the reconstruction process, we introduce an Adaptive Feature Fusion (AFF) module to facilitate interactions between low-level structural information and high-level semantic information. Extensive experiments on public benchmark datasets indicate that the proposed model is more efficient than state-of-the-art methods.

<!-- src: S054 -->
In future work, we plan to incorporate frequency-domain representations [60] to further enrich the network's ability to capture fine-grained details across multiple scales. Additionally, we aim to reduce the computational cost of normalization by exploring adaptive alternatives to conventional methods, such as DyT [61].

## Acknowledgments

<!-- No separate Acknowledgment section in this paper; the first-page manuscript footnote (S011)
     carries the funding statement. Metadata portion of S011 kept under Other. -->

<!-- src: S011 (funding portion) -->
This work was supported in part by the National Natural Science Foundation of China under Grant 62272308, and in part by the Capacity Construction Project of Shanghai Local Colleges under Grant 23010504100.

## References

<!-- original heading: "REFERENCES" (S055). Entries [1]-[61] split from glued multi-reference blocks
     (src S056-S065). Note: [57] SGDR and [58] Adam appear swapped relative to the in-text citations
     ("Adam [57]", "Cosine Annealing scheme [58]"); [59] (DRRN) is never cited in the extracted text.
     Preserved as printed. -->

[1] C. Dong, C. C. Loy, K. He, and X. Tang, "Learning a deep convolutional network for image super-resolution," in Proc. 13th Eur. Conf. Comput. Vis. (ECCV), 2014, pp. 184–199.

[2] C. Dong, C. C. Loy, K. He, and X. Tang, "Image super-resolution using deep convolutional networks," IEEE Trans. Pattern Anal. Mach. Intell., vol. 38, no. 2, pp. 295–307, Feb. 2016.

[3] J. Kim, J. K. Lee, and K. M. Lee, "Deeply-recursive convolutional network for image super-resolution," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016, pp. 1637–1645.

[4] F. Yuan, Y. Peng, Q. Huang, and X. Li, "A bi-directionally fused boundary aware network for skin lesion segmentation," IEEE Trans. Image Process., vol. 33, pp. 6340–6353, 2024.

[5] F. Yuan, Z. Zhang, and Z. Fang, "An effective CNN and transformer complementary network for medical image segmentation," Pattern Recognit., vol. 136, Apr. 2023, Art. no. 109228.

[6] Y. Zhang, K. Li, K. Li, L. Wang, B. Zhong, and Y. Fu, "Image super-resolution using very deep residual channel attention networks," in Proc. Eur. Conf. Comput. Vis. (ECCV), 2018, pp. 286–301.

[7] J. Zhang, Y. Zhang, J. Gu, Y. Zhang, L. Kong, and X. Yuan, "Accurate image restoration with attention retractable transformer," 2023, arXiv:2210.01427.

[8] H. Zhao, X. Kong, J. He, Y. Qiao, and C. Dong, "Efficient image super-resolution using pixel attention," in Proc. Comput. Vis. (ECCV), 2020, pp. 56–72.

[9] K. Li, F. Yuan, and C. Wang, "An effective multi-scale interactive fusion network with hybrid Transformer and CNN for smoke image segmentation," Pattern Recognit., vol. 159, Mar. 2025, Art. no. 111177.

[10] Z. Liu et al., "Swin transformer: Hierarchical vision transformer using shifted windows," in Proc. IEEE/CVF Int. Conf. Comput. Vis., 2021, pp. 9992–10022.

[11] A. Dosovitskiy et al., "An image is worth 16x16 words: Transformers for image recognition at scale," 2021, arXiv:2010.11929.

[12] K. Li, F. Yuan, and C. Wang, "Frequency-space interaction with hierarchical aggregation network for lightweight smoke image segmentation," IEEE Trans. Consum. Electron., vol. 71, no. 2, pp. 2632–2643, May 2025.

[13] L. Zhou et al., "Efficient image super-resolution using vast-receptive-field attention," in Proc. Eur. Conf. Comput. Vis., 2022, pp. 256–272.

[14] K. Wang, X. Yang, and G. Jeon, "Hybrid attention feature refinement network for lightweight image super-resolution in metaverse immersive display," IEEE Trans. Consum. Electron., vol. 70, no. 1, pp. 3232–3244, Feb. 2024.

[15] X. Liao, X. Wei, and M. Zhou, "Minimax concave penalty regression for superresolution image reconstruction," IEEE Trans. Consum. Electron., vol. 70, no. 1, pp. 2999–3007, Feb. 2024.

[16] W. Shi et al., "Real-time single image and video super-resolution using an efficient sub-pixel convolutional neural network," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016, pp. 1874–1883.

[17] Z. Hui, X. Wang, and X. Gao, "Fast and accurate single image super-resolution via information distillation network," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2018, pp. 723–731.

[18] X. Zhang, H. Zeng, and L. Zhang, "Edge-oriented convolution block for real-time super resolution on mobile devices," in Proc. 29th ACM Int. Conf. Multimedia, 2021, pp. 4034–4043.

[19] A. Ignatov et al., "Efficient and accurate quantized image super-resolution on mobile NPUs, mobile AI & AIM 2022 challenge: Report," in Proc. Eur. Conf. Comput. Vis., 2022, pp. 92–129.

[20] Z. Li et al., "Blueprint separable residual network for efficient image super-resolution," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2022, pp. 833–843.

[21] N. Ahn, B. Kang, and K.-A. Sohn, "Fast, accurate, and lightweight super-resolution with cascading residual network," in Proc. Eur. Conf. Comput. Vis. (ECCV), 2018, pp. 252–268.

[22] J. Kim, J. K. Lee, and K. M. Lee, "Accurate image super-resolution using very deep convolutional networks," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016, pp. 1646–1654.

[23] W.-S. Lai, J.-B. Huang, N. Ahuja, and M.-H. Yang, "Deep laplacian pyramid networks for fast and accurate super-resolution," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2017, pp. 624–632.

[24] B. Lim, S. Son, H. Kim, S. Nah, and K. M. Lee, "Enhanced deep residual networks for single image super-resolution," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. Workshops, 2017, pp. 136–144.

[25] Y. Zhang, Y. Tian, Y. Kong, B. Zhong, and Y. Fu, "Residual dense network for image super-resolution," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2018, pp. 2472–2481.

[26] B. Niu et al., "Single image super-resolution via a holistic attention network," in Proc. 16th Eur. Conf. Comput. Vis. (ECCV), 2020, pp. 191–207.

[27] J. Liang, J. Cao, G. Sun, K. Zhang, L. Van Gool, and R. Timofte, "SwinIR: Image restoration using Swin transformer," in Proc. IEEE/CVF Int. Conf. Comput. Vis., 2021, pp. 1833–1844.

[28] X. Zhang, H. Zeng, S. Guo, and L. Zhang, "Efficient long-range attention network for image super-resolution," in Proc. Eur. Conf. Comput. Vis., 2022, pp. 649–667.

[29] H. Wang, X. Chen, B. Ni, Y. Liu, and J. Liu, "Omni aggregation networks for lightweight image super-resolution," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023, pp. 22378–22387.

[30] Z. Chen, Y. Zhang, J. Gu, L. Kong, and X. Yang, "Recursive generalization transformer for image super-resolution," in Proc. 12th Int. Conf. Learn. Represent., 2024, pp. 1–12.

[31] F. Li, R. Cong, J. Wu, H. Bai, M. Wang, and Y. Zhao, "Transformer-style ConvNet for lightweight image super-resolution," Int. J. Comput. Vis., vol. 133, no. 1, pp. 173–189, 2025.

[32] C. Dong, C. C. Loy, and X. Tang, "Accelerating the super-resolution convolutional neural network," in Proc. 14th Eur. Conf. Comput. Vis. (ECCV), 2016, pp. 391–407.

[33] Z. Hui, X. Gao, Y. Yang, and X. Wang, "Lightweight image super-resolution with information multi-distillation network," in Proc. 27th ACM Int. Conf. Multimedia, 2019, pp. 2024–2032.

[34] J. Liu, J. Tang, and G. Wu, "Residual feature distillation network for lightweight image super-resolution," in Proc. Eur. Conf. Comput. Vis. Workshops (ECCV), 2020, pp. 41–55.

[35] L. Sun, J. Dong, J. Tang, and J. Pan, "Spatially-adaptive feature modulation for efficient image super-resolution," in Proc. IEEE/CVF Int. Conf. Comput. Vis., 2023, pp. 13190–13199.

[36] Y. Wang and T. Zhang, "OSFFNet: Omni-stage feature fusion network for lightweight image super-resolution," in Proc. AAAI Conf. Artif. Intell., 2024, pp. 5660–5668.

[37] Y. Zhang, K. Zhang, L. Van Gool, M. Danelljan, and F. Yu, "Lightweight image super-resolution via flexible meta pruning," in Proc. 12th Int. Conf. Learn. Represent. (ICLR), 2024, pp. 1–10.

[38] M. Zheng, L. Sun, J. Dong, and J. Pan, "SMFANet: A lightweight self-modulation feature aggregation network for efficient image super-resolution," in Proc. Eur. Conf. Comput. Vis. (ECCV), 2024, pp. 359–375.

[39] D. Hendrycks and K. Gimpel, "Gaussian error linear units (GELUs)," 2023, arXiv:1606.08415.

[40] Z. Tu et al., "Maxim: Multi-axis MLP for image processing," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2022, pp. 5769–5780.

[41] H. Liu, Z. Dai, D. So, and Q. V. Le, "Pay attention to MLPs," in Proc. 35th Adv. Neural Inf. Process. Syst., 2021, pp. 9204–9215.

[42] J. L. Ba, J. R. Kiros, and G. E. Hinton, "Layer normalization," 2016, arXiv:1607.06450.

[43] J. Yang, C. Li, X. Dai, and J. Gao, "Focal modulation networks," in Proc. 36th Adv. Neural Inf. Process. Syst., 2022, pp. 4203–4217.

[44] M. S. Ryoo, A. Piergiovanni, A. Arnab, M. Dehghani, and A. Angelova, "TokenLearner: What can 8 learned tokens do for images and videos?" 2022, arXiv:2106.11297.

[45] L. Wang et al., "Exploring sparsity in image super-resolution for efficient inference," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2021, pp. 4917–4926.

[46] F. Kong et al., "Residual local feature network for efficient super-resolution," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2022, pp. 766–776.

[47] L. Sun, J. Pan, and J. Tang, "Shufflemixer: An efficient ConvNet for image super-resolution," in Proc. Adv. Neural Inf. Process. Syst., 2022, pp. 17314–17326.

[48] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016, pp. 770–778.

[49] J. Xu, Z. Xiong, and S. P. Bhattacharyya, "PIDNet: A real-time semantic segmentation network inspired by PID controllers," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023, pp. 19529–19539.

[50] W. Li, K. Zhou, L. Qi, N. Jiang, J. Lu, and J. Jia, "LAPAR: Linearly-assembled pixel-adaptive regression network for single image super-resolution and beyond," in Proc. Adv. Neural Inf. Process. Syst., 2020, pp. 20343–20355.

[51] R. Timofte, E. Agustsson, L. Van Gool, M.-H. Yang, and L. Zhang, "NTIRE 2017 challenge on single image super-resolution: Methods and results," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. Workshops, 2017, pp. 114–125.

[52] M. Bevilacqua, A. Roumy, C. Guillemot, and M. L. Alberi-Morel, "Low-complexity single-image super-resolution based on nonnegative neighbor embedding," in Proc. 23rd BMVC, 2012, pp. 1–135.

[53] R. Zeyde, M. Elad, and M. Protter, "On single image scale-up using sparse-representations," in Proc. 7th Int. Conf. Curves Surfaces, 2012, pp. 711–730.

[54] P. Arbelaez, M. Maire, C. Fowlkes, and J. Malik, "Contour detection and hierarchical image segmentation," IEEE Trans. Pattern Anal. Mach. Intell., vol. 33, no. 5, pp. 898–916, May 2010.

[55] J.-B. Huang, A. Singh, and N. Ahuja, "Single image super-resolution from transformed self-exemplars," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2015, pp. 5197–5206.

[56] Y. Matsui, K. Ito, Y. Aramaki, A. Fujimoto, T. Ogawa, T. Yamasaki, and K. Aizawa, "Sketch-based manga retrieval using manga109 dataset," Multimedia Tools Appl., vol. 76, pp. 21811–21838, Oct. 2017.

[57] I. Loshchilov and F. Hutter, "SGDR: Stochastic gradient descent with warm restarts," 2017, arXiv:1608.03983.

[58] D. P. Kingma, "Adam: A method for stochastic optimization," 2014, arXiv:1412.6980.

[59] Y. Tai, J. Yang, and X. Liu, "Image super-resolution via deep recursive residual network," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2017, pp. 3147–3155.

[60] Y. Cui, W. Ren, X. Cao, and A. Knoll, "Image restoration via frequency selection," IEEE Trans. Pattern Anal. Mach. Intell., vol. 46, no. 2, pp. 1093–1108, Feb. 2024.

[61] J. Zhu, X. Chen, K. He, Y. LeCun, and Z. Liu, "Transformers without normalization," in Proc. Comput. Vis. Pattern Recognit. Conf., 2025, pp. 14901–14911.

## Other

### Figure and table captions

Fig. 1. Comparisons of ×4 image super-resolution on the Urban100 dataset. <!-- C001, p.2 -->

Fig. 2. Comprehensive Feature Aggregation Network (CFAN). (a) The structure of CFAN; (b) Omni-Domain Feature Modulation (ODFM) including a Hybrid Pixel Attention block (HPA) and a Multi-Scale Channel Attention (MSCA) module; (c) Adaptive Feature Fusion (AFF) for texture details and structural information. <!-- C002, p.3 -->

Fig. 3. Three Different Pixel Attention. (a) The structure of the three attention modules. Feature extraction blocks for (b) Local Pixel Attention (LPA), (c) Dense Pixel Attention (DPA), and (d) Sparse Pixel Attention (SPA). <!-- C003, p.4 -->

Fig. 4. The structure of the proposed Multi-Scale Channel Attention (MSCA) module. (a) MSCA; (b) Token Learner. <!-- C004, p.5 -->

TABLE I ABLATION STUDY ON NETWORK DESIGN FOR CFAN <!-- C005, p.6 -->

TABLE II QUANTITATIVE COMPARISONS OF DIFFERENT WINDOW SIZES IN THE HPA MODULE <!-- C006, p.7 -->

Fig. 5. Comparisons of LAMs and DIs with the state-of-the-art methods on ×4 SR. <!-- C007, p.7 -->

TABLE III EFFECTS OF THE PROPOSED AFF. THE RESULTS (×4) ARE EVALUATED ON THE DIV2K VALIDATION SET <!-- C008, p.7 -->

Fig. 6. Visual comparisons of state-of-the-art SR models for the ×4 upscaling task. <!-- C009, p.8 -->

TABLE IV COMPARISONS OF EFFICIENT SR NETWORK ON FIVE BENCHMARK DATASETS <!-- C010, p.9 -->

TABLE V MEMORY AND INFERENCE TIME COMPARISONS ON ×4 SR <!-- C011, p.9 -->

### Article metadata

<!-- src: S011 (metadata portion) -->
Received 1 April 2025; revised 11 June 2025 and 27 July 2025; accepted 27 August 2025. Date of publication 1 September 2025; date of current version 8 December 2025. (Corresponding author: Feiniu Yuan.) Feiniu Yuan is with Shanghai Normal University, Shanghai 200234, China (e-mail: yfn@ustc.edu.cn). Changhong Xie and Biao Xiang are with Shanghai Normal University, Shanghai 200234, China. Digital Object Identifier 10.1109/TCE.2025.3605068
