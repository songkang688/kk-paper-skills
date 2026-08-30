# 30_DualEncoded_Curvelet_KSII2019_Smoke_Recognition — Clean English Corpus

<!-- Stage 00 Wave 3 Agent H. English **Original:** blocks only; no Chinese content.
     Source: /workspace/30_DualEncoded_Curvelet_KSII2019_Smoke_Recognition.md (bilingual reader).
     Anchors in comments (SXXX/CXXX) refer to reader block ids.
     Authorship context (do not re-derive): Tier A2, weight 0.90; Yuan first author, correspondence
     explicitly assigned to Xue Xia and Jinting Shi (then-students).
     Extraction quality: MEDIUM — prose is in reading order, but display equations (1)-(14) arrived
     with scattered sub/superscripts. Equations below are reconstructed where the intended form is
     unambiguous (standard Curvelet/LBP/CLBP/RBF definitions cross-checked against the surrounding
     prose); reconstructions are marked. Table numeric rows (in C005, C007, C009, C010) excluded as
     non-prose; figure-diagram debris stripped from S045, S078. -->

## Title

<!-- src: S001, S002, S003 (byline/affiliations de-interleaved from two scrambled blocks), S005 -->
Dual-Encoded Features from Both Spatial and Curvelet Domains for Image Smoke Recognition

Feiniu Yuan (1,2), Tiantian Tang (3), Xue Xia (2,*), Jinting Shi (4,*), Shuying Li (5)

(1) College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, China [e-mail: yfn@ustc.edu.cn]. (2) School of Information Technology, Jiangxi University of Finance and Economics, China [e-mail: yeziandkuma@qq.com]. (3) School of Communications and Electronics, Jiangxi Science and Technology Normal University, China. (4) Vocational School of Teachers and Technology, Jiangxi Agricultural University, China [e-mail: icanflysjt@126.com]. (5) School of Automation, Xi'an University of Posts & Telecommunications, China.

*Corresponding author: Xue Xia, Jinting Shi

KSII Transactions on Internet and Information Systems, 2019. Received March 5, 2018; revised October 22, 2018; accepted November 7, 2018; published April 30, 2019.

## Abstract

<!-- src: S007 + S008 + S009 (single abstract paragraph split across three reader blocks) -->
Visual smoke recognition is a challenging task due to large variations in shape, texture and color of smoke. To improve performance, we propose a novel smoke recognition method by combining dual-encoded features that are extracted from both spatial and Curvelet domains. A Curvelet transform is used to filter an image to generate fifty sub-images of Curvelet coefficients. Then we extract Local Binary Pattern (LBP) maps from these coefficient maps and aggregate histograms of these LBP maps to produce a histogram map. Afterwards, we encode the histogram map again to generate Dual-encoded Local Binary Patterns (Dual-LBP). Histograms of Dual-LBPs from Curvelet domain and Completed Local Binary Patterns (CLBP) from spatial domain are concatenated to form the feature for smoke recognition. Finally, we adopt Gaussian Kernel Optimization (GKO) algorithm to search the optimal kernel parameters of Support Vector Machine (SVM) for further improvement of classification accuracy. Experimental results demonstrate that our method can extract effective and reasonable features of smoke images, and achieve good classification accuracy.

<!-- src: S010 -->
Keywords: Curvelet Transform, Dual-encoded Local Binary Pattern (Dual-LBP), Completed Local Binary Pattern (CLBP), Gaussian Kernel Optimization (GKO), Smoke Recognition

## Introduction

<!-- original heading: "1. Introduction" (S012) -->

<!-- src: S013 -->
Generally, fire causes significant economic losses and probably lead to severe death. In order to avoid fire occurrence, many traditional fire detection technologies have been widely used. These methods are usually based on temperature sensors, humidity sensors, and traditional ultraviolet and infrared fire detectors. Since traditional methods need to sample combustion products for analysis, they are required to be placed in the vicinity of fire.

<!-- src: S014 -->
In addition, traditional detectors are susceptible to external environment influences, such as airflow, dust. Traditional methods cannot provide us with detailed information about burning situation. Therefore, traditional smoke detectors are unreliable in open, large and special spaces. In most cases, fire will be initially accompanied by the emergence of smoke, and smoke often lasts for a few minutes before flames emerge.

<!-- src: S015 -->
According to this observation, visual smoke detection methods detect smoke from videos or images, and they are able to give early alarms of fire. Early smoke has special visual features, such as color, texture, and shape, which play an important role in fire detection. There are many texture feature extraction methods that have been proposed.

<!-- src: S016 -->
Gray-level co-occurrence matrices [1] is a way to describe texture by exploring spatial correlation between gray values of neighboring pixels. LBP [2] provides a binary-coding feature extraction manner by encoding the relationship between central pixels and their neighboring pixels. HOG [3] extracts features of edges and gradients. Many methods can achieve excellent performance by capturing multi-scale and multi-direction information in transform or frequency domains.

<!-- src: S017 -->
Compared with other transforms, Curvelet transform is strongly anisotropic and its needle-shaped elements provide a high directional sensitivity to represent curved singularities in images. In contrast, wavelet transform shows a good representation only at point singularities because it has a poor directional sensitivity.

<!-- src: S018 -->
Additional directional-based transforms, such as Dual-Tree Complex Wavelet Transform (DTCWT) and Gabor Wavelets, provide more multi-direction information than Wavelets, but they still have limited directional selectivity. Ridgelet is suitable for representing line singularities in objects, so it's rarely found in practical applications [4]. To extract discriminative features, we propose a novel feature extraction based on spatial and Curvelet domains.

<!-- src: S019 + S020 + S021; enumerated contribution list re-split (glued in extraction) -->
The main contributions of this paper are listed as follows:

1) We use Curvelet transform to extract discriminative features from original images, and then encode these images consisting of discriminative Curvelet coefficients to generate LBP codes based on Curvelet domains.

2) We first aggregate histograms of LBP maps from Curvelet domains to produce a histogram image of size 256×50, and then encode the histogram image again to generate novel codes, which are called Dual-encoded Local Binary Patterns (Dual-LBP).

3) We concatenate histograms of Dual-LBPs from Curvelet domain and Completed Local Binary Patterns (CLBP) from spatial domain to generate dual-encoded features for smoke classification.

Finally, we adopt Gaussian Kernel Optimization (GKO) algorithm to search the optimal kernel parameters of Support Vector Machine (SVM) for further improvement of classification accuracy.

## RelatedWork

<!-- original heading: "2. Related Work" (S022) -->

<!-- src: S023 + S024 + S025 + S026 (blocks split mid-sentence at citation boundaries "Celik et al." / "[7]",
     "Zhang et al." / "[9]", "Toreyin et al." / "[11]"; seams rejoined). "fire-like object" and
     "Texture feature features" preserved as printed (suspected source typos). Extraction artifact
     "[10]presented" respaced. -->
There are many methods proposed for smoke detection. Chenebert et al. [5] presented a flame pixel detection method in video images or still images using a non-temporal texture driven approach. The method did not use any time information. Chen et al. [6] used a color model based on RGB for fire smoke detection. However, there are many objects having the same color distribution as fire, so the method gives a false alarm inevitably for these fire-like object. Celik et al. [7] proposed a universal color model for fire pixel detection, and the algorithm used the YCbCr color space to separate chrominance and luminance components more effectively than other color spaces (such as RGB). Yuan et al. [8] proposed an accumulative motion model based on integral image techniques. The model estimated movement directions of objects in real-time for analysis of smoke. Zhang et al. [9] proposed a real-time forest fire detection algorithm using artificial neural networks based on dynamic characteristics of fire regions segmented from video images. Yu et al. [10] presented a method by using color and motion features for video smoke detection. The method could distinguish smoke from objects with similar color distribution by involving motion features and color information, which greatly improved the reliability of video smoke detection. Toreyin et al. [11] achieved smoke detection based on edge magnitude differences, in which the characteristics of smoke such as movement, flashing, edge blur and color were used. Once the scene lacks obvious edges or cluttered objects, the method raises false alarms. Texture feature features play a key role in smoke detection, Ojala et al. [2] firstly proposed Local Binary Pattern (LBP) for texture classification.

<!-- src: S027 + S028 + S029 (seam at "Yuan et al." / "[12]"). "an BP neural network" preserved as printed. -->
It is an efficient and simple gray-scale texture descriptor, which captures spatial characteristics of texture. LBP features have demonstrated very powerful discriminative capability, low computational complexity, and low sensitivity to illumination variations. To further improve the discriminative capability of LBP, many variants of LBP were proposed in the past decade. Yuan et al. [12] proposed an effective smoke detection method, in which features were extracted by concatenating histograms of local binary patterns (LBP) and local binary pattern variances (LBPV) from image pyramids, and an BP neural network was used for classification. Yuan et al. [13] presented sub-oriented histograms of LBP for image smoke classification. Gubbi et al. [14] proposed a video smoke detection algorithm based on wavelet and Support Vector Machines (SVM) classification. Liao et al. [15] proposed Dominant Local Binary Patterns (DLBP) for texture classification by regarding the more frequently occurred patterns as dominant features. Guo et al. [16] proposed a Completed LBP (CLBP) approach, which encoded the magnitudes and signs of differences between a center pixel and its neighbors. CLBP provides excellent classification performance. Above-mentioned methods extract features in spatial domains.

<!-- src: S030 + S031 (seam at "Ucar et al." / "[18]"). "multimodel" preserved as printed (suspected typo for "multimodal"). -->
Many methods achieve robust features from transform or frequency domains. Elaiwat et al. [17] proposed a multimodel Curvelet-based method for textured 3D face recognition. Each keypoint was detected across number of frequency bands and angles on 3D faces. Ucar et al. [18] presented an algorithm that was for facial expression recognition by integrating Curvelet transform and online sequential extreme learning machine (OSELM) with radial basis function (RBF) hidden node having optimal network architecture.

<!-- src: S032; "a holistic features" preserved as printed -->
Although Curvelet transform provides a powerful multi-scale capability to extract discriminative smoke features, Curvelet-based image classification methods are limited to features, since the Curvelet coefficients are regarded as a holistic features extracted from the whole images [19]. To this end, we propose a duplex feature coding approach based on Curvelet transform to extract features from interpolated smoke images.

<!-- src: S033 + S034 + S035 (seam at "Wu et al." / "[22]") -->
Many papers have been proposed to optimize kernel functions. Chapelle et al. [20] devised a gradient-based algorithm, which optimized a kernel function with multiple unconstrained parameters for SVM. Ghiasi-Shirazi et al. [21] considered the problem of optimizing a kernel function over translation invariant kernels for the task of binary classification. Wu et al. [22] proposed a direct method to build sparse kernel learning algorithms by adding one more constraint to the original convex optimization problem for sparse large margin classifiers. Ye et al. [23] considered the problem of multiple kernel learning (MKL) for regularized kernel discriminant analysis (RKDA), in which the optimal kernel matrix was obtained as a linear combination of pre-specified kernel matrices. All above methods formulated the kernel learning problem as an optimization problem based on a special task, such as SVM.

## Methods

<!-- original heading: "3. Our Algorithm" (S036) -->

<!-- src: S037 -->
The framework of our method is shown in Fig. 1. Our method consists of four main steps: Curvelet transform of original images, extraction of Dual-encoded Local Binary Patterns (Dual-LBP) on Curvelet coefficient sub-images, concatenation of histograms of Dual-LBP and Completed Local Binary Patterns (CLBP), and Gaussian Kernel Optimization (GKO) of SVM classification.

### 3.1 Curvelet transform

<!-- original heading: "3.1 Curvelet transform" (S038) -->

<!-- src: S039 -->
Curvelet transform was first proposed and structured with the tight frame by Candes and Donoho in 1999 [24]. Motivated by the need of image analysis, the second generation Curvelet transform [25] was introduced in 2005. It is not only simpler, but also faster and less redundant. Curvelets exhibit highly anisotropy and commendable directionality, which are beneficial for image edge representation.

<!-- src: S040; equations (1)-(2) reconstructed from scattered-subscript debris
     ("∑W2(2jr)=1,r∈( , ) (1) 4 2" with orphaned "3 3" / "4 2" fraction digits) — standard Curvelet
     admissibility conditions, consistent with surrounding prose -->
Smoke image edges are always curved, so Curvelet is almost the optimal representation of a singular smooth curve. A pair of window functions, which are called "radial window" and "angular window", are defined as W(r) and V(t). These windows meet the following admissibility conditions:

Σ_{j=−∞}^{∞} W^2(2^j r) = 1,  r ∈ (3/4, 3/2)  (1)

Σ_{l=−∞}^{∞} V^2(t − l) = 1,  t ∈ (−1/2, 1/2)  (2)

<!-- src: S041; equation (3) reconstructed (standard frequency-window definition; "j/2 represents the
     integer part of j/2" per source prose, i.e. floor) -->
Then, the frequency window U_j is defined:

U_j(r, θ) = 2^{−3j/4} W(2^{−j} r) V(2^{⌊j/2⌋} θ / (2π))  (3)

where ⌊j/2⌋ represents the integer part of j/2. Hence, the support of U_j is a polar "wedge" that is defined by the support of W and V. Varying scales j and directions U produce multi-scale and multi-direction transform. These digital transforms are linear.

<!-- src: S042 + S043 (equation number "(4)" split across the block seam); equation (4) reconstructed -->
We take a Cartesian array f[t_1, t_2] (0 ≤ t_1, t_2 < n) as input and get an output of digital coefficients from the digital Curvelet transform. The digital Curvelet coefficients are defined:

c^D(j, θ_l, k) = Σ_{0 ≤ t_1, t_2 < n} f[t_1, t_2] φ^D_{j,θ_l,k}[t_1, t_2]  (4)

where each φ^D_{j,θ_l,k} is a digital mother Curvelet (the superscript D represents "digital"), t_1 and t_2 are spatial variable, and j, θ_l and k are scale, orientation, and position index, respectively. In the first step of our method, bilinear interpolation is needed to generate normalized images of size 128×128 from original images with different sizes.

<!-- src: S044; "log2(min(w, h)) − 3" reconstructed from drifted subscript ("log (min(w, h)−3) ... 2"),
     consistent with "the scale is 4 for a 128×128 image" (log2(128) − 3 = 4) -->
The scale number of subbands is set to log_2(min(w, h)) − 3, where w and h are width and height of input images, respectively. Hence, the scale is 4 for a 128×128 image. Digital Curvelet coefficients are real-valued. The multi-resolution Curvelet transform of different scales have different characteristics.

<!-- src: S045; trailing Fig. 2 scale-diagram angle-label debris ("θ θ 32 25 θ θ 1 24 ... Scale 2 θ 8 17")
     stripped as figure content -->
Lower scales, denoted as coarser scales, contain low frequency information whereas higher scales, known as detailed and finer scales, consist of high frequency information.

<!-- src: S046 -->
To implement Curvelet transforms, we first perform a 2D FFT on the interpolated 128×128 image. Then the 2D Fourier frequency plane of the image is divided into many parabolic wedges. Finally, an inverse FFT of each wedge is applied to find the Curvelet coefficients at each scale j (j=1,2,3,4) and angle θ_l, and the range of l varies at different scales. An example of Curvelet coefficients at each scale is shown in Fig. 2.

<!-- src: S047 -->
A red rectangular box stands for the coefficient map at one scale on one direction. The coefficient at scale 1 is displayed in the center. The coefficients at scale 2 on 8 directions and those at scale 3 on 16 directions are displayed in two loops around scale 1. Each block is equivalent to the pseudo polar tiling of the frequency plane with trapezoids.

<!-- src: S048 + S049 + S050 (four-step FDCT wrapping procedure; steps (1)-(4) were interleaved with
     formula debris across the three blocks; reconstructed from the standard wrapping-based FDCT
     description that the debris unambiguously matches. Notation f̃ = wrapped product.) -->
There are two different digital implementations of Fast Digital Curvelet Transform (FDCT), which are based on Unequally Spaced Fast Fourier Transform (USFFT) and Wrapping Transform, respectively. In this paper, we use wrapping based Curvelet for feature extraction. The procedure of Curvelet based on wrapping is as follow:

(1) Apply the 2D FFT and obtain Fourier samples f̂[n_1, n_2], −n/2 ≤ n_1, n_2 < n/2, where n_1 and n_2 are frequency-domain variable.

(2) For each scale j and angle θ_l, form the product Û_{j,θ_l}[n_1, n_2] f̂[n_1, n_2].

(3) Wrap this product around the origin and obtain f̃_{j,l}[n_1, n_2] = W(Û_{j,θ_l} f̂)[n_1, n_2], where 0 ≤ n_1 < L_{1,j} and 0 ≤ n_2 < L_{2,j} for θ_l ∈ (−π/4, π/4).

(4) By applying the inverse 2D FFT to each f̃_{j,l}, discrete coefficients c^D(j, l, k) are obtained.

According to the above process, as shown in Fig. 2, we obtain a set of coefficient maps with four scales and sixteen directions from a normalized smoke image. Thus, we obtain coefficient maps containing coarse-to-fine and multi-directional texture information.

<!-- src: S051 -->
The first and fourth scales contain only one coefficient map, and the second and third scales contain sixteen and thirty-two coefficient maps, respectively. It is worth noting that coefficient maps are in different sizes. Being different from other traditional multi-scale transforms like wavelet transform, the coefficient map generated by Curvelet contains directional information of smoke, elevates ability to represent smoke textures and singularities along smoke edges.

<!-- src: S052 -->
To extract features from these coefficient maps, we propose Dual-encoded Local Binary Patterns (Dual-LBP) to get information on each coefficient map.

### 3.2 Dual-encoded Local Binary Patterns

<!-- original heading: "3.2 Dual-encoded Local Binary Patterns" (S053) -->

<!-- src: S054 -->
LBP is a gray-scale texture descriptor and can achieve rotation invariance after being mapped to RI (Rotation Invariant) pattern [2]. LBP captures spatial structures of textures in an image by encoding differences between one central pixel and its local neighborhood. However, structural frequency information is not involved in LBP codes.

<!-- src: S055 -->
To solve this problem, we use LBPs to extract frequency structures of images from Curvelet coefficient maps with different scales, orientations and locations. In the Curvelet coefficients, the first scale contains only one coefficient map c(1,1), the second one contains sixteen coefficient maps c(2,l) (l=1, 2,…, 16), and the third one contains thirty-two coefficient maps c(3,l) (l=1, 2,…, 32), and the fourth scale also contains only one coefficient map c(4,1).

<!-- src: S056 + S057 (equation number "(5)" split across the seam); equation (5) reconstructed from
     scattered subscripts -->
We compute LBP maps from coefficient maps of all scales. These LBP maps on coefficient maps can capture variations of coefficients in a local region for all scales. To avoid interpolation of coefficients, we employ a 3×3 rectangular neighborhoods instead of circular neighborhoods to compute an LBP codes as follows:

map_{m,n}(j, l) = Σ_{p=0}^{P−1} s(c^p_{m,n}(j, l) − c_{m,n}(j, l)) 2^p  (5)

where c_{m,n}(j, l) denotes the value of a central point (m, n) in a coefficient map c(j, l), c^p_{m,n}(j, l) is the value of the pth neighbor of the center point (m, n), P is the number of neighbors, s(x) is a binarization function that returns 0 for negative values and 1 otherwise, and map_{m,n}(j, l) is just an original LBP code at pixel (m, n) for the coefficient map c(j, l).

<!-- src: S058; "coefficent" preserved as printed -->
Since we have a set of coefficient maps c(j, l), we obtain 50 LBP maps map(j, l) from these coefficient maps. LBP codes of each coefficent contain contrast information in local regions.

<!-- src: S059 + S060 (equation number "(6)" split across the seam); equation (6) reconstructed -->
We compute the histogram of each coefficient LBP code map map(j, l), formulated as follows:

H_{j,l}(b) = (1/(MN)) Σ_{m=0}^{M−1} Σ_{n=0}^{N−1} δ(map_{m,n}(j, l) − b)  (6)

where δ(x) is a function that returns 1 for x=0 and 0 otherwise, and H_{j,l} ∈ R^{256×1}. We can obtain a lot of histograms H_{j,l} from a set of coefficient LBP maps map(j, l). In our implementation, the first scale has only one histogram H_{1,1}, the second one generates 16 histograms H_{2,l} (l=1,…,16), the third one obtains 32 histograms H_{3,l} (l=1,…,32), and the fourth scale also has only one histogram H_{4,1}. Therefore, we have 50 histograms.

<!-- src: S061; equation (7) reconstructed -->
To combine information from different scales and orientations, we aggregate all these histograms together to form an LBP histogram map of size 256×50, formulated as follows:

M = [H_{1,1}, H_{2,1}, …, H_{2,16}, H_{3,1}, …, H_{3,32}, H_{4,1}]  (7)

where H_{j,l} is just a column vector of the histogram map M, which represents the histogram of each LBP map c(j, l). Hence, we obtain the new map M that is aggregated by normalized LBP histograms with 256 bins from fifty coefficient maps.

<!-- src: S062; equation (8) reconstructed -->
Apparently, the size of the aggregated histogram map M is equal to 256×50. In the second step of encoding, we apply the LBP encoding method again on the histogram map M to generate another LBP map, defined as follows:

E_{m,n} = Σ_{p=0}^{P−1} s(M^p_{m,n} − M_{m,n}) 2^p  (8)

where E_{m,n} is an Dual-LBP code at a center point (m, n), M_{m,n} is the value of the aggregated histogram map at the center point, and M^p_{m,n} is the pth neighboring value of the center point.

<!-- src: S063 -->
Thus, we obtain another new LBP map from the histogram map M. Then we compute the histogram of the histogram map M. Dual-LBP extracts more details about frequent features from smoke images. The framework of Dual-LBP Encoding method is shown in Fig. 3.

### 3.3 Completed Local Binary Patterns

<!-- original heading: "3.3 Completed Local Binary Patterns" (S064) -->

<!-- src: S065 + S066 (sentence split at "CLBP_M," / "respectively."); equations (9)-(10) reconstructed
     from scattered subscripts split across the S066/S067 seam -->
The original LBP is a computationally simple and efficient operator, but it only computes differences between a center pixel value and its corresponding neighbors' gray values. The original LBP operator discards the magnitudes of differences by encoding the signs of differences in a 3×3 rectangular neighborhood. Guo et al. [16] proposed CLBP, an extension of the original LBP operator. The CLBP operator contains three operators, which are denoted as CLBP_S, CLBP_C and CLBP_M, respectively. The CLBP_S operator is just the same as the original LBP operator, which encodes the sign of local differences to reflect directions of local gradients. While CLBP_M involves the magnitudes to preserve variance information. CLBP_C encodes the differences between local center pixels and the global one to represent whole image gray levels. CLBP_C and CLBP_M are defined as follows:

CLBP_C_{P,R} = s(g_c − c_1)  (9)

CLBP_M_{P,R} = Σ_{p=0}^{P−1} s(m_p − c_2) 2^p  (10)

<!-- src: S067 -->
where c_1 is the average gray level of the whole image, c_2 is the mean difference magnitude of local neighborhood, g_c is the gray level of the center point, and m_p is the magnitude of the pth local difference, s(x) is defined as a binarization function, which is the same as Eq. (5).

### 3.4 Final features

<!-- original heading: "3.4 Final features" (S068) -->

<!-- src: S069; subscript debris re-attached: "the histogram H of CLBP" + orphaned "CLBP" =
     H_CLBP; "The histogram E of ... m,n" = E_{m,n}. "The CLBP method is encoded textures" preserved
     as printed (suspected source grammar slip). -->
We use CLBP to obtain three kinds of codes, which are CLBP_S, CLBP_C and CLBP_M, for each pixel. We compute a joint 2D histogram of CLBP_M and CLBP_C, and then reshape the 2D histogram to a 1D histogram. Finally, we concatenate the 1D histogram with the histogram of CLBP_S to obtain the histogram H_CLBP of CLBP. The histogram E_{m,n} of Dual-LBP method captures frequency features of images in Curvelet domains. The CLBP method is encoded textures of images in spatial domains.

<!-- src: S070; equation (11) reconstructed -->
We think that visual characteristics of smoke can be better captured if we combine spatial and frequency information. Hence, the final histogram H is obtained by combining E_{m,n} and H_CLBP, formulated as follows:

H = [E_{m,n}, H_CLBP]  (11)

After extracting features, we will consider the issue of features classification. We input the obtained histogram H into SVM for training and testing.

<!-- src: S071 -->
Since Curvelet coefficients contain components of different frequency, which correspond to different spatial distribution, they reflect spatial texture structure. Dual LBP models the relations between different coefficients to intrinsically captures co-occurrence texture structure. In other words, the proposed Dual LBP describes smoke textures in a macroscopic view [26].

### 3.5 Classification using SVM with GKO

<!-- original heading: "3.5 Classification using SVM with GKO" (S072) -->

<!-- src: S073 -->
We used Support Vector Machines (SVM) [27] to solve the image smoke classification problem. SVM is widely used in different fields such as clustering, classification, and dimensionality reduction. SVM is divided into two forms, which are linearly separable and linearly inseparable, respectively. Here we involve kernel trick to deal with linear inseparable features.

<!-- src: S074 + S075 (sentence continues across the seam "as shown in Eq." / "(12)"); equation (12)
     reconstructed (standard RBF kernel; numerator/denominator were scattered) -->
Kernel trick is thus a way to implicitly transform linear inseparable features of data onto a new space where the data becomes linearly separable [28]. The implicit new space is always higher-dimensional (possibly infinite) [29]. In general, the Gaussian kernel function, also known as Radial Basis Function (RBF) [30], to describe the relationship between every two feature vectors, as shown in Eq. (12),

K(x_i, x_j) = exp( − ||x_i − x_j||^2 / (2σ^2) )  (12)

where K(x_i, x_j) is the correlation or similarity between each two features x_i and x_j that are histograms H. The earliest method of optimizing β = 2σ^2 is to use cross-validation or grid search. One of the most well known methods is leave-one-out, which leaves only one sample as the test set and the remaining samples as the training set.
<!-- note: "In general, the Gaussian kernel function ... to describe the relationship" lacks a main verb
     in the source (suspected source-level slip); preserved. S075/S076 sentence seam rejoined. -->

<!-- src: S076 -->
Because each sample is repeatedly used during iterations, the method consumes a large amount of computation time. Hence, we use Gaussian Kernel Optimization (GKO) [31] to optimize β in our experiments. GKO is a kernel optimizing method for unsupervised learning, which is different from optimized methods of other supervised learning.

<!-- src: S077; variance definition partially garbled in extraction ("σ2 = ∑ ∑ −µ)."), reconstructed
     as far as unambiguous; the exact summand of the variance formula is NOT fully recoverable from
     the text layer — refer to PDF / [31] for the precise form -->
The GKO method does not need any constraints, and the β value obtained by the GKO method can be used as a starting point for further optimization. Hence, we use the GKO method to calculate the optimal value of β in Eq. (12). We define random variable Y_ij = X_ij^2 / σ^2 that satisfies the non-central Chi-square distribution with a degree of freedom one, where X_ij = ||x_i − x_j|| and the variance σ^2 = (1/n^2) Σ_{i} Σ_{j} (X_ij − µ)^2 [exact summation limits garbled in extraction; see Eq. (13) context and ref. [31]].

<!-- src: S078; piecewise equation (13) reconstructed from scattered fragments
     ("σ2 2.6 λ≤0.01  β≈σ2 L(λ) 0.01<λ<100 (13)  λσ2 =µ2 λ≥100"); trailing Fig. 4 axis debris
     ("3.0 2.5 2.0 L(λ)1.5 ... 10-2 10-1 100 101 102 λ") stripped as figure content -->
The optimal value of β can be obtained by the following equation:

β ≈ { 2.6 σ^2, if λ ≤ 0.01;  σ^2 L(λ), if 0.01 < λ < 100;  λσ^2 = µ^2, if λ ≥ 100 }  (13)

where L(λ) represents a function of λ. The relationship between λ and L(λ) is shown in Fig. 4, where λ = (µ/σ)^2 and µ = (1/n^2) Σ_{i=1}^{n−1} Σ_{j=1}^{n−1} X_ij represents the mean of the data set. The detailed proof of Eq. (13) is provided in [31].

<!-- src: S079 -->
According to the above method, β is optimized. In our smoke recognition experiments, gamma = 1/β = 4.6283 in the kernel function and the cost c = 35 in the loss function.

## Results

<!-- original heading: "4. Experimental Results and Analysis" (S080).
     Experimental setup (4.1 Data sets, 4.2 Implementation) and results (4.3 Analysis) are separate
     subsections in the source and kept in source order. -->

### 4.1 Data sets

<!-- original heading: "4.1 Data sets" (S081) -->

<!-- src: S082 -->
Several experiments were conducted on four data sets, each of which has an imbalanced number of smoke and non-smoke images. All images were manually cropped, resized and labeled as smoke images or non-smoke images. Smoke images of the data sets are easily distinguished by human eyes. The data sets are available at http://staff.ustc.edu.cn/~yfn/index.html. Smoke images of all datasets were resized to the size of 48×48 and converted to grayscale images for feature extraction.

<!-- src: S083 -->
Table 1 lists the details of the data sets. We used Set1 for training, and Set2, Set3, and Set4 for testing. Some samples are shown in Fig. 5. It can be seen that both intra-class and inter-class variances of smoke and non-smoke images are very large.

### 4.2 Implementation of compared methods

<!-- original heading: "4.2 Implementation of compared methods" (S084) -->

<!-- src: S085 + S086 (equation number "(14)" split across the seam); evaluation-criteria equations
     reconstructed from scattered subscripts -->
In order to verify the effectiveness of our method, we compared our method with some state-of-the-art algorithms by the three evaluation criteria in [32], which are Detection Rate (DR), False Alarm Rate (FAR) and Error Rate (ERR). They are defined as follows:

DR = P_p / Q_p × 100%;  FAR = N_p / Q_n × 100%;  ERR = ((Q_p − P_p) + N_p) / (Q_p + Q_n) × 100%  (14)

where P_p and N_p respectively denote the numbers of accurately detected true positive samples and negative samples mistakenly classified as positive samples, and Q_p and Q_n are the numbers of positive and negative samples, respectively.

### 4.3 Analysis of results

<!-- original heading: "4.3 Analysis of results" (S087) -->

<!-- src: S088; "MDLBP [37] LTrP [38]" missing comma preserved as printed -->
In our experiments, we used several feature extraction methods to validate the ability of our method to distinguish between smoke and non-smoke images on the three test sets. These compared methods are DRLBP [33], CLBP [16], LDBP [34], PLBP [35], PRICoLBP [36], MDLBP [37] LTrP [38] and DFD [39]. The compared LBP variants are all un-mapped for fair comparisons.

<!-- src: S089 -->
The threshold for LTrP is set to 0.1 to demonstrate better performance, and g for RBF in SVM is set to 1/1383 for all other comparison features. For DFD, default setting is adopted to extract features.

<!-- src: S090; "cocatenated" preserved as printed (suspected source typo for "concatenated") -->
We involve LBP and CLBP in our feature extraction step. Dual-LBP features based on the Curvelet domain and CLBP features on spatial domain are combined to form the final feature. In our CLBP, histograms of sign component and joint histograms of magnitude and center pixel maps are cocatenated to form CLBP_S_M/C. Finally, we aggregate dual LBP and CLBP features (denoted as Dual-LBP + CLBP) as our final feature vector, whose dimension is 256+768=1024.

<!-- src: S091 -->
From Table 2, we find that our method achieves lower FARs than other methods on three testing data sets. MDLBP involves information across RGB channels, so it obtains the best DRs among all the methods. While all the other LBP variants are conducted on grayscale images. So it does not provide fair comparisons. At the same time, the DRs got by our method are not obviously higher than other methods.

<!-- src: S092 -->
Hence, ROC (Receiver Operating Characteristic Curve) is adopted to present a more comprehensive comparison, as shown in Fig. 6. By varying classification threshold t from -1 to 1 at step 0.1, DR and FAR pairs are obtained at every step to plot ROC.

<!-- src: S093; "Table. 3" normalized to "Table 3" -->
Although the DRs of our method do not exceed the ones of other methods obviously, the ROCs illustrate that our method outperforms others, which means that the best classification planes are not always at t=0. The encoding step in our method can be replaced by any LBP-based methods. For instance, in Table 2 and Fig. 6, Dual-LBP + CLBP is adopted. Similarly, the other three combinations are Dual-LBP + LBP, Dual-CLBP + CLBP, Dual-CLBP + LBP.

<!-- src: S094 + S095 (sentence split across page 11/12 break: "performs best among all the" +
     "combinations.") -->
The experimental results of the 4 combinations are shown in Table 3. Although the FAR of our method is not the lowest on Set3 and Set4, the DR of our method is highest and ERR is lowest. Overall, our Dual-LBP + CLBP performs best among all the combinations.

<!-- src: S096 -->
It is notable that Dual-CLBP + CLBP performs worse than others on Set3 and Set4. The reasons may be: 1) After Curvelet transform, an original image is decomposed into sub-bands. Low-frequency ones correspond to flat regions, in which the sign of gradient can better capture the invariance than magnitudes do. 2) There are correlations between Curvelet coefficients. Hence, the M and C components in CLBPs bring redundancy rather than improvement.

<!-- src: S097 -->
Lower FAR means lower accidental false alarm, which is of great significance for smoke classification, and it can reduce the serious consequences of false alarms. Therefore, our method is of great practical application value.

<!-- src: S098 -->
As shown in Table 4, we employ different parameter optimization methods to demonstrate the performance of GKO. We also compare our approach with the grid search, which is proposed in [30]. According to the experimental results, grid search method is proved not suitable for parameters optimization for different datasets. The GKO algorithm improves the accuracy of SVM.

<!-- src: S099; "shorten the classifying time" preserved as printed -->
Although the GKO step is time-consuming, it provides better classification performance and shorten the classifying time. Meanwhile, grid search consumes 214.1 seconds. Hence the GKO algorithm yields better performance than the grid search one. The computation time and the number of support vectors by the GKO algorithm are less than that of grid search on Set2.

## Discussion

<!-- No standalone Discussion section in this paper. Discussion-style analysis is embedded in
     4.3 Analysis of results (S091-S099) and kept there in source order. -->

## Conclusion

<!-- original heading: "5. Conclusion" (S100) -->

<!-- src: S101 + S102 + S103 (single concluding passage split across three blocks and the p12/p13 break) -->
In order to improve the performance of the smoke classification, we present a novel feature extraction method termed Dual-LBP, and we combine the proposed Dual-LBP and CLBP to improve the discriminative ability of features. The Dual-LBP method first adopts Curvelet transform to decompose smoke textures into coarse-to-fine components. Then LBP histograms are extracted from the decomposed components, i.e., Curvelet coefficients, to generate a histogram map to describe local distributions of coarse-to-fine smoke textures. Third, LBP encoding is applied to the histogram map to capture texture distribution relations between different frequencies. The advanced feature encoding is explored, which connected Curvelet domains and spatial domains. Furthermore, our method discovers the potential relationship between each scale of the Curvelet coefficients and improves the smoke classification performances. Extensive experiments show that our method achieves improvements in smoke recognition over some state-of-the-art methods.

## Acknowledgments

<!-- No separate Acknowledgment section in this paper; the funding footnote (S011, p.1) serves that role. -->

<!-- src: S011 -->
This research was supported by National Natural Science Foundation of China (Grant No. 61862029, Grant No. 61562031), Science Technology Application Project of Jiangxi Province (No. GJJ170317).

## References

<!-- original heading: "References" (S104). Complete list [1]-[39], src S105-S143.
     "Article (CrossRef Link)." trailing markers preserved as printed (KSII house style).
     [15] author names mangled in source ("L. S, L. MW, and C. AC" — actual authors S. Liao,
     M. W. Law, A. C. Chung); preserved as printed. -->

[1] C. Palm, "Color texture classification by integrative co-occurrence matrices," Pattern Recognition, vol. 37, no. 5, pp. 965-976, May, 2004. Article (CrossRef Link).

[2] T. Ojala, M. Pietikäinen, and T. Mäenpää, "Multiresolution gray-scale and rotation invariant texture classification with Local Binary Patterns," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 24, no. 7, pp. 971-987, July, 2002. Article (CrossRef Link).

[3] N. Dalal and B. Triggs, "Histograms of oriented gradients for human detection," in Proc. of IEEE Computer Society Conf. on Computer Vision and Pattern Recognition, pp. 886-893, June 20-25, 2005.

[4] J. Ma and G. Plonka, "The Curvelet transform: A review of recent applications," IEEE Signal Processing Magazine, vol. 27, no. 2, pp. 118-133, March 2010. Article (CrossRef Link).

[5] A. Chenebert, T. P. Breckon, and A. Gaszczak, "A non-temporal texture driven approach to real-time fire detection," in Proc. of 18th IEEE International Conf. on Image Processing, pp. 1741-1744, September 11-14, 2011.

[6] T. H. Chen, P. H. Wu, and Y. C. Chiou, "An early fire-detection method based on image processing," in Proc. of Int. Conf. on Image Processing, pp. 1707-1710, October 24-27, 2004. Article (CrossRef Link).

[7] T. Çelik and H. Demirel, "Fire detection in video sequences using a generic color model," Fire Safety Journal, vol. 44, no. 2, pp. 147-158, February, 2009. Article (CrossRef Link).

[8] F. Yuan, "A fast accumulative motion orientation model based on integral image for video smoke detection," Pattern Recognition Letters, vol. 29, no. 7, pp. 925-932, May, 2008. Article (CrossRef Link).

[9] D. Zhang, S. Han, J. Zhao, Z. Zhang, C. Qu, Y. Ke, et al., "Image Based Forest Fire Detection Using Dynamic Characteristics with Artificial Neural Networks," in Proc. of Int. Joint Conf. on Artificial Intelligence, pp. 290-293, April 25-26, 2009. Article (CrossRef Link).

[10] C. Yu, J. Fang, J. Wang, and Y. Zhang, "Erratum to: Video fire smoke detection using motion and color features," Fire Technology, vol. 46, no. 3, pp. 651-663, July, 2010. Article (CrossRef Link).

[11] B. U. Toreyin, Y. Dedeoglu, and A. E. Cetin, "Wavelet based real-time smoke detection in video," in Proc. of 13th European Signal Processing Conf., pp. 1-4, September 4-8, 2005. Article (CrossRef Link).

[12] F. Yuan, "Video-based smoke detection with histogram sequence of LBP and LBPV pyramids," Fire Safety Journal, vol. 46, no. 3, pp. 132-139, April, 2011. Article (CrossRef Link).

[13] F. Yuan, J. Shi, X. Xia, Y. Yang, Y. Fang, and R. Wang, "Sub oriented histograms of Local Binary Patterns for smoke detection and texture classification," Ksii Transactions on Internet & Information Systems, vol. 10, no. 4, pp. 1807-1823, April, 2016. Article (CrossRef Link).

[14] J. Gubbi, S. Marusic, and M. Palaniswami, "Smoke detection in video using wavelets and support vector machines," Fire Safety Journal, vol. 44, pp. 1110-1115, November, 2009. Article (CrossRef Link).

[15] L. S, L. MW, and C. AC, "Dominant local binary patterns for texture classification," IEEE Transactions on Image Processing, vol. 18, no. 5, pp. 1107-1118, March, 2009. Article (CrossRef Link).

[16] Z. Guo, L. Zhang, and D. Zhang, "A completed modeling of Local Binary Pattern operator for texture classification," IEEE Transactions on Image Processing, vol. 19, no. 6, pp. 1657-1663, March, 2010. Article (CrossRef Link).

[17] S. Elaiwat, M. Bennamoun, F. Boussaid, and A. El-Sallam, "A Curvelet-based approach for textured 3D face recognition," Pattern Recognition, vol. 48, no. 4, pp. 1235-1246, April, 2015. Article (CrossRef Link).

[18] A. Uçar, Y. Demir, and C. Güzeliş, "A new facial expression recognition based on Curvelet transform and online sequential extreme learning machine initialized with spherical clustering," Neural Computing & Applications, vol. 27, no. 1, pp. 131-142, April, 2016. Article (CrossRef Link).

[19] T. Mandal, Q. M. J. Wu, and Y. Yuan, "Curvelet based face recognition via dimension reduction," Signal Processing, vol. 89, no. 12, pp. 2345-2353, December, 2009. Article (CrossRef Link).

[20] O. Chapelle, V. Vapnik, O. Bousquet, and S. Mukherjee, "Choosing multiple parameters for Support Vector Machines," Machine Learning, vol. 46, no. 1-3, pp. 131-159, May, 2002. Article (CrossRef Link).

[21] K. Ghiasi, R. Safabakhsh, and M. Shamsi, "Learning Translation Invariant Kernels for Classification," Journal of Machine Learning Research, vol. 11, pp. 1353-1390, April, 2010. Article (CrossRef Link).

[22] M. Wu, B. Schölkopf and G. Baktr, "A direct method for building sparse kernel learning algorithms," Journal of Machine Learning Research, vol. 7, pp. 603-624, April, 2006. Article (CrossRef Link).

[23] J. Ye, S. Ji, and J. Chen, "Multi-class discriminant kernel learning via convex programming," Journal of Machine Learning Research, vol. 9, pp. 719-758, June, 2008.

[24] E. J. Candès and D. L. Donoho, "Recovering Edges in Ill-Posed Inverse Problems: Optimality of Curvelet Frames," Annals of Statistics, vol. 30, no. 3, pp. 784-842, June, 2002. Article (CrossRef Link).

[25] E. Candès, L. Demanet, D. Donoho, and L. Ying, "Fast discrete Curvelet transforms," Multiscale Modeling & Simulation, vol. 5, no. 3, pp. 861-899, September, 2006. Article (CrossRef Link).

[26] Q. Wang, M. Chen, F. Nie and X. Li, "Detecting coherent groups in crowd scenes by multiview clustering," IEEE Transactions on Pattern Analysis and Machine Intelligence, pp. 1-1, 2018. (Online) Article (CrossRef Link).

[27] M. A. Hearst, S. T. Dumais, E. Osuna, J. Platt, and B. Scholkopf, "Support vector machines," IEEE Intelligent Systems & Their Applications, vol. 13, no. 4, pp. 18-28, July-August, 1998. Article (CrossRef Link).

[28] A. Temko, C. Nadue, "Classification of acoustic events using SVM-based clustering schemes," Pattern Recognition, vol. 39, pp. 682-694, April, 2006. Article (CrossRef Link).

[29] S. Yin, J. Yin, "Tuning kernel parameters for SVM based on expected square distance ratio," Information Sciences, vol. 370-371, pp. 92-102, November, 2016. Article (CrossRef Link).

[30] B. Scholkopf, K. Sung, C.J.C. Burges, F. Girosi, P. Niyogi, T. Poggio, and V. Vapnik, "Comparing support vector machines with Gaussian kernels to radial basis function classifiers," IEEE Transactions on Signal Processing, vol. 45, no. 11, pp. 2758-2765, November, 1997. Article (CrossRef Link).

[31] J. B. Yin, T. Li, and H. B. Shen, "Gaussian kernel optimization: Complex problem and a simple solution," Neurocomputing, vol. 74, pp. 3816-3822, November, 2011. Article (CrossRef Link).

[32] F. Yuan, J. Shi, X. Xia, Y. Fang, Z. Fang, and T. Mei, "High-order local ternary patterns with locality preserving projection for smoke detection and image classification," Information Sciences, vol. 372, pp. 225-240, December, 2016. Article (CrossRef Link).

[33] R. Mehta, K. Egiazarian, "Dominant Rotated Local Binary Patterns (DRLBP) for texture classification," Pattern Recognition Letters, vol. 71, pp. 16-22, February, 2016. Article (CrossRef Link).

[34] P. S. Hiremath, R. A. Bhusnurmath, "Multiresolution LDBP descriptors for texture classification using anisotropic diffusion with an application to wood texture analysis," Pattern Recognition Letters, vol. 89, pp. 8-17, April, 2017. Article (CrossRef Link).

[35] X. Qian, X. S. Hua, P. Chen, and L. Ke, "PLBP: An effective local binary patterns texture descriptor with pyramid representation," Pattern Recognition, vol. 44, no. 10-11, pp. 2502-2515, October-November, 2011. Article (CrossRef Link).

[36] X. Qi, R. Xiao, C-G. Li, et al., "Pairwise rotation invariant co-occurrence local binary pattern," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 36, no. 11, pp. 2199-2213, April, 2014. Article (CrossRef Link).

[37] S. R. Dubey, S. K. Singh, and R. K. Singh, "Multichannel decoded local binary patterns for content-based Image retrieval," IEEE Transactions on Image Processing, vol. 25, no. 9, pp. 4018-4032, June, 2016. Article (CrossRef Link).

[38] S. Murala, R. P. Maheshwari, and R. Balasubramanian, "Local tetra patterns: a new feature descriptor for content-based image retrieval," IEEE Transactions on Image Processing, vol. 21, no. 5, pp. 2874-2886, April, 2012. Article (CrossRef Link).

[39] Lei Z, Pietikainen M, Li S Z, "Learning discriminant face descriptor," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 36, no. 2, pp. 289-302, February, 2014. Article (CrossRef Link).

## Other

### Figure and table captions

<!-- Caption text only; numeric table rows in C005, C007, C009, C010 excluded as non-prose table debris -->

Fig. 1. The proposed smoke recognition framework <!-- C001, p.4 -->

Fig. 2. The four-scale Curvelet coefficients of a smoke image <!-- C002, p.5 -->

Fig. 3. Dual-Encoded features from Curvelet coefficient maps <!-- C003, p.7 -->

Fig. 4. Relationship between λ and L(λ) when λ ∈ (0.01, 100) <!-- C004, p.9 -->

Table 1. The image datasets <!-- C005, p.10; numeric rows excluded -->

Fig. 5. Samples from the four data sets. (a) Smoke and (b) non-smoke images from Set 1. (c) Smoke and (d) non-smoke images from Set 2. (e) Smoke and (f) non-smoke images from Set 3. (g) Smoke and (h) non-smoke images from Set 4. <!-- C006, p.10 -->

Table 2. Experimental results for smoke detection <!-- C007, p.11; numeric rows excluded -->

Fig. 6. ROCs of comparison methods on Set2, Set3 and Set4. <!-- C008, p.11 -->

Table 3. Comparisons of 4 combinations for our method <!-- C009, p.12; numeric rows excluded -->

Table 4. Performance comparisons on GKO and other versions of SVM <!-- C010, p.12; numeric rows excluded -->

### Author biographies

<!-- src: S144 + S145 (Yuan bio split across two blocks), S146-S149 -->

Feiniu Yuan received his B.Eng. and M.E. degrees in Mechanical Engineering from Hefei University of Technology, Hefei, China, in 1998 and 2001, respectively, and his Ph.D. degree in Pattern Recognition and Intelligence System from University of Science and Technology of China (USTC), Hefei, in 2004. From 2004 to 2006, he worked as a post-doctor with State Key Lab of Fire Science, USTC. From 2010 to 2012, he was a Senior Research Fellow with Singapore Bioimaging Consortium, Agency for Science, Technology and Research, Singapore. He is currently a professor and a PhD supervisor with Jiangxi University of Finance and Economics. His research interests include 3D modeling, image processing and pattern recognition.

Tiantian Tang received her B.E. degree in Communication Engineering from Institute of Technology, East China Jiaotong University, Nanchang, China, in 2011, and her M.E. degree in Signal and Information Processing from Jiangxi Science and Technology Normal University, Nanchang, China, in 2015. Her research interests include image processing and pattern recognition.

Xue Xia received her B.E. degree in Film & TV Arts and Technology and M.E. degree in Communication and Information Engineering from Shanghai University, Shanghai, China, in 2011 and 2014, respectively. She is currently a PhD candidate with School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, China. Her research interests include 3D display technology, image processing and pattern recognition.

Jinting Shi received her B.E. degree in Computer Science and Technology from Jiangxi Normal University, Nanchang, China, in 2003, M.S. degree in Computer Science and Technology from Jiangxi Agricultural University, Nanchang, China, in 2008, and Ph.D. degree in Management Science and Engineering from Jiangxi University of Finance and Economics, Nanchang, China. Her research interests include image processing and pattern recognition.

Shuying Li received the B.E. degree from University of Science and Technology of China, Hefei, China, and the Ph.D degree from Chinese Academy of Sciences. She is currently a professor with School of Automation, Xi'an University of Posts & Telecommunications, Xi'an, Shaanxi, China. Her research interest includes remote sensing, computer vision and pattern recognition.
