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
