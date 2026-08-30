## Methods

The overall flowchart of the data processing pipeline is shown in Fig. 1. The rectangles in solid lines represent approaches that are involved in our method, while those in dashed lines are the inputs and outputs in every step.

As shown in Fig. 1, the overall flowchart of the pipeline mainly includes three steps that are original feature extraction, dimensionality reduction, and classification. We use LBP variants to extract original features from input images. Then Kernel Principal Component Analysis (KPCA) is adopted for dimensionality reduction to obtain compact representations of images, which are known as mapped features. At last, the mapped features are used as final features and are sent to Gaussian Process Regression (GPR) for classification to output predicted labels for the images. Below we will describe each step in details.

### A. LBP features

The original LBP code [7] is obtained by comparing the value of a center pixel gc with the values of its neighborhood pixels gi (i = 0, 1, . . . 7), as shown in the two equations below.

LBP = Σ_{i=0}^{P-1} s(g_i − g_c) 2^i  (1)

s(x) = 1 if x ≥ 0;  s(x) = 0 if x < 0  (2)

where P points are re-sampled in a circular neighborhood with radius R around the center pixel gc. As an alternative, there are three mapping patterns in original LBP, which are "Uniform" (U2), "Rotation Invariant" (RI) and "Rotation Invariant and Uniform" (RIU2). The most frequently used parameters are P = 8 and R = 1, thus the dimensions of LBP^{U2}_{P,R}, LBP^{RI}_{P,R} and LBP^{RIU2}_{P,R} are 59, 36, and 10.

For the sake of simplicity, we just use histograms of LBP codes extracted by existing methods as the original features for Kernel Principal Component Analysis (KPCA). In the future, we will focus on research of specific feature extraction methods, which are even not limited to LBP-like features, in order to generate more stable, compact and robust representations for images.

For the i-th gray-scale training image f_i(x, y), we compute the histogram of original LBP codes as follows:

x_i(k) = Σ_{y=0}^{h-1} Σ_{x=0}^{w-1} δ(LBP(x, y) − k)  (3)

where δ(v) is the delta function that returns 1 if v = 0 and 0 for v ≠ 0, x_i(k) stands for the k-th bin of the histogram, w and h are the width and height of the image f_i(x, y), and LBP(x, y) denotes the LBP code map of the image f_i(x, y).

### B. Kernel principal component analysis (KPCA)

Principal Component Analysis (PCA) is defined as an orthogonal linear transformation, which is often used to transform the data onto a new sub-space. The transformation matrix is formed by the top-d eigenvectors of covariance matrix. X = {x_1, . . . , x_N} stands for the input data with zero mean. The i-th sample is denoted by x_i, while the mean vector of all the samples x_i (i = 1, . . . , N) is denoted by x_C. The optimized projection matrix is obtained by minimizing the following goal function:

W = arg min_W { tr(W^T C W) − λ(I − W^T W) }  (4)

Where tr(A) denotes the trace of a matrix A. The covariance matrix C is defined as follows.

C = (1/N) Σ_{i=1}^{N} (x_i − x_C)(x_i − x_C)^T  (5)

By solving the above equations, W is just formed by the first-d eigenvectors, sorted in descending order by eigenvalues, of the covariance matrix C, i.e., W = [w_1, w_2, . . . , w_d]. As the dimension is reduced, some information is lost but not too much because the discarded eigenvalues are small [30]. For a given sample x, the projected data y is computed as follows: y = W^T x. The dimension of y is often less than x.

Kernel Principal Component Analysis (KPCA) was proposed by [31] to extend the original linear PCA to non-linear data distributions [32]. Before applying a PCA, the input data should be nonlinearly mapped into a high dimensional feature space [33], [34]. The mapping function is defined as: φ : x → φ(x).

Generally, the mapping function φ(x) is unknown. A kernel function k(x_i, y_j) is used to avoid explicitly specifying the unknown mapping function. We empirically choose the Gaussian kernel in KPCA to keep consistent with the kernel function of the covariance function for simplicity of computation. The kernel function k(x_i, y_j) used here is defined as a Radius Basis Function (RBF), which is defined in Eq. 8. Then the mapped samples are fully represented by the kernel matrix K. The i-th row and j-th column element of the kernel matrix K is often calculated by a Gaussian kernel:

K_{ij} = k(x_i, x_j) = exp( − ||x_i − x_j||^2 / (2σ^2) )  (8)

It is impossible to explicitly center the data in the feature space since the mapping function is unknown. The kernel trick is used to indirectly center the kernel matrix K. The mean of the mapped samples φ(x_i) (i = 1, . . . , N) in the feature space is computed by φ_0 = (1/N) Σ_i φ(x_i). Then, the centered version φ^C(x_i) of a mapped sample φ(x_i) is equal to φ^C(x_i) = φ(x_i) − φ_0. The i-th row and j-th column element of the centered kernel matrix K^C is calculated as follows:

K^C_{ij} = ⟨φ^C(x_i), φ^C(x_j)⟩ = K_{ij} − (1/N)Σ_l K_{il} − (1/N)Σ_k K_{kj} + (1/N^2)Σ_{k,l} K_{kl}  (10)

K^C = K − 1_N K − K 1_N + 1_N K 1_N  (11)

The a-th eigenvector w_a of the covariance matrix C can be expressed by a linear combination of φ^C(x_i), so the coefficients α_{1a}, . . . , α_{Na} are required [35]. In other words, the a-th eigenvector w_a is conversely converted to a point α_a in the mapped sample space, which is spanned by the centered mapped samples φ^C(x_i) (i = 1, . . . , N). The combination is defined as: w_a = Σ_{i=1}^{N} α_{ia} φ^C(x_i).

The coefficient vector α_a is just the eigenvector of the centered kernel matrix K^C, which is represented as: K^C α_a = N λ_a α_a. The eigenvector w_a has unit length, so we normalize the eigenvector as follows: α_a = α_a / √(N λ_a).

Once a coefficient vector α_a is acquired, corresponding projection vector w_a is uniquely determined by Eq. 12. Since the mapped data φ^C(x_i) is unknown, we can not compute w_a explicitly. However, we can directly project a new data z onto the a-th eigenvector w_a by the kernel trick. We map and center the new data z to obtain a centered feature φ^C(z) = φ(z) − φ_0, then we compute the projection of the centered feature φ^C(z) on w_a as follows:

w_a^T φ^C(z) = Σ_{i=1}^{N} α_{ia} ⟨φ^C(x_i), φ^C(z)⟩ = Σ_{i=1}^{N} α_{ia} k^C(x_i, z)  (15)

The centered kernel k^C(x_i, z) between the i-th mapped training sample φ^C(x_i) and the new mapped data φ^C(z) is computed as in Eq. 16.

### C. Gaussian process regression (GPR)

The central limit theorem gives that the sum of a sufficiently large number of independent random variables will be approximately normally distributed [36]. Hence, in smoke detection, the samples and their corresponding labels can be regarded as random variables that follow the zero mean normal distribution.

Given a set of training samples X = [x_1, x_2, . . . , x_N] and corresponding labels y = [y_1, y_2, . . . , y_N]^T, the relationship between X and y is modeled as a multivariate Gaussian distribution with zero mean, covariance matrix K: y ∼ N(0, K).

The i-th row and j-th column element k(x_i, x_j) of covariance matrix K is usually defined as a squared exponential kernel function of any two samples (x_i, x_j), which reflects the similarity between the two samples. Therefore, K can be regarded as an N × N covariance matrix controlled by the parameter set θ = {θ_0, θ_1, θ_2}.

K_{ij} = k(x_i, x_j) = θ_0 exp(−θ_1 ||x_i − x_j||) + θ_2 + δ_{ij} σ^2  (18)

The joint distribution of the training samples X and a new test sample x_* can be modeled as the following multivariate Gaussian distribution:

[y; y_*] ∼ N( [0; 0], [[K, K_*]; [K_*^T, K_{**}]] )  (19)

The marginal likelihood is specified as a prior that is a Gaussian function p(y | X, θ) ∼ N(0, K + σ^2 I), so the parameters θ can be solved by minimizing the negative log marginal likelihood defined in Eq. 20.

−log p(y | X, θ) = (1/2) ln det(K + σ^2 I) + (1/2) y^T (K + σ^2 I)^{−1} y + C  (20)

Since the predictive distribution is represented by Eq. 18 and Eq. 19, the distribution of the prediction value y_* can be calculated by Eq. 21.

p(y_* | x_*, X, y) = N(μ_*, σ_*^2)

σ_*^2 = K_{**} − K_*^T (K + σ^2 I)^{−1} K_* + σ^2

μ_* = K_*^T (K + σ^2 I)^{−1} y  (21)

### D. The data flow of the pipeline

The detailed data flow of the pipeline is demonstrated in Fig. 2. The pipeline has two phases including training and testing. The training phase consists of original feature extraction, dimensionality reduction by KPCA and training of GPR. The testing phase includes original feature extraction, dimensionality reduction by KPCA and testing of GPR. So there are total four steps drawn in gray rounded rectangles, which are original feature extraction, dimensionality reduction by KPCA, training and testing of GPR.

Bold red arrows stand for the flowing direction of data in the testing phase while thin blue arrows denote the data flowing direction during learning. Solid red rectangles are processing methods. Blue dashed rectangles are input and output data for training methods, while red dashed rectangles are inputs and outputs for testing methods.

In the original feature extraction step of the training phase, LBP like features are first extracted from training images f_i(x, y) (i = 1, . . . , N) using LBP variants. The features extracted from the training images are aggregated into a matrix X = [x_1, x_2, . . . , x_N], whose columns are the original features of all the training images.

Then we use unsupervised KPCA to learn an implicit mapped feature φ^C(x_i) for each image f_i(x, y) and obtain an implicit projection matrix W = [w_1, w_2, . . . , w_d]. In fact, we can not explicitly achieve the mapped features and the projection matrix. However, we can directly compute the projection of the mapped features, W^T * φ^C(X), by the kernel trick of KPCA using Eq. 11 and Eq. 12.

In the last step of the training phase, we input the projected features, W^T * φ^C(X), of all training images and the labels of training images, y = [y_1, y_2, . . . , y_N]^T, to the Gaussian Process Regression (GPR), and we learned a GPR classification model described by Eq. 21.

As shown in Fig. 2, the training data in the data processing pipeline flows along thin arrows from a module to another. In the testing phase, we use the similar data flow procedure to process a test image f_*(x, y) to output a predicted label y_*, as shown in Fig. 2. For the testing image f_*(x, y), we first use LBP variants to extract the original LBP feature, which is denoted by a feature vector z. Then we use the kernel trick of KPCA to compute the projection of the original feature z in the sub-space of the mapped feature space, which is just the final mapped feature W^T * φ^C(z). Finally, we use the GPR model to calculate the predicted label y_* for the test image f_*(x, y). The data in the test phase flows along bold arrows, as shown in Fig. 2.
