# High-order local ternary patterns with locality preserving projection for smoke detection and image classification

**Paper_ID:** 19_HighOrder_LTP_IS2016_Smoke_Detection
**Authors:** Feiniu Yuan, Jinting Shi, Xue Xia, Yuming Fang, Zhijun Fang, Tao Mei
**Venue:** Information Sciences 372 (2016) 225–240
**DOI:** 10.1016/j.ins.2016.08.040

## Abstract

It is a challenging task to recognize smoke from visual scenes due to large variations in the color, texture, shapes of smoke. To improve detection accuracy, we propose a novel feature extraction method by encoding high order directional derivatives at each pixel. We first quantize the directional derivatives into ternary values to generate Local Ternary Patterns (LTP). For the sake of simplification, each LTP code is usually decomposed into an upper LBP code and a lower LBP code, but this leads to loss of information. Hence, we use joint histograms to preserve the co-occurrence of upper and lower LBP codes for each order LTP. Then we concatenate all joint histograms from different orders to propose High-order Local Ternary Patterns (HLTP). To improve computational efficiency, we apply Locality Preserving Projection (LPP) to reduce the dimension of HLTP. To further improve performance, we present a noise resistant mechanism to remove noisy derivatives, and then propose HLTP based on Magnitudes of noise removed derivatives and values of Center pixels (HLTPMC). Finally, the Support Vector Machine (SVM) is used for training and classification. Experiments on large scale smoke data sets show that our method can achieve detection rates above 94% with false alarm rates below 1.33%. Experiments on a multi-class Brodatz texture data set also achieved good performance with low dimensional features. So our method has powerful discriminative capabilities and compact feature representation for multi-class image classification.

**Keywords:** Local ternary patterns; High order derivatives; Locality preserving projection; Smoke detection; Image classification.

## Introduction

### 1. Introduction

Traditional fire detection methods typically use point based sensors that are implemented by smoke particle sampling, atmosphere temperature sampling, relative humidity sampling, or other analyses [49]. Traditional fire sensors are widely applied because they are simple, cheap and accurate. However, traditional fire sensors have various shortcomings that are difficult to solve. Exposure of traditional fire sensors to combustion products is required because these sensors need to analyze particles, temperature or humidity. Hence, traditional fire sensors must be installed in close proximity to fires. This limits conventional fire detection technologies to applications only in small or indoor spaces. In addition, it may take a long time to transfer combustion products, such as smoke particles, to fire sensors, resulting in slow response.

To overcome the above mentioned limitations of traditional fire detection methods, fire detection from visual scenes has been widely investigated. Smoke often appears earlier than flames, so smoke detection provides earlier fire alarms than flame detection. Earlier fire alarms play an important role in fire extinguishment and personnel evacuation. A variety of algorithms have been proposed for smoke detection in recent years. Toreyin et al. [40] proposed smoke detection by fusing features of motion, flicker, edge blurring and color. Gubbi et al. [8] computed the arithmetic mean, geometric mean, standard deviation, skewness, kurtosis, and entropy over each sub-band of three level wavelet transformed images and then used Support Vector Machine (SVM) to detect smoke from videos. Gottuk et al. [7] evaluated the effectiveness of commercial video fire detection systems for small and cluttered spaces on navy ships and concluded that video fire detection systems can detect fires more accurately and efficiently than traditional systems in specific spaces. In our previous work, we proposed a fast accumulative motion orientation model based on integral image [48], histograms of Local Binary Pattern (LBP) and Local Binary Pattern Variance (LBPV) based on pyramids [50], and shape-invariant features on multi-scale partitions with AdaBoost [47] for smoke detection.

Texture plays an important role in image classification. Many texture feature extraction methods have been proposed, such as LBP [33], co-occurrence matrices [36], Gabor filter and wavelet transform methods [21], and so on. LBP is a simple but efficient texture operator. LBP encodes values of neighboring pixels around a center pixel into binary patterns. LBP has many advantages, such as powerful discriminative capability, low computational complexity and low sensitivity to illumination variation. To suppress noise, Local Ternary Pattern (LTP) quantizes the differences of the center pixel and its neighbors into a ternary value instead of a binary one [39]. Several LBP variants have been successfully applied in some applications, such as face recognition [41], image annotation [27], and image retrieval [28].

However, existing feature extraction methods cannot achieve satisfying performance in smoke detection. The main reason is that smoke has large variations in color, texture and shape. In addition, smoke blurs visual scenes, leading to unstable features. Therefore, it is still a challenging task to accurately detect smoke from images. To improve detection accuracy, we need to study specialized feature extraction methods for smoke detection.

Features by different methods have respective advantages, so it is natural for us to combine different features together to enhance robustness. For example, Yu et al. [46] proposed a multi-view stochastic learning (HD-MSL) method for image classification, which effectively combines varied features from multiple views and integrates the labeling information with each other.

Motivated by the success of feature combination, we also fuse LTP, signs and magnitudes of high order derivatives, and manifold methods together to propose robust and compact features for smoke detection and image classification. Our experiments validate that feature combination truly improves performance, but it is difficult for us to theoretically prove it. LTP uses a pre-specified threshold to quantize 1st order directional derivatives into ternary values, but it discards information on high-order derivatives. To include more information, we first propose high order LTP by encoding high order directional derivatives at the center pixel. Then, we use joint histograms of upper and lower LBP codes to capture the co-occurrence of the two codes and concatenate all joint histograms of LTPs with different orders. Furthermore, we use a manifold dimensionality reduction method, Locality Preserving Projection (LPP), to reduce the dimension of the concatenated histogram. Our method can improve both computational efficiency and classification accuracy. We call the proposed method High order Local Ternary Patterns (HLTP). To further improve performance, noisy derivatives are removed by thresholding. Finally, we encode the noise removed magnitudes of derivatives and the values of the center pixel together to propose High order Local Ternary Patterns based on Magnitudes of derivatives and values of Center pixels (HLTPMC).

Our contributions can be summarized as follows. Firstly, we present High order Local Ternary Patterns (HLTP) by quantizing high order directional derivatives into ternary values. Secondly, we concatenate joint histograms of upper and lower LBP codes and use locality preserving projection to reduce the dimension of the concatenated histogram to propose efficient and compact features. Lastly, we use a thresholding method to suppress noisy derivatives and then present high order local ternary patterns based on magnitudes of noise removed derivatives and values of center pixels (HLTPMC).

This paper is organized as follows. Section II briefly describes related work on variants of LBP. Section III presents local binary patterns, directional derivatives, local ternary patterns, LPP and HLTP. Section IV gives experimental results from comparisons. Conclusions are drawn in Section V.

## RelatedWork

### 2. Related work

There are a lot of LBP variants proposed by modifying neighborhoods or quantization methods. Zhou et al. [55] analyzed structures and occurrence probabilities to propose a new LBP operator for classification and combination of "non-uniform" local patterns. Guo et al. [9] encoded signs and magnitudes of 1st order derivatives, and values of center pixels to propose the Completed model of Local Binary Patterns (CLBP) for texture classification. Ren et al. [37] presented Noise Resistant Local Binary Patterns by correcting uncertain bits that are polluted by noise. Guo et al. [10] proposed Local Binary Pattern Variance (LBPV), which can be regarded as the integral projection along the variance axis. Liao et al. [20] regarded the top 80% frequent patterns as dominant features to present dominant local binary patterns for texture classification. Jun et al. [18] proposed Compact Local Binary Patterns by maximizing mutual information between features and labels. Vu and Caplier [41] proposed Patterns of Oriented Edge Magnitudes (POEM) for face recognition. POEM uses Whitened PCA to obtain a compact, robust, and discriminative descriptor. Murala et al. [30] devised local tetra patterns (LTrP) for content based image retrieval. LTrP encodes the relationship between the referenced pixel and its neighbors in vertical and horizontal directions.

Some LBP variants adopt multi-resolution analysis to obtain scale invariance. Qian et al. [35] extended local binary patterns to image pyramids to propose Pyramid Local Binary Pattern (PLBP). Jia et al. [17] proposed multi-scale local binary patterns with filters for fingerprint detection. Zou et al. [57] applied Multi-Scale Completed Local Binary Patterns (MS-CLBP) over an original image and its Gabor feature images to extract global features, and then fused local and global spatial features for scene classification. Hadizadeh [13] used a bank of Gabor wavelets as local filters at different scales and orientations to compute the outputs of the local filters, and then compared the outputs at different orientations with the global mean of filters to propose Local Gabor Wavelets Binary Pattern (LGWBP). A major limitation of LBP is its sensitivity to affine transformations. Hegenbart and Uhl [15] presented scale and rotation invariant computation of LBP using alignment and scale space. Guo et al. [12] extended Dominant LBP to scale space for texture classification.

Other LBP variants encode information on high order derivatives. Zhang et al. [52] proposed Local Derivative Pattern (LDP) for face recognition by defining the kth order derivatives as the spatial variations of the (k−1)th LDP computed in some pre-specified directions. The number of directions determines the number of codes for each pixel. Guo et al. [11] encoded directional derivatives to propose Local Directional Derivative Pattern (LDDP). Li et al. [19] divided uniform patterns of original LBP into sub-uniform patterns, and then circularly aligned the histogram of sub-uniform patterns to the dominant bin with the maximum value in scale space. Yuan [49] used scale space to propose high order Derivative Local Binary Patterns based on Circular shift sub-uniform and Scale space (DLBPCS). Fan and Hung [4] proposed Local Vector Pattern (LVP) in high order derivative space for face recognition. To extract more information, LVP is greatly improved by varying local derivative directions for the kth order LVP computed in (k−1)th order derivative space. Zhang et al. [53] proposed high order local ternary patterns by encoding directional variations of local derivatives into a 3-valued code. Although the method is called high order local ternary patterns, the high order directional variations of local derivatives are not the true high order derivatives of pixel values. Hence, the method is completely different from our high order local ternary patterns.

## Methods

### 3. Approach

In this paper, we propose a novel feature extraction method that is obviously different from existing methods. The main differences between our HLTP and LTP [39] are that our method encodes high order derivatives, uses joint histograms to capture the co-occurrence of upper and lower LBP codes, and applies LPP to reduce the dimension of joint histograms. Another difference is that we encode magnitudes of noise-removed derivatives and concatenate histograms together to preserve information from different orders. By fully modeling high order directional derivatives and center pixel values, we present high order local ternary patterns based on magnitudes of derivatives and center pixel values (HLTPMC). In HLTPMC, we quantize the signs of high order derivatives into 3-value codes, and use a noise resistant method to encode the magnitudes of noise removed derivatives, so our HLTPMC is also obviously different from CLBP [9].

> Fig. 1. Circular neighborhood for LBP codes with 2nd order derivatives.

#### 3.1. Local binary patterns

An LBP code [33] is determined by comparing the value of a center pixel with the values of its neighboring pixels. The LBP code for the center pixel is computed as

LBP_{P,R} = Σ_{i=0}^{P−1} s2(g_i − g_c) · 2^i  (1)

where g_c is the gray scale value of the center pixel, g_i the value of its ith neighbor, P the number of neighbors, R the radius of the circular neighborhood, and s2(x) an indicator function defined as follows:

s2(x) = 1 if x ≥ 0; 0 otherwise  (2)

LBP defines three mapping modes, which are uniform (U2), rotation invariant (RI) and rotation invariant uniform (RIU2) patterns. The uniform value U of an LBP code is defined as the number of circularly spatial transitions of 0/1 bits. Uniform patterns LBP^{U2}_{P,R} are defined as patterns whose uniform values are no more than 2, i.e., U ≤ 2. Given the number of neighbors P, uniform patterns have P × (P − 1) + 3 different output values [10]. The rotation invariant pattern LBP^{RI}_{P,R} of an LBP code is defined as the minimum value among all circularly bitwise right shifted values of LBP_{P,R}. The combination of rotation invariant and uniform patterns produces rotation invariant uniform patterns LBP^{RIU2}_{P,R}. If P and R are respectively set to 8 and 1, the dimensions of the three histograms for LBP^{U2}_{P,R}, LBP^{RI}_{P,R}, and LBP^{RIU2}_{P,R} are 59, 36 and 10, respectively.

#### 3.2. Local ternary patterns with high order derivatives

High order directional derivatives can also be encoded in the same way as LBP [49]. The pixel value along a discrete direction i can be expressed as a one dimensional signal f_i(u). As shown in Fig. 1, circular red dots denote resampled points along the ith direction, while green ones represent resampled points of other directions. According to the Taylor signal expansion theory, the resampled signal f_i(u) along direction i, where u stands for the local coordinate of re-samplings, can be expanded at 0 as follows:

f_i(u) = f_i(0) + f_i^{(1)}(0) · u + (1/2!) · f_i^{(2)}(0) · u² + ···  (3)

where f_i^{(k)}(0) stands for the kth order derivative evaluated at 0 for direction i. Obviously, f_i(0) = g_c and f_i(R) = g_i. The original LBP encodes the 1st order derivatives f_i^{(1)}(0) to achieve illumination invariance. Both the DC component f_i(0) and high order derivatives f_i^{(k)}(0) with k > 1 are discarded. Discarding high order derivatives simplifies computation, but it leads to loss of high order information and thus reduces classification accuracy.

The kth order directional derivatives f_i^{(k)}(0) (i = 0, …, P−1) can also be encoded in the same way as the 1st derivatives. The kth order LBP code can be similarly computed as follows:

LBP^k_{P,R} = Σ_{i=0}^{P−1} s2(f_i^{(k)}(0)) · 2^i  (4)

LBP^1_{P,R} by encoding the 1st derivatives is just the original LBP defined in Eq. (1). If we want to encode K orders of derivatives, we will obtain K different codes for each pixel, i.e., LBP^1_{P,R}, LBP^2_{P,R}, …, LBP^K_{P,R}. Similarly, the k-th order code LBP^k_{P,R} can be also mapped to U2, RI and RIU2 patterns, which are denoted as LBP^{k,U2}_{P,R}, LBP^{k,RI}_{P,R} and LBP^{k,RIU2}_{P,R}, respectively.

Tan and Triggs [39] proposed Local Ternary Patterns (LTP) by extending 2-value instances of LBP to 3-value codes. A neighboring pixel value g_i within the range (g_c − t, g_c + t) around the value of a center pixel g_c is quantized to zero, while the value above the range is quantized to +1 and the one below the range is quantized to −1. The indicator function s2(x) for 2 values is replaced by a 3-value function s3(g_i, g_c, t):

s3(g_i, g_c, t) = +1 if g_i − g_c ≥ t; 0 if |g_i − g_c| < t; −1 if g_i − g_c ≤ −t  (5)

where g_c is the gray scale value of the center pixel, g_i is the value of its ith neighbor, and t is a threshold for quantization.

LTP suppresses noise and provides more information. However, thresholding would lead to side effects. For example, LTP is no longer strictly invariant to illumination. Moreover, LTP produces 3^P different patterns, which are far more than 2^P by LBP.

> Fig. 2. Local ternary patterns by encoding 1st and 2nd order directional derivatives. (a) Image pixel values; (b) LTP 3-value codes of 1st and 2nd order directional derivatives; (c) Upper LBP codes; (d) Lower LBP codes.

To reduce the number of LTP patterns, an LTP 3-value pattern is usually decomposed into an upper LBP code and a lower LBP code [39] by the following two indicator functions:

s_U(g_i, g_c, t) = 1 if g_i − g_c ≥ t; 0 otherwise  (6)

s_L(g_i, g_c, t) = 1 if g_i − g_c ≤ −t; 0 otherwise  (7)

Combining Eqs. (6) and (7) with Eq. (1), we can obtain two patterns, i.e., an upper LBP code and a lower LBP code. Circular neighborhoods require the interpolation of pixel values. To improve computational efficiency, we instead use rectangular neighborhoods in our implementation. Fig. 2a shows pixel values of a gray scale image. We encode the 1st order directional derivatives D1 = {−11, −3, −2, +2, +4, +9, +6, −6} at a center pixel drawn in a red dot with a threshold t1 = 5 and generate a 3-value code LTP1 = (−1)000011(−1). Then, we decompose the 3-value code into an upper 2-value code LBP_{U,1} = 00000110 and a lower 2-value code LBP_{L,1} = 10000001, as shown in the top row of Fig. 2b, c, and d. The two codes can also be mapped to uniform, rotation invariant, and rotation invariant uniform patterns.

In fact, g_i − g_c is just the 1st order directional derivatives for direction i at the center pixel. Similarly, we encode the kth order derivatives (k > 1) to propose the kth order LTP. As shown in Fig. 2, we encoded the 2nd order directional derivatives D2 = {+6, −1, −1, −2, −2, −6, −4, +6} at the center pixel (Fig. 2a) with another threshold t2 = 4, and obtained a 3-value code LTP2 = 10000(−1)01. Then, we decomposed the ternary code into an upper code LBP_{U,2} = 10000001 and a lower code LBP_{L,2} = 00000100, as shown in the bottom row of Fig. 2b, c, and d. The two codes for the 2nd order LTP2 can also be mapped to uniform, rotation-invariant, and rotation-invariant uniform patterns. For upper and lower codes of LTP, we can separately compute histograms of the two codes and then concatenate the two histograms together to generate a feature vector. Obviously, the dimension of the feature vector is 2 times as long as the dimension of each histogram. Because the concatenated histogram does not include spatial information, it is invariant to rotation and translation, but this leads to loss of information on spatial structures.

#### 3.3. Joint histograms of upper and lower codes

To overcome the above-mentioned drawback, joint histograms are used to capture the co-occurrence of the two codes. Each entry in a joint histogram is the co-occurring number of an upper code and a lower code. Joint histograms are more discriminative than concatenated histograms. Experiments also validate that joint histograms have better performance than concatenated histograms. Given an upper code LBP_{U,k} and a lower code LBP_{L,k} for the kth order LTP, we mathematically define the joint histogram of the kth order LTP as follows:

h_k(i, j) = Σ δ(LBP_{U,k} − i) · δ(LBP_{L,k} − j)  (8)

where δ(v) is the delta function returning 1 if v = 0 and 0 for v ≠ 0, and h_k(i, j) is the ith row and jth column entry of the 2D joint histogram. The top row of Fig. 3 illustrates upper LBP codes, lower LBP codes and corresponding joint histograms. To clearly illustrate the numeric values of upper and lower LBP codes, we resized the original images in Fig. 3a and h to the size of 20 × 20 before extracting HLTP. Fig. 3b and c show upper and lower LBP codes of the 1st order LTP for the resized smoke image, respectively. Fig. 3d gives the joint histogram of the 1st order LTP. Fig. 3e, f and g are upper LBP codes, lower LBP codes and the joint histogram of the 2nd order LTP, respectively. The bottom row of Fig. 3 shows HLTP patterns and joint histograms of a non-smoke image. Fig. 3i, j, and k illustrate upper LBP codes, lower LBP codes and the joint histogram of the 1st order LTP for the non-smoke image (Fig. 3h), respectively. Accordingly, Fig. 3l, m and n show upper LBP codes, lower LBP codes and the joint histogram of the 2nd order LTP.

> Fig. 3. HLTP patterns and joint histograms for smoke and non-smoke images.

If K orders of derivatives are used, there will be K joint histograms h_k (k = 1, …, K). We concatenate the K joint histograms together to form a large histogram H_s = {h_1, …, h_K}. Due to the high dimension of each joint histogram, the dimension of the concatenated joint histogram H_s is also high. There are a variety of algorithms proposed for dimensionality reduction. Xu et al. [43] explored a dimensionality reduction problem in a new weakly supervised setting and then proposed a novel framework that integrates two aspects of the large margin principle. The Multi-view Intact Space Learning (MISL) algorithm [42] integrates the encoded complementary information in multiple views to discover a latent intact representation of data. The theory of information bottleneck (IB) was extended to learned examples represented by multi-view features [44]. Geodesic based manifold learning algorithms, such as Isomap and GeoNLM, fail to model data that is sampled from several clusters or manifolds. Fan et al. [5] proposed an isometric Multi-manifold Proximity Embedding (MPE) to preserve both the geodesic distances of intra and inter manifolds. Yu et al. [45] adopted a hypergraph to build a group of manifolds. A hyper edge in a hypergraph to connect a set of vertices was used to preserve the local smoothness of the constructed sparse codes. Deng et al. [3] proposed Discriminated Locality Preserving Projection (DLPP) to reduce the data dimension in a nonlinear manifold. Ji et al. [16] proposed a Semi-Supervised LPP algorithm (SSLPP) by incorporating relevance information into LPP. To preserve more information, a Pearson Correlation Coefficient (PCC) based SSLPP algorithm (PCC-SSLPP) was further developed. To improve discriminative ability and decrease computational complexity, we use Locality Preserving Projection (LPP) [14] to reduce the dimension of joint histograms.

#### 3.4. Dimensionality reduction of joint histograms

Given a set of feature points x_1, x_2, …, x_Q in R^D, LPP finds a transformation matrix A that maps the Q points onto a set of points y_1, y_2, …, y_Q in R^d (d << D), i.e., y_i = A^T x_i. In fact, LPP is a linear approximation of the nonlinear Laplacian Eigenmap, summarized as follows: (1) Constructing the adjacency graph G with Q nodes. We put a weighted edge between nodes i and j if x_i and x_j are "close" enough. The definition of "close" can be specified by ε-neighborhoods or k-nearest neighbors. (2) Choosing a weight model to compute the weight matrix W. The weight coefficients can be defined as the heat kernel or the simple minded model. (3) Solving eigenmaps to obtain the projection matrix A. Suppose a is a transformation vector of a linear Laplacian eigenmap that is a column vector of A; we can compute the eigenvectors and eigenvalues for the generalized eigenvector problem as follows:

X L X^T a = λ X D X^T a  (9)

where X = {x_1, x_2, …, x_Q}, T stands for the transpose of a matrix, D is a diagonal matrix whose entries are column sums of W, i.e., D_ii = Σ_j W_ji, and L = D − W is the Laplacian matrix.

Column vectors a_0, a_1, …, a_{d−1} of A are just the bottom d eigenvectors of the generalized eigenvector problem whose eigenvalues are sorted in ascending order, i.e., λ0 < λ1 < … < λd−1.

Fig. 4 gives the processing flow chart for HLTP, joint histograms and LPP projection. To include more information, original images may be divided into overlapped or non-overlapped blocks, and then HLTP features are extracted from these blocks. Fig. 4a shows an original image and a pooling scheme specified by a set of blocks. Fig. 4b illustrates upper LBP codes and lower LBP codes of the k-th order LTP for a block in a red rectangle. The 2D joint histograms of the two codes are calculated and shown in Fig. 4c. Then, we stack the 2D joint histogram into a 1D vector, and concatenate all of the vectors from different blocks and orders of derivatives to form a high dimensional feature vector (Fig. 4d). Finally, we apply LPP to project the high dimensional feature vector to obtain a low dimensional feature vector (Fig. 4e).

> Fig. 4. HLTP, joint histograms and dimensionality reduction. (a) An original image and pooling blocks; (b) Upper LBP codes and lower LBP codes; (c) 2D joint histograms of upper and lower LBP codes; (d) Stack joint histograms into a 1D vector; (e) The 1D feature vector transformed by LPP.

#### 3.5. HLTP based on magnitudes of derivatives and center pixel values

Completed Local Binary Patterns (CLBP) [9] demonstrates good performance due to the completed modeling of signs of derivatives, magnitudes of derivatives, and values of center pixels. Inspired by CLBP, we also take magnitudes of derivatives and center pixel values into account for HLTP. Images inevitably contain noise. High order derivatives of images are more sensitive to noise. Therefore, it is necessary to remove or suppress noise before encoding. Liu et al. [23] extensively investigated noise issues by studying a classification problem of randomly corrupted sample labels. Manhattan nonnegative matrix factorization (MahNMF) models the heavy tailed Laplacian noise by minimizing the Manhattan distance between a nonnegative matrix and the product of two nonnegative low rank factor matrices. Liu et al. [24] studied the statistical performance of MahNMF in the frame of the statistical learning theory. Cauchy regression (CR) has the capability to learn a robust model from noisy big data [25]. The above mentioned methods can achieve very good results, but they are time consuming. To reduce computation time, the threshold for local ternary binary is used again to eliminate noisy magnitudes of derivatives:

d_{1,i} = |g_i − g_c| if |g_i − g_c| ≥ t; 0 if |g_i − g_c| < t  (10)

where g_c is the gray scale value of the center pixel, g_i is the value of its i-th neighbor, and d_{1,i} is the magnitude of the 1st order derivatives with noise removed by the threshold t for LTP.

We adopt the same method described in Eq. (10) to process high order derivatives for noise removal. Then, we compute the average magnitude m_k from all noise removed magnitudes of kth order derivatives d_{k,i} over an image. We encode the kth order magnitudes d_{k,i} of P directions around the center pixel in a similar way to CLBP [9]:

LTPM_{P,R} = Σ_{i=0}^{P−1} s_m(d_{k,i}, m_k) · 2^i  (11)

s_m(d, m) = 1 if d ≥ m; 0 otherwise  (12)

We compute the average pixel value c for the entire image and then use the same method proposed in [9] by simply comparing each pixel value with the average value c to obtain a 1-bit local pattern as follows:

LTPC_{P,R} = s_m(g_c, c)  (13)

> Fig. 5. The processing flow chart of HLTPMC.

Now, each pixel has three types of local patterns, which are high order local ternary patterns (HLTP), local magnitude patterns (LTPM), and local center patterns (LTPC). Finally, we calculate and concatenate histograms of HLTP, LTPM and LTPC to construct a combined feature vector. We call the method High order Local Ternary Patterns based on Magnitudes of derivatives and Center pixel values (HLTPMC). Fig. 5 shows the flow chart of HLTPMC. Because joint histograms have high dimensions, LPP may be applied to joint histograms of HLTP for dimensionality reduction. However, LPP is not compulsory if we do not care about efficiency. To extract robust features, we may divide an image into different rectangular blocks and then extract HLTP, LTPM, and LTPC for each block of the image. The procedure is known as pooling. We calculate histograms of HLTP, LTPM, and LTPC for all blocks. We may apply LPP to reduce the dimensions of the histograms of HLTP. If we do not care about computational efficiency, we may not apply LPP. Histograms of HLTP, LTPM, and LTPC are concatenated together to generate HLTPMC.

#### 3.6. Feature and classifier for smoke detection

Suppose that there are N rectangular blocks and K orders of derivatives. We generate a large concatenated histogram of joint histograms of HLTP from blocks as follows:

H_s = {h_{k,i} | k = 1, …, K, i = 1, …, N}  (14)

The dimension of the concatenated histogram H_s is K∗N times as long as each joint histogram h_{k,i}, so it may be very high. Here, we can use LPP to learn a projection matrix A from a training set and then project the histogram H_s onto the subspace of A to obtain a low dimensional histogram H_p as follows:

H_p = A^T H_s  (15)

Similarly, we can obtain a concatenated histogram of LTPM from N blocks and K orders as follows:

H_m = {h^m_{k,i} | k = 1, …, K, i = 1, …, N}  (16)

Finally, we can obtain a histogram h_c with two bins. Thus, the dimension of h_c is only 2. Now, we have 4 types of histograms: H_s, H_p, H_m, and h_c. We can combine these histograms to form a feature vector in different ways. If we use only high order local ternary patterns and do not apply LPP for classification, the feature vector for HLTP is H_s. If we apply LPP to H_s, the feature extraction method is denoted as HLTP + LPP, and the feature vector of HLTP + LPP is represented by H_p.

H_s, H_m, and h_c are combined together to enhance robustness, and this combination is denoted as HLTPMC. The feature vector of HLTPMC is formulated as follows:

F1 = {H_s, H_m, h_c}  (17)

To reduce the dimensions of joint histograms, we apply LPP to H_s. Then we combine the histograms of H_p, H_m, and h_c to propose another method denoted as HLTPMC + LPP. The feature vector can be formulated as follows:

F2 = {H_p, H_m, h_c}  (18)

We used LIBSVM [6] for training and testing, which is an open source library for Support Vector Machine (SVM). For smoke detection, we used Gaussian Radial Basis Function kernels for SVM. The penalty coefficient c and gamma coefficient g of SVM are set to 1. For fair comparisons on image classification, we implemented our methods using Visual C++ to extract features from a texture data set and save them in MATLAB matrix format. Then we used the same MATLAB code of [34] to classify the features to obtain the average detection rates of our methods. The classifier in the MATLAB code is an SVM with χ2 kernels, which is very suitable to histogram features.

## Results

### 4. Experiments

> Table 1. Summary of the 23 LBP methods.

> Table 2. Image data sets for training and testing.

#### 4.1. Methods for comparisons

LBP has three mapping modes, which are uniform (U2), rotation invariant (RI) and rotation invariant uniform patterns (RIU2) [33]. CLBP [9] with the three mapping modes are denoted as CLBP U2, CLBP RI, and CLBP RIU2, respectively. We implemented Noise Resistant Local Binary Patterns (NRLBP) [37] with U2 only because NRLBP does not have other mapping modes. We implemented Patterns of Oriented Edge Magnitudes (POEM) [41]. The cell size, block size, orientation number, and neighbor number of POEM were set to 7, 10, 3 and 6, respectively. POEM with the three mapping modes are denoted as POEM U2, POEM RI, and POEM RIU2. We implemented Local Tetra Patterns (LTrP) [30], which has 13 binary patterns for each pixel. We applied the three mapping modes to obtain LTrP U2, LTrP RI, and LTrP RIU2. We implemented PLBP [35] with U2, RI and RIU2. Local Derivative Pattern (LDP) [52] defines four kinds of 2nd order derivatives computed along the four directions (0º, 45º, 90º and 135º), so LDP generates four codes for each pixel. Each code was also mapped to the three mapping modes, denoted as LDP4 U2, LDP4 RI, and LDP4 RIU2. To reduce the dimension of histograms, we computed the histogram of each code and then concatenated the four histograms together.

In summary, we used 23 variants of LBP to perform extensive experiments. Table 1 summarizes the 23 methods with detailed descriptions, including four versions of our method.

#### 4.2. Experiments for smoke detection

We established four smoke and non-smoke data sets for comparisons. The images of the four data sets were manually captured by cameras or collected from the Internet [51]. All the images were manually cropped, resized and labeled as smoke or non-smoke. All the images of the data sets are easily distinguished by human eyes. Table 2 lists the details of the data sets. We used Set1 for training, and Set2, Set3, and Set4 for testing. As shown in Fig. 6, both intra-class and inter-class variances of smoke and non-smoke are very large. That is the reason why it is very challenging to detect smoke from visual scenes.

> Fig. 6. Images from the four data sets. (a) Smoke images and (b) non-smoke images from Set 1. (c) Smoke images and (d) non-smoke images from Set 2. (e) Smoke images and (f) non-smoke images from Set 3. (g) Smoke images and (h) non-smoke images from Set 4.

##### 4.2.1. Evaluation methods

To quantitatively compare our methods with the state-of-the-art algorithms, we define Detection Rate (DR), False Alarm Rate (FAR) and Error Rate (ERR) as follows:

DR = P_p / Q_p × 100%; FAR = N_p / Q_n × 100%; ERR = (Q_p − P_p + N_p) / (Q_p + Q_n) × 100%  (19)

> Table 3. Experimental results for smoke detection.

##### 4.2.2. Our methods

We first compared our four methods with each other. As shown in Table 3, our HLTP without LPP achieved a detection rate of 97.5%, a false alarm rate of 1.71% and an error rate of 2.06% on Set2. For the large image sets Set3 and Set4, the algorithm achieved DR = 95.1% and 95.7%, FAR = 2.11% and 1.72%, and ERR = 2.69% and 2.26%, respectively. The dimension of HLTP is 200, and the number of support vectors learned from Set1 is equal to 462.

In HLTP + LPP, we applied LPP to project the concatenated histogram of HLTP onto a linear subspace whose dimension is set to 40. The number of support vectors with HLTP + LPP is much less than that with HLTP.

HLTPMC achieved better performance than HLTP. As shown in Table 3, DRs of HLTPMC are consistently higher than those of HTLP. We also found FARs and ERRs of HLTPMC are always smaller than those of HTLP. However, the dimension and the number of support vectors for HLTPMC are more than those for HLTP.

To evaluate the importance of dimensionality reduction, we also tested HLTPMC + LPP on the data sets. FARs and ERRs of HLTPMC + LPP are consistently smaller than those of HLTPMC for all the testing sets. For DRs, there are small ups and downs between HLTPMC + LPP and HLTP. In summary, HLTPMC + LPP has the best performance among the four methods. Table 3 shows that our methods obviously outperform most existing methods. The main reason is that our methods fully utilize information from high order derivatives, magnitudes of derivatives, center pixel values and manifold dimensionality reduction.

##### 4.2.3. Original LBPs

Comparing our methods with original LBPs, we found that LBP U2, LBP RI and LBP RIU2 achieved high detection rates, but they obtained high false alarm and error rates. LBP U2 achieved lower FARs and ERRs than LBP RI and LBP RIU2 on all the sets, except for the FAR of LBP RI that is equal to that of LBP U2. Although DRs of our methods are slightly smaller than the original LBPs on Set2, Set3, and Set4, our methods achieved distinctly lower false alarm rates and error rates on all the sets.

##### 4.2.4. Completed LBPs

CLBP RIU2 achieved the highest DR among CLBPs with U2, RI and RIU2. It achieved slightly higher DRs than our methods. However, FARs and ERRs of CLBP RIU2 are far higher than those of our methods. Thus, our methods have better generalization performance than CLBP. The dimension of CLBP is equal to the dimension of the original LBP times 2 plus 2. Thus, the dimensions of CLBP U2, CLBP RI and CLBP RIU2 are equal to 59 × 2 + 2 = 120, 36 × 2 + 2 = 74, and 10 × 2 + 2 = 22, respectively.

##### 4.2.5. Noise resistant LBPs

NRLBP is generated by changing the value of an uncertain bit to form a possible uniform code. Thus, NRLBP cannot be mapped to RI and RIU2. As shown in Table 3, DRs of NRLBP are very low, and FARs and ERRs of NRLBP are extremely high. So NRLBP is not suitable for smoke detection. The possible reason is that smoke blurs images and this leads to noisy patterns.

##### 4.2.6. Patterns of oriented edge magnitudes

Table 3 lists the experimental results of Patterns of Oriented Edge Magnitudes (POEM). DRs of POEM RI are 74.3%, 70.6% and 70.4% on the testing sets. DRs of POEM RIU2 are 76.0%, 70.6% and 69.2% on the testing sets. In addition, false alarm rates and error rates are very high, ranging from 28.7% to 36.0%. The dimensions of POEM with U2, RI and RIU2 are 33 × 3 = 99, 14 × 3 = 42, and 8 × 3 = 24, respectively. The numbers of support vectors with the three mapping modes are 1259, 1041, and 1008, respectively. Apparently, POEM is not suitable for smoke detection.

##### 4.2.7. Local tetra patterns

DRs of LTrP U2 are 57.3%, 63.4% and 60.4% on Set2, Set3 and Set4, respectively. So LTrP U2 has very poor performance for smoke detection. LTrP RI achieved DRs of 94.9%, 95.1% and 94.1%, FARs of 0.36%, 0.78% and 0.96%, and ERRs of 2.53%, 1.62% and 2.02% on the training sets. Compared with HLTPMC + LPP, LTrP achieved slightly lower false alarm rates than our method on Set2, Set3 and Set4. However, its error rates are inversely higher than those of our method on Set2 and Set4. The dimension of LTrP RI is far higher than that of HLTPMC + LPP. In addition, the number of support vectors for LTrP RI is much more than that of HLTPMC + LPP. LTrP RIU2 achieved slightly higher DRs than LTrP RI. However, LTrP RIU2 obtained apparently higher detection rates than LTrP U2.

##### 4.2.8. Pyramid LBPs

Detection rates of PLBP are 91.0%, 90.5% and 89.6% on Set2, Set3 and Set4, respectively. The number of support vectors is 1024, which is too many for a training set of 1383 images. PLBP RI achieved DR = 95.5%, FAR = 1.59%, and ERR = 2.92% on Set2, DR = 94.7%, FAR = 4.66%, and ERR = 4.80% on Set3, and DR = 94.6%, FAR = 4.02%, and ERR = 4.30% on Set4. PLBP with RIU2 achieved DR = 97.7%, FAR = 2.20%, and ERR = 2.26% on Set2, DR = 96.8%, FAR = 5.32%, and ERR = 4.89% on Set3, and DR = 97.1%, FAR = 4.46%, and ERR = 4.12% on Set4. So PLBP obtained worse performance than our methods.

##### 4.2.9. Local derivative patterns

Detection rates of LDP4 U2 are 77.6%, 80.0% and 79.9% on Set2, Set3 and Set4, respectively. Thus, its performance is not good. When RI and RIU2 mapping modes are used, the generalization performance of LDP is greatly improved. DRs of LDP4 RI are slightly higher than those of HLTPMC + LPP on Set3 and Set4. But FARs and ERRs of LDP4 RI are obviously larger than those of HLTPMC + LPP on all the sets. LDP4 RIU2 achieved very stable detection rates on the testing sets.

##### 4.2.10. Summary for smoke detection

Although some LBP methods can achieve excellent performance for texture classification, these methods cannot obtain good results for smoke detection. We also found that some variants of LBP are not suitable to be mapped to uniform patterns (U2) for smoke detection, such as LTrP U2, PLBP U2 and LDP4 U2. Experimental results also show that the RI and RIU2 mapping modes are more effective than the U2 mapping mode for smoke detection.

Our final objective is to detect smoke from video, so computational efficiency is also an important factor for feature extraction methods. Hence, we performed experiments on a notebook with an Intel i7-4720 CPU and recorded processing times of the above mentioned methods, as shown in Table 3. LTrP with U2 consumed the longest times among all the methods. It took 3.229, 21.03 and 20.58 seconds to classify Set2, Set3, and Set4, respectively. Our HLTP consumed 0.733, 4.384, and 4.305 seconds for Set2, Set3, and Set4, respectively. Although manifold learning methods need extra computation time for matrix factorization, our HLTP with LPP consistently spent less time than HLTP for all the smoke data sets. The reason is that LPP can provide compact features and produce less support vectors for SVM. The same results also appear on the smoke data sets for HLTPMC and HLTPMC + LPP. The timing results in Table 3 show that our methods are computationally efficient. In summary, our methods achieved better performance than existing methods.

#### 4.3. Comparisons for texture classification

To further evaluate the performance of our methods, we also tested our methods on a texture data set for image classification. We used the Brodatz album [2], which is a well-known texture classification benchmark data set, to assess the performance of our methods for multi-class image classification. It contains 111 texture classes with 9 images in each class. Fig. 7 shows some images from the texture data set. To facilitate comparisons, we adopted the same classifier and experimental scheme as [34]. 3 images were randomly selected from the 9 images of each class for training and the remaining 6 images were used for testing. The experiments were repeated 100 times to obtain average accuracy for the final evaluation.

> Fig. 7. Sample images from Brodatz album data set.

> Table 4. Comparisons on Brodatz texture data set.

We compared our method with the same LBP variants described in [34], including PRICoLBP [34], LBPV [10], CoALBP [32], LBPHF_S [1], LBPHF_S_M [54], and CLBP [9]. To facilitate comparisons, we used our method to extract features for 999 images of the Brodatz data set and saved the extracted features as a MATLAB file, which is available at http://staff.ustc.edu.cn/~yfn/Brodatz_HLTPMC_LPP.mat. Then, we used the MATLAB SVM code of [34] to compute the average recall rate of our method for fair comparisons. Table 4 lists the comparison results. We can see that our method achieved a recall rate of 96.06%, which obviously outperforms all of the LBP variants except PRICoLBP. Although PRICoLBP slightly outperformed our method, the feature dimension of PRICoLBP is far higher than that of our method. The experiments show that our method has powerful discriminative capabilities and compact feature representation for multi-class texture classification.

## Conclusion

### 5. Conclusions

Smoke has very large variations in color, texture and shapes, so it is still a challenging task to accurately recognize smoke from visual scenes. In this paper, we present a novel feature extraction method for smoke detection and image classification. Local Ternary Patterns (LTP) has demonstrated promising performance for texture classification. To further improve the discriminability of LTP, kth order derivatives around a center pixel are encoded to generate the kth order LTP, which is decomposed into an upper LBP code and a lower LBP code. Then we use joint histograms of the two LBP codes to preserve the co-occurrence of the two LBP codes and concatenate all joint histograms of LTPs extracted from different orders. In this way, we propose High order Local Ternary Patterns (HLTP) for smoke detection and image classification. Additionally, we apply a manifold dimensionality reduction method, Locality preserving Projection (LPP), to reduce the dimension of HLTP. However, LPP is not compulsory, so we may not apply LPP if we do not care about dimensions and computation time. Inspired by Completed Local Binary Patterns (CLBP), we also take the magnitudes of directional derivatives and values of center pixels into account for HLTP, but we encode magnitudes into 3-value codes instead of binary codes. We assign zeros to the magnitudes of derivatives that are less than a threshold to suppress noisy derivatives, and then propose High order Local Ternary Patterns based on Magnitudes of derivatives and Center pixel values (HLTPMC). Extensive experiments show that HLTP and HLTPMC with LPP can achieve high detection rates with low false alarm rates, and the proposed methods obviously outperform existing methods. Our methods also achieve good performance on the Brodatz texture set, so our methods have powerful discriminative capabilities for texture classification. Additionally, our method can generate a compact feature representation for texture classification.

## Acknowledgments

This work was partially supported by the Natural Science Foundation of China (61363038), the Cultivated Talent Program for Young Scientists of Jiangxi Province (20142BCB23014) and the Science Technology Application Projects of Jiangxi Province (KJLD12066, GJJ150459).

## References

[1] T. Ahonen, J. Matas, C. He, M. Pietikäinen, Rotation invariant image description with local binary pattern histogram fourier features, in: Proc. 16th Scandinavian Conf. Image Anal, 2009, pp. 61–70.
[2] P. Brodatz, Textures: A Photographic Album for Artists and Designers, Dover, New York, NY, USA, 1999.
[3] S. Deng, Y. Xu, Y. He, J. Yin, Z. Wu, A hyperspectral image classification framework and its application, Inf. Sci. 299 (2015) 379–393.
[4] K. Fan, T. Hung, A novel local pattern descriptor—local vector pattern in high-order derivative space for face recognition, IEEE Trans. Image Process. 23 (2014) 2877–2891.
[5] M. Fan, X. Zhang, H. Qiao, B. Zhang, Efficient isometric multi-manifold learning based on the self-organizing method, Inf. Sci. 345 (2016) 325–339.
[6] R. Fan, P. Chen, C. Lin, Working set selection using second order information for training SVM, J. Mach. Learn. Res., 6, 2005, pp. 1889–1918.
[7] D. Gottuk, J. Lynch, S. Rose-Pehrssonb, J. Owrutskyband, J. Owrutsky, F. Williams, Video image fire detection for shipboard use, Fire Safety J. 41 (2006) 321–326.
[8] J. Gubbi, S. Marusic, M. Palaniswami, Smoke detection in video using wavelets and support vector machines, Fire Safety J. 44 (2009) 1110–1115.
[9] Z. Guo, L. Zhang, D. Zhang, A completed modeling of local binary pattern operator for texture classification, IEEE Trans. Image Process. 19 (2010) 1657–1663.
[10] Z. Guo, L. Zhang, D. Zhang, Rotation invariant texture classification using LBP variance (LBPV) with global matching, Pattern Recogn. 43 (2010) 706–719.
[11] Z. Guo, Q. Li, J. You, D. Zhang, W. Liu, Local directional derivative pattern for rotation invariant texture classification, Neural Comput. Appl. 21 (2012) 1893–1904.
[12] Z. Guo, X. Wang, J. Zhou, J. You, Robust texture image representation by scale selective local binary patterns, IEEE Trans. Image Process. 25 (2015) 687–699.
[13] H. Hadizadeh, Multi-resolution local Gabor wavelets binary patterns for gray-scale texture description, Pattern Recognit. Lett. 65 (2015) 163–169.
[14] X. He, S. Yan, Y. Hu, P. Niyogi, H. Zhang, Face recognition using laplacianfaces, IEEE Trans. Pattern Anal. Mach. Intell. 27 (2005) 328–340.
[15] S. Hegenbart, A. Uhl, A scale- and orientation-adaptive extension of Local Binary Patterns for texture classification, Pattern Recognit. 48 (2015) 2633–2644.
[16] Z. Ji, Y. Pang, Y. He, H. Zhang, Semi-supervised LPP algorithms for learning-to-rank-based visual search reranking, Inf. Sci. 302 (2015) 83–93.
[17] X. Jia, X. Yang, K. Cao, Y. Zang, N. Zhang, R. Dai, X. Zhu, J. Tian, Multi-scale local binary pattern with filters for spoof fingerprint detection, Inf. Sci. 268 (2014) 91–102.
[18] B. Jun, T. Kim, D. Kim, A compact local binary pattern using maximization of mutual information for face analysis, Pattern Recognit. 44 (3) (2011) 532–543.
[19] Z. Li, G. Liu, Y. Yang, J. You, Scale- and Rotation-Invariant Local Binary Pattern Using Scale-Adaptive Texton and Subuniform-Based Circular Shift, IEEE Trans. Image Process. 21 (2012) 2874–2886.
[20] S. Liao, Max, W.K. Law, Albert, C.S. Chung, Dominant local binary patterns for texture classification, IEEE Trans. Image Process. 18 (5) (2009) 1107–1118.
[21] C. Liu, H. Wechsler, Gabor feature based classification using the enhanced Fisher linear discriminant model for face recognition, IEEE Trans. Image Process. 11 (4) (2002) 467–476.
[22] L. Liu, P. Fieguth, G. Zhao, M. Pietikäinen, D. Hu, Extended local binary patterns for face recognition, Inf. Sci. (19 April) (2016) Available online, doi: 10.1016/j.ins.2016.04.021.
[23] T. Liu, D. Tao, Classification with Noisy Labels by Importance Reweighting, IEEE Trans. Pattern Anal. Machine Intell. 38 (2015) 447–461.
[24] T. Liu, D. Tao, On the Performance of Manhattan Nonnegative Matrix Factorization, IEEE Trans. Neural Netw. Learning Syst. 99 (Aug) (2015) 1–13, doi: 10.1109/TNNLS.2015.2458986.
[25] T. Liu, D. Tao, On the Robustness and Generalization of Cauchy Regression, in: IEEE International Conference on Information Science and Technology (ICIST), 2014, pp. 100–105.
[26] R. Mehta, K. Egiazarian, Dominant Rotated Local Binary Patterns (DRLBP) for texture classification, Pattern Recognit. Lett. 71 (2016) 16–22.
[27] T. Mei, Y. Wang, X. Hua, S. Gong, S. Li, Coherent image annotation by learning semantic distance, in: Computer Vision and Pattern Recognition, 24-26 June, Anchorage, Alaska, USA, 2008.
[28] T. Mei, Y. Rui, S. Li, Q. Tian, Multimedia Search Reranking: A Literature Survey, ACM Comput. Surveys 46 (2014) 57–76.
[29] S. Murala, Q. Wu, Spherical symmetric 3D local ternary patterns for natural, texture and biomedical image indexing and retrieval, Neurocomputing 149 (2015) 1502–1514.
[30] S. Murala, R. Maheshwari, R. Balasubramanian, Local tetra patterns: A new feature descriptor for content-based image retrieval, IEEE Trans. Image Process. 21 (2012) 2874–2886.
[31] L. Nanni, S. Brahnam, A. Lumini, A local approach based on a Local Binary Patterns variant texture descriptor for classifying pain states, Expert Syst. with Appl. 37 (2010) 7888–7894.
[32] R. Nosaka, Y. Ohkawa, K. Fukui, Feature extraction based on co-occurrence of adjacent local binary patterns, in: Proc. 5th Pacific Rim Conf. Adv. Image Video Technol, 2012, pp. 82–91.
[33] T. Ojala, M. Pietikainen, T. Maenpaa, Multiresolution gray-scale and rotation invariant texture classification with local binary pattern, IEEE Trans. Pattern Anal. Mach. Intell. 24 (2002) 971–987.
[34] X. Qi, R. Xiao, C. Li, Y. Qiao, J. Guo, X. Tang, Pairwise rotation invariant co-occurrence local binary pattern, Trans. Pattern Anal. Mach. Intell. 36 (2014) 2199–2211.
[35] X. Qian, X. Hua, P. Chen, L. Ke, PLBP: An effective local binary patterns texture descriptor with pyramid representation, Pattern Recognit. 44 (2011) 2502–2515.
[36] C. Qing, J. Jiang, Z. Yang, Normalized co-occurrence mutual information for facial pose detection inside videos, IEEE Trans. Circuits Syst. Video Technol. 20 (2010) 1898–1902.
[37] J. Ren, X. Jiang, J. Yuan, Noise-resistant local binary pattern with an embedded error-correction mechanism, IEEE Trans. Image Process. 22 (2013) 4049–4060.
[38] A. Satpathy, X. Jiang, H. Eng, LBP-based edge-texture features for object recognition, IEEE Trans. Image Process. 23 (2014) 1953–1964.
[39] X. Tan, B. Triggs, Enhanced local texture feature sets for face recognition under difficult lighting conditions, Analysis and modelling of faces and gestures, Lecture Notes Comput. Sci. (LNCS) 4778 (2007) 168–182.
[40] B. Toreyin, Y. Dedeoglu, A. Cetin, Wavelet based real-time smoke detection in video, in: 13th European Signal Processing Conference, Antalya, Turkey, 2005.
[41] N. Vu, A. Caplier, Enhanced Patterns of Oriented Edge Magnitudes for Face Recognition and Image Matching, IEEE Trans. Image Process. 21 (2012) 1352–1365.
[42] C. Xu, D. Tao, C. Xu, Multi-View Intact Space Learning, Trans. Pattern Anal. Mach. Intell. 37 (2015) 2531–2544.
[43] C. Xu, D. Tao, C. Xu, Y. Rui, Large-margin Weakly Supervised Dimensionality Reduction, in: Proceedings of the 31st International Conference on Machine Learning, Beijing, China, 2014, pp. 865–873.
[44] C. Xu, D. Tao, Large-margin Multi-view Information Bottleneck, Trans. Pattern Anal. Mach. Intell. 36 (2014) 1559–1572.
[45] J. Yu, Y. Rui, D. Tao, Click prediction for web image reranking using multimodal sparse coding, IEEE Trans. Image Process. 23 (2014) 2019–2032.
[46] J. Yu, Y. Rui, Y. Tang, D. Tao, High-order distance-based multiview stochastic learning in image classification, IEEE Trans. Cybernetics 44 (2014) 2431–2442.
[47] F. Yuan, A double mapping framework for extraction of shape-invariant features based on multi-scale partitions with Adaboost for video smoke detection, Pattern Recognit. 45 (2012) 4326–4336.
[48] F. Yuan, A fast accumulative motion orientation model based on integral image for video smoke detection, Pattern Recognit. Lett. 29 (2008) 925–932.
[49] F. Yuan, Rotation and scale invariant local binary pattern based on high order directional derivatives for texture classification, Digital Signal Process. 26 (2014) 142–152.
[50] F. Yuan, Video-based smoke detection with histogram sequence of LBP and LBPV pyramids, Fire Safety J. 46 (2011) 132–139.
[51] F. Yuan, Z. Fang, S. Wu, Y. Yang, Y. Fang, A Real-Time Video Smoke Detection Using Staircase Searching Based Dual Threshold AdaBoost and Dynamic Analysis, IET Image Process. 9 (2015) 849–856.
[52] B. Zhang, Y. Gao, S. Zhao, J. Liu, Local Derivative Pattern Versus Local Binary Pattern: Face Recognition With High-Order Local Pattern Descriptor, IEEE Trans. Image Process. 19 (2010) 533–544.
[53] Y. Zhang, S. Li, S. Wang, Y. Shi, Revealing the traces of median filtering using high-order local ternary patterns, IEEE Signal Process. Lett. 21 (2014) 275–280.
[54] G. Zhao, T. Ahonen, J. Matas, M. Pietikainen, Rotation invariant image and video description with local binary pattern features, IEEE Trans. Image Process. 21 (4) (2012) 1465–1477.
[55] H. Zhou, R. Wang, C. Wang, A novel extended local-binary-pattern operator for texture analysis, Inf. Sci. 178 (2008) 4314–4325.
[56] C. Zhu, R. Wang, Local multiple patterns based multiresolution gray-scale and rotation invariant texture classification, Inf. Sci. 187 (2012) 93–108.
[57] J. Zou, W. Li, C. Chen, Q. Du, Scene classification using local and global features with collaborative representation fusion, Inf. Sci. 348 (2016) 209–226.

## Other

### Author biographies

Feiniu Yuan received B.Eng. and M.E. degrees in mechanical engineering from the Hefei University of Technology, Hefei, China, in 1998 and 2001, respectively, and a Ph.D. degree in pattern recognition and intelligence system from the University of Science and Technology of China (USTC), Hefei, in 2004. From 2004 to 2006, he worked as a post-doctorate with USTC. From 2010 to 2012, he was a Senior Research Fellow with Singapore Bioimaging Consortium, Agency for Science, Technology and Research, Singapore. He is currently a professor and a PhD supervisor at Jiangxi University of Finance and Economics. His research interests include 3D modeling, image processing and pattern recognition.

Jinting Shi received a B.E. degree in computer science and technology from the Jiangxi Normal University, Nanchang, China, in 2003, and an M.S. degree in computer science and technology from Jiangxi Agricultural University, Nanchang, China, in 2008. She is currently a PhD candidate with the School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, China. Her research interests include image processing and pattern recognition.

Xue Xia received a B.E. degree in Film & TV Arts and Technology and an M.E. degree in Communication and Information Engineering from Shanghai University, Shanghai, in 2011 and 2014, respectively. She is currently a PhD candidate with the School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, China. Her research interests include 3D display technology, image processing and pattern recognition.

Yuming Fang is currently a faculty member of the School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, China. He received a Ph.D. degree in Computer Engineering from Nanyang Technological University, Singapore in Feb. 2013. Previously, he obtained B.E. and M.S. degrees from Sichuan University and Beijing University of Technology, China, respectively. From October 2011 to January 2012, he was a visiting Ph.D. student at National Tsinghua University, Taiwan. From September 2012 to December 2012, he was a visiting scholar in University of Waterloo, Canada. He was also a (visiting) Postdoctoral Research Fellow in the IRCCyN lab, PolyTech' Nantes & Univ. Nantes, Nantes, France, University of Waterloo, Waterloo, Canada and Nanyang Technological University, Singapore. His research interests include visual attention modeling, visual quality assessment, image retargeting, computer vision, and 3D image/video processing. He was a secretary of HHME2013 (the 9th Joint Conference on Harmonious Human Machine Environment). He was also a workshop organizer in ICME 2014 and a special session organizer at VCIP 2013 and QoMEX 2014.

Zhijun Fang received a Ph.D. degree from Shanghai Jiaotong University, Shanghai, China. He is currently a professor in the College of Electronic and Electrical Engineering, Shanghai University of Engineering Science, Shanghai, China. His research interests include image processing, video coding, and pattern recognition. He was the General Chair of HHME2013 (the 9th Joint Conference on Harmonious Human Machine Environment) and a General Co-Chair of ISITC2014 (2014 International Symposium on Information Technology Convergence).

Tao Mei (M'07-SM'11) is a Lead Researcher with Microsoft Research, Beijing, China. He received a B.E. degree in automation and a Ph.D. degree in pattern recognition and intelligent systems from the University of Science and Technology of China, Hefei, China, in 2001 and 2006, respectively. His current research interests include multimedia information retrieval and computer vision. He has authored or co-authored over 100 papers in journals and conferences, 10 book chapters, and edited four books. He holds 13 U.S. patents and more than 20 in pending. Tao was the recipient of several paper awards from prestigious multimedia journals and conferences, including the IEEE Circuits and Systems Society Circuits and Systems for Video Technology Best Paper Award in 2014, the IEEE Trans. on Multimedia Prize Paper Award in 2013, the Best Student Paper Award at the IEEE VCIP in 2012, the Best Paper Award at the ACM ICIMCS in 2012, and the Best Paper Awards at ACM Multimedia in 2009 and 2007, etc. He is an Associate Editor of IEEE Trans. on Multimedia, ACM/Springer Multimedia Systems, and Neurocomputing, and a Guest Editor of six international journals. He is the General Co-chair of ACM ICIMCS 2013, the Program Co-chair of IEEE ICME 2015, IEEE MMSP 2015 and MMM 2013, the Workshop Co-chair of IEEE ICME 2012/4, and the Area Chair for ACM Multimedia 2010/2/3, ACM CIKM 2014, IEEE ICME 2013/4, PCM 2013, etc.
