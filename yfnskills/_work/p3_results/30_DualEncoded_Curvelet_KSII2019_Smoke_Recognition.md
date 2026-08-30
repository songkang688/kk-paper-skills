## Results

### 4.1 Data sets

Several experiments were conducted on four data sets, each of which has an imbalanced number of smoke and non-smoke images. All images were manually cropped, resized and labeled as smoke images or non-smoke images. Smoke images of the data sets are easily distinguished by human eyes. The data sets are available at http://staff.ustc.edu.cn/~yfn/index.html. Smoke images of all datasets were resized to the size of 48×48 and converted to grayscale images for feature extraction.

Table 1 lists the details of the data sets. We used Set1 for training, and Set2, Set3, and Set4 for testing. Some samples are shown in Fig. 5. It can be seen that both intra-class and inter-class variances of smoke and non-smoke images are very large.

### 4.2 Implementation of compared methods

In order to verify the effectiveness of our method, we compared our method with some state-of-the-art algorithms by the three evaluation criteria in [32], which are Detection Rate (DR), False Alarm Rate (FAR) and Error Rate (ERR). They are defined as follows:

DR = P_p / Q_p × 100%;  FAR = N_p / Q_n × 100%;  ERR = ((Q_p − P_p) + N_p) / (Q_p + Q_n) × 100%  (14)

where P_p and N_p respectively denote the numbers of accurately detected true positive samples and negative samples mistakenly classified as positive samples, and Q_p and Q_n are the numbers of positive and negative samples, respectively.

### 4.3 Analysis of results

In our experiments, we used several feature extraction methods to validate the ability of our method to distinguish between smoke and non-smoke images on the three test sets. These compared methods are DRLBP [33], CLBP [16], LDBP [34], PLBP [35], PRICoLBP [36], MDLBP [37] LTrP [38] and DFD [39]. The compared LBP variants are all un-mapped for fair comparisons.

The threshold for LTrP is set to 0.1 to demonstrate better performance, and g for RBF in SVM is set to 1/1383 for all other comparison features. For DFD, default setting is adopted to extract features.

We involve LBP and CLBP in our feature extraction step. Dual-LBP features based on the Curvelet domain and CLBP features on spatial domain are combined to form the final feature. In our CLBP, histograms of sign component and joint histograms of magnitude and center pixel maps are cocatenated to form CLBP_S_M/C. Finally, we aggregate dual LBP and CLBP features (denoted as Dual-LBP + CLBP) as our final feature vector, whose dimension is 256+768=1024.

From Table 2, we find that our method achieves lower FARs than other methods on three testing data sets. MDLBP involves information across RGB channels, so it obtains the best DRs among all the methods. While all the other LBP variants are conducted on grayscale images. So it does not provide fair comparisons. At the same time, the DRs got by our method are not obviously higher than other methods.

Hence, ROC (Receiver Operating Characteristic Curve) is adopted to present a more comprehensive comparison, as shown in Fig. 6. By varying classification threshold t from -1 to 1 at step 0.1, DR and FAR pairs are obtained at every step to plot ROC.

Although the DRs of our method do not exceed the ones of other methods obviously, the ROCs illustrate that our method outperforms others, which means that the best classification planes are not always at t=0. The encoding step in our method can be replaced by any LBP-based methods. For instance, in Table 2 and Fig. 6, Dual-LBP + CLBP is adopted. Similarly, the other three combinations are Dual-LBP + LBP, Dual-CLBP + CLBP, Dual-CLBP + LBP.

The experimental results of the 4 combinations are shown in Table 3. Although the FAR of our method is not the lowest on Set3 and Set4, the DR of our method is highest and ERR is lowest. Overall, our Dual-LBP + CLBP performs best among all the combinations.

It is notable that Dual-CLBP + CLBP performs worse than others on Set3 and Set4. The reasons may be: 1) After Curvelet transform, an original image is decomposed into sub-bands. Low-frequency ones correspond to flat regions, in which the sign of gradient can better capture the invariance than magnitudes do. 2) There are correlations between Curvelet coefficients. Hence, the M and C components in CLBPs bring redundancy rather than improvement.

Lower FAR means lower accidental false alarm, which is of great significance for smoke classification, and it can reduce the serious consequences of false alarms. Therefore, our method is of great practical application value.

As shown in Table 4, we employ different parameter optimization methods to demonstrate the performance of GKO. We also compare our approach with the grid search, which is proposed in [30]. According to the experimental results, grid search method is proved not suitable for parameters optimization for different datasets. The GKO algorithm improves the accuracy of SVM.

Although the GKO step is time-consuming, it provides better classification performance and shorten the classifying time. Meanwhile, grid search consumes 214.1 seconds. Hence the GKO algorithm yields better performance than the grid search one. The computation time and the number of support vectors by the GKO algorithm are less than that of grid search on Set2.
