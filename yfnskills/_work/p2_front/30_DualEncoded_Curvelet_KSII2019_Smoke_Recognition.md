# 30_DualEncoded_Curvelet_KSII2019_Smoke_Recognition — Clean English Corpus

## Title

Dual-Encoded Features from Both Spatial and Curvelet Domains for Image Smoke Recognition

Feiniu Yuan (1,2), Tiantian Tang (3), Xue Xia (2,*), Jinting Shi (4,*), Shuying Li (5)

(1) College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, China [e-mail: yfn@ustc.edu.cn]. (2) School of Information Technology, Jiangxi University of Finance and Economics, China [e-mail: yeziandkuma@qq.com]. (3) School of Communications and Electronics, Jiangxi Science and Technology Normal University, China. (4) Vocational School of Teachers and Technology, Jiangxi Agricultural University, China [e-mail: icanflysjt@126.com]. (5) School of Automation, Xi'an University of Posts & Telecommunications, China.

*Corresponding author: Xue Xia, Jinting Shi

KSII Transactions on Internet and Information Systems, 2019. Received March 5, 2018; revised October 22, 2018; accepted November 7, 2018; published April 30, 2019.

## Abstract

Visual smoke recognition is a challenging task due to large variations in shape, texture and color of smoke. To improve performance, we propose a novel smoke recognition method by combining dual-encoded features that are extracted from both spatial and Curvelet domains. A Curvelet transform is used to filter an image to generate fifty sub-images of Curvelet coefficients. Then we extract Local Binary Pattern (LBP) maps from these coefficient maps and aggregate histograms of these LBP maps to produce a histogram map. Afterwards, we encode the histogram map again to generate Dual-encoded Local Binary Patterns (Dual-LBP). Histograms of Dual-LBPs from Curvelet domain and Completed Local Binary Patterns (CLBP) from spatial domain are concatenated to form the feature for smoke recognition. Finally, we adopt Gaussian Kernel Optimization (GKO) algorithm to search the optimal kernel parameters of Support Vector Machine (SVM) for further improvement of classification accuracy. Experimental results demonstrate that our method can extract effective and reasonable features of smoke images, and achieve good classification accuracy.

Keywords: Curvelet Transform, Dual-encoded Local Binary Pattern (Dual-LBP), Completed Local Binary Pattern (CLBP), Gaussian Kernel Optimization (GKO), Smoke Recognition

## Introduction

Generally, fire causes significant economic losses and probably lead to severe death. In order to avoid fire occurrence, many traditional fire detection technologies have been widely used. These methods are usually based on temperature sensors, humidity sensors, and traditional ultraviolet and infrared fire detectors. Since traditional methods need to sample combustion products for analysis, they are required to be placed in the vicinity of fire.

In addition, traditional detectors are susceptible to external environment influences, such as airflow, dust. Traditional methods cannot provide us with detailed information about burning situation. Therefore, traditional smoke detectors are unreliable in open, large and special spaces. In most cases, fire will be initially accompanied by the emergence of smoke, and smoke often lasts for a few minutes before flames emerge.

According to this observation, visual smoke detection methods detect smoke from videos or images, and they are able to give early alarms of fire. Early smoke has special visual features, such as color, texture, and shape, which play an important role in fire detection. There are many texture feature extraction methods that have been proposed.

Gray-level co-occurrence matrices [1] is a way to describe texture by exploring spatial correlation between gray values of neighboring pixels. LBP [2] provides a binary-coding feature extraction manner by encoding the relationship between central pixels and their neighboring pixels. HOG [3] extracts features of edges and gradients. Many methods can achieve excellent performance by capturing multi-scale and multi-direction information in transform or frequency domains.

Compared with other transforms, Curvelet transform is strongly anisotropic and its needle-shaped elements provide a high directional sensitivity to represent curved singularities in images. In contrast, wavelet transform shows a good representation only at point singularities because it has a poor directional sensitivity.

Additional directional-based transforms, such as Dual-Tree Complex Wavelet Transform (DTCWT) and Gabor Wavelets, provide more multi-direction information than Wavelets, but they still have limited directional selectivity. Ridgelet is suitable for representing line singularities in objects, so it's rarely found in practical applications [4]. To extract discriminative features, we propose a novel feature extraction based on spatial and Curvelet domains.

The main contributions of this paper are listed as follows:

1) We use Curvelet transform to extract discriminative features from original images, and then encode these images consisting of discriminative Curvelet coefficients to generate LBP codes based on Curvelet domains.

2) We first aggregate histograms of LBP maps from Curvelet domains to produce a histogram image of size 256×50, and then encode the histogram image again to generate novel codes, which are called Dual-encoded Local Binary Patterns (Dual-LBP).

3) We concatenate histograms of Dual-LBPs from Curvelet domain and Completed Local Binary Patterns (CLBP) from spatial domain to generate dual-encoded features for smoke classification.

Finally, we adopt Gaussian Kernel Optimization (GKO) algorithm to search the optimal kernel parameters of Support Vector Machine (SVM) for further improvement of classification accuracy.

## RelatedWork

There are many methods proposed for smoke detection. Chenebert et al. [5] presented a flame pixel detection method in video images or still images using a non-temporal texture driven approach. The method did not use any time information. Chen et al. [6] used a color model based on RGB for fire smoke detection. However, there are many objects having the same color distribution as fire, so the method gives a false alarm inevitably for these fire-like object. Celik et al. [7] proposed a universal color model for fire pixel detection, and the algorithm used the YCbCr color space to separate chrominance and luminance components more effectively than other color spaces (such as RGB). Yuan et al. [8] proposed an accumulative motion model based on integral image techniques. The model estimated movement directions of objects in real-time for analysis of smoke. Zhang et al. [9] proposed a real-time forest fire detection algorithm using artificial neural networks based on dynamic characteristics of fire regions segmented from video images. Yu et al. [10] presented a method by using color and motion features for video smoke detection. The method could distinguish smoke from objects with similar color distribution by involving motion features and color information, which greatly improved the reliability of video smoke detection. Toreyin et al. [11] achieved smoke detection based on edge magnitude differences, in which the characteristics of smoke such as movement, flashing, edge blur and color were used. Once the scene lacks obvious edges or cluttered objects, the method raises false alarms. Texture feature features play a key role in smoke detection, Ojala et al. [2] firstly proposed Local Binary Pattern (LBP) for texture classification.

It is an efficient and simple gray-scale texture descriptor, which captures spatial characteristics of texture. LBP features have demonstrated very powerful discriminative capability, low computational complexity, and low sensitivity to illumination variations. To further improve the discriminative capability of LBP, many variants of LBP were proposed in the past decade. Yuan et al. [12] proposed an effective smoke detection method, in which features were extracted by concatenating histograms of local binary patterns (LBP) and local binary pattern variances (LBPV) from image pyramids, and an BP neural network was used for classification. Yuan et al. [13] presented sub-oriented histograms of LBP for image smoke classification. Gubbi et al. [14] proposed a video smoke detection algorithm based on wavelet and Support Vector Machines (SVM) classification. Liao et al. [15] proposed Dominant Local Binary Patterns (DLBP) for texture classification by regarding the more frequently occurred patterns as dominant features. Guo et al. [16] proposed a Completed LBP (CLBP) approach, which encoded the magnitudes and signs of differences between a center pixel and its neighbors. CLBP provides excellent classification performance. Above-mentioned methods extract features in spatial domains.

Many methods achieve robust features from transform or frequency domains. Elaiwat et al. [17] proposed a multimodel Curvelet-based method for textured 3D face recognition. Each keypoint was detected across number of frequency bands and angles on 3D faces. Ucar et al. [18] presented an algorithm that was for facial expression recognition by integrating Curvelet transform and online sequential extreme learning machine (OSELM) with radial basis function (RBF) hidden node having optimal network architecture.

Although Curvelet transform provides a powerful multi-scale capability to extract discriminative smoke features, Curvelet-based image classification methods are limited to features, since the Curvelet coefficients are regarded as a holistic features extracted from the whole images [19]. To this end, we propose a duplex feature coding approach based on Curvelet transform to extract features from interpolated smoke images.

Many papers have been proposed to optimize kernel functions. Chapelle et al. [20] devised a gradient-based algorithm, which optimized a kernel function with multiple unconstrained parameters for SVM. Ghiasi-Shirazi et al. [21] considered the problem of optimizing a kernel function over translation invariant kernels for the task of binary classification. Wu et al. [22] proposed a direct method to build sparse kernel learning algorithms by adding one more constraint to the original convex optimization problem for sparse large margin classifiers. Ye et al. [23] considered the problem of multiple kernel learning (MKL) for regularized kernel discriminant analysis (RKDA), in which the optimal kernel matrix was obtained as a linear combination of pre-specified kernel matrices. All above methods formulated the kernel learning problem as an optimization problem based on a special task, such as SVM.
