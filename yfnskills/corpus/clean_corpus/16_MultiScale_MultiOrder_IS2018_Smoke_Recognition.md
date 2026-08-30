<!--
FnyPro-1 Stage 00 Wave 3 Agent G clean corpus
Paper_ID: 16_MultiScale_MultiOrder_IS2018_Smoke_Recognition
Source: /workspace/16_MultiScale_MultiOrder_IS2018_Smoke_Recognition.md (bilingual reader, **Original:** blocks only)
Content policy: English original text only. Excluded: all Chinese, reader navigation/glossary/reading notes,
the venue/DOI line (S003), running headers ("F. Yuan et al. / Information Sciences 468 (2018) ..." in
S078/S118), and numeric table data rows embedded in text blocks (S060, S061, S067, S089, S100, S101, S102).
Body sentences trapped behind those table rows were recovered and rejoined (S059+S061 tail, S066+S067 tail,
S088+S090 tail, S102 tail). The reference list (S113-S120) appears verbatim and is retained, reflowed one
entry per line with cross-page splits rejoined. Author biographies (S121-S125) retained in an appendix.
Fixes applied: section-title glue split for 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 4.2.1 (headings were embedded
mid-paragraph); cross-column joins (S039+S040 "Projected|feature maps", S075+S076 "for|SOHLBP",
S077+S078 "Both|versions", S053+S054 "In the|second layer"); equations (1), (2), (4), (5), (7), (9)-(12),
(14) reassembled from fragments -- flagged inline, verify against PDF; Eq. (13) formula lost in extraction
(placeholder note inline). Heading "4.1 Smoke recognition" level lost in extraction (inferred, see comment).
OCR fixes: "com putation"->"computation", "sam pling"->"sampling", "K TH-TIPS"->"KTH-TIPS",
"MSD2L"->"MSD-2L", "withinvariances"->"within-variances", "10,0 0 0"->"10,000" (in ref [36]),
"KJLD120 6 6"->"KJLD12066", "f eature"->"feature" (in ref [14]); dangling footnote superscripts after
"VLFeat toolbox" and "vl_SVM" dropped. Authorial wording otherwise preserved verbatim, including
"Datesets"/"Comparision" (table captions), "symmentric" (ref [27]), "HLTPMC_LPP" vs "HLTPMC-LPP"
inconsistency, and "don't distinguish much between each other".
-->

# Learning multi-scale and multi-order features from 3D local differences for visual smoke recognition

Feiniu Yuan, Xue Xia, Jinting Shi, Lin Zhang, Jifeng Huang

## Abstract

To overcome shortages of conventional hand-crafted features, we propose a learning based feature extraction method for visual smoke recognition. We first slide a 3D sampling window in the scale space of images to densely compute 3D local differences across scales, and learn a projection matrix from all 3D local differences of training images. Then the projection matrix is used to transform 3D local differences of each image to generate feature maps, which naturally contain both local and holistic information. To further generate robust descriptors, we process these feature maps in two encoding ways: within-map and between-map encodings. The within-map encoding way generates an Local Binary Pattern (LBP) map for each feature map, while the between-map way encodes pixel-wise values across different feature maps to generate only one LBP map, denoted as a cross-sign map, for every eight feature maps. To make the two encoding ways have the same contributions, we weight the histograms of cross-sign maps and LBP maps with different coefficients. Each computational layer includes calculation of 3D local differences, learning of projection matrices, and encoding of projected features. Several computational layers can be stacked on top of each other to present a hierarchical structure to extract multi-order and high-level features. Subsequent layers carry higher order information on variations of local pixel values, which is more discriminative but also more sensitive to noise. To make a tradeoff between discriminative ability and noise suppression, Taylor-like coefficients are proposed to weight histograms computed from different computational layers. Experimental results demonstrate that the proposed method achieves better performance than most existing handcrafted methods and learning based feature extraction methods on both smoke recognition and texture classification.

Keywords: Feature learning; 3D local differences; Scale invariance; Smoke recognition; Local feature

## 1. Introduction

It has been proved that visual detection techniques can effectively detect fires in large and open spaces [9]. Visual smoke recognition provides earlier fire alarms, faster response and wider surveillance ranges than traditional sampling based fire detection methods [45]. Early video smoke detection methods usually analyzed smoke motion, color or shapes for feature representation. Yuan [45] captured edge, color and saturation information, and then selected shape-invariant features for video smoke detection. Yu et al. [44] proposed a smoke detection method by analyzing smoke color and motion. Jia et al. [15] used color and motion features to propose a salient smoke detection model for smoke detection. Kim et al. [18] proposed a smoke detection method based on Gaussian Mixture Models (GMM) for outdoor environments. However, for scenes captured by telephoto lenses or in an absence of wind, the distribution or shape of smoke does not change obviously in adjacent frames [1], so static features play more important roles than dynamic features in large wild space with distant views.

The general framework of single frame-based smoke detection in large wild scenes mainly contains three steps, which are image partition, feature extraction for every patch, classification of each patch and holistic decision of an image. We focus on the steps of feature extraction and classification of each patch, denoted as smoke recognition. Apparently, smoke recognition is the basic and key part of smoke detection. The fundamental task of visual smoke recognition is to distinguish smoke images or patches from non-smoke ones using computer vision algorithms. However, it is a challenging task to accurately recognize smoke from visual scenes, since smoke has no significant visual appearances, such as regular color and fixed geometric shapes. Fortunately, we find that smoke has obvious texture patterns, which are not subject to environment conditions and burning materials. Hence, texture information plays a reliable role in representing smoke [38].

Based on the above analysis and successful applications, we also adopt texture features to describe smoke. Accordingly, we regard smoke recognition as a kind of two-class texture classification. Local features are widely used to represent textures due to rotation invariance, illumination invariance and computational simplicity. As powerful image descriptors, local binary features are invariant to changes of local pixel values [25] caused by varying shapes and illuminations. Local feature descriptors have been proved effective and efficient in representing texture patterns, such as Local Binary Patterns (LBP) [30], Gabor feature vector [6], Local Ternary Patterns (LTP) [37], and Local Directional Pattern (LDP) [16]. There are many methods representing smoke by texture features. Zhao et al. [50] extracted spatio-temporal features and dynamic texture features to present a forest fire detection method. In the method, the spatio-temporal energy features were extracted from adjacent frames, and Local Binary Motion Pattern (LBMP) was presented to extract dynamic texture features. Yuan et al. [46] proposed high-order local ternary patterns by encoding magnitudes of noise-removed derivatives and values of center pixels (HLTPMC). Nevertheless, conventional texture descriptors still suffer from some prominent limitations, as will be illustrated in detail later. The main flaws of LBP-like methods are three folds: (1) manually designed features require domain knowledge, (2) multi-scale extensions do not involve relations between scales, (3) high-order extensions lack noise resistance.

In this paper, we propose a learning based multi-scale and multi-order feature extraction method, which does not require domain knowledge and is totally driven by data. We construct a scale space from an image and calculate 3D local differences across scales to extract multi-scale variations of pixel values. Then a projection matrix is learnt from all 3D differences of training images to find optimal projection directions. With the help of the learnt projection matrix, texture features belonging to different classes can be separated as far as possible while similar ones can be projected as close as possible. Afterwards, the projected differences, i.e., the feature maps, are encoded in two encoding ways to generate LBP codes with different orders. To balance the contributions of LBP histograms with different orders, different weights are used to concatenate these histograms for classification.

The main contributions of this paper are summarized as follows: (1) To capture cross-scale variations of pixel values, we compute 3D local differences across scales instead of 2D local differences in a single scale. Thus we can obtain stronger scale invariance than existing methods that extract features within a single scale. (2) In each layer, we process feature maps computed by a learnt projection matrix in two LBP-like encoding ways: within-map and between-map encodings. The within-map encoding way generates an LBP map for each feature map, while the between-map way encodes pixel-wise values across different feature maps to generate only one LBP map for every eight feature maps. (3) Different coefficients are used to weight histograms of LBP maps computed in the two encoding ways. Eight feature maps can produce one cross-sign map by between-map encoding and eight LBP maps by within-map encoding. To make the two encoding ways have the same contributions, we concatenate the cross-sign histogram with a weight of 1.0 and the eight LBP histograms with another weight of 0.125. (4) Taylor-like coefficients are proposed to weight histograms computed from different layers since subsequent layers carry higher order information on variations of local pixel values. Higher order information is more discriminative but also more sensitive to noise, so smaller coefficients are used to weight higher order features to make a tradeoff between discriminative ability and noise suppression.

The remainder of the paper is organized as follows. Section 2 describes related work on local and global feature descriptors of patches. In Section 3, we present the 3D difference-based feature learning method in detail. Then, extensive experiments are given in Section 4. At last, we conclude the paper in Section 5.

## 2. Related work

Early LBP-based local texture descriptors are restricted to relatively small neighborhoods on a single scale [27], and they cannot perfectly involve local and holistic information across entire images and scales. To solve these problems, multi-scale, high-order and global information is involved to better represent texture distributions.

Existing multi-scale extensions to traditional methods usually enlarge supporting areas of features to obtain rich information. Guo et al. [12] took magnitudes of neighboring differences into account to improve the representation ability of original LBPs, and then achieved scale invariance [11] by regarding the maximum frequency in histograms among different scales as the scale invariant feature. Hergenbart and Uhl [13] used Gaussian filters with different variances to construct a scale space, and computed scale adaptive LBPs by finding optimized neighboring points for LBP codes. The above two methods extracted multi-scale features from a single image by altering supporting areas of local features. Song et al. [35] adopted Differences of Gaussians (DoG) and Differences of offset Gaussians (DooG) for extraction of scale invariant texture features. However, the relations between different scales were still not investigated. In addition, multi-scale response maps obtained by transforms, like Gabor filters, often result in high dimensional features or require high computational consumption. To reduce computational complexity, Liu et al. [22] proposed to use random projections for texture segmentation, which are viewed as the functions of non-adaption, information preserving, and universal dimensionality reduction without losing salient information. Guo and Mu [10] simultaneously implemented biologically-inspired features (BIF) and manifold learning to achieve a low-dimensional feature representation for age estimation, but this method suits for biometric measures [33] rather than smoke textures. Cao et al. [3] proposed a multi-scale descriptor for leaf image retrieval, which adaptively varied the sampling radii of local features with respect to each contour point in leaves. The above-mentioned methods intrinsically accomplished multi-scale analysis by concatenating features from different scales, which can be computed by different operators or a single operator with different parameters [17]. However, these kinds of methods achieved limited improvements since the relations between features from different scales were not effectively explored.

Global features have been combined with local features to obtain more accurate prediction results for texture classification [20]. To capture the intrinsic correlation between LBPD and other features, Hong et al. [14] combined LBP differences (LBPD) with a covariance matrix to propose the covariance and LBPD descriptor (COV-LBPD). Wang et al. [41] captured the global intrinsic relationships of neighboring pixels to improve object segmentation performance. Khadiri et al. [17] involved both local and global information to represent multi-scale salient local texture structures.

Although high-order variants of these features capture more information on local pixel values and produce compact codes [46], these methods lack noise resistances. Yuan et al. [48] leveraged Hamming distances to discover the co-occurrence of neighboring LBP codes as high-order information, and used Gaussian kernels to suppress noise before encoding. Nevertheless, the above features are designed in manual ways, so domain knowledge is usually required to explore effective features. To overcome drawbacks of manual features, feature learning methods have been successfully proposed for face recognition [19,23,24,39], object classification [20,24] and texture classification [28]. Lei et al. [19] learnt discriminant features in a data-driven way. Mehta and Egiazarian [28] proposed a texture descriptor called dense micro-block difference (DMD), in which micro-block-pairs in a set of image patches were sampled from isotropic Gaussian distributions. In addition, Fisher vectors were adopted in encoding to preserve more information. Lu et al. [23] proposed an unsupervised feature learning approach. The codebook, coefficient and projection matrices were learned iteratively. Lu et al. [24] learned a cost-sensitive local binary descriptor from raw pixels for facial age estimation. However, these features were learned from a single scale. To our knowledge, there are few traditional smoke recognition methods in the literature, which can perfectly involve the aforementioned information, and especially information across both scales and orders for smoke recognition.

In deep learning, a hierarchical network structure is usually constructed for automatic feature extraction and classification. Multi-channel convolutions and hierarchical representations widely used in deep learning can be used to extract cross-scale information. As a hierarchical structure goes deeper, more abstract or higher level information can be captured. Oh et al. [29] modeled cross-scale information by a network based on Gabor filtering. Xu et al. [40] proposed local binary convolution (LBC) as an alternative to layers in standard convolutional neural networks (CNN), but the performance might be unstable because of stochastically initialized binary kernels. Shi et al. [34] facilitated ground-based cloud classification using deep CNN models. Shallow layers extracted low-level orderless texture information while deeper ones captured high-level spatial layout. Deep learning methods can extract high-level features, but a huge number of labeled samples are needed for training [36]. Xu et al. [42] acquired diverse samples by synthesizing adequate smoke images, thus the goal of their method was to decrease the gap between synthetic and real images, and simultaneously separate smoke and non-smoke images. Frizzi et al. [9] adopted CNN to identify fire and smoke in videos, and the localization was achieved by sliding windows. But only red fire can be detected by the method, and more than 20 thousand images were needed in training while less than 6 thousand images were used in testing. These indicate that the number and diversity of samples are limitations for training deep models [42].

Inspired by successful applications of both learning based features and local features, we first compute 3D local differences from training samples, then learn cross-scale and high-order features from these differences, and finally encode these features for smoke recognition. To our knowledge, feature learning methods have not been used for smoke recognition, and we also do not find that the combination of learning and encoding methods is used in smoke recognition, so the proposed method is quite novel and original in the literature.

## 3. The proposed method

In this section, we detail the proposed method from three steps: 3D difference calculation, projection matrix learning, and feature encoding.

### 3.1. 3D difference calculation

<!-- Heading "3.1. 3D difference calculation" was glued mid-paragraph in extraction block S023; split here. -->

In order to get multi-scale and hierarchical features, we construct a scale space by Gaussian filters without down sampling [21] and calculate 3D local differences in the scale space. Conventional multi-scale images are obtained by constructing a Gaussian image pyramid, which is generated by Gaussian filtering and down sampling. To facilitate cross-scale encoding, we do not use down sampling to change the size of feature maps. Thus, we establish a scale space L consisting of images with the same resolution using the following equation:

<!-- Equation (1) reassembled from inline fragments in S023. Verify against PDF. -->

L_1 = I, k = 1; L_k = I * G_k, k = 2, 3, ..., K, (1)

where L_k is the k th scale of the scale space L, and * stands for convolution. I is an original image located at the first scale denoted as L_1, and G_k represents the k th Gaussian filter with variance σ_k, which varies from the 2nd scale to the K th scale.

By constructing the scale space, every original image I in a dataset is augmented to K levels of multi-scale images. Each L_k in the scale space is in different sharpness but shares the same resolution, so that 3D samplings can be easily computed. Through 3D sampling, we can obtain a huge number of 3D local differences in the scale space for capturing local features in the view of several scales.

An LBP code encodes local differences between values of a center pixel and its neighbors. Histograms of LBP codes can represent local changes of pixel values in local regions around each pixel. Inspired by LBP coding, we extract variations of pixel values across scales in a similar way. We compute a 3D difference matrix in a 3D local region centered at (x, y) according to Eq. (2), which removes the mean of pixel values across K scales. Thus, a 3D difference vector, which is grouped from the 3D local difference matrix, is obtained from every local region and the illumination sensitivity is decreased.

<!-- Equation (2) reassembled from a heavily garbled three-part display (matrix braces shattered
in extraction, block S025). Structure inferred from the surrounding prose. Verify against PDF. -->

R_k = [ L_k(x-r, y-r) ... L_k(x-r, y+r); ... L_k(x, y) ...; L_k(x+r, y-r) ... L_k(x+r, y+r) ],

m_R = (1 / ((2r+1)^2 × K)) Σ_{k=1}^{K} Σ_{i=-r}^{r} Σ_{j=-r}^{r} R_k(i, j),

D_k = [ R_k(0,0) - m_R ... R_k(0,2r) - m_R; ... R_k(i,j) - m_R ...; R_k(2r,0) - m_R ... R_k(2r,2r) - m_R ], (2)

where R_k is a local matrix with radius r centered at (x, y) on the k th scale. Obviously, R_k ∈ R^((2r+1)×(2r+1)). R_1, R_2, ..., R_K share the same size, so we can build a 3D local region R = [R_1, ..., R_K], which is intrinsically a 3D tensor, and R ∈ R^(K×(2r+1)×(2r+1)). m_R is the mean of pixel values in the 3D local region R, and D_k is a corresponding local difference matrix on the k th scale obtained by subtracting the mean m from every local matrix R_k. By changing the center coordinates (x, y) of the 3D local region, we can regard the 3D local region R as a sliding 3D sampling window.

We compute 3D local differences in a scale space instead of an image pyramid. The reason is that we can avoid an "out of boundary" problem. For example, if we slide the 3D local re-sampling window R in the image pyramid to compute 3D differences, we will encounter a serious problem that the 3D re-sampling window R may be out of the image pyramid, as shown in Fig. 1(a). Hence, we choose to compute 3D local differences in the scale space, as shown in Fig. 1(b).

According to Eq. (2), D_k ∈ R^((2r+1)×(2r+1)), and K scales of D_k comprise a 3D local difference matrix D_local = [D_1, ..., D_K]. Hence, D_local has K(2r+1)^2 elements, which are aggregated together to form a column vector d ∈ R^(K(2r+1)(2r+1)×1), as shown in Fig. 2.

Similar to the illumination invariance brought by LBP local differences, illumination sensitivity is suppressed by encoding mean-removed 3D local differences. In our implementation, r = 1 and K = 3, so R_k ∈ R^(3×3).

With the help of Gaussian filters, an image in a fine scale has more detailed textures than a coarse one [2], but fine scales contain more noise than coarse scales. Thus, we use scale space to achieve a coarse-to-fine sketch of texture distributions. Since texture representations across different scales are involved, multi-scale information is captured in R and illumination invariance is additionally achieved by encoding D_local. Multi-scale information is less sensitive to noise and scales [8].

To fully extract 3D local information, we slide the 3D sampling window R in scale space to densely compute difference vectors in horizontal and vertical steps of s pixels. For the sake of symbol re-usage, d_i denotes a 3D local difference vector d centered at the i th pixel, and all difference vectors { d_i | i = 1, 2, ..., n } from the j th image are aggregated to form a difference matrix D^j_vec, formulated as:

<!-- Equation (3) and the D_all definition reassembled from block S030, where the fragment
"vec , D 2 vec , ..., D N" had been displaced to the end of the paragraph. Verify against PDF. -->

D^j_vec = [ d_1, d_2, ..., d_n ], (3)

where n is the sliding number. We aggregate all D^j_vec from N training images to produce a training difference matrix D_all = [ D^1_vec, D^2_vec, ..., D^N_vec ], which has the dimension of K(2r+1)^2 × nN. Since D_all contains holistic and local differences, a projection matrix should be learnt from D_all to span a feature space where both holistic and local information can be preserved in a more discriminative and compact way.

### 3.2. Discriminative projection matrix learning

<!-- Heading "3.2. Discriminative projection matrix learning" was glued mid-paragraph in block S030; split here. -->

Calculation of our 3D local differences takes multi-scale information into account, but produces a great number of differences. So dimensionality reduction is needed. One way to avoid high dimensions of differences is to split images into several non-overlapping patches [26]. However, structure information across patches in smoke and texture images is not as clear as that in face images. Texture and smoke images contain self-similar structures or certain color patterns, while face images have geometrical structures, facial key points or facial landmarks. As a result, concatenated features from too many patches may not reflect global structure information but bring redundancy for texture images. Another way is to learn projection matrices from data. Appropriate projections transform high-dimensional data into a low-dimensional equivalent representation while retaining most information to increase discrimination and reduce redundancy simultaneously. Hence, projecting rather than splitting images is adopted in our method.

Based on the above analyses, the goal of projection is to find several dominant directions, where local differences can be projected to minimize reconstruction errors, or to simultaneously separate different samples and cluster similar samples. Aiming at smoke recognition, i.e., to solve a binary classification problem, linear discriminant analysis (LDA) is used as the projection criterion according to Eqs. (4)-(7). The within-class scatter matrix S_w^c of the c th class and the total within-class scatter matrix S_w are defined as follows:

<!-- Equation (4) reassembled from garbled display in S031 (brace fragments, shattered summation
bounds). Summation structure inferred from the prose in S032. Verify against PDF. -->

S_w = Σ_c S_w^c,

S_w^c = Σ_{i=1}^{n} Σ_{j=1}^{N_c} (d^j_i - m_{c,i})(d^j_i - m_{c,i})^T,

m_{c,i} = (1/N_c) Σ_{j=1}^{N_c} d^j_i, (4)

where N_c represents the number of images of the c th class, n is the sliding number in every image, d^j_i stands for a local difference vector at the i th sliding position of the j th image, and m_{c,i} denotes the mean vector of N_c local difference vectors d_i at the i th sliding position for the c th class.

The between-class scatter matrix S_b is defined as follows:

<!-- Equation (5) reassembled from garbled display in S033; the normalizer of m_i was lost in
extraction (fragment "m i = 1 ... d j i") and is inferred as the mean over all samples. Verify against PDF. -->

S_b = Σ_c Σ_{i=1}^{n} N_c (m_{c,i} - m_i)(m_{c,i} - m_i)^T,

m_i = (1/N) Σ_{j=1}^{N} d^j_i, (5)

where m_i is the mean vector of 3D local difference vectors at the i th sliding position throughout all samples.

Actually, m_i and m_{c,i} are the centroid of all classes and the c th class at the i th sliding position, respectively. Denoting a projection vector as ω, we can define the corresponding within-class and between-class scatter matrices of the projected data as ω^T S_w ω and ω^T S_b ω, respectively. Since the goal is to maximize the between-class scatter and minimize the within-class scatter simultaneously, the projection matrix W = [ω_1, ω_2, ..., ω_l], where l < min(K(2r+1)^2, C-1), can be obtained by maximizing the following criterion:

J(ω) = (ω^T S_b ω) / (ω^T S_w ω). (6)

Constrained by normalization ω^T S_w ω = 1, Eq. (6) can be re-written as a Lagrange equation. Then the goal can be reached by solving the partial derivative of L with respective to ω, formulated as:

L(ω) = ω^T S_b ω - λ(ω^T S_w ω - 1), ∂L(ω)/∂ω = 0, (7)

where [...]. <!-- The clause after "where" in Eq. (7)'s explanation was lost in extraction
(presumably identifying λ as a Lagrange multiplier); consult PDF. -->

Eq. (7) has a closed-form solution and can be further simplified to S_b ω_i = λ_i S_w ω_i, which is just a generalized eigenvalue problem. By solving the generalized eigenvalue problem, l eigenvectors can be obtained. In order to encode the projected differences in an LBP-like way, l is set to a multiple of 8. In our smoke recognition experiments, l = 8. Thus, 8 eigenvectors corresponding to the 8 biggest eigenvalues are adopted, i.e., [...]. <!-- Fragment after "i.e.," lost in extraction; based on Section 3.4 (block S048)
it is presumably "W = [ω1, ω2, ..., ω8]". Consult PDF. -->

Different from conventional LDA, the two scatter matrices are not computed from all differences of every whole image, but from 3D differences at each sliding position across all images. That is to say, the centroids are computed in a sliding-position-wise way instead of a vector-wise one, as shown in Fig. 3.

In binary classification, the rank of conventional S_b is 1 because S_b is the sum of difference matrices between two centroids of each class and the global centroid of all classes. Hence, the maximum number of eigenvectors with non-zero eigenvalues is equal to 1. As a result, the projected feature has only one dimension since there is only one projection vector whose eigenvalue is not zero, so most information is lost after projection. However, as shown in Fig. 4, our method computes the scatter matrices at every sliding position across all training images, so the rank of S_b is absolutely far bigger than 1. Our method can obtain more projection vectors to constitute a projection matrix. Then the projection matrix is used to transform 3D local differences to a more discriminant feature space, in which texture-related information is well preserved and more discriminatively represented.

We use the projection matrix W to transform a difference vector d_i at the i th sliding position in an image to produce a projected feature vector x_i, formulated as:

x_i = W^T d_i = [ω_1, ω_2, ..., ω_8]^T d_i, (8)

where the eigenvector ω_k stands for the k th column vector of the projection matrix W, and x_i ∈ R^(8×1).

ω_k can be used to transform all difference vectors d_1, ..., d_n to generate corresponding projected features x_1(k), ..., x_n(k), which are then reshaped to form the k th feature map M_k with n features. The projection matrix W, which consists of eight eigenvectors ω_1, ..., ω_8, is used to transform all difference vectors d_1, ..., d_n to obtain eight feature maps M_1, ..., M_8, as shown in Fig. 5. In Fig. 6, a scale space is constructed and 3D local differences are computed in step (a), projection matrices and feature maps are obtained in step (b), and LBP maps are calculated by two encoding ways in step (c).

The bigger the eigenvalue is, the more important the corresponding eigenvector is. By computing the eigenvectors with top eigenvalues, principal information of multi-scale 3D differences is explored and preserved, thus redundancy brought by densely sliding the 3D sampling window is significantly reduced.

### 3.3. Within-map and between-map encodings

<!-- Heading "3.3. Within-map and between-map encodings" was glued mid-paragraph in block S039;
split here. The dangling word "Projected" at the end of S039 continues in S040 ("feature maps are
derived..."); rejoined below. -->

Based on the facts that local binary features are more robust to illumination [25], and that high order information helps improve the discriminant ability of features [46], we use two encoding methods to extract local binary features. Projected feature maps are derived from local differences that contain actually first-order information about pixel values. The within-map encoding way is individually used on each feature map and encodes differences of features to extract original LBP codes apparently carrying second-order information about pixel values, while the between-map way directly encodes the signs of sliding-position-wise values from different feature maps to generate the first-order representation for pixel values.

We use the within-map way to generate eight original LBP maps, denoted as LBP_1, ..., LBP_8, from these eight feature maps in Fig. 6. M_k(x, y) represents the value at a center pixel (x, y) in the k th feature map, and M_k(x_i, y_i) denotes the value of the i th neighbor of the center pixel, so an original LBP code LBP_k(x, y) for the center pixel can be computed as follows:

<!-- Equations (9)-(11) reassembled from garbled display fragments in block S041. Verify against PDF. -->

LBP_k(x, y) = Σ_{i=0}^{7} s( M_k(x, y) - M_k(x_i, y_i) ) 2^i,

s(v) = 1 if v ≥ 0; 0 otherwise, (9)

Simultaneously, we use the between-map way to generate an LBP map across these feature maps M_1, ..., M_8, as shown in Fig. 7. First, these feature maps are squashed to binary maps with values of 0 and 1 according to the rule that 1 is outputted for positive entries and 0 otherwise. For a pixel at (x, y), eight binary bits are obtained from the same coordinates (x, y) across eight feature maps, and the i th bit corresponds to the i th feature map. Then, eight binary bits are regarded as a decimal code for the pixel at (x, y). Thus we obtain another LBP map LBP_0, which is called a cross-sign map, formulated as Eq. (10). The LBP code at the pixel (x, y) of LBP_0 is computed as follows:

LBP_0(x, y) = Σ_{k=1}^{8} s( M_k(x, y) ) 2^(k-1). (10)

To improve discriminative ability for texture classification, we generate a cross-magnitude map. The calculation of the cross-magnitude map is similar to CLBP [12]. These feature maps are holistically mean-removed, quantized and decimalized to generate the cross-magnitude map. The processing is formulated as follows:

LBP_mag(x, y) = Σ_{k=1}^{8} s( |M_k(x, y)| - (1/(ab)) Σ_{i,j} |M_k(i, j)| ) 2^(k-1), (11)

where a and b are the width and height of feature maps, and ab = n.

The between-map encoding not only combines information from different maps but also captures the relation between maps in an LBP-like way. The between-map way generates two LBP maps, which are a cross-sign map LBP_0 and a cross-magnitude map LBP_mag for texture classification. A cross-magnitude map is not needed for smoke recognition since small images in our smoke datasets can be well characterized merely by a cross-sign map LBP_0.

In summary, we use the within-map and between-map encoding ways to generate eight LBP maps LBP_1, ..., LBP_8 and one cross-sign map LBP_0 from every eight feature maps for smoke recognition, respectively. We use the two encoding ways to generate eight LBP maps LBP_1, ..., LBP_8, one cross-sign map LBP_0 and one cross-magnitude map LBP_mag from every eight feature maps for texture classification. Histograms of LBP_mag, LBP_0, ..., LBP_8 can be calculated respectively by Eq. (12).

<!-- Equation (12) reassembled from garbled display in block S043. Verify against PDF. -->

h_symbol(j) = Σ_{x,y} δ( LBP_symbol(x, y) - j ), (12)

where symbol ∈ {mag, 0, 1, 2, ..., 8}, δ(v) is a function that returns 1 for v = 0 and 0 otherwise, and j denotes the j th bin of a histogram h_symbol computed from an LBP map LBP_symbol.

The final feature vector is the concatenation of eight LBP histograms h_1, ..., h_8 and only one histogram h_0 of a cross-sign map for smoke recognition. In texture classification, the final feature vector is generated by concatenating all histograms h_mag, h_0, h_1, ..., h_8. To make the two encoding ways have the same contributions, we weight these histograms by Eq. (13) before concatenation.

<!-- The formula of Eq. (13) was lost in extraction (only its number "(13)" survived in block S045).
Based on the surrounding prose it weights the cross-sign histogram by α0 = 1 and each LBP histogram
by α1 = 0.125 before concatenation. Consult PDF for the exact expression. -->

We set α0 = 1 and α1 = 0.125 so that α0 and α1 are inversely proportional to the number of cross-sign histogram and LBP histograms. Thus the contribution made by the two encoding ways is balanced.

### 3.4. The overall framework of our method

<!-- Heading "3.4. The overall framework of our method" was glued mid-paragraph in block S045; split here. -->

The pipeline of our feature extraction method is illustrated in Fig. 8. Three main steps in the above three sections are marked by gray rectangles with blue letters. First, a scale space L is constructed by Gaussian filters. Second, with the help of a sliding sampling window R, the 3D local differences D_local are acquired by subtracting local means m_R from values of pixels in local regions. 3D difference vectors of all training images aggregated in D_all are used for projection matrix learning. These procedures are grouped into step A.

In step B, scatter matrices of difference vectors across all images are accumulated at each sliding position from D_all, then a projection matrix W is learnt by maximizing between scatters and minimizing within scatters simultaneously.

In step C, local difference vectors are projected into a discriminant space to generate eight feature maps through W. Then within-map and between-map encoding methods are applied on these feature maps to generate eight LBP maps and two cross-maps. Histograms of these maps are computed and then concatenated with different weights to form a multi-scale, high-order, and compact feature vector.

The number of projection vectors in W is usually set to a multiple of eight so that between-map encoding can generate codes with eight binary bits. In our implementation, we preserve eight projection vectors for smoke recognition, i.e., W = [ω_1, ω_2, ..., ω_8]. Finally, we use the projection matrix W to generate eight LBP histograms and two cross-histograms. As illustrated in Fig. 8, except for step B that is only applied to images for projection matrix learning, all the other steps are applied to either training images or other ones.

Since a sliding sampling window produces lots of 3D local differences, the learning of W from many differences captures very general properties of cross-scale differences. Thus, steps A and B can be separated as a learning step. Therefore, we propose a classification or recognition framework consisting of learning (known as projection matrix learning), feature extraction and classification, as shown in Fig. 9. The samples for projection matrix learning and feature extraction neither have to be the same ones nor have to come from the same dataset. This simplifies learning-based feature extraction procedures, since only feature extraction and classification are needed once the learning step is completed. The framework of our method is extensible and flexible. The characteristics of our framework is summarized as follows: (1) The learning method is not limited to LDA. (2) The encoding method of original LBP can be replaced by other methods, such as CLBP [12], HLTP [46]. (3) Grouping steps A, B and C into a computational layer, then more layers can be stacked on top of each other to build a framework with deep hierarchical structures. This is an extension to the framework in Fig. 9 and will be illustrated in the next section. (4) The learning step is needed only once. Hence, the computational complexity will not increase heavily when the structure goes deeper.

### 3.5. Extension and visualization

<!-- Heading "3.5. Extension and visualization" was glued mid-paragraph in block S050; split here. -->

The general framework in Fig. 10 extends the feature extraction part of our original framework to a multi-layer network without feedback. Learning is demonstrated on the left while feature extraction on the right. In Fig. 10, there are q layers, each of which contains three above-mentioned steps A, B and C. Step D stands for a non-linear transform process and is optional. Step E is a feature fusing method, which assigns Taylor-like coefficients to histograms from different layers for concatenation.

In learning, 3D local differences are computed by step A, and projection matrices are learnt by step B. Then feature maps for calculating 3D differences in the next layer are generated by step C. A q-layer network produces q projection matrices { W^i | i = 1, 2, ..., q }, which are used for generating feature maps in feature extraction steps. Accordingly, the superscript q indicates the q th layer. For instance, W^1 is the matrix W in the 1st layer.

In the 1st layer of feature extraction, the projection matrix W^1 transforms an input image to generate eight feature maps M^1, from which weighted LBP histograms h^1 are computed by Eqs. (12) and (13). Similarly, the projection matrix W^i in the i th layer is used to transform these 3D differences of feature maps M^(i-1) in the (i-1)th layer into feature maps M^i and corresponding histograms h^i.

High order information helps improve discriminative ability but sensitive to noise [46]. In real signals, high order information usually has smaller energy than high order components, and this phenomenon can be easily observed in the Taylor series expansion of a signal:

<!-- Equation (14) reassembled from garbled display in block S053. Verify against PDF. -->

g(x + 0) ≈ Σ_k ( g^(k)(0) / k! ) x^k = g(0) + g^(1)(0) x + ( g^(2)(0) / 2! ) x^2 + ..., (14)

where g^(k)(0) denotes the k th order derivative at 0. Our 3D local differences actually contain information of g^(1)(0), and the within-map and between-map ways are equivalent to encoding of g^(2)(0) and g^(1)(0) in the 1st layer, respectively. In the second layer, the two ways encodes g^(3)(0) and ignores g^(2)(0). Therefore, the deeper the features goes, the higher order they are.

To balance discriminative ability and noise suppression, we weight histograms of higher order features with smaller coefficients before concatenating them. Regarding the factorials in Eq. (13) as weights, higher order information plays less important role in feature representation. Based on this, we propose a Taylor-like histogram weighting method, in which smaller weights are assigned to higher order histograms to make a tradeoff between discriminative information extraction and noise suppression. Thus, a multi-layer feature can be defined as h_final = [ h^1, h^2/2!, ..., h^q/q! ] for final classification.

The deep structure of our method is different from PCA-Net [4]. The main differences are that we slide 3D local sampling windows in scale space for difference computation, propose the within-map and between-map encoding ways to extract local features, and use Taylor-like coefficients to weight histograms from difference layers. To gain insights into the behavior of our feature extraction process, we visualize multi-scale images, feature maps and LBP-like maps including original LBP maps and cross-maps. As shown in Fig. 11, 3D local differences containing multi-scale information are projected onto 8 discriminant directions, on which edges and textures are clearly preserved.

Original LBP maps of eight feature maps carry high order information, so visualization of the two encoding ways show that eight original LBP maps in Fig. 11(g) have much more noise than those in Fig. 11(d) and (e). The cross-sign map is a discriminative and compact integration of LBP maps from multi-scale images, so the texture distributions in cross-sign maps are more stable. Cross-magnitude maps characterize the magnitudes of local differences, which contribute less to textures than signs do [12], so the patterns in Fig. 11(e) are not as many as those in Fig. 11(d).

To further analyze our projection and encoding step, we preserve 16 projection vectors as demonstrated in Fig. 8, generate cross-sign maps and cross-magnitude maps using the 16 projection vectors, and visualize these maps as shown in Fig. 12. Edges and shapes are mostly preserved in Fig. 12(a), which is obtained by the top 8 projection vectors, while Fig. 12(c) shows the result by last 8 projection vectors. In other words, cross-sign map in Fig. 12(a) carries more information than that in Fig. 12(c). Thus, it is proved that most information is resided in the first 8 projection vectors corresponding to the 8 biggest eigenvalues. Besides, the two cross-magnitude maps do not distinguish from each other since cross-magnitude maps hold less patterns, which has been proved in [12].

According to the above analyses, if more than 8 projection vectors are preserved during learning, projection vectors except for the top 8 ones are used only for cross-sign maps and not for cross-magnitude ones. In our experiments, we compute a cross-sign histogram and eight original LBP histograms in smoke recognition. So the standard feature for smoke recognition is in dimension of 256 + 256 × 8 = 2304. For texture classification, we use the two encodings to extract a cross-sign histogram, a cross-magnitude histogram and eight LBP histograms from the top 8 feature maps, and we calculate only one cross-sign histogram for the 9th–16th eigenvectors. As a result, the dimension of the texture features is 256 × 2 + 256 × 8 + 256 = 2816.

<!-- The final sentence above ("cross-sign histogram, ... 2816") was recovered from block S061,
where it had been glued behind the Table 2 data rows; rejoined to the dangling "to extract a" in S059. -->

## 4. Experiments

<!-- The heading level "4.1. Smoke recognition" (and likely a "4.1.1" heading, e.g. "Datasets and
compared methods") is missing from the extraction: the reader jumps from "4. Experiments" straight
into setup paragraphs and then "4.1.2. Experimental protocols and results". A dataset-description
paragraph around Table 1 may also be lost (translation notes flag an extraction gap). Consult PDF. -->

Besides the first scale that is an input image, three scales were generated for construction of the scale space. The same parameters of Gaussian filters were used for the four data sets.

Ten comparison methods with twelve versions of features in total are listed in Table 2. The three LBP mapping patterns, rotation invariant (RI) pattern, uniform pattern (U2), and rotation invariant and uniform pattern (RIU2), were not involved in our LBP encoding in the first layer. Hence, LBP and its variants in the comparison experiments were also not mapped for fair comparisons. DNCNN is a deep learning framework for an end-to-end visual smoke recognition. Experiments show that DNCNN outperforms some classical networks in our smoke datasets, so we adopted this method for comparisons. We demonstrate comparisons between our method with one layer (denoted as MSD-1L) and with two layers (denoted as MSD-2L). The features of MSD-2L come from 2 layers. In the 1st layer, the dimension is 256 + 256 × 8 = 2304. In the 2nd layer, the dimension is 256 + 36 × 8 = 544. So the feature dimensions of MSD-1L and MSD-2L are 2304 and 2304 + 544 = 2848, respectively.

### 4.1.2. Experimental protocols and results

We adopted MATLAB to implement comparison methods, and LIBSVM [4] was used for classification. The Chi-square kernel was utilized as the kernel function for histogram features, while a linear SVM that was implemented by the VLFeat toolbox was adopted for DMD features [28] in smoke recognition. The reason is that the dimension of DMD features is high enough to represent complicatedly distributed data in a linearly separable way. Hence, the high dimensional features were directly sent to the linear SVM. On the contrary, low dimensional features tend to be linearly inseparable. Therefore, Chi-square kernels were adopted to transform low dimensional features into a kernel space to make them linearly separable. Also, hyper parameters for the classifier were adjusted to get optimized results. The classification protocol is the same as [46], where cost c = 500. In addition, the weights for positive and negative samples, i.e., w_pos and w_neg, have been adjusted to balance the numbers of positive and negative samples. Set1 contains 552 positive samples and 831 negative ones, so w_pos / w_neg = 831/552. The decision threshold t for binary classification is set to 0.

<!-- The sentence "Chi-square kernels were adopted ..." onward was recovered from block S067,
where it had been glued behind the Table 3 data rows; rejoined to the dangling "Therefore," in S066. -->

The dimensions of DMD and DFD features depend on their settings. In DMD, the numbers of Gaussian Mixture Models (GMM) and clustering centers determine the dimension of final features. We adopted the default setting without prepartition, so the dimension of DMD features was 128 × 80 × 2 = 20,480. Similarly, the numbers of clustering centers and pre-partitions in DFD determine the feature dimension. The images were divided into 4 × 4 non-overlapped patches, and the clustering numbers were set to 256, so the dimension of DFD features was 4 × 4 × 256 = 4096. Default settings of 7 × 7 patches with 1024 clustering centers were discarded because this setting brought high dimensionality without excellent results.

Three indicators, detection rate (DR), false alarm rate (FAR) and error rate (ERR), are commonly used to evaluate the performances of smoke recognition. DR is the equivalent of true positive rate (TPR), and FAR is the false positive rate (FPR). We aimed at decreasing FARs and ERRs without dropping DRs.

Learning based methods, DFD, achieves excellent results in face recognition, but not so good ones in smoke recognition. Unlike face images with aligned landmarks, smoke textures are always self-similar in local patches, so smoke images do not contain obviously holistic structure information. Therefore, dividing images into patches does not significantly improve the representation for smoke, but leads to high dimensional features.

As shown in Table 3, MDLBP including information across RGB channels achieves high DRs, but it is not suitable for grayscale images. Thus, MDLBP provides an unfair comparison, since other methods extract features from grayscale images. In addition, features with high-order information can decrease FARs and ERRs, for instance, SOHLBP, HLTP and PRICoLBP. Although HLTP and LBP without mapping achieve higher DRs, their FARs and ERRs are unfortunately higher. By adding the 2nd layer, FARs and ERRs of MSD-2L are all lower than those of MSD-1L. On Set3 and Set4, DRs of MSD-1L outperformed those of MSD-2L at the expenses of adverse higher FARs and ERRs. We will illustrate the difference between the two versions of our method later. Overall, our methods achieved the highest DRs with lower FARs and the lowest ERRs among these compared methods.

Actually, the deep learning based method provides an unfair comparison here. The reasons are two folds: (1) Deep learning based methods require a huge number of training samples to learn intrinsic data structures for smoke. But there are only 1383 samples in the training set, which are too small for training a convolutional network, and (2) deep learning based methods mostly conduct an end-to-end task, in which feature extraction step cannot be separated. While our method aims at feature extraction, our method can be combined with different classifiers to achieve different results. Table 3 indicates that traditional methods outperform deep ones with inadequate training samples.

### 4.1.3. ROC curves and further analysis for comparisons

Since hyper parameters affect classification performances, ROC (Receiver Operating Characteristic) curves are adopted to demonstrate the discriminative ability of our descriptors with the same classifier, i.e., SVM. By varying the decision threshold t of SVM, we modified the decision hyper-plane of SVM to generate many pairs of DRs and FARs for plotting ROC curves of DRs against FARs. The closer the ROC curve is to the upper left corner, the better the descriptor is. Among the ten methods, we involved seven methods that achieved better performance in Table 3 for plotting ROC curves. These compared methods were designed for standard texture classification rather than smoke recognition.

As shown in Table 1, Set2 has only 1505 images, among which the number of non-smoke images is about 1.2 times as that of smoke images. In Fig. 13, SOHLBP [47] has the second best ROC curves, but it achieves neither the highest DR, nor the lowest FAR or ERR in Table 3. This means that there are better classification parameters than those in Table 3 for SOHLBP [47]. Thus it is further proved that ROC curves are necessary to gain overall insights for comparisons. HLTPMC-LPP [46] is the third closest to the upper left corner among the seven compared curves, and it also achieves the lowest FAR on Set2 in Table 3. The reason may be that it involves ternary patterns rather than binary ones. Our MSD-2L achieves the best result here, while both of our MSD-1L and MSD-2L perform best on two larger datasets.

Figs. 14 and 15 illustrate the ROC curves of the seven methods on Set3 and Set4, respectively. It is obvious that the relative rankings of all the methods are similar in the two figures, but they are different from the rankings in Fig. 13. Both versions of our method consistently rank in the top positions on Set3 and Set4. HLTPMC-LPP reaches the second and third rankings on Set3 and Set4, respectively, because it involves high-order information but not feature learning strategy. Besides, all curves on Set3 and Set4 are much smoother than those on Set2. The reason is that both Set3 and Set4 contain far more images than Set2, so the curves show stable results in a more macroscopic perspective.

Although the parameters for SVM are adjusted to get a relatively better classification results for all the methods, the adaptive parameters of DMD descriptor are difficultly fine-tuned because there are too many combinations. In short, default settings are adopted for DMD. This may be one of the reasons why DMD achieves the worst results on the two sets. Another reason is that DMD applies dense sampling using blocks sliding throughout every image and extracts discriminative information from sampled blocks. However, images in our smoke datasets are in small size of 48 × 48, so sliding blocks may not be able to provide enough local samples for the feature selection process in DMD. Similarly, the discriminative ability of PRICoLBP may also be decreased due to small sizes of images.

It is proved on Set2 and Set4 that hierarchical features help improve discriminative ability since MSD-2L outperforms MSD-1L. While on Set3, the two versions don't distinguish much between each other. The reason may be that the within-variances of samples in Set3 are not so big as those in Set2 and Set4. MSD-2L seems to be inferior to MSD-1L in Table 3, while MSD-2L is superior to MSD-1L in Figs. 13–15. The reasons are two folds: (1) the resolution of our samples is 48 × 48, which is too small for the 2nd layer to capture rich textures, and (2) the best classifying hyper-planes of MSD-1L and MSD-2L are not located at the same decision threshold t = 0. Similar contradicts happen to other methods. For instance, HLTPMC_LPP is slightly inferior to our methods in Table 3 and it achieves the lowest FARs on Set2 and Set4, but HLTPMC_LPP is significantly inferior to ours in ROC curves. This proves the above analysis that the best discrimination hyper-planes may correspond to different thresholds t, and thus ROC curves are a good way to take all the hyper-planes into consideration to demonstrate comprehensive results.

In summary, ROC curves generated by our methods are the closest to the upper left corner. Therefore, features extracted by our methods, even without the 2nd layer, have more powerful generalization ability than others. Besides, our method is able to extract discriminative features from grayscale images of small sizes.

### 4.2. Texture classification

#### 4.2.1. Classifiers

<!-- Headings "4.2. Texture classification" and "4.2.1. Classifiers" were glued mid-paragraph in block S081; split here. -->

To further evaluate the performances of our method on texture feature representation and multinomial classification, we tested our feature extraction method on some public texture datasets. As explained before, an SVM with Chi-square kernel was used as the classifier for histogram features, while a linear SVM was adopted for DMD features [28]. The multi-class texture classification was realized by the one-versus-all mechanism.

For DMD features, vl_SVM was adopted as the classifier in paper [28]. In our experiments, DMD features has been proved to achieve relatively better results with LIBSVM in texture classification. Therefore, we adopted LIBSVM [5] for DMD with the same hyper-parameters to all experiments.

#### 4.2.2. Datasets for learning

We learned the projection matrix from a learning dataset that is not involved in classifier training. UMD and FMD were used in our learning step because the samples in these two datasets are concrete objects rather than locally self-similar textures. The sampling window in learning based methods always slides throughout a whole image, so local structure is captured at every sliding position. If locally-similar texture images are used for learning, there will be too much redundant information. We adopted datasets that contain images of identifiable objects for projection matrix learning. In UMD, images in the same class are visually separable but similar to each other. All images were resized to 200 × 200 and used for projection matrix learning. In FMD, samples from the same class vary heavily, and we randomly selected one sample in every class of FMD for learning. The densely sampling windows can generate a huge number of local difference matrices even from several samples.

In learning, the 3 × 3 sampling window was set to slide with a step of 3 so that non-overlap sampling was achieved. In feature extraction, the sliding step was set to 1 for densely capturing texture structure. The projection matrix W was computed from less differences in learning step but applied to more differences during feature extraction, this not only avoids overfitting but also proves the generalization ability of our learning strategy.

#### 4.2.3. Classification protocols

Two versions of Brodatz, KTH-TIPS, KTH-TIPS2-a, and CUReT were adopted for experiments. The two Brodatz datasets in our experiments come from [28] and [31]. The Brodatz from [31] has 999 images of 111 classes, which are in size of 213 × 213 without any transform. This version of Brodatz is denoted as Brod111 in this paper. For classification, we followed the protocol in [31], so we randomly selected 3 images from every class for training and the other 6 for testing.

The Brodatz from [28] contains 32 classes, and each class has 64 grayscale images. Among the 64 images of each class, 16 images are original ones, and the remaining 48 ones are transformed by scaling, rotation, and both scaling and rotation. We denote this version of Brodatz as Brod32 in this paper. Using the protocol in [28], all the images were resized to 200 × 200 pixels, and 32 images were randomly selected for training and the remaining 32 for testing.

<!-- The sentence "denote this version of Brodatz ..." onward was recovered from block S090, where
it had been glued behind the Table 5 rows; rejoined to the dangling "We" in S088. -->

For KTH-TIPS, 40 samples were randomly selected from every class as training samples and the remaining 41 as testing ones. 46 samples were adopted for training and the other 46 for testing in CUReT. In KTH-TIPS2-a, there are four sample sets consisting of images of 11 classes under varying illumination, viewpoints and scales. Three of the sample sets were used for training and the remaining one for testing at each run. Due to the varying and the classification protocol, the accuracy on KTH-TIPS-2a is lower than those on other datasets.

#### 4.2.4. Evaluation protocols

We applied two protocols for fair comparisons. Following the protocol in [31], denoted as PRICoLBP's protocol, every loop of training and testing in classification was repeated for 100 times and the performance was reported in terms of the mean classification accuracy (mAP). The second protocol comes from [28], in which the accuracy was reported on 10-fold cross validation. In addition, the standard deviation of mAP was also adopted as the evaluation metric for these feature descriptors.

#### 4.2.5. Comparisons between learning based methods

The projection matrix W contains 16 projection vectors. In Table 4, the number in parentheses denotes the number of eigenvectors for projection. For example, UMD_(8) means that we use the first eight vectors to project images on UMD. "Original" means that we used the original version of DMD features in [28], in which the learning step was conducted in every loop of classification, and samples for learning come from the same datasets as those for feature extraction.

As more projection vectors are adopted, mAPs are increased except for FMD_(16) on KTH-TIPS. The reason may be that the within-class variance between samples is small in KTH-TIPS but large in FMD. Thus the top 8 projection vectors learnt from only 10 FMD images are discriminative enough to provide a good representation in KTH-TIPS, while the 9th–16th projection vectors bring more redundancy instead of more effectiveness. As for DMD, when samples for learning become less, mAP is decreased heavily.

Our method outperforms DMD on all datasets except for KTH-TIPS2-a. The reason may be that our method treats all the fixed-length difference vectors on an equal basis, and our learning method is based on a single strategy of LDA. So it is very difficult to recognize images with significant changes in viewpoints and rotation. DMD adopts dense samplings using different sampling window sizes and isotropic selections to capture variations at different scales. Hence, DMD features are robust to heavy transforms while our method achieves better resistance to subtle and small transforms. Although quantization is applied during both between-map and within-map encodings in our method, our features are somewhat more discriminative than DMD, in which quantization is not adopted. The dimension of our features is about 10% of that of DMD features. Furthermore, our method is able to learn general projection matrices and features rather than specific ones, even when training data is scarce.

#### 4.2.6. Comparisons with some state-of-the-art methods

To analyze the performance of the proposed feature learning method, we also conducted extensive experiments on the above-mentioned datasets using 6 state-of-the-art texture descriptors, as listed in Table 5. Two versions of classification and evaluation protocols were applied for the sake of fair comparisons.

The experimental results are listed in Tables 6 and 7. We adopted our features of the FMD_(16) and UMD_(16) versions, so our feature dimension is 2816. All the LBP based features were not mapped, so every LBP histogram has a dimension of 256. CLBP-all denotes for CLBP features that involves center pixel values, signs and magnitudes of differences in encoding. We computed signs and magnitudes with two scales for LBPHF. Three levels of pyramids were adopted for PLBP features. Default setting was used for PRICoLBP.

<!-- The paragraph above was recovered from block S102, where it had been glued behind the Table 8 rows. -->

Two learning based methods, our method and DMD, significantly outperform most of the traditional LBP based methods. The accuracy of our method ranks third on Brod111 because the samples in this dataset are all un-transformed, while our method is designed for transform invariance. However, the standard deviation of accuracy by our method ranks second, so it means that our method achieves more stable results than DMD. In Table 6, our methods achieve the best results on three of the four datasets. While in Table 7, our methods obtain the best performances on three of the five datasets. To clearly demonstrate the rankings in our comparison experiments, we counted average rankings for the top three ranked methods, i.e., our method, PRICoLBP and DMD.

Table 8 shows that the average ranking of our method is superior to other methods. DMD and PRICoLBP compute features in local multi-scale coordinates. Our features are computed from fixed local coordinates, and the multi-scale information of our method comes from 3D difference computation. Consequently, we should improve our descriptor by learning a local difference selection strategy, thus we obtain more transform invariance.

<!-- The paragraph above was mislabeled as a caption (C024) by the reader; it is body text. -->

In conclusion, our feature learning method is able to generate a general projection matrix, which is used to compute discriminant features for different classifications even when training and learning data is scarce. The extracted smoke features, recognition and ROC plotting code and texture features of our method can be downloaded via http://staff.ustc.edu.cn/~yfn/index.html.

## 5. Conclusions

To overcome drawbacks of handcrafted features, we propose a method to learn multi-scale, multi-order discriminative features from 3D local differences. In this method, we first densely compute 3D local differences by sliding a 3D sampling window in scale space. 3D local differences capture not only multi-scale information but also the relations across different scales. Second, a projection matrix is learnt from 3D local differences throughout all training images, so both holistic and local information is involved. Then 3D differences are projected using the learnt matrix to obtain feature maps. The projection optimizes the original 3D differences to achieve compact and discriminative features, and reduces the dimensions of 3D differences. In addition, the projection matrix learnt from a training set can be generally applied to other datasets.

Afterwards, between-map and within-map encodings are proposed to encode feature maps to generate multi-order features. At last, weighted concatenation is used to fuse features in each computational layer and Taylor-like coefficients are assigned to features from different computational layers.

Our method can extract multi-order, multi-scale features from images under varying illumination and scales. The sliding 3D sampling window in scale space extracts fine-to-coarse information. The mean-removed local differences not only preserve multi-scale representation but also suppress illumination sensitivity by encoding. Learning of the holistic projection matrix provides a way to intrinsically explore the most stable component of textures in multi-scale views, and it also extracts common attributes within classes and significant differences between classes. In this way, a compact and discriminative feature space is created to generate a scale-invariant representation for smoke. Then, between-map encoding further involves cross-map information along multi-projection orientations, while the within-map encoding presents high-order features. At last, the Taylor-coefficient weighted concatenation is used to extract features in a noise-resistant way. Thus, multi-scale, multi-order, local and global information are captured by our feature extraction method.

As the structure of layers becomes deeper, more hierarchical, abstract and powerful features can be computed. However, a limited number of projection vectors inevitably produces reconstruction errors, which will be passed to deeper layers and be accumulatively magnified, especially in the case of non-linear operations applied to feature maps. Hence, a strategy of backward propagation is needed for error correction. In addition, the 3D sampling windows are in the same size, so we may improve the sampling and learning strategy in the future to involve more potential areas for learning, and may extend the structure to a feedback network to further capture higher level features.

## Acknowledgments

This work was partially supported by National Natural Science Foundation of China (61862029), Cultivated Talent Program for Young Scientists of Jiangxi Province (20142BCB23014), Science Technology Application Project of Jiangxi Province (GJJ170317, KJLD12066), and Key Technology R&D Program of Jiangxi Province (2015ZBBE50013).

## References

<!-- Reference entries appear verbatim in extraction blocks S113-S120 (unlike the reader-condensed
lists in some sibling papers). Reflowed one entry per line; cross-page splits rejoined
([6], [20], [23], [26], [30], [33]); OCR spacing fixes noted in header comment. -->

[1] D.K. Appana, R. Islam, S.A. Khan, J.-M. Kim, A video-based smoke detection using smoke flow pattern and spatial-temporal energy analyses for alarm systems, Inf. Sci. 418–419 (2017) 91–101.

[2] J. Babaud, A.P. Witkin, M. Baudin, R.O. Duda, Uniqueness of the gaussian kernel for scale-space filtering, IEEE Trans. Pattern Anal. Mach. Intell. 8 (1986) 26–33.

[3] J. Cao, B. Wang, D. Brown, Similarity based leaf image retrieval using multiscale R-angle description, Inf. Sci 374 (2016) 51–64.

[4] T. Chan, K. Jia, S. Gao, J. Lu, Z. Zeng, Y. Ma, PCANet: a simple deep learning baseline for image classification, IEEE Trans, Image Process. 24 (2015) 5017–5032.

[5] C.-C. Chang, C.-J. Lin, LIBSVM: a library for support vector machines, ACM Trans, Intell. Syst. Technol. 2 (2011) 1–27.

[6] L. Chengjun, H. Wechsler, Gabor feature based classification using the enhanced fisher linear discriminant model for face recognition, IEEE Trans. Image Process. 11 (2002) 467–476.

[7] S.R. Dubey, S.K. Singh, R.K. Singh, Multichannel decoded local binary patterns for content-based image retrieval, IEEE Trans. Image Process. 25 (2016) 4018–4032.

[8] J.B. Florindo, O.M. Bruno, Discrete Schroedinger transform for texture recognition, Inf. Sci. 415–416 (2017) 142–155.

[9] S. Frizzi, R. Kaabi, M. Bouchouicha, J.M. Ginoux, E. Moreau, F. Fnaiech, Convolutional neural network for video fire and smoke detection, in: Proceedings of the IEEE Conference on Industrial Electronics Society (IECON), 2016, pp. 877–882.

[10] G. Guo, G. Mu, Simultaneous dimensionality reduction and human age estimation via kernel partial least squares regression, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Colorado, Colorado, 2011, pp. 657–664.

[11] Z. Guo, X. Wang, J. Zhou, J. You, Robust texture image representation by scale selective local binary patterns, IEEE Trans. Image Process. 25 (2016) 687–699.

[12] Z. Guo, L. Zhang, D. Zhang, A completed modeling of local binary pattern operator for texture classification, IEEE Trans. Image Process. 19 (2010) 1657–1663.

[13] S. Hegenbart, A. Uhl, A scale- and orientation-adaptive extension of local binary patterns for texture classification, Pattern Recognit. 48 (2015) 2633–2644.

[14] X. Hong, G. Zhao, M. Pietikainen, X. Chen, Combining LBP difference and feature correlation for texture description, IEEE Trans. Image Process. 23 (2014) 2557–2568.

[15] Y. Jia, J. Yuan, J. Wang, J. Fang, Q. Zhang, Y. Zhang, A saliency-based method for early smoke detection in video sequences, Fire Technol. 52 (2016) 1271–1292.

[16] T. Jabid, M.H. Kabir, O. Chae, Local directional pattern (LDP) for face recognition, in: Proceeding of the IEEE International Conference on Consumer Electronics, 2010, pp. 329–330.

[17] I. El Khadiri, M. Kas, Y. El Merabet, Y. Ruichek, R. Touahni, Repulsive-and-attractive local binary gradient contours: new and efficient feature descriptors for texture classification, Inf. Sci. (2018). https://doi.org/10.1016/j.ins.2018.02.009. (in press).

[18] H. Kim, D. Ryu, J. Park, Smoke detection using GMM and Adaboost, Int. J. Comput. and Commun. Eng. 3 (2014) 123–126.

[19] Z. Lei, M. Pietikainen, S.Z. Li, Learning discriminant face descriptor, IEEE Trans. Pattern Anal. Mach. Intell. 36 (2014) 289–302.

[20] F. Li, F. Shao, Q. Jiang, R. Fu, G. Jiang, M. Yu, Local and global sparse representation for no-reference quality assessment of stereoscopic images, Inf. Sci. 422 (2018) 110–121.

[21] D.G. Lowe, Distinctive image features from scale-invariant keypoints, Int. J. Comput. Vision 60 (2004) 91–110.

[22] L. Liu, L. Wang, L. Zhao, P. Fieguth, Random projections and single BoW for fast and robust texture segmentation, Inf. Sci. 370–371 (2016) 428–445.

[23] J. Lu, V.E. Liong, J. Zhou, Simultaneous local binary feature learning and encoding for homogeneous and heterogeneous face recognition, IEEE Trans. Pattern Anal. Mach. Intell. 40 (2018) 1979–1993.

[24] J. Lu, V.E. Liong, J. Zhou, Cost-sensitive local binary feature learning for facial age estimation, IEEE Trans. Image Process. 24 (2015) 5356–5368.

[25] J. Lu, V.E. Liong, X. Zhou, J. Zhou, Learning compact binary face descriptor for face recognition, IEEE Trans. Pattern Anal. Mach. Intell. 37 (2015) 2041–2056.

[26] J. Lu, Y. Tan, G. Wang, Discriminative multimanifold analysis for face recognition from a single training sample per person, IEEE Trans. Pattern Anal. Mach. Intell. 35 (2013) 39–51.

[27] R. Manthalkar, P.K. Biswas, B.N. Chatterji, Rotation invariant texture classification using even symmentric Gabor filters, Pattern Recognit. Lett. 24 (2003) 2061–2068.

[28] R. Mehta, K. Egiazarian, Texture classification using dense micro-block difference, IEEE Trans. Image Process. 25 (2016) 1604–1616.

[29] B.-S. Oh, K. Oh, A.B.J. Teoh, Z. Lin, K.-A. Toh, A gabor-based network for heterogeneous face recognition, Neurocomputing 261 (2017) 253–265.

[30] T. Ojala, M. Pietikainen, T. Maenpaa, Multiresolution gray-scale and rotation invariant texture classification with local binary patterns, IEEE Trans. Pattern Anal. Mach. Intell. 24 (2002) 971–987.

[31] X. Qi, R. Xiao, C.-G. Li, Y. Qiao, J. Guo, X. Tang, Pairwise rotation invariant co-occurrence local binary pattern, IEEE Trans. Pattern Anal. Mach. Intell. 36 (2014) 2199–2213.

[32] X. Qian, X. Hua, P. Chen, L. Ke, PLBP: an effective local binary patterns texture descriptor with pyramid representation, Pattern Recognit. 44 (2011) 2502–2515.

[33] D. Sánchez, P. Melin, O. Castillo, Optimization of modular granular neural networks using a firefly algorithm for human recognition, Eng. Appl. Artif. Intell. 64 (2017) 172–186.

[34] C. Shi, C. Wang, Y. Wang, B. Xiao, Deep convolutional activations-based features for ground-based cloud classification, IEEE Geosci. Remote Lett. 14 (2017) 816–820, doi: 10.1109/LGRS.2017.2681658.

[35] Y. Song, S. Zhang, B. He, Q. Sha, Y. Shen, T. Yan, R. Nian, A. Lendasse, Gaussian derivative models and ensemble extreme learning machine for texture image classification, Neurocomputing 277 (2018) 53–64.

[36] Y. Sun, X. Wang, X. Tang, Deep learning face representation from predicting 10,000 classes, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2014, pp. 1891–1898.

[37] X. Tan, B. Triggs, Enhanced local texture feature sets for face recognition under difficult lighting conditions, IEEE Trans. Image Process. 19 (2010) 1635–1650.

[38] H. Tian, W. Li, P.O. Ogunbona, L. Wang, Detection and separation of smoke from single image frames, IEEE Trans. Image Process. 27 (2018) 1164–1177.

[39] D.M. Vo, S.-W. Lee, Robust face recognition via hierarchical collaborative representation, Inf. Sci. 432 (2018) 332–346.

[40] F.J. Xu, V.N. Boddeti, M. Savvides, Local binary convolutional neural networks, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 4284–4293.

[41] T. Wang, J. Yang, Q. Sun, Z. Ji, P. Fu, Q. Ge, Global graph diffusion for interactive object extraction, Inf. Sci. 460–461 (2018) 103–114.

[42] G. Xu, Y. Zhang, Q. Zhang, G. Lin, J. Wang, Deep domain adaptation based video smoke detection using synthetic smoke images, Fire Saf. J. 93 (2017) 53–59.

[43] Z. Yin, B. Wan, F. Yuan, X. Xia, J. Shi, A deep normalization and convolutional neural network for image smoke detection, IEEE Access 5 (2017) 18429–18438.

[44] C. Yu, J. Fang, J. Wang, Y. Zhang, Video fire smoke detection using motion and color features, Fire Technol. 46 (2010) 651–663.

[45] F. Yuan, A double mapping framework for extraction of shape-invariant features based on multi-scale partitions with AdaBoost for video smoke detection, Pattern Recognit. 45 (2012) 4326–4336.

[46] F. Yuan, J. Shi, X. Xia, Y. Fang, Z. Fang, T. Mei, High-order local ternary patterns with locality preserving projection for smoke detection and image classification, Inf. Sci. 372 (2016) 225–240.

[47] F. Yuan, J. Shi, X. Xia, Y. Yang, Y. Fang, R. Wang, Sub oriented histograms of local binary patterns for smoke detection and texture classification, KSII Trans. Internet Inf. Syst. 10 (2016) 1807–1823.

[48] F. Yuan, X. Xia, J. Shi, Mixed co-occurrence of local binary patterns and hamming-distance-based local binary patterns, Inf. Sci. 460–461 (2018) 202–222.

[49] G. Zhao, T. Ahonen, J. Matas, M. Pietikainen, Rotation-invariant image and video description with local binary pattern features, IEEE Trans. Image Process. 21 (2012) 1465–1477.

[50] Y. Zhao, Z. Zhou, M. Xu, Forest fire smoke video detection using spatiotemporal and dynamic texture features, J. Electr. Comput. Eng. 2015 (2015) 1–7.

## Appendix: Author biographies (from pp. 19-20; verbatim)

Feiniu Yuan received B.Eng. and M.E. degrees in mechanical engineering from the Hefei University of Technology, Hefei, China, in 1998 and 2001, respectively, and a Ph.D. degree in pattern recognition and intelligence system from the University of Science and Technology of China (USTC), Hefei, in 2004. From 2004 to 2006, he worked as a post-doctorate with USTC. From 2010 to 2012, he was a Senior Research Fellow with Singapore Bioimaging Consortium, Agency for Science, Technology and Research, Singapore. He is currently a full professor and a PhD supervisor at Jiangxi University of Finance and Economics. His research interests include 3D modeling, image processing and pattern recognition.

Xue Xia received a B.E. degree in Film & TV Arts and Technology and an M.E. degree in Communication and Information Engineering from Shanghai University, Shanghai, in 2011 and 2014, respectively. She is currently a Ph.D. candidate with the School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, China. Her research interests include image processing and pattern recognition.

Jinting Shi received a B.E. degree in computer science and technology from the Jiangxi Normal University, Nanchang, China, in 2003, and an M.S. degree in computer science and technology from Jiangxi Agricultural University, Nanchang, China, in 2008. She is currently a Ph.D. candidate with the School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, China. Her research interests include image processing and pattern recognition.

Lin Zhang received her B.E. degree in computer science and technology from East China Jiaotong University, Nanchang, China, in 2004, and her M.E. degree in computer application technology from Jiangxi University of Finance and Economics, Nanchang, China, in 2007. She is currently pursuing her Ph.D. degree with the School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, China. Her research interests include image processing and pattern recognition.

Jifeng Huang received the B.S. degree in radio engineer from Zhengzhou University, Zhengzhou, Henan, China, in 1984, the M.S. degree in communication and electronic system from Xi'an Jiaotong University, Xi'an, Shaanxi, China, in 1989, and the Ph.D. degree in measurement and control technology and automation instrument from the East China University of Science and Technology, Shanghai, China, in 2006. From 1989 to 1999, he was a Teacher with the Zhengzhou University of Aeronautics, Zhengzhou. Since 1999, he has been a Professor with the College of Information, Mechanical and Electrical Engineer, Shanghai Normal University. His research interests include pattern recognition, machine learning, and automation instrument. Dr. Huang received the award for scientific and technological advancement from the Aviation Ministry of China.

## Appendix: Figure and table captions (segregated from body; numeric table content excluded,
see PDF for data rows; original caption typos "Datesets"/"Comparision" preserved)

Fig. 1. Examples of 3D sampling windows in image pyramid and scale space with r = 1 and K = 3.

Fig. 2. Calculation of 3D local differences.

Fig. 3. The calculation of the c th within-scatter matrix S_w^c.

Fig. 4. The calculation of between-scatter matrix S_b.

Fig. 5. The generation of 8 feature maps in the ith image.

Fig. 6. Feature extraction procedure of a layer. (a) Calculation of 3D differences. (b) Learning and projection. (c) Within-map and between-map encodings.

Fig. 7. Between-map encoding.

Fig. 8. Feature extraction of our method for texture classification. (A) Scale space construction and local difference calculation. (B) Projection matrix learning. (C) Projection, between-map and within-map encodings and weighted concatenation.

Fig. 9. The original framework of our method for learning, feature extraction and classification.

Fig. 10. An extension of our feature extraction method.

Fig. 11. Visualization of our learning-based projection and encoding results. (a) An input image. (b) and (c) Gaussian filtered images with different variances. (d) The cross-sign map LBP_0 from (f) in the between-map encoding way. (e) The cross-magnitude map LBP_mag obtained from (f) by between-map encoding. (f) The eight feature maps generated from (a), (b) and (c). (g) The original LBP maps, LBP_1, ..., LBP_8, computed from (f) by within-map encoding.

Fig. 12. Cross-sign and cross-magnitude maps obtained from sixteen feature maps. (a) The cross-sign map and (b) the cross-magnitude map generated from the top 8 feature maps. (c) The cross-sign map and (d) the cross-magnitude map computed by the 9th to 16th feature maps.

Fig. 13. The ROC curves of compared methods on Set2.

Fig. 14. The ROC curves of compared methods on Set3.

Fig. 15. The ROC curves of compared methods on Set4.

Table 1. Datesets for smoke recognition.

Table 2. Compared methods for smoke recognition.

Table 3. Experimental results for smoke recognition.

Table 4. Comparision results (%) of two learning-based methods.

Table 5. Compared methods on texture classification.

Table 6. Comparision results (%) using PRICoLBP's protocol.

Table 7. Comparision results (%) using DMD's protocol.

Table 8. Performance rankings for Table 7.
