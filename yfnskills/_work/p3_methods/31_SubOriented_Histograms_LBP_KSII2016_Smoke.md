## 2. Local Binary Pattern with Gradient analysis

### 2.1 Local Binary Patterns

Traditional LBP computes in a simple way of comparing the value of a center pixel g_c with the values of its 3×3 rectangular neighborhood pixel value g_i (i = 0, ..., 7) as shown in Fig. 1(a). The LBP pattern code is computed as follows:

LBP = Σ_{i=0}^{7} s(g_i - g_c) 2^i, (1)

s(x) = 1 if x ≥ 0; 0 if x < 0, (2)

Ojala et al. [16] expanded rectangular neighborhood to circularly symmetric neighborhood to achieve multiresolution performance. However, P points are re-sampled in a circular neighborhood with radius R around the center pixel. There are three mapping patterns, which are defined as "Uniform", "Rotation Invariant" and "Rotation Invariant and Uniform", respectively. Experimental results show that the most "frequent" uniform binary patterns correspond to primitive micro features, such as edges, corners, and spots. "Uniform" is defined as a pattern which has no more than 2 spatial transitions (bitwise 0/1 or 1/0 changes). The patterns with more than 2 spatial transitions will be considered as identical patterns. So there are P*(P-1)+3 different patterns. The uniform value can be computed by:

U(LBP_{P,R}) = Σ_{i=1}^{P-1} | s(g_{(i+1)%P} - g_c) - s(g_i - g_c) |, (3)

where % denotes the modulo operation. "Rotation Invariant" is defined to remove the effect of rotation as

LBP^{ri}_{P,R} = min{ ROR(LBP_{P,R}, i) | i = 0, ..., P-1 }, (4)

where ROR(x, i) denotes a circular bit-wise right shift on the number x i times. "Rotation Invariant and Uniform" pattern is a combination of "Uniform" pattern and "Rotation Invariant" pattern. It is defined as:

LBP^{riu2}_{P,R} = Σ_{p=0}^{P-1} s(g_p - g_c) if U(LBP_{P,R}) ≤ 2; P + 1 otherwise, (5)

If P and R is respectively set to 8 and 1, the circularly symmetric neighborhood can be simplified to a 3×3 rectangular neighborhood as shown in Fig. 1(b). Although multiresolution can be applied in a circularly neighborhood, interpolation is required and leads to increasing the computation complexity (e.g. the neighbors' values g_1, g_3, g_5 and g_7 are computed by interpolation). Therefore, we use the 3×3 rectangular neighborhood to avoid re-sampling of pixel values.

We compute original LBP codes for the whole image. These original LBP codes will be first used for analysis of the orientation of gradient to extract the relationship between the two LBP codes described in section C. According to these gradient orientations, we calculate the LBP histogram in each orientation respectively. The original LBP code is directly used to compute the gradient orientation. Because any of "Uniform", "Rotation Invariant" or "Rotation Invariant and Uniform" mapping patterns will generate a new numeric label, which leads to loss of texture information. The details will be described in section 2.2.

### 2.2 Distance measure for LBP codes

According to the definition of LBP, each bit represents the binarized difference of pixel values in a certain direction. Similarly, we can encode the changes of the bits in the same direction of two LBP codes to extract these variations of the two codes. As illustrated in Fig. 2(b), the LBP code in the center is "1" and the code in the direction "7" is "0", so both the Euclidean and Hamming distances between the two codes are 1, and the two distances are coincident. But for the direction 5, things will be so different. The Euclidean distance between the center code ("1") and the code ("255") in the direction 5 is 254 while the Hamming distance between the two codes is 7. The two distances are very different. As we can see, the Hamming distance metric is more concordant than the Euclidean distance metric.

Therefore, the variation degree of texture can be measured by the Hamming distance between two LBP codes along each direction. As shown in Fig. 2(b), the number in brackets following the red number, which is the Euclidean distance, is just the Hamming distance between two LBP codes. In the directions "3" and "4", their Hamming distances are 3, i.e., there are 3 directions where the LBP bits change, but the Euclidean distances are 5 and 14, respectively. Notice that the LBP code has no numerical meaning. Thus, the difference value can't represent the number of changed directions.

So we use Hamming distance to measure two LBP codes [22]-[24]. Hamming distance is firstly introduced in error detection and correction code in the literatures. Hamming distance between two equal length strings is defined as the number of positions where corresponding characters are different. Consider Hamming distance between strings "smoke" and "smile", because the third and fourth characters in the word "smoke" are different from the third and fourth characters in the word "smile" respectively, so there are two corresponding positions that have different symbols, thus the Hamming distance is 2. We can see that each bit of LBP code corresponds to a direction of local neighborhood. If we need to compare two LBP codes in each direction to acquire information of variation trends, we can compare each bit of two LBP codes with each other. In other words, we consider an LBP code as a sequence of bits. By regarding each LBP code as a binary string of length P, we calculate Hamming distance of two LBP codes x and y as follows:

d = Σ_{i=0}^{P-1} ( x(i) ⊕ y(i) ), (6)

where x(i) and y(i) are the i-th bits of x and y respectively for i = 0, ..., P-1, ⊕ represents exclusive or operation. In our implementation, P is set to 8.

As shown in Fig. 2(b), the Hamming distance between the LBP code in the center that is "00000001" and its adjacent LBP code in direction 6 that is "00011111" is 4. The distance value just shows there are 4 directions where there are changes of bits.

### 2.3 Gradients of LBP codes with two coordinate systems

Edge information is one of the most fundamental characteristics in an image. The gradient of an image is usually used to approximately detect edges. There are a lot of feature extraction methods based on gradient for object detection, such as Scale-Invariant Feature Transform (SIFT) [25], Histogram of Oriented Gradients (HOG) [26] and so on. HOG achieves good performance especially in pedestrian detection and face detection.

Fig. 3 shows processing flow of HOG, where we need to estimate the gradient of an image, and compute the magnitude and orientation of the gradient. We can use Sobel operators or central differences of an image f(x,y) to compute the gradient (fx, fy) of the image. Then we use Eq. (7) and (8) to calculate the magnitude and orientation of the gradient.

mag = sqrt( fx^2 + fy^2 ), (7)

θ = tan^{-1}( fy / fx ), (8)

where fx stands for horizontal differences of the image, fy stands for vertical differences of the image, mag in Eq.(7) represents the gradient magnitude of image, and θ denotes the gradient the orientation of the gradient. θ is quantized into several bins. In HOG, mag in Eq.(7) is accumulated as a weight into the corresponding bin defined by θ.

But when we directly use HOG for smoke detection, experiments show that the result is not as good as other detections. The reason may be that the edge of smoke is not as salient as other objects. To improve performance, we propose to extract sub oriented LBP code maps from LBP code maps and compute oriented histograms of LBPs from the oriented maps.

In order to illustrate special characteristics of smoke images, we compare the image "lena" (Fig. 4a) with the image "smoke" (Fig. 4e). As we can see, the edge of "lena" (Fig. 4b) is more distinct than "smoke" (Fig. 4f). In addition, the edges of "lena" are denser than that of "smoke". The reason is that smoke often has low contrast, and the situation gets worse especially for mist-like smoke. Too low contrast leads to low detection rates and high false alarm rates.

LBP has powerful discriminative capabilities in feature extraction from an image. Fig. 4(c) and Fig. 4(g) are LBP code maps of "lena" and "smoke", respectively. Histograms of LBP codes reflect frequency of each LBP code and obtain robust performance in many applications.

But histograms discard spatial distributions of LBP codes in the whole image. As we mentioned in above sections, the difference of two LBP codes is actually the Euclidean distance of the two codes, which is not coincident with our intuition. Therefore, we propose to use Hamming distance for computation of gradients over LBP codes.

However, there are two issues to be solved. The first is that the difference of gradient can be either positive or negative, but the Hamming distance is always a non-negative number. If we use Hamming distance to compute gradients for HOG, the orientation θ is always located in the first quadrant that leads to a drop of discriminative performance. To solve this issue, we introduce a reference code c, and the difference between two LBP codes can be re-defined as the difference between the differences of the two LBP codes and the reference code c as follows:

d = ||x - c|| - ||y - c||, (9)

where x and y are the two LBP codes, and ||·|| denotes a distance measure that can be L1 or L2 norms [24]. Since the distance defined in Eq. (9) may be zero, positive or negative, θ may be located in any quadrant. So the discriminative capability can be improved. If we set the reference code c to "00000000", Eq. (9) is reduced to

d = ||x|| - ||y||, (10)

Fig. 4(d) and Fig. 4(h) respectively show gradient magnitudes of "lena" and "smoke" based on Hamming distances of LBP codes, which are estimated by Eq.(10).

Second, original LBP codes reflect variation of pixel values in sample directions. We often use the distances of two LBP codes along two orthogonal directions to estimate gradients, so four LBP codes are involved, as shown in Fig. 5(a). If the LBP code map is rotated 45° as shown in Fig. 5(b), the other 4 LBP codes can be involved. Rotation of 45° can avoid re-sampling of pixel intensities for computation efficiency. To include more information of LBP codes for estimation of gradients, we propose to use two coordinates systems to estimate two gradients. Therefore, there are two orientations θ1 and θ2 for each point.

### 2.4 Sub oriented histograms of LBP codes

As shown in Fig. 6, suppose that we quantize the two orientations into n1 and n2 bins, so there are n1*n2 different combinations of the two discrete orientations (θ1, θ2) that are (0, 0), (0,1), (0,2), ..., (n1-1, n2-1), respectively. As for a specific pair of orientations θ1 and θ2, we can generate a sub LBP code map from the original LBP code map. Hence, we obtain n1*n2 sub LBP code maps from the original LBP code map denoted as Mlbp. A sub code map M_sub^{o1,o2} for a specific pair of discrete orientations (o1, o2) can be generated as follows:

M_sub^{o1,o2}(i, j) = M_lbp(i, j) if o1 = θ1(i, j) and o2 = θ2(i, j); L_new else, (11)

where L_new is a new label that can be specified any value out of the LBP value range.

We can generate an LBP histogram from each sub LBP map. For a given pair of orientations (o1, o2), the histogram of a sub LBP map, which is also called sub oriented histogram by us, can be computed as follows:

H_sub^{o1,o2}(k) = (1/(w*h)) Σ_{i=0}^{h-1} Σ_{j=0}^{w-1} δ( M_sub^{o1,o2}(i, j) - k ), (12)

where δ(v) is the delta function returning 1 if v=0 and 0 for v≠0, w and h are the width and height of the sub code map, respectively.

Since there are n1*n2 sub LBP code maps, we have n1*n2 histograms. As for each histogram, we compute only the frequency of the original LBP labels except for the new label Lnew. The reason is that the new label of a given pair stands for LBP labels whose orientations are not inside the given pair but must be inside some pairs, so it is unnecessary to count the frequency repeatedly. Finally, we concatenate all the histograms H_sub^{o1,o2} together to form a robust vector F to describe image samples:

F = [ H_sub^{0,0}, H_sub^{0,1}, ..., H_sub^{n1-1,n2-1} ], (13)

We extract the feature of testing images in the same way for training images. Support vector machine (SVM) has outstanding performance on classification, so we input the extracted feature vector F into SVM for training and testing. Fig. 6. gives the overall framework of the feature extraction procedure.
