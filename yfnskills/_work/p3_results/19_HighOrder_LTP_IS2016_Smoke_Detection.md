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
