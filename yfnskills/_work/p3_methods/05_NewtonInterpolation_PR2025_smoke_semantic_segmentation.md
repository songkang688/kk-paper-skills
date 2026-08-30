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
