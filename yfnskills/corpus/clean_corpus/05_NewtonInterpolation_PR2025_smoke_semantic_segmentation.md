<!--
FnyPro-1 Stage 00 Wave 3 Agent G clean corpus
Paper_ID: 05_NewtonInterpolation_PR2025_smoke_semantic_segmentation
Source: /workspace/05_NewtonInterpolation_PR2025_smoke_semantic_segmentation.md (**Original:** blocks only)
Reconstruction notice: the source extraction had severe two-column interleaving. Paragraph order was
rebuilt by joining dangling sentence fragments across blocks (e.g. S006->S009, S044->S040, S078->S069,
S068->S076, S048->S046, S022->S014-orphan). Equations (4), (6), (9), (19) had fraction bars broken across
blocks and were reassembled; lost superscripts restored with caret/underscore notation (e.g. 0.1^n).
Excluded: Chinese text, reader nav/glossary, page footer S007 (DOI/dates), corresponding-author footnote
inside S006, reference entries (S077-S081, interleaved beyond reliable reconstruction), author bios
(S080/S082-S084, flagged medium confidence), and numeric table rows embedded in body blocks
(S039/S051-S059/S062/S070/S072-S075 fragments; tables exist as images in the reader).
"[...]" marks text lost at column boundaries. No grammar rewriting; authorial wording preserved.
STYLE CAVEAT (from authorship_weights.csv): CRediT assigns Writing - original draft to Guiqian Wang.
-->

# A newton interpolation network for smoke semantic segmentation

Feiniu Yuan a,d,e, Guiqian Wang b,d,e,*, Qinghua Huang c, Xuelong Li c

a College of Information, Mechanical and Electrical Engineering, Shanghai Normal University (SHNU), Shanghai 201418, China
b Mathematics and Science College, Shanghai Normal University, Shanghai 200233, China
c School of Artificial Intelligence, Optics and Electronics (iOPEN), Northwestern Polytechnical University, Xi'an 710072, China
d Research Base of Online Education for Shanghai Middle and Primary Schools, Shanghai Normal University, Shanghai 201418, China
e Shanghai Engineering Research Center of Intelligent Education and Bigdata, Shanghai Normal University, Shanghai 200234, China

Keywords: Smoke segmentation; Newton interpolation; Newton interpolation module; Structured information; Deep neural network

## Abstract

Smoke has large variances of visual appearances that are very adverse to visual segmentation. Furthermore, its semi-transparency often produces highly complicated mixtures of smoke and backgrounds. These factors lead to great difficulties in labelling and segmenting smoke regions. To improve accuracy of smoke segmentation, we propose a Newton Interpolation Network (NINet) for visual smoke semantic segmentation. Unlike simply concatenating or point-wisely adding multi-scale encoded feature maps for information fusion or re-usage, we design a Newton Interpolation Module (NIM) to extract structured information by analyzing the feature values in the same position but from encoded feature maps with different scales. Interpolated features by our NIM contain long-range dependency and semantic structures across different levels, but traditional fusion of multi-scale feature maps cannot model intrinsic structures embedded in these maps. To obtain multi-scale structured information, we repeatedly use the proposed NIM at different levels of the decoding stages. In addition, we use more encoded feature maps to construct a higher order Newton interpolation polynomial for extracting higher order information. Extensive experiments validate that our method significantly outperforms existing state-of-the-art algorithms on virtual and real smoke datasets, and ablation experiments also validate the effectiveness of our NIMs.

## 1. Introduction

In daily life, fires are one of the major disasters that endanger public safety. Visual fire detection methods require to recognize and localize visual objects of smoke and flame. Detecting smoke can provide earlier fire warnings than flames, because smoke often emerges first in most of fires. In most cases, fires are usually caused by explosions, dropped cigarettes or aging electrical appliances, and so on. Smoke is not only a significant clue of fires at their early stages, but also is diffusive everywhere and prominent after fires break out.

[...] algorithms attempt to separate smoke regions from cluttered backgrounds using techniques of image segmentation. It is very important for firefighters or decision makers to analyze possible safe areas, predict fire developing trends, and draw up evacuation plans. Smoke segmentation can be used for simulating smoke dynamics, estimating fire spreading trends and human evacuations. In addition, smoke segmentation methods can provide more accurate fire detection than object detection methods. Early smoke semantic segmentation algorithms mainly rely on handcrafted features. Due to the large variance of smoke visual appearances, it is very difficult to manually design proper features for smoke segmentation.

Visual fire alarming can be mainly implemented in three ways, which are smoke recognition, detection and segmentation. Image smoke recognition methods [1,2] have been fully investigated, but they lack spatial information about fires. There are lots of visual smoke detection algorithms that have been proposed for forest fire surveillance [3,4], video surveillance [5–7], general fire detection [8–10], and so on. Recently, smoke segmentation methods [11,12] have paid more attentions to pixel-wise localization of smoke regions. These kinds of Convolutional Neural Networks (CNNs) can automatically extract powerful features from images and provide robust representations in many computer vision tasks [13], avoiding complicated designs of hand-crafted features. Semantic segmentation is a position-sensitive task that requires high-resolution representations to complete accurate positioning. There are two main kinds of semantic segmentation paradigms, as shown in Fig. 1(a) and 1(b). The first one uses a backbone network to encode an input image to produce low-resolution feature maps but with contextual information, and then it gradually recovers high-resolution feature maps from these low-resolution ones, such as SegNet [14], U-Net [15]. To compensate for the loss of spatial information during down-sampling, short-cut connections are widely used. The second one does not reduce the sizes of feature maps much using atrous convolutions [16] except for several low layers. Thus, it can obtain large receptive fields and avoid loss of spatial resolutions at the same time. Finally, these methods use different strategies [17,18] to up-sample feature maps to the sizes of original images and enhance high-resolution representations for end-to-end predictions [19,20].

Smoke is a kind of continuous fluids, so it certainly has common properties of fluids, such as time-varying colors, shapes, scales and semitransparency. As shown in Fig. 2, smoke has very large variances of colors, textures, shapes and semi-transparency, and it is often confused with clouds and fog. These fluid properties directly lead to poor segmentation results. Therefore, we need to design specialized network structures to extract robust features for smoke.

In this paper, to solve above-mentioned challenging problems, we propose a Newton Interpolation Network (NINet) for smoke semantic segmentation. Most existing methods simply concatenate or add multiscale maps of encoded features for information fusion, but our method designs a Newton Interpolation Module (NIM) to extract structured information by fully analyzing the feature values in the same position but from feature maps with different scales. The main contributions of this paper can be summarized as follows:

1) Our NIM adopts Newton Interpolation to extract structured information from sequential feature values in the same position but from several feature maps with different scales. Structured information is especially useful for extracting long-range dependency. Traditional methods adopt simple concatenation or point-wise sum to implement information fusion or re-usage, but these manners cannot efficiently extract structured information.

2) To fully capture multi-scale information, we repeatedly stack several NIMs at different levels of decoding stages. Each level NIM is responsible for extracting specific scale information. Fusing features by different NIMs include multiple scale information, thus we can further improve scale invariance of decoded features.

3) We propose to use more feature maps to construct a higher order Newton interpolation polynomial for capturing structured and scaleinvariance information. High order information significantly enhances spatial details and contextual semantics. To further improve segmentation accuracy, Newton interpolations with different orders are used for different decoding stages. In addition, we use a direct short connection for further enhancement of spatial details.

This paper is organized as follows. Section 2 describes related work on image semantic segmentation and smoke segmentation. In Section 3, we describe the main idea of this paper. Section 4 presents experiments and analysis. At last, we conclude this paper in Section 5.

## 2. Related work

In this section, we review existing techniques commonly used for image semantic segmentation, such as reduction and restoration of resolutions, maintenance of high-resolution representations, and fusion of multi-scale features. In addition, we also mention some previous work related to semantic segmentation of smoke images.

### 2.1. Semantic segmentation

To obtain contextual feature maps, the original FCN [21] was proposed by removing the fully connected layers from the classification network, and then feature maps are up-sampled to obtain the final segmentation map. It has achieved good results of semantic segmentation in an end-to-end way. In most methods for image semantic segmentation [14,15], a classification network without fully-connected layers is often regarded as an encoder, which generates low-resolution contextual representations by down-sampling techniques, such as pooling. A decoder is just an inverse process of an encoder, which gradually recovers the resolution of feature maps. High-resolution representations are gradually restored using up-sampling techniques, such as bilinear interpolation, de-convolution. The de-convolution [22] is a learnable up-sampling technique, which has achieved excellent results but increased network parameters. Compared with de-convolutions, interpolations are simple and computationally efficient for greatly accelerating training and inferring. In most methods, nearest neighbor and bilinear interpolation methods are often used.

An encoder is the backbone of a segmentation network, which completes the feature extraction from the input, and it affects the whole performance of the model. Direct use of classification networks as the backbone may lose spatial details inevitably due to lots of downsampling operations. Some methods have been proposed to alleviate the loss of spatial details. Deeplab v1 [17], Deeplab v2 [18], Deeplab v3 [19] and Deeplab v3+ [20] adopt atrous convolutions to down-sample feature maps too much, thus these methods can maintain feature maps to be in high resolutions. Pohlen et al. [25] proposed full-resolution residual networks to maintain the size of feature maps at a high level for preserving more spatial information. Wang et al. [26] discussed the strategy of neural architecture designs, and presented a High-Resolution Network (HRNet) to learn high-resolution representations. Wang et al. [27] proposed an Enhancement-Fusion Network (EFNet) by designing multiple enhancement modules to process inputs for obtaining multiple features. Transformer is the latest powerful encoder in vision tasks. For examples, GasHis-Transformer [28] and CVM-Cervix [29] have achieved excellent results.

To improve spatial details in decoding stages, researchers focus on how to make good use of the features acquired by the encoder. FCN [21], RefineNet [23] and UNet++ [24] extract feature representations with different scales, and use short connections for long-distance feature fusion, which are often implemented by pixel-wise addition or channel concatenation. Zhao et al. [30] used adaptive pooling to propose a Pyramid Pooling Module (PPM), which is processed in a manner of image pyramids. Li et al. [31] proposed a Gated Fully Fusion Network (GFFNet) by designing a gate control module, which integrates features at different levels. In its decoding stage, GFFNet adopts a fusion method that is similar to DenseNet [32]. Wang et al. [33] designed a spatio-temporal non-local block to propose a Non-local Neural Network. This method is inspired by non-local means, and it is actually an attention algorithm. Fu et al. [34] proposed a Dual Attention Network (DANet) for scene segmentation by designing position and channel attention modules. Inspired by the non-local block [33], Huang et al. [35] designed a Criss-Cross attention Network (CCNet) for speeding up semantic segmentation. Unlike the parallel connection of channel and spatial attention modules, Woo et al. [36] designed a Convolutional Block Attention Module (CBAM) by connecting a channel attention module and a spatial attention module in series. These methods are processed in high resolutions for maintaining more spatial details. To accelerate computations, lightweight models [37] have been proposed for image segmentation.

### 2.2. Smoke semantic segmentation

Traditional hand-crafted methods have tried to separate smoke objects from cluttered backgrounds by exploring color characteristics of images in different color spaces. Filonenko et al. [5] combined color and shape features, and used CUDA to speed up computations. Dimitropoulos et al. [7] proposed a high-order linear dynamical system for smoke detection, which uses background removal methods and color feature analysis to filter non-smoke pixels. Zhao et al. [8] combined rough sets with color features, used Kalman filters to update the background to remove objects with colors similar to smoke, and then adopted the rough distribution of smoke in the RGB space to segment them. Luo et al. [9] used the motion features of smoke objects for smoke segmentation. Lin et al. [38] directly used the Kalman filter to estimate smoke contours for obtaining accurate results. However, it is difficult for traditional methods to obtain robust results.

With the rapid development of deep learning in recent years, Deep Neural Networks (DNNs) have widely been used for smoke semantic segmentation. DNN based smoke semantic segmentation methods combine feature extraction and classification without complicatedly hand-crafted feature designs. Tao et al. [39] directly used the original AlexNet [40] for smoke detection. Kaabi et al. [41] directly adopted a deep belief network to classify every pixel as smoke or non-smoke. Li et al. [42] proposed a 3D parallel full CNN to separate smoke regions from videos. Yuan et al. [43] proposed a dual-channel encoding-decoding network with dual paths to obtain detailed spatial information and semantic abstraction of smoke. Yuan et al. [44] proposed a Wave-shaped deep neural Network (W-Net) for smoke density estimation by repeatedly stacking encoders and decoders. It is actually a method for soft segmentation of smoke, but which is far more challenging than hard smoke segmentation. Yuan et al. [12] proposed a gated recurrent network with dual classification assistance for smoke semantic segmentation by fully exploiting long-range dependency and global category information at the same time.

According to the analysis of above methods, it is a reasonable trend to combine global and local features from different levels for improving performance. In this paper, we mainly focus on designing a structured fusion strategy of feature maps from different levels, and use mathematical derivation to propose a network for fully mining structured information embedded in multi-scale feature maps.

## 3. The proposed method

Fig. 3 shows the overall framework of our Newton Interpolation Network (NINet). It is composed of a backbone network for encoding features and a decoding network with a Newton interpolation module for extracting structured information from encoded features. Our NINet not only extracts intrinsic structures embedded in feature maps, but also restores spatial details of original data in high resolutions.

### 3.1. Encoding stages

We adopt the ResNet network [45] as the backbone network of our NINet for feature encoding. The backbone network has five stages of feature extraction. Down-sampling can capture contextual features but it loses spatial details. To avoid loss of spatial information, we replace down-sampling operations by atrous convolutions in the fourth and fifth stages. In other words, the last three stages produce the same size of feature maps. For an input image with size of H×W, the sizes of output feature maps in the five stages are H/2×W/2, H/4×W/4, H/8×W/8, H/8×W/8, and H/8×W/8, respectively.

To facilitate description of our method, we use symbols of mathematical forms for presentation. As shown in Fig. 3, the positional indices of five stages are denoted as s1, s2, s3, s4, and s5, respectively. Accordingly, their feature values are expressed as f(s1), f(s2), f(s3), f(s4), and f(s5).

### 3.2. Decoding stages

#### 3.2.1. Pyramid pooling module

The size of convolution kernels determines the receptive field of neurons, which have significant impacts on the feature extraction capability of CNN based models. To improve feature representation, an effective way is to combine local and global information captured from receptive fields with different sizes. Liu et al. [46] proposed a ParseNet by fusing global and local features. In the ParseNet, global features are obtained by global pooling, L2 normalized, and unpooled for final fusion. But it fuses only two levels of features, not enough for capturing robust features. Zhao et al. [30] proposed a Pyramid Scene Parsing Network (PSPNet) by designing a Pyramid Pooling Module (PPM). The PPM uses adaptive pooling to generate several feature maps with different sizes, resulting in a feature pyramid. These feature maps are convolved and up-sampled to the same size of the input for concatenation. Thus, it can fuse information from different levels.

Since smoke greatly varies in sizes, colors and textures, we need to extract robust contextual features with different scales for improving feature representation capabilities. Therefore, we also use PPM at the highest level of encoding stages, since higher levels contain more global information.

#### 3.2.2. Newton interpolation theory

Before describing our module in detail, we need to introduce and understand the Newton interpolation method. The interpolation method constructs an algebraic polynomial P(s) from a set of known function values, f(s0), …, f(sn), and then P(s) is used to approximate f(s). The algebraic polynomial not only accurately reflects the characteristics of the original function f(s) but also has low computational complexity.

Let s0, …, sn denote given points of function parameters, and f(si) stand for the known value of the function at point si (i=0, …, n). Apparently, an n-order interpolation polynomial Pn(s) satisfies the following conditions:

Pn(si) = f(si), i = 0, 1, ⋯, n.    (1)

Assume that Pn(s) is an algebraic polynomial whose power does not exceed n. The specific formula of Pn(s) is defined as

Pn(s) = a0 + a1 s + ⋯ + an s^n    (2)

where s is a positional parameter, and ai is the ith unknown coefficient (i=0, …, n). The next task is to use the more general Newton Interpolation Method to solve these coefficients.

In the case of n=0, there is only one interpolation point s0, so it is factually degenerated into the zero-order interpolation polynomial of P0(s)=f(s0). For n=1, we have two points, i.e. s0 and s1, resulting in the first-order interpolation polynomial P1(s). We estimate the first derivative of original signals by the first order difference, defined as follows:

P1(s) = f(s0) + f[s0, s1](s − s0)    (3)

where f[s0, s1] is the forward difference for approximating the first-order derivative of function values, defined as

f[s0, s1] = (f(s1) − f(s0)) / (s1 − s0)    (4)

Similarly, three interpolation points produce the second-order interpolation polynomial, formulated as

P2(s) = P1(s) + f[s0, s1, s2](s − s0)(s − s1)    (5)

where f[s0, s1, s2] is the second-order forward difference, defined as

f[s0, s1, s2] = (f[s1, s2] − f[s0, s1]) / (s2 − s0)    (6)

Combining Eqs. (3) and Eq. (5), we have

P2(s) = f(s0) + f[s0, s1](s − s0) + f[s0, s1, s2](s − s0)(s − s1)    (7)

For n+1 points, we can obtain the nth-order interpolation polynomial, defined as

Pn(s) = f(s0) + f[s0, s1](s − s0) + f[s0, s1, s2](s − s0)(s − s1) ⋯ + f[s0, ⋯, sn](s − s0)⋯(s − sn)    (8)

where f[s0, ⋯, sn] is the nth-order forward difference, defined as

f[s0, s1, ⋯, sn] = (f[s1, ⋯, sn] − f[s0, ⋯, sn−1]) / (sn − s0)    (9)

#### 3.2.3. Newton interpolation module

In deep neural networks, short-connection paths alleviate the gradient vanishing problem and play a very key role in improving performance. Traditional short connections simply use concatenation or summation of feature maps from encoding stages. In this way, models can compensate spatial details lost by down-sampling operations. However, these methods do not model intrinsic structures between feature maps with different scales.

To mine more structures in sequential feature maps, we use the above-mentioned newton interpolation method to estimate a new feature map from these sequential feature maps, instead of feature concatenation or summation. The Newton interpolation method models the values of a given function to obtain its continuous value representation, so it can predict the function value at any position and estimate the continuous curve of function values. Unlike concatenation or summation, Newton interpolation tends to extract structured information from these sequential maps. Therefore, the interpolated feature map very likely contains more powerful features than concatenated or summed feature maps.

According to the above discussion, we propose a Newton Interpolation Network (NINet) for smoke segmentation, as shown in Fig. 3. Our NINet consists of encoding and decoding stages. The encoding stages usually use the ResNet network [45] as backbone. To effectively fuse feature maps from encoding stages, we propose a Newton Interpolation Module (NIM) for extracting structured information across different stages. Each stage has a specific scale, so our NIM captures scale invariant features.

Fig. 4 shows the network structure of our NIM. It has an input feature map from a previous decoding layer (denoted as Input in Fig. 4), one common feature map from the first encoding stage for implementing traditional short connection (denoted as f(s1) in Fig. 4), and at least two feature maps from the encoding stages for interpolation (denoted as f(sk), …, f(s5) in Fig. 4, where 1<k<5). The sequential features of f(sk), …, f(s5) are used to estimate structured features using the Newton interpolation method. For k=4, 3, and 2, we obtain the first-order, secondorder and third-order interpolation polynomials, which are denoted as P1(s), P2(s) and P3(s), respectively.

In the case of k=4, we have two features at the same position, i.e. f(s4) and f(s5), for interpolation, so the polynomial of P1(s) in Fig. 4 is defined as

P1(s7) = f(s4) + f[s4, s5](s7 − s4)    (10)

In the case of k=3, we have three features at the same position, i.e. f(s3), f(s4) and f(s5), for interpolation, so the Newton interpolation polynomial of P2(s) has two orders, defined as

P2(s8) = f(s3) + f[s3, s4](s8 − s3) + f[s3, s4, s5](s8 − s3)(s8 − s4)    (11)

In the case of k=2, we have four features at the same position, i.e. f(s2), f(s3), f(s4) and f(s5), for interpolation. The Newton interpolation polynomial of P3(s) has three orders, defined as

P3(s9) = f(s2) + f[s2, s3](s9 − s2) + f[s2, s3, s4](s9 − s2)(s9 − s3) + f[s2, s3, s4, s5](s9 − s2)(s9 − s3)(s9 − s4)    (12)

For the sake of easily understanding our Newton interpolation module, we use the stage index as the value of horizontal axis, and put the value at the same position of a feature map in a given stage onto the vertical axis, as shown in Fig. 5. Feature values at the same position from sequential stages may exhibit certain patterns or structures about objects. Feature maps in different stages represent cross-level information about objects, and they absolutely have strong correlations between them. From a point of view, feature maps in deeper layers are closer to semantic and contextual features. Therefore, we use our Newton interpolation module to model structured information to extract intrinsic patterns. As shown in Fig. 5, the feature values at a given position from stages s1, s2, s3, s4, s5 and s6 are respectively f(s1), f(s2), f(s3), f(s4), f(s5) and f(s6), and these values proximately form a polynomial curve. Therefore, it is very reasonable for us to use Newton Interpolation to estimate structured features g(s7), g(s8) and g(s9) for feature fusion in stages of s7, s8 and s9.

After we obtain structured features, we concatenate the major input feature, the structured feature and the first stage feature together to generate a fused feature map, and then use convolution, batch normalization and activation to generate an output feature for our NIM. In this way, we can perfectly extract structured information from encoding stages and fuse it with decoded features for improving both spatial details and long-range dependency representations.

### 3.3. Simplification of Newton interpolation module

As shown in Figs. 3 and 5, we divide our network into nine stages whose indices are s1, s2, s3, s4, s5, s6, s7, s8 and s9, respectively. We first adopt the Newton Interpolation method to construct a polynomial curve from feature values at the encoding stages, and then use the constructed curve to interpolate the features for skip connections in the decoding stages. In this way, the structured information contained in the polynomial curve is extracted to enhance the decoding capability of our method. The truncation error of the Newton interpolation is defined as follows:

Rn(x) = f[x, x0, ⋯, xn](x − x0)(x − x1)⋯(x − xn)    (13)

Estimated errors become large due to the extrapolation nature of the Newtonian interpolation. The experimental results also verify that the results get worse in the case of large interpolation intervals. In Eq. (8), the difference of order n is multiplied by the corresponding power of 0.1 to the nth power. The formula variants are:

Pn(s) = f(s0) + f[s0, s1](s − s0) × 0.1 + f[s0, s1, s2](s − s0)(s − s1) × 0.1^2 ⋯ + f[s0, ⋯, sn](s − s0)⋯(s − sn) × 0.1^n    (14)

According to Eq. (13), the truncation error is:

Rn(x) = f[x, x0, ⋯, xn](x − x0)(x − x1)⋯(x − xn) × 0.1^(n+1)    (15)

From Eq. (15), we know that the truncation error of the Newtonian interpolation polynomial tends to be close to 0. As shown in Figs. 4 and 5, suppose that nine stages are placed on the equally spaced horizontal axis, and the interval between two adjacent stages is set to 1, i.e. sk − sk−1 = 1. From Eq. (14), under the assumption of deformation and equal spacing of the interpolated formula, Eqs. (10)–(12) are reduced to:

P1(s7) = 0.7 × f(s4) + 0.3 × f(s5)    (16)

P2(s8) = 0.6 × f(s3) + 0.3 × f(s4) + 0.1 × f(s5)    (17)

P3(s9) = 0.475 × f(s2) + 0.385 × f(s3) + 0.105 × f(s4) + 0.035 × f(s5)    (18)

The sizes of structured feature maps in stages s7, s8 and s9 are H/8×W/8×512, H/8×W/8×512, and H/4×W/4×256, respectively. The final output for each stage has the same size as its structured feature map. We used the same configuration for all training, test and ablation experiments.

## 4. Experimental results

### 4.1. Datasets and implementation details

According to the fluid characteristics of smoke, Yuan et al. [44] used computer simulation and volume rendering techniques to create a virtual synthetic smoke training dataset containing 70,632 images, and three virtual synthetic smoke test datasets that are named as DS01, DS02 and DS03. Each test set has 1000 images with different backgrounds. These datasets are very challenging due to large variations in textures, shapes, colors, scales and semi-transparency degrees. Among the three synthetic test datasets, DS02 contains more sparse smoke, so it has more complicatedly mixed textures of smoke and backgrounds. To validate our method, we randomly selected 10k virtual synthetic smoke images for training, use DS01, DS02 and DS03 as verification sets, and adopted six real smoke images without labels for visualized comparisons. To enhance the generalization performance of our network on real smoke images, we used a real smoke dataset [47] to fine-tune our network. This dataset includes 416 real smoke images with pixel-level manual annotations.

All experiments were conducted on a PC with NVIDIA RTX3090, Windows 10, Python 3.7 and PyTorch 1.7. The loss function is the Dice loss for supervising the training of our method, and the optimizer is the Stochastic Gradient Descent algorithm (SGD). The epoch, learning rate, attenuation and momentum are set to 600, 0.0001, 0.95 and 0.9, respectively. We report all results in terms of mean Intersection over Union (mIoU), which has widely been used to evaluate the overall performance of semantic segmentation algorithms. The mIoU reflects the similarity between a predicted result and its corresponding ground truth, defined as follows:

mIoU = (1/N) Σ_{k=1}^{N} (Pk ∩ Gk) / (Pk ∪ Gk)    (19)

where Pk and Gk are the predicted map and corresponding ground truth map for the kth image, respectively. In addition, we use the mean pixel accuracy (mPA) as an indicator for comparisons.

### 4.2. Comparison experiments

To evaluate the effectiveness of our framework, we tested our method and some state-of-the-art semantic segmentation methods on the three synthetic test datasets [44] and the real smoke dataset [47]. These comparison segmentation methods include FCN [21], PSPNet [30], SegNet [14], U-Net [15], U-Net++ [24], RefineNet [23], Deeplab v3+ [20], DSS [43], LWNet [37], CCA [51], and W-Net [44]. Transformers have achieved amazing results on Natural Language Processing (NLP). Transformer based methods have been widely applied to vision tasks and also obtained very good performance. To further validate the effectiveness of our method, we also compared it with several Transformer based segmentation models, such as ViT [58], Swin-Transformer [59], BVM [60] and SegFormer [61]. ViT [58] was originally presented for image classification, so we replaced the last layers of ViT [58] with a CNN decoder to implement image segmentation. To objectively and fairly evaluate the performance of each method, we used the same dataset and configurations to train all the comparison methods. DSS [43] and W-Net [44] are our previous work.

#### 4.2.1. Test on synthetic datasets

Table 1 lists quantitative comparison results on the three synthetic datasets. Our method achieves the highest mIoU and mPA on DS01, DS02 and DS03 among all comparison methods. Fig. 6 shows results of some synthetic smoke images segmented by these comparison methods, respectively. To better illustrate the functionality of our method, we selected some representative examples for visualization analysis.

According to Table 1, FCN [21] achieves higher mIoUs than SegNet [14] and U-Net++ [24], but it cannot preserve accurate smoke boundaries well, as shown in Fig. 6(c)–6(e). In contrast, SegNet [14] and U-Net++ [24] fusing shallow features from the backbone network have the worst accuracy compared to other networks, but they produce more accurate smoke edges. This also proves that spatial texture details for smoke images play a key role in improving the accuracy of segmentation. The Transformer-based methods do not achieve satisfactory results. For instance, SegFormer [61] demonstrates good performance on specific datasets, but its mIoU (78%) is noticeably lower than ours. Since our NINet integrates spatial structured features and contextual ones together for improving performance, the results of all selected samples segmented by our NINet are significantly better than those by other comparison methods.

#### 4.2.2. Test on real smoke images

To validate the performance of our method on real images, we conducted comparative experiments on some real smoke images collected from the Internet. FCN [21], SegNet [14] and U-Net++ [24] do not achieve accurate results, as shown in Fig. 7b–7d. PSPNet [30] and Deeplab v3+ [20] produce the results with less spatial details than other methods. UNet++ [24] uses dense connections between encoders and decoders to conduct feature fusion, but it does not obtain good results on real smoke images. The reason may be that dense connections tend to extract more contextual information than spatial details. RefineNet [23] uses multi-resolution fusion to obtain good performance, but this is not accurate enough for smoke images. To accurately segment smoke regions, our NINet extracts local detailed features and global semantic abstractions to precisely localize smoke boundaries. As shown in Fig. 7o, segmented regions of the real smoke images by our NINet are basically consistent with real smoke regions. By carefully observing visual comparison experiments on virtual smoke datasets and real smoke ones, we find that Transformer based methods may probably encounter the overfitting problem. These methods achieve satisfactory results on virtual data, but they perform poorly on real data. In addition, some of them cannot even segment the main parts of smoke, such as Fig. 7k–7n.

By carefully observing experimental results, our method is significantly better than other methods, including U-shaped networks (UNet++ [24] and RefineNet [23]), and high-resolution maintenance ones (PSPNet [30] and Deeplab v3+ [20]). The main reason is that our method not only maintains high resolutions but also extracts structured information from multi-scale features. In addition, our NINet also outperforms our previous work, including DSS and W-Net. Different from previous methods, our NINet uses the Newton Interpolation algorithm to fuse multi-scale features at different levels, and at the same time keep high resolutions to ensure that smoke boundaries are effectively represented. These techniques greatly improve the representation ability of our network. Surprisingly, these Transformer based methods are not as effective as the CNN based networks in terms of accuracy and visualization results.

It is very important to distinguish smoke and clouds in some applications, such as forest fire detection. To remove the disturbance of clouds, we fine-tuned our NINet on the 143 images from the real smoke dataset [47]. We tested our method on the remaining 273 images of the dataset, and achieved an mIoU of 80.25% and an mPA of 92.47% on the remaining real dataset. Fig. 8 shows the visualized results of our method on some challenging real samples. Our method achieves very accurate results, as shown in Fig. 8c. Although some images contain both real smoke and clouds, our NINet can accurately segment them. The first row of Fig. 8 shows the results that have smoke contours with average accuracy. In the second row of Fig. 8, our method segments only one smoke region but misses a small one. The third row shows black storm clouds, which have visual appearances similar to smoke. However, our method does not produce any false segmentation. Although the fifth row shows a very small smoke object, our method accurately segments the smoke object. In general, our method can accurately discriminate smoke objects. There are blurry boundaries between smoke and background objects in some results. The main reasons are that smoke is very similar to cloud, and it has less textures.

#### 4.2.3. Test on a real smoke video

We tested our method on a real smoke video. The smoke video contains a forest fire that produces white smoke. The smoke color is very similar to the sky color. This video is available via http://smoke.ustc.edu.cn/datasets.htm. The first and third rows of Fig. 9 are original frames of the forest fire. The second and fourth rows of Fig. 9 show corresponding results segmented by our method for the first and third rows of Fig. 9, respectively. According to the results, our method can accurately segment real smoke regions of the smoke video, and it does not misclassify the white area of the sky as smoke.

#### 4.2.4. Test on a general segmentation dataset

The above experiments have shown that our method has achieved good results in smoke segmentation. In fact, our method is designed as a general semantic segmentation model. To prove the capability for improving the performance of general segmentation, we test our method on the Pascal VOC2012 dataset. For the sake of fairness, we adopt the same experimental setting as smoke segmentation. We compare our method with several existing methods, including KSAC [48], APCNet [49], RefineNet [23], DANet [34], PSPNet [30], EncNet [50], CCA [51], CANet [52], and RecoNet [53]. Table 2 lists experimental results and network parameter numbers on the VOC2012 dataset. Our method achieves the highest accuracy among existing state-of-the-art segmentation methods. In addition, the parameter size of our model is about 59M, which ranks approximately in the middle position. This means that our method has powerful segmentation capability.

### 4.3. Ablation experiments

The essence of our NIM is a multi-scale fusion module that is derived from the mathematical form of Newton Interpolation. We explore the effectiveness of the proposed fusion module from two aspects that are weighting manners of different order information and combination ways of short connections.

#### 4.3.1. Validating the importance of weights and orders

The weights for fusing the features from encoders are very important, and the number of encoded feature maps also play a significant role in improving the performance of our segmentation model. Therefore, we design seven variants of our method for validation.

First, as shown in Fig. 11, we create three fusion modules, denoted as Newton Interpolation Fusion (NIF) by removing the feature f(s1) in the first encoding stage, Direct Addition Fusion (DAF) by replacing Newton Interpolation with point-wise addition, and Normalized weighting Addition Fusion (NAF) by replacing Newton Interpolation with normalized weighting addition. Then, we design three combinations of orders to construct seven variants of our method for evaluating the importance of the order of a feature set. Theoretically, one feature map provides only zero-order information, two maps offers one-order information, and k maps provide up to (k-1)-order information. The zeroorder feature sets include three sets, each of which has only one feature. Fig. 12a shows the common encoding path of different variants. The three zero-order feature sets are respectively f(s2), f(s3) and f(s4), as shown in Fig. 12b. The 3rd order feature sets have two different types. The first type set has a 1st order subset of f(s3) and f(s4), a 2nd order subset of f(s3), f(s4) and f(s5), and a 3rd order subset of f(s2), f(s3), f(s4) and f(s5), as shown in Fig. 12c, 12e and 12g. The second type set has three subsets with the same 3rd order feature sets of f(s2), f(s3), f(s4) and f(s5), as shown in Fig. 12d, 12f and 12h. Table 3 gives the detailed descriptions of our variants for validating the importance of weights and orders.

According to the results listed in Table 4, Model 6, Model 7 and Model 2 achieve the highest mIoUs among all the variants on DS01, DS02 and DS03, respectively. Two of the best three models adopts the combination of 1st, 2nd and 3rd order feature subsets, and uses Newton Interpolation Fusion (NIF). Therefore, this proves that information with different orders and Newton interpolation can really improve accuracy of smoke segmentation. To demonstrate the role of Newton Interpolation, we visualize the feature maps of middle layers in Model 2, Model 4, and Model 6, as shown in Fig. 10. As we use Newton interpolation with higher orders, the visualized feature maps are more similar to the ground truth.

#### 4.3.2. Exploring the importance of short connections and weighting manners

Short connections and weighting manners greatly influence the final accuracy of segmentation. To find an optimized combination of short connections and weighting ways, we design three new variants of our method. First, we create three types of short connections, as shown in Fig. 13. The feature map f(s1) is only copied and resized for concatenation, which is denoted as SC1 (Fig. 13a). SC2 is just to use f(s2) for concatenation, as shown in Fig. 13b. The third type SC3 uses both f(s1) and f(s2) for concatenation, as shown in Fig. 13c. Then, we design two interpolation modules, as shown in Fig. 14. The first one uses only Newton interpolation without short connections, which is just the NIF module described in Fig. 11a. The second one adopts both Newton interpolation and short connections, which is actually our NIM module described in Fig. 4. Finally, we design two segmentation frameworks, as shown in Fig. 15. The first one is a Framework with only Short Connections (FSC), and the second one is a Framework with Newton Interpolation and Short Connections (FNISC). In Fig. 15, SC1/2/3 denotes to use SC1, SC2 or SC3, and NIF/M means NIF or NIM.

According to Figs. 13–15, we use five combinations to create five variant models for evaluating the importance of short connections and weighting manners. The results are listed in Table 5. Model 6 adopts FNISC with NIF, which is just the same model in Table 4. Models 8, 9 and 10 have the same model framework FSC but with different short connections of SC1, SC2 and SC3. Our NINet uses the framework of FNISC with NIM, which achieves the best results among all the five models.

To validate the effectiveness of our NIM module, we replace the fusion module of our NIM by pixel-wise addition and concatenation to create two new variants, named as Model 11 and Model 12, respectively. The baseline of Model 6 is the same as the one of Model 11 and Model 12. From Table 6, we find that NIM achieves significantly higher mIoUs than Addition and Concat on the three test data sets.

To validate that the fixed fusion weights of Newton Interpolation are better than learnable weights, we replace the Newton Interpolation fusion method by a learnable fusion one for ablation experiments. By observing the results in Table 7, we can find that the Newton interpolation method achieves far higher accuracy than the learnable one.

### 4.4. Lightweight experiments

Computational complexity is a key factor for improving real time performance, so we insert the proposed NIM into the MobileNet [57] for evaluating its effectiveness. Attention mechanism is an effective weighting method for improving accuracy. Our NIM is compared with several attention modules, such as SE-Block [54], CBAM [55] and ECA-Block [56]. Table 8 lists the results of the lightweight variants with NIM and several attention modules. Experiments show that our NIM achieves better results than these attention modules. In addition, our NIM has far less FLOPs than the compared attention modules. The MobileNet [57] has only 2.91G FLOPs. Adding our NIM only brings an increase of 0.92G FLOPs. Our NIM achieves about 25 FPS. In fact, the processing speed is greatly influenced by other operations including image I/O, so our NIM has the same frame rates as attention modules.

## 5. Conclusions

In most fires, smoke exhibits very large variances of visual appearances, including highly different colors, shapes and textures. One of the adverse properties for visual processing is the semi-transparency of smoke, which may produce very complicated mixtures of smoke and background textures. This is one of the main reasons that leads to great difficulties in labelling and segmenting smoke regions.

To improve the performance of smoke segmentation methods, we analyze existing methods to propose a Newton Interpolation Network (NINet) for smoke segmentation. Existing methods tend to use simple concatenations or addition for fusing multi-scale features. Unlike traditional fusion manners, we design a Newton Interpolation Module (NIM) to extract structured information by analyzing the feature values in the same position but from feature maps with different scales. The proposed NIM is able to find or mine the structures embedded in encoded feature maps. Traditional fusion method cannot model such intrinsic structures very well. To further obtain multi-scale structured information, we repeatedly use the proposed NIM in different-level decoding stages. According to the theory of interpolation, more features contain higher order information. Therefore, we adopt higher order Newton interpolation polynomials for higher layers by copying and resizing more encoded feature maps to our NIM. Extensive experiments validate that our method significantly outperforms existing state-of-art algorithms on both virtual and real smoke datasets. In addition, extensive ablation experiments also validate the effectiveness of our modules.

Although our network achieves excellent performance, it deeply depends on the levels of encoded features that directly determine the overall order of interpolation polynomials. Higher orders not only increase the computation complexity of interpolations, but also augment the risk of overfitting. Hence, a suitable order may play a key role in improving the performance of our network. Order optimization in a layer by layer manner may be a good choice.

## CRediT authorship contribution statement

Feiniu Yuan: Writing – review & editing, Methodology, Funding acquisition. Guiqian Wang: Writing – original draft, Software, Methodology, Investigation. Qinghua Huang: Writing – review & editing, Validation, Formal analysis. Xuelong Li: Writing – review & editing, Validation, Methodology, Formal analysis.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work was partially supported by the National Natural Science Foundation of China (62272308) and the Capacity Construction Project of Shanghai Local Colleges (23010504100).

## Data availability

Data will be made available on request.

## References

<!-- Reference entries omitted from clean corpus: in the source extraction (S077-S081) the reference
list is interleaved line-by-line with Conclusions text and author biographies, making verbatim
per-entry reconstruction unreliable. Consult the source PDF for the reference list. -->

## Appendix: Figure and Table Captions (segregated from body)

Fig. 1. Two main kinds of semantic segmentation paradigms. (a) An encoderdecoder framework with short connections; (b) An Atrous convolution frame work without reducing resolutions to small sizes.

Fig. 2. Some challenging smoke images.

Fig. 3. The structure of our Newton Interpolation Network (NINet). Up×k represents k times of upsampling operations. s1~s9 represent the indices of processing stages that also are the coordinate points for Newton interpolation.

Fig. 4. The network structure of Newton Interpolation Module (NIM). f(sk), …, f(s5) denote the feature function values extracted in the encoding stages. P5-k(s) is an algebraic polynomial with the power of 5-k modelled by the Newton interpolation method.

Fig. 5. Structured feature values extracted by Newton interpolation from sequential features of different encoding stages.

Fig. 6. Results on the synthetic smoke test datasets. (a) Synthetic smoke images. (b) Corresponding ground truths. Segmented results by (c) FCN, (d) SegNet, (e) UNet, (f) UNet++, (g) PSPNet, (h) Deeplab v3+, (i) RefineNet, (j) DSS, (k) W-Net, (l) ViT, (m) Swin Transfromer, (n) BVM, (o) SegFormer and (p) NINet.

Fig. 7. Results on real smoke images from the internet. (a) Real smoke images. Experimental results segmented by (b) FCN, (c) SegNet, (d) U-Net, (e) UNet++, (f) PSPNet, (g) Deeplab v3+, (h) RefineNet, (i) DSS, (j) W-Net, (k) ViT, (l) Swin-Transfromer, (m) BVM, (n) SegFormer and (o) NINet.

Fig. 8. Experimental results of some samples from the real smoke dataset. (a) Real smoke images, (b) Corresponding ground truths and (c) Segmented results by our NINet.

Fig. 9. Results on a real smoke video.

Fig. 10. Visualized feature maps of middle layers in Model 2, Model 4 and Model 6.

Fig. 11. Variants of our fusion module. (a) Newton Interpolation Fusion (NIF) by removing f(s1); (b) Direct Addition Fusion (DAF) by replacing Newton Interpolation with point-wise addition; (c) Normalized weighting Addition Fusion (NAF) by replacing Newton Interpolation with normalized weighting addition, which is formulated as [caption formula truncated in extraction; fragment: "1 ... i=1 f(xi)"].

Fig. 12. Variants of our method for validating the importance of weights and orders. (a) The common part of all the variants, and the different parts for Model 1 to Model 7 are from (b) to (h), respectively.

Fig. 13. Different types of short connections. (a) SC1 denotes the first type of a short connection with one feature map f(s1); (b) SC2 is the second type of short connection with f(s2); (c) SC3 denotes the third type of short connections with two feature maps of f(s1) and f(s2).

Fig. 14. Combinations of Newton interpolation and short connections. (a) NIF (Newton Interpolation Fusion without short connections); (b) NIM (Newton Inter polation Model with short connections).

Fig. 15. Variants of segmentation frameworks for Newton interpolation and short connections. (a) A Framework with Short Connections (FSC); (b) A Framework with Newton Interpolation and Short Connections (FNISC).

Table 1 Segmentation results of different methods on the three synthetic test datasets.

Table 2 Experimental results on VOC2012.

Table 3 Detailed description of our variants for validating the importance of weights and orders.

Table 4 Comparison results of the variants with different weights and orders.

Table 5 Comparison results of model variants for short connections and weighting manners.

Table 6 Comparison results of different feature fusion methods for skip connections.

Table 7 Comparison of Newton weights and learnable weights.

Table 8 The results of the MobileNet using NIM and attention modules.
