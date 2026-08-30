# Video-based smoke detection with histogram sequence of LBP and LBPV pyramids

**Paper_ID:** 21_LBP_LBPV_FireSafety2011_Video_Smoke_Detection
**Authors:** Feiniu Yuan
**Affiliation:** School of Information Technology, Jiangxi University of Finance and Economics, Nanchang 330032, Jiangxi, China
**Venue:** Fire Safety Journal 46 (2011) 132–139
**DOI:** 10.1016/j.firesaf.2011.01.001

## Abstract

Video surveillance systems are widely applied in a variety of fields. Hence, video-based smoke detection is regarded as an effective and inexpensive way for fire detection in an open or large spaces. In order to improve the efficiency of the video-based smoke detection, a novel video-based smoke detection method is proposed by using a histogram sequence of pyramids. The method involves four steps. Firstly, through multi-scale analysis, a 3-level image pyramid is constructed. Secondly, local binary patterns (LBP), which are insensitive to image rotation and illumination conditions, are extracted at each level of the image pyramid with uniform pattern, rotation invariance pattern and rotation invariance uniform pattern to generate an LBP pyramid. Thirdly, local binary patterns based on variance (LBPV) with the same patterns are also adopted in the same way to generate an LBPV pyramid. And fourthly, histograms of the LBP and LBPV pyramids are computed, and then all the histograms are concatenated into an enhanced feature vector. A neural network classifier is trained and used for discrimination of smoke and non-smoke objects. Experimental results show that the features are insensitive to rotation and illumination, and that the method is feasible and effective for video-based smoke detection at interactive frame rates.

**Keywords:** Video-based smoke detection; Local binary pattern; Multi-scale analysis; Neural network

## Introduction

### 1. Introduction

Traditional smoke detectors usually detect the presence of combustion products through an ionization or photometry based sensors. But it takes a long time for combustion products to reach these sensors in outdoor or open spaces and in the case of a strong wind, combustion products may even be blown away, thus failing to give fire alarms. Therefore, traditional smoke detectors are not suitable in such cases. In recent years, researchers have used computer vision technology in the field of fire detection in order to overcome the aforementioned deficiencies of traditional sensors. Video-based fire detection is one of the computer vision-based methods and can be classified into two categories: video-based flame and video-based smoke detections.

### 1.1. Video fire and smoke detection

Many approaches to the video-based flame detection have been discussed by different worldwide researchers. Yamagishi and Yamaguchi [1] presented a flame detection algorithm based on the spatio-temporal fluctuation data of flame contours. Noda and Ueda [2] proposed a flame detection system based on gray scale images for tunnels. Phillips III et al. [3] implemented a video flame detection method, using a Gaussian-smoothed color histogram. Töreyin et al. [4] presented the video flame detection method based on motion, flicker, edge blurring and color features. Yuan et al. [5] proposed a video flame detection method, using the mixture Gaussian model to extract temporal features. Ko et al. [6] presented a fire detection method using techniques of moving detection and fire-colored pixels.

In many cases of fire, smoke is usually visible before the flame can be sighted, so video-based smoke detection is able to give fire alarms earlier than the video-based flame detection. Most methods of video-based smoke detection often extract motion, edge, color and texture features from video for the discrimination of smoke and non-smoke objects. Toreyin et al. [7] used the features of motion, flicker, edge blurring and color to detect smoke. In the method presented by Gubbi et al. [8], some statistical features, such as arithmetic mean, geometric mean, standard deviation, skewness, kurtosis and entropy, were computed on each sub-band of 3-level wavelet transformed images. Then, the SVM light implementation of support vector machines was used for detection of smoke. Guillemant and Vicente [9] proposed a method of smoke detection applied in the forests. Ferrari et al. [10] proposed a real-time image processing technique for the detection of steam in videos. They used Hidden Markov Tree (HMT), which was derived from the coefficients of the dual-tree complex wavelet transform (DT-CWT) in small local regions, to characterize the steam texture pattern, and an SVM classifier was used to detect the steam. This approach has the referential significance to smoke detection, because smoke has characteristics similar to steam.

Gottuk et al. [11] evaluated the effectiveness of several commercial video-based fire detection systems for small spaces on navy ships. Their experiments showed that the video-based fire detection systems detected more fires faster than the traditional systems. Yuan [12] adopted the integral image technique to quickly estimate the motion of moving objects and proposed an accumulative motion model for the video smoke detection. To reduce false alarms, the orientation is accumulated over time to compensate the results for the inaccuracy of orientation. Han and Lee [13] presented a flame and smoke detection method to be used in tunnels by analyzing color and motion information.

### 1.2. Texture analysis

Texture analysis is an effective method for the smoke detection. Most of the existing methods are sensitive to rotation and illumination. Although some methods of texture analysis, such as co-occurrence matrix methods [14], are insensitive to rotation, it depends greatly on illumination conditions. Histogram equalization is often performed to reduce the adverse effects of varying illumination. However, histogram equalization may decrease other characteristics of images. Ojala et al. [15] presented local binary patterns (LBP) for rotation and illumination invariant texture classification. Huang et al. [16] improved this method by computing the derivative based LBPs for face alignment. To prevent loss of global information caused by an LBP, Jafari-Khouzani and Soltanian-Zadeh [17] used the radon transform to estimate the principal orientation of the texture image and then computed the wavelet energy features along the principal orientation. The radon transform though is time consuming. Generally, texture can be precisely characterized by a spatial statistical measure and image contrast. So Ojala et al. [15] used the LBP and variance joint histogram for rotation invariant texture classification. Guo et al. [18] observed that a quantization step is required due to the continuity attribute of the variance value. The quantization step and the computation of the joint histogram were completely avoided by proposing a new operator, which is called the local binary pattern variance (LBPV). In fact, this operator can be regarded as the integral projection along the variance axis. Liao et al. [19] proposed dominant local binary patterns for texture classification by regarding the first 80% most frequent patterns as dominant features.

In this paper, we make use of the histogram sequence of LBP and LBPV pyramids to propose a new approach to the video-based smoke detection. The LBP and LBPV features, which were presented by Ojala et al. [15] and Guo et al. [18], respectively, are computed at each level of the 3-level image pyramid with uniform, rotation-invariance and rotation-invariance-uniform patterns. Then, all the histograms of the LBP and LBPV pyramids are concatenated into a feature vector for smoke detection. Hence, the feature vector contains both local and global informations. This paper presents at least two innovative ideas on the video-based smoke detection. First, LBP-related texture analysis methods are used to detect smoke. Second, different LBP patterns are used at different levels of the image pyramid, in order to collect local and global informations.

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

## Results

### 5. Experimental results

The LBP and LBPV-based smoke detection methods were implemented using Visual C++, and it was tested on a PC platform. To evaluate the validity of our method, we firstly constructed an image database, where there are 1220 smoke images and 1648 non-smoke images. For the purpose of training and testing, we selected 552 smoke and 831 non-smoke images from the image database to form a training set for the neural network, and the remainder images, which include 668 smoke and 817 non-smoke images, are regarded as a testing image set for the validity testing of the method. Fig. 8 shows several samples of smoke and non-smoke images from the image database.

> Fig. 8. Some samples from the image database: (a) smoke images and (b) non-smoke images.

The neural network classifier was trained on the training set until a pre-determined error threshold was reached. About 519 rounds of training were performed when the total error was just less than the threshold. Fig. 9 shows curve of the training error of the classifier.

> Fig. 9. Training error curve of the neural network.

After the classifier was trained, we performed classification on the training and testing sets to validate discrimination of the LBP and LBPV combined features. Classification on the training set was done to observe the convergence of the total misclassification error. Classification of the testing set was performed to evaluate the generalization performance of our method. As shown in the first row of Table 1, the detection rate on the training image set is very high and the false alarm rate is very low. The second row of Table 1 shows experimental results on the testing image set. The classifier is able to obtain a satisfactory detection rate and false alarm rate. The results show that our method has good generalization performance. So the LBP and LBPV combined features of a 3-level pyramid are efficient.

> Table 1. Experimental results on the training and testing image sets.

The method is also tested on several smoke videos recorded by CCD cameras. As shown in Fig. 10(a), the first video contains white smoke generated by smoldering of dry leaves. Red rectangles denote valid searched windows, which are correctly classified as smoke regions. It is observed that there exist some smoke regions misclassified as non-smoke regions. Fig. 10(b) illustrates experimental results on another video, which includes black smoke produced by the combustion of diesel fuel. We also notice that some smoke regions are misclassified, but no non-smoke regions are mistakenly classified as the smoke region.

> Fig. 10. Smoke videos: (a) smoldering of dry leaves and (b) combustion of diesel fuel. (For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)

Then, we tested the method on several non-smoke videos. As shown in Fig. 11(a), a traffic video was recorded on a street. The street is one of the trunk roads in our city. Tens of thousands of vehicles, such as cars, trucks, buses and so on, are running on the street everyday. So it is an ideal cluttered non-smoke video to evaluate false alarm rates of the method. Fig. 11(b) shows a video recorded on a road at a university. Several pedestrians and motorcycles passed in front of our CCD camera. The scene is less complicated than that in the video of Fig. 11(a). Experiments show that no misclassified regions are found in Fig. 11(a) and 11(b). After carefully observing the whole process of smoke detection on the two videos, we found that there were rarely misclassified regions.

> Fig. 11. Non-smoke videos: (a) traffic on a street and (b) traffic on a road.

For isolated or small misclassified regions, segmentation techniques and the accumulation methods proposed by Yuan [12] are used to remove most of the disturbances of occasional false alarms. For example, Fig. 12(a) shows that there are several misclassified regions on a video which display several students moving around on the playground. Segmentation techniques are used to re-classify the misclassified region as a non-smoke region, which is marked by a green rectangle. Fig. 12(b) shows the water surface of a pond, and there are several regions that are misclassified as smoke. In the left of the figure, isolated regions can be immediately ruled out by segmentation techniques. As for regions whose areas are larger than a predetermined threshold, an accumulation and motion detection technique can be used to remove those misclassified regions as much as possible.

> Fig. 12. Non-smoke videos with false alarms: (a) playground and (b) water surface of a pond. (For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)

For outdoor smoke detection, the video based smoke detection method has obvious advantages over traditional ion or photo based methods. The proposed algorithm should be compared with those of the same kind video based methods. So our method was compared with the algorithm proposed by Toreyin et al. [4] on two smoke and two non-smoke videos, which were captured outdoors by us. Fig. 13(a), (b), (c) and (d) illustrates snapshots of one black smoke video, one white smoke video, one waving leaves video and one basketball yard video, respectively. As shown in Table 2, our method has a better performance than Toreyin's method when the smoke videos are tested. After observing the frame number of an alarm, we can see that our method can provide an earlier fire alarm than Toreyin's method. Our method has the same performance as Toreyin's method on the waving leaves video, and has fewer false alarms on the basketball playground video by observing the number of false alarms. The reason that our method can achieve a better performance is mainly the robustness of LBP features. But the processing speed of our method is slower than Toreyin's method.

> Fig. 13. Testing videos: (a) black smoke, (b) white smoke, (c) waving leaves and (d) basketball playground.

> Table 2. Smoke detection performance comparisons on videos.

## Discussion

### 6. Discussion

The algorithm can detect the presence of smoke in a video with the size of 320×240 at about 10 frames per second (fps). It cannot obtain real time processing frame rates (above 25 fps). The algorithm needs a training image set. In fact, the positive and negative images used in the algorithm are impossible to cover all kinds of smoke and non-smoke objects. Therefore, detection and false alarm rates of the system highly depend on the training image set. The algorithm performs well on several videos we captured. If a video contains too many objects which are not included in the training set, the system performance will drop obviously. So we do not know the performance on unknown videos. That is the lower limit of smoke detection of the video system. Solution to the above mentioned problems is to create a representative image database and improve the algorithm itself.

## Conclusion

### 7. Conclusions

With the rapid development of video science and technology, cameras with large storage are getting so cheap that video surveillance systems are widely applied in a variety of fields. Video-based smoke detection can make full use of this surveillance hardware. Therefore, smoke detection by camera is considered as an effective and an inexpensive way for fire detection in open or large spaces. In this paper, a novel video smoke detection method is proposed. The method is based on the histogram sequence of LBP and LBPV pyramids. First, an image is decomposed into a 3-level image pyramid by using a multi-scale analysis. Second, local binary patterns, which are proved very insensitive to image rotation and illumination conditions, are extracted for the 3-level image pyramid with a uniform pattern, a rotation-invariance pattern and a rotation-invariance-uniform pattern. Moreover a variance-based local binary pattern with the same pattern type is also extracted at each level. Then, histograms of LBP and LBPV pyramids are computed, and all the histograms are concatenated to form a high dimensional feature vector. At last, a neural network classifier is used for classification. Several experiments on the training and testing sets, smoke and non-smoke videos show that the features are insensitive to rotation and illumination and the method has good generalization performance for smoke detection at interactive frame rates.

## Acknowledgments

This project was supported by the National Natural Science Foundation of China (61063034). Special thanks are given to anonymous reviewers for their helpful suggestions and the corrections of grammatical errors.

## References

[1] H. Yamagishi, J. Yamaguchi, A contour fluctuation data processing method for fire flame detection using a color camera, IECON 2000.
[2] S. Noda, K. Ueda, Fire detection in tunnels using an image processing method, VNIS 1994.
[3] W. Phillips III et al., Flame recognition in video, IEEE Workshop on Applications of Computer Vision, 2000.
[4] B.U. Toreyin et al., Computer vision based method for real-time fire and flame detection, Pattern Recognition Letters 27 (1) (2006) 49–58.
[5] FeiNiu Yuan et al., Vision based fire detection using mixture Gaussian model, IAFSS 2005.
[6] Byoung Chul Ko et al., Fire detection based on vision sensor and support vector machines, Fire Safety Journal 44 (3) (2009) 322–329.
[7] B. Ugur Toreyin et al., Wavelet based real-time smoke detection in video, EUSIPCO 2005.
[8] J. Gubbi et al., Smoke detection in video using wavelets and support vector machines, Fire Safety Journal (2009).
[9] P. Guillemant, J. Vicente, Real-time identification of smoke images, Optical Engineering 40 (4) (2001) 554–563.
[10] R.J. Ferrari et al., Real-time detection of steam in video images, Pattern Recognition 40 (3) (2007) 1148–1159.
[11] D.T. Gottuk et al., Video image fire detection for shipboard use, Fire Safety Journal 41 (4) (2006) 321–326.
[12] FeiNiu Yuan, A fast accumulative motion orientation model, Pattern Recognition Letters 29 (7) (2008) 925–932.
[13] Dongil Han, Byoungmoo Lee, Flame and smoke detection method for early real-time detection of a tunnel fire, Fire Safety Journal 44 (2009) 951–961.
[14] R.M. Haralik et al., Texture features for image classification, Engineering 3 (6) (1973) 610–621.
[15] T. Ojala et al., Multiresolution gray-scale and rotation invariant texture classification with local binary pattern, IEEE TPAMI 24 (7) (2002) 971–987.
[16] X. Huang et al., Shape localization based on statistical method using extended local binary pattern, ICIG 2004.
[17] K. Jafari-Khouzani, H. Soltanian-Zadeh, Radon transform orientation estimation, IEEE TPAMI 27 (6) (2005) 1004–1008.
[18] Z.H. Guo et al., Rotation invariant texture classification using LBP variance (LBPV), Pattern Recognition (2009).
[19] S. Liao et al., Dominant local binary patterns for texture classification, IEEE TIP 18 (5) (2009) 1107–1118.
[20] W. Wang et al., Face description and recognition by LBP pyramid, Journal of Computer Aided Design & Computer Graphics 21 (1) (2009) 94–100.
[21] W.S. Mcculloch, W. Pitts, A logical calculus of the ideas immanent in nervous activity, Bulletin of Mathematical Biophysics 5 (1943) 115–133.
[22] K. Hornik et al., Multilayer feed forward networks are universal approximators, Neural Networks 2 (1989) 359–366.
[23] S.I. Amari et al., Asymptotic statistical theory of over training and cross-validation, IEEE TNN 8 (1997) 985–996.
