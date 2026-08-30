## Methods

### 2. Local binary pattern

#### 2.1. LBP

Local binary pattern (LBP) is a gray-scale texture operator, which can capture spatial characteristics of images. At a center pixel, a pattern number is computed by comparing its value with values of its neighboring pixels. The LBP initial label for that center pixel is given by

LBP_{P,R} = Σ_{i=0}^{P−1} s(g_i − g_c) · 2^i  (1)

s(x) = 1 if x ≥ 0; 0 otherwise  (2)

where g_c is the gray scale value of the center pixel, g_i is the value of its ith neighbor, P is the number of neighbors and R is the radius of the neighborhood which is the Euclidean distance between the center point and its neighbors.

Fig. 1 shows examples of circularly symmetric neighbor sets for different P and R. LBP_{8,1}, LBP_{8,2} and LBP_{16,2} denote a point set with P=8 and R=1, one with P=8 and R=2, and one with P=16 and R=2, respectively.

> Fig. 1. LBP texture operator.

As the radius increases, an LBP contains more global information of texture patterns and also needs more neighbors, thus increasing the computational cost. If a large radius R is mixed with small P, it will result in severe artifacts in the re-sampling. So in our smoke detection, for the sake of balance between information and computation, the number of neighbors is set to 8, and the radius is set to 1. Circularly symmetric neighbor sets require bi-linear interpolation of pixel values. It may take a lot of time to interpolate values of all the neighbors. In order to further improve the computational performance, the Euclidean distance is replaced with the block distance, as shown in Fig. 2. Thus, re-sampling of the values of the neighbors is completely avoided. Ojala et al. [15] defined three different types of patterns, which are uniform, rotation-invariant and rotation-invariant-uniform.

> Fig. 2. Modified LBP texture operator with block distance (LBP_{8,1}).

The uniform value of an LBP pattern, which is actually the number of spatial transition (bitwise 0/1 changes), can be computed by

U(LBP_{P,R}) = Σ_{i=0}^{P−1} |s(g_{(i+1) mod P} − g_c) − s(g_i − g_c)|  (3)

where a mod b returns the remainder. For example, patterns 00000000 and 11111111 have U=0; patterns 01101101, 00111001 and 11110001 have U values of 6, 4 and 2, respectively.

Ojala et al. [15] defined the uniform pattern as one that has no more than 2 spatial transitions (U≤2). They also observed that uniform patterns are one of the fundamental patterns within image textures. The uniform patterns have P·(P−1)+3 different output values. Mapping from an original pattern LBP_{P,R} to a uniform pattern LBP^{u2}_{P,R} can be efficiently implemented with a lookup table of 2^P elements.

A rotation invariant version of an original pattern, called the rotation invariant pattern LBP^{ri}_{P,R}, is defined as

LBP^{ri}_{P,R} = min_{0≤i≤P−1} ROR(LBP_{P,R}, i)  (4)

where ROR(x,i) performs a rotated bit-wise right shift on x i times. The rotation-invariant-uniform pattern LBP^{riu2}_{P,R} is defined as:

LBP^{riu2}_{P,R} = Σ_{i=0}^{P−1} s(g_i − g_c) if U(LBP_{P,R}) ≤ 2; P+1 otherwise  (5)

In our implementation with P=8 and R=1, histogram dimensions of LBP^{u2}_{P,R}, LBP^{ri}_{P,R} and LBP^{riu2}_{P,R} are 59, 36 and 10, respectively.

#### 2.2. LBPV

Local binary pattern LBP characterizes an information of local spatial patterns, while variance VAR contains local contrast of pixel values. The joint histogram of LBP and VAR is able to include local patterns and local contrast at the same time. However, VAR has continuous values so it must be quantized before the computation of the joint histogram. Therefore, a learning procedure is required to obtain feature distributions, which are used to guide users to perform suitable quantization of continuous variance values [15]. To avoid quantization of continuous variance values, LBPV was proposed by Guo et al. [18]. The LBPV histogram is computed as

LBPV^{type}_{P,R}(k) = Σ_i Σ_j w(LBP^{type}_{P,R}(i,j), k)  (6)

w(LBP^{type}_{P,R}(i,j), k) = VAR_{P,R}(i,j) if LBP^{type}_{P,R}(i,j) = k; 0 otherwise  (7)

The superscript type can be u2, ri and riu2. The LBPV is actually an integral projection along the VAR axis. In our implementation, the histogram dimensions of LBPV^{u2}_{P,R}, LBPV^{ri}_{P,R} and LBPV^{riu2}_{P,R} are also 59, 36 and 10, respectively.

### 3. Histogram sequence

#### 3.1. Image decomposition

In our implementation, the LBP and LBPV patterns contain little global information, because the radius R is small. To include more global information of the image textures, a 3-level image pyramid is constructed. Then LBP and LBPV patterns are computed at each level of the image pyramid, in order to generate LBP and LBPV pyramids. Histograms are computed at each level of the LBP and LBPV pyramids. This method is similar to the method proposed by Wang et al. [20]. But in our method, three different pattern types of u2, ri and riu2 are simultaneously used, and an LBP based on variance is also adopted and two pyramids are used.

As shown in Fig. 3(a), an image is decomposed into three sub-images I_0, I_1 and I_2. In our implementation, the size of the nth level image is just half the size of the (n−1)th level image. Fig. 3(b) shows a flow chart of the image decomposition. The original image, which is just the 0th level image I_0 of the pyramid, is firstly smoothed by convolving it with Gaussian low pass filter (LPF). Then, the smoothed version of an image I_0 is down-sampled every 2 pixels to generate the 1st level image I_1. The 1st level image is also smoothed and down-sampled in the same way to generate the 2nd level image I_2. In our implementation, a 3×3 template of the 2D Gaussian low pass filter was used as shown in Fig. 3(c). The smoothing of an image at each level is completed by convolving the image with the 2D template.

> Fig. 3. Pyramid decomposition of an image: (a) image pyramid, (b) flow chart of an image decomposition and (c) template of the low pass filter.

#### 3.2. Histogram sequence of LBP and LBPV pyramids

For each level of the image pyramid, both LBP and LBPV patterns are computed to generate two pyramids, which are the LBP pyramid and the LBPV pyramid. Then, different mapping schemes are applied to different level images. At the 0th level, the uniform patterns are used to produce LBP^{u2}_{P,R} and LBPV^{u2}_{P,R}. At the 1st level, the rotation-invariant patterns are used to produce LBP^{ri}_{P,R} and LBPV^{ri}_{P,R}. At the 2nd level, the rotation-invariant-uniform patterns are used to produce LBP^{riu2}_{P,R} and LBPV^{riu2}_{P,R}.

Fig. 4 shows the LBP and LBPV pyramids generated by the aforementioned method. Therefore, there are three LBP images and three LBPV images in the two pyramids. Then, we compute histograms of these six images, which are denoted as H^{u2}_0, HV^{u2}_0, H^{ri}_1, HV^{ri}_1, H^{riu2}_2 and HV^{riu2}_2. At last, all the histograms are concatenated to form a 210 dimensional feature vector

F = {H^{u2}_0, HV^{u2}_0, H^{ri}_1, HV^{ri}_1, H^{riu2}_2, HV^{riu2}_2}  (8)

> Fig. 4. LBP and LBPV pyramids.

In fact, LBP patterns in the nth level image are just the same as the LBP patterns with a larger radius R in the (n−1)th level image, but each neighbor in the nth level image is generated by calculating the weighted sum of 3×3 pixels in the (n−1)th level image, as shown in Fig. 5. In other words, an LBP at a high level is equivalent to an LBP with the same P and larger R at a low level after the low level image is convolved with the low pass filter. As the level increases, the equivalent radius also increases. The LBPV has the same properties as an LBP, so we do not discuss it again in detail.

> Fig. 5. Enlargement of the radius.

### 4. Classification with the neural network

It is necessary to enlarge the size of the searching windows before the histograms are computed. In our implementation, the minimum size of the searching window is set to 24×24 for smoke detection. Histograms may be sparse and unstable for the highest level images of pyramids, because they are too small. For a 3-level pyramid decomposition of images with the size of 24×24, the smallest size of the 2nd level image is 6×6, which is too small to obtain a stable histogram of LBP patterns. To solve this problem, we add the surrounding regions of the searching windows to them. In other words, the original searching window is implicitly enlarged. As shown in Fig. 6, the blue solid rectangle is the original searching window which contains 24×24 pixels, and the red dash rectangle denotes the enlarged searching window. The size of the enlarged window is 48×48.

> Fig. 6. Enlarged searching windows. (For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)

The BP neural network is used for smoke detection in our implementation. The neural network was first developed by McCulloch and Pitts [21] in 1943. The multilayer feed forward network is the most mature and widely used model. Hornik et al. [22] drew a conclusion that a neural network with a single hidden layer can approximate any continuous non-linear function to any desired accuracy. A typical BP neural network model includes input, hidden and output layers [23].

Fig. 7 shows the BP neural network used for smoke detection. All neurons from one layer are connected to all neurons in the next layer. Each neuron receives a signal from the neurons in the previous layer. Each of those signals is multiplied by a separate weight value. The weighted inputs are summed, and passed through a sigmoid activation function which scales the output to a fixed range of values. The output of the function is then broadcast to all of the neurons in the next layer.

> Fig. 7. The structure of BP neural network used for smoke detection.

The goal of training the neural network is to find weights that minimize overall error measures, which usually are the sum of the squared errors. The training procedures are as follows: (1) The 210 features are extracted through the aforementioned method. The output vector for smoke samples is Y_i=(1,0)^T and for non-smoke samples Y_i=(0,1)^T. (2) Connecting weights are randomly set within (−0.2, 0.2). (3) Forward propagation calculates the output vector and misclassification error of each sample; errors are back-propagated and weights updated. (4) If the total error E_t is less than a pre-determined threshold ε, training terminates; otherwise proceed to step 3.
