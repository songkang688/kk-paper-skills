# 11_Confidence_Prior_PR2021_Image_Dehazing — Clean English Corpus

<!-- Stage 00 Wave 3 Agent H. English **Original:** blocks only; no Chinese content.
     Source: /workspace/11_Confidence_Prior_PR2021_Image_Dehazing.md (bilingual reader).
     Anchors in comments (SXXX/CXXX) refer to reader block ids.
     Authorship context (do not re-derive): Tier A2, weight 0.90; first of 5 authors. Topic confound: dehazing, not smoke.
     Equation-heavy paper: PDF text layer scrambled most display equations; readable equations normalized inline, irreparable ones flagged with [Eq. (N) garbled in extraction].
     Suspected source typos preserved as printed (see cleaning log): "natual", "uncorrected", "Fatal [12]", "halo aircrafts". -->

## Title

<!-- src: S001, S002, S003 -->
A confidence prior for image dehazing

Feiniu Yuan, Yu Zhou, Xue Xia, Xueming Qian, Jian Huang

Pattern Recognition 119 (2021) 108076. DOI: 10.1016/j.patcog.2021.108076

## Abstract

<!-- src: S005 -->
By sorting channel-minimized values in an ascending order, we individually put the values of several existing image dehazing priors on the curve of sorted values to propose a framework for unifying and understanding these priors. Then we propose a confidence ratio to specify the probability of each channel-minimized value within a range, and thus we can intuitively find a suitable point from the curve, which is actually defined as a novel prior. Although our novel prior and existing ones are perfectly unified under the same framework, our prior has an important advantage that it can freely control the suppression degree of outliers by directly adjusting the confidence ratio of channel-minimized values. In this way, we can remove influence of outliers in a controllable manner. To solve the problems caused by heterogeneity of pixel values and abrupt jumps of scene depths in hazy images, we adopt a regression method to adaptively learn the relationship between patch appearance and confidence ratios for all pixels. To further improve robustness, we use a Gaussian kernel to smooth the estimated confidence ratios for local consistency. Extensive experiments on both natural and synthetic images show that our confidence prior achieves significantly better performance than existing state-of-the-art methods.

## Introduction

<!-- original heading: "Introduction" (S007; unnumbered in extraction) -->

<!-- src: S008 -->
Images taken in outdoor environments often suffer poor visibility and low contrast due to the presence of haze and dust in the atmosphere. If a camera is far from scene objects, tiny particles suspended in the atmosphere inevitably degrade image quality. The faint color and shifted luminance of images have an adverse impact on vision applications, such as object detection [1], recognition [2], and classification [3]. Haze removing is a critical issue for image processing and computer vision.

<!-- src: S009 -->
Existing haze removal methods are usually based on the formation model of hazy images. The formation model divides the light reflected by objects in hazy scenes into an attenuation term and an airlight one. However, the dehazing physical model is a severely ill-posed problem. To make the problem solvable, researchers have proposed several priors based on statistical observation of hazy images. The accuracy and rationality for prior selection are crucial for image dehazing. Some methods utilize certain features of local pixels in hazy images as priors for transmission estimation, while others adopt the geometry of pixel cluster distributions for transmission estimation. However, these priors are significantly influenced by outliers or noises in hazy images, so dehazed results are usually unsatisfactory in some cases.

<!-- src: S010 -->
In this paper, we first propose a unified framework for better understanding of several well-known priors, including the color ellipsoid prior by Bui and Kim [4], the dark channel prior by He et al. [5], and the filtering prior by Tarel and Hautiere [6]. Then we propose a confidence prior to accurately estimate scene transmissions for image dehazing. We take a minimization operation in each patch among channels, and then use Gaussian models to statistically fit channel-minimized values of pixels in the patch. To control the removal degree of outliers or noises, we propose to use a ratio to compute our confidence priors. Considering heterogeneity of image signals and abrupt depth jumps in hazy images, we adopt a regression method to learn the relationship between patch appearance and confidence ratios. Once we obtain these confidence ratios, we can easily compute scene transmissions to robustly generate dehazed images.

<!-- src: S011; large internal duplication removed (second copy of "confidence prior for each pixel … summarized as follows:" was a column re-read) -->
Our confidence prior is completely different from existing methods under the unified framework. Bui and Kim [3] used an ellipsoid geometry to fit the distribution of pixel values, and embedded a fuzzy process into the construction of color ellipsoids. Unlike the color ellipsoid prior, we learn a ratio to adaptively adjust the confidence prior for each pixel. Our method is also different from the dark channel prior, which is actually the minimum value of pixels in each patch but sensitive to noises. Our method can remove the influence of outliers and noises in a controllable manner in a viewpoint of statistics. Tarel and Hautiere [6] proposed a "median of median" filter for prior estimation. However, it lacks reasonable explanation of statistical analysis, and it cannot control the removal degree of outliers or noises. The main contributions of our method are summarized as follows:

<!-- src: S012; re-split enumerated contribution list -->
1) We propose a framework to unify several well-known priors. By ascendingly sorting channel-minimized values in local patches, we find that each of the priors is perfectly related to a certain point on the curve formed by the sorted values. In this way, we put these well-known priors under a unified framework for better understanding.

2) According to the unified framework, we present a confidence prior that is determined by a ratio. The confidence ratio is multiplied with a standard deviation to control the confidence of values that are statistically located in a range. The ratio can adjust the removal degree of outliers. Thus, we can statistically remove influence of outliers or noises, and accordingly obtain more robust estimation of priors than existing methods.

3) To solve the drawback of fixed ratios, we propose to use a learning method for adaptive estimation of confidence ratios. Our confidence prior determined by a fixed ratio usually fails in regions with abrupt depth jumps, so we need to adaptively estimate confidence ratios. For the sake of simplicity, we use a regression method to learn the relationship between patch appearance and confidence ratios in our implementation. Thus, we can use patch appearance to infer a ratio for adaptively estimating a confidence prior. The adaptive confidence prior is more robust than a fixed confidence prior.

<!-- src: S013 -->
The structure of this paper is organized as follows. We introduce previous work on image dehazing in section 2. In section 3, we first present a unified framework of channel-minimized values. Then, under the unified framework, we propose a confidence prior for efficient removal of outliers or noises. Section 4 compares our method with state-of-the-art methods on different image datasets. Finally, we summarize the proposed method and draw the conclusion in section 5.

## RelatedWork

<!-- original heading: "Related work" (S014) -->

<!-- src: S015 -->
Most image dehazing methods obtain restored images by inversely solving the formation model of hazy images. To recover haze-free images, dehazing algorithms usually estimate the parameters of the haze formation model, including the transmission of scenes and the intensity of atmospheric light.

<!-- src: S016; "et al ." spacing artifacts normalized -->
Early methods mainly rely on additional information about the scene to remove the veiling layer of haze, such as depth information, polarization angles of multiple images. Narasimhan et al. [7] presented a geometric framework for scene understanding under hazy weather conditions, and computed the three-dimensional structure and color of the scene from two or more hazy images. Schechner et al. [8] proposed an image defogging algorithm using two polarization images, because the airlight scattered by atmospheric particles is partially polarized. These two polarization images are captured through parallel and perpendicular orientations, respectively. To implement haze removal, Kopf et al. [9] used scene depth information, which is directly accessible in geo-referenced digital terrain or city models. Haze removal methods from several images are very flexible, but they are highly dependent on applications.

<!-- src: S017; "RoblesKelly" line-break artifact fixed to "Robles-Kelly"; "Fatal [12]" and "uncorrected" preserved as printed -->
Compared to restoration methods from multiple hazy images, visibility restoration from a single image has received more attention in recent years, but it is a very challenging problem. Solutions for single image dehazing have been intensively developed in recent years. Tan [10] maximized local contrast in every patch of input images to increase the visibility of images, because image contrast is usually reduced by haze. By assuming that surface shading and transmission are locally uncorrected, Fattal [11] used Independent Component Analysis (ICA) to estimate scene albedos. The method uses statistical property to estimate parameters for single image dehazing, but it fails in the case of dense fog. To further improve performance, Fatal [12] proposed a color line model by assuming that pixel values in a small patch typically exhibit a linear relationship in the RGB color space. Unfortunately, the color line model does not always hold. He et al. [5] observed a phenomenon that the minimum color components of haze-free patches are usually small and prone to zero. The phenomenon is called dark channel prior. He et al. [5] computed dark channel priors by using two minimization operations in local patches. The dark channel prior provides an efficient way to enhance the visibility of hazy images, but it cannot accurately handle bright areas and it is sensitive to noises. Many methods have been proposed to improve the dark channel prior [13]. For example, Meng et al. [14] added a boundary constraint on the transmission function by exploring scene radiance. Ancuti et al. [15] implemented image dehazing based on multi-scale fusion. Nishio et al. [16] proposed a Bayesian defogging algorithm, according to the fact that scene albedos and depths are two statistically independent variables. Mutimbu and Robles-Kelly [17] proposed an evidence combining method that exploits the ability of factor graphs. Some dehazing methods [18,19] combine the physical model with the Retinex assumption. Choi et al. [20] achieved haze removal based on fog density perception. Their strategy is the same as haze density estimation also used by Jiang et al. [21] and Ling et al. [22].

<!-- src: S018 -->
Filtering based dehazing methods have been proposed. Li and Zheng [23] introduced a globally guided image filtering to preserve fine structures of dehazed images. By assuming that scene depths are smooth in a local region, Tarel and Hautiere [6] proposed a fast image restoration algorithm by using median filtering. The algorithm can achieve real-time performance. Locally Adaptive Wiener Filters were used by Gibson and Nguyen [24] to refine estimation of fog amount in an image.

<!-- src: S019 -->
With the rapid development of machine learning and deep learning, haze-relevant priors are recently investigated in a learning framework. Tang et al. [25] investigated features related to the properties of hazy images, and then used random forests to learn a mapping function between the haze-relevant features and transmission in every patch. Zhu et al. [26] created a linear model to estimate scene depths of hazy images under a color attenuation prior. According to the prior, the parameters of a linear function were learned using a supervised learning method. Berman et al. [27] focused on hazy lines derived from the linear color blending of similar pixels collected from entire images, and then proposed a non-local prior that restores haze-free images using various patch-based local priors. The prior is obviously different from traditional patch-based methods. Yang and Sun [28] proposed a deep learning approach for single image dehazing. Gandelsman et al. [29] proposed an unsupervised coupled deep-image-prior network for haze removal. Cai et al. [30] proposed an end-to-end CNN network with a novel BReLU unit for intelligently extracting haze features and estimating transmission. Ren et al. [31] proposed a multi-scale deep neural network to learn a mapping function between hazy images and corresponding transmission maps. Li et al. [32] proposed an All-in-One Dehazing Network (AOD-Net) for image dehazing. Chen et al. [33] restored clear images using an adaptive model, which can automatically select a patch size for each pixel. Ren et al. [34] designed a network to learn confidence maps and propose a fusion-based approach for haze removal.

<!-- src: S020; "endto-end" line-break artifact fixed -->
Recently, Generative Adversarial Networks (GAN) have achieved great successes in many computer vision applications. Zhang and Patel [35] used a GAN model to remove haze in images. Santra et al. [36] proposed a CNN-based comparator for image dehazing. Song et al. [45] recovered clear images by using a ranking CNN. Ren et al. [37] proposed a single image dehazing via multi-scale convolutional neural networks with holistic edges, which consists of a coarse-scale net to predict a holistic transmission map, and a fine-scale net to locally refine dehazed results. Wu et al. [38] proposed a learning interleaved cascade of shrinkage fields to achieve haze removal for avoiding the weakness of noise sensitivity in most existing methods. Liu et al. [39] proposed a Grid dehazing Network (GridNet) for single image dehazing. Li et al. [40] proposed a level-aware progressive network for single image dehazing, which can progressively learn the gradually aggravating haze. Deng et al. [41] presented a multi-model fusing network for boosting the single-image dehazing. Qu et al. [42] designed an enhanced pix2pix dehazing network (EPDN) to generate clear results. Li et al. [43] restored haze-free image based on a conditional generative adversarial network (cGAN). Chen et al. [44] proposed an end-to-end gated context aggregation network for visibility restoration from a single haze image. Dudhane et al. [46] proposed a varicolored end-to-end image de-hazing network to recover a haze-free image from a given varicolored hazy image. Li et al. [47] proposed a task-oriented network for image dehazing, which involved a hybrid network containing an encoder and decoder network and a spatially variant recurrent neural network motivated by the image formation of haze process.

<!-- src: S021 -->
In this paper, we also propose a single image dehazing method. The main idea is to propose a confidence prior by freely controlling the removal degree of outliers or noises. Different from previous single image dehazing approaches, our method is built on a statistical analysis and a probability model of local patches. A Gaussian model is used to fit the probability distribution of each patch, and a learning method is adopted to adaptively learn a prior ratio by patch appearance.

## Methods

<!-- original heading: "The proposed algorithm" (S022) -->

<!-- src: S023; Eq. (1) normalized -->
According to the Mie scattering theory [48], McCartney proposed the atmospheric scattering physical model in the 1970s. The scattering theory models a hazy image I as a linear combination of an attenuation term I_att and an airlight one I_air: I = I_att + I_air (1)

<!-- src: S024; Eq. (2) normalized -->
The attenuation term describes the decay of scene radiance. Only a part of light reflected from the scene reaches the camera, and other part of light changes its direction several times by particles in the atmosphere. The attenuation is exponentially related to the distance between the object and the camera: I_att(x) = J(x) e^(−βd(x)) (2), where d(x) is the depth from the camera to the scene object for pixel x, β is a scattering coefficient, and J(x) denotes the intensity of the reflected light.

<!-- src: S025; Eq. (3) normalized -->
The airlight term I_air is described by an airlight model, as shown in Fig. 1. The scene light propagates in straight lines, but the light direction may be changed several times because of aerosols in the atmosphere. A part of the airlight finally reaches the imaging equipment, and this reached light is often considered as the fog component of the image. The airlight model is formulated as follows: I_air(x) = A(1 − e^(−βd(x))) (3)

<!-- src: S026; Eq. (4) normalized -->
where A is a 3D vector of RGB values denoting the global atmospheric light. Further assuming that the atmosphere is homogenous, we can define a scene transmission t(x) as: t(x) = e^(−βd(x)) (4)

<!-- src: S027 + S028 (merged; equations (5)–(8) normalized, Eq. (8) partially garbled in text layer) -->
Combining Eq. (2), Eq. (3) and Eq. (4), the atmospheric scattering model can be rewritten as: I(x) = J(x)t(x) + A(1 − t(x)) (5). According to Eq. (5), the key to obtain a clear image is to estimate the transmission t(x) and the global atmospheric light A from a single input hazy image I(x). The global atmospheric light is often assumed as a known global constant and it is independent of spatial coordinates. If we get the airlight term I_air, the transmission for each channel is computed by: t(x) = 1 − I^c_air(x)/A^c (6), where c denotes one channel of RGB colors. So RGB images have three transmissions. To obtain only one transmission from RGB images, a channel-wise minimization operation on a hazy image I(x) is usually used to produce a channel-minimized image I^m1(x): I^m1(x) = min_{c∈{r,g,b}}(I^c(x)) (7), where I^c is a channel c of I(x). We adopt Eq. (7) to rewrite Eq. (6) to obtain a unique transmission for pixel x: t(x) = 1 − I^m1_air(x)/A^m1 (8) [Eq. (8) reconstructed from garbled text layer; see PDF].

<!-- src: S029 -->
The above equation is usually unstable and sensitive to noises since it considers only one pixel. This problem is usually solved by performing the minimization operation again over a local region.

### The overall flowchart of our method

<!-- original heading: "The overall flowchart of our method" (S030) -->

<!-- src: C002 (body prose mislabeled as caption in reader; restored to body) -->
Fig. 2 shows the overall flowchart of our method consisting of learning and dehazing stages. In the learning stage, we compute the mean and deviation of channel-minimized pixel values in a patch to represent the appearance of the patch, and then learn the relationship between patch appearance and confidence ratios for adaptive removal of outliers or noises. In the dehazing stage, we use the learned model to infer a confidence ratio for each pixel, then smooth confidence ratios with a kernel to remove noise, and finally we use the ratio to adaptively estimate a transmission map for computing a dehazed image. For the sake of simplicity, we use a linear regression for learning in our implementation. Other linear or nonlinear models can be used to learn a mapping function between appearance features and confidence ratios.

### A unified framework of existing priors

<!-- original heading: "A unified framework of existing priors" (S031) -->

<!-- src: S032; restored missing sentence-final period -->
The transmission estimation is a highly ill-posed problem since the number of unknowns is more than the number of equations. There are many dehazing priors based on channel-minimized values to solve the ill-posed problem. We use Eq. (7) to obtain a channel-minimized version I^m1 from a hazy image I, and then sort pixel values in a local patch Ωi of I^m1 in ascending order. We discover that several existing priors can be unified under a framework of sorted channel-minimized values, as shown in Fig. 3.

#### The dark channel prior under the framework

<!-- original heading: "The dark channel prior under the framework" (S033) -->

<!-- src: S034 + S035; Eq. (9) garbled in text layer, flagged -->
In Fig. 3, a diamond point a stands for the minimum value I^m1_a of pixels in Ωi, which is just the dark channel prior (DCP) proposed by He et al. [5], defined as: [Eq. (9) garbled in extraction: I^m1_a = min_{x∈Ωi}(I^m1(x)) = min_{x∈Ωi}(min_{c∈{r,g,b}}(I^c(x))); see PDF].

<!-- src: C004 (body prose mislabeled as caption) + S036 (merged across column break; "channelminimized" line-break artifact fixed) -->
Fig. 4(a) and (b) are an input image I and its channel-minimized version I^m1, respectively. Fig. 4(c) and Fig. 4(i) show the dark channel prior I^m1_a and corresponding dehazed image, respectively. The dehazed image by DCP [5] has block artifacts on object boundaries, and halo artifacts in the sky region. The minimal value of I^m1 is not suitable for depth discontinuity and bright regions.

#### The filtering prior under the framework

<!-- original heading: "The filtering prior under the framework" (S037) -->

<!-- src: S038 + S039 + S040 (merged across caption interruption C005; duplicated column-break word "The" removed; Eqs. (10)–(11) garbled in text layer, flagged) -->
The value of the sorted curve at point c, denoted as a triangle, is the filtering prior (FP) proposed by Tarel and Hautiere [6]. The value I^m1_c at the triangular point c is computed by: [Eq. (10) garbled in extraction: I^m1_c = m − median_{x∈Ωi}(|I^m1(x) − m|); see PDF] where m stands for the median of I^m1 in Ωi that is the value at a circular point f, defined as: [Eq. (11) garbled in extraction: m = I^m1_f = median_{x∈Ωi}(I^m1(x)); see PDF]. Tarel and Hautiere [6] viewed image dehazing as a filtering problem, and then proposed a prior I^m1_c by using a "median of median" filter, formulated by Eq. (10) and Eq. (11). Fig. 4(d) and (j) show the prior image I^m1_c and its corresponding dehazed image [6], respectively. The "median of median" filter can greatly reduce halo artifacts, but the median of I^m1 in a patch lacks statistical basis and it cannot accurately estimate scene depths. Dehazed images by [6] also suffer from color distortion and are not visually satisfying due to lack of depths. Comparing Fig. 4(a) with Fig. 4(j), we find that the haze was not effectively removed.

#### The color ellipsoid prior under the framework

<!-- original heading: "The color ellipsoid prior under the framework" (S041) -->

<!-- src: S042 + S043 + S044 (merged; Eqs. (12), (14) garbled in text layer, flagged; Eq. (13) readable) -->
As shown in Fig. 3, we use a point e marked as a rectangle to hold the mean of values I^m1 in a local patch Ωi, defined as: [Eq. (12) garbled in extraction: μi = I^m1_e = mean_{x∈Ωi}(I^m1(x)) = (1/|Ωi|) Σ_{x∈Ωi} I^m1(x); see PDF] where |Ωi| denotes the pixel number of the local patch Ωi. The value I^m1_d at point d, denoted by an ellipse, is actually the color ellipsoid prior (CEP) proposed by Bui and Kim [4], defined as: I^m1_d = μi − σi (13) [Eq. (14), the definition of σi, garbled in extraction; see PDF].

<!-- src: S045 -->
Under the proposed framework, the Color Ellipsoid Prior (CEP) [4] is actually the difference between the mean μi and the deviation σi of channel-minimized values in a patch. Fig. 4(e) and (k) show the color ellipsoid prior and its corresponding recovered image, respectively. The color ellipsoid prior, defined as μi − σi, actually makes only 68.3% of pixel values in a range of [μi − σi, μi + σi]. In other words, the half of 31.7% pixel values, i.e. 15.85%, make contributions to the location of the prior.

<!-- src: S046 + S047 (merged across p4→p5 page break; dangling "The value" joined) -->
We observe the above-mentioned priors from a point view of statistical histograms. Fig. 5 shows the histogram of I^m1 in a patch Ωi in Fig. 3. The horizontal axis denotes pixel values, while the vertical axis shows the frequency of corresponding pixel values. The abscissa value of I^m1_a is the dark channel prior by He et al. [5]. I^m1_a is the minimum value of I^m1 in Ωi. However, I^m1_a is possibly the value of an outlier that is rarely correlated to the majority of pixel values, and an outlier leads to an inaccurate estimation. The value of I^m1_e denotes the median value of I^m1 in the patch. I^m1_e is embedded in the prior proposed by Tarel and Hautiere [6] to estimate the airlight. The estimated airlight is just the abscissa value of I^m1_c. The prior I^m1_c seems statistically robust in the view of random variables due to the difference of two median filtering results (Eq. 10). However, the prior lacks intuitionistic explanation, and it also fails in some hazy images. Bui and Kim [4] proposed the prior I^m1_d by fitting the channel-minimized values I^m1 in a patch to a unit ellipsoid. The prior can reduce noises, but it is actually obtained by a fixed confidence ratio for every pixel according to our unified framework. Hence, it does not adapt to patches with different distributions.

### The proposed confidence prior

<!-- original heading: "The proposed confidence prior" (glued to body in S048; unglued) -->

<!-- src: S048 -->
To obtain more reliable estimation of transmission maps, we fit the histogram of I^m1 by a normal distribution to easily remove outliers or noises. Fig. 5 shows a dashed curve standing for a Gaussian distribution, which is used to statistically approximate the distribution of channel-minimized values. Each channel-minimized value I^m1(y) at y in Ωi is regarded as a random variable with a Gaussian distribution:

<!-- src: S049 + S050 (Eq. (15) readable, Eq. (16) garbled, flagged) -->
I^m1(y) ∼ N(μi, σ²i) (15). The mean μi is a positional parameter describing the center of the normal distribution, while the deviation σi measures the dispersion degree of data distribution. The probability density of v = I^m1(y) in Ωi can be fitted by a Gaussian function: [Eq. (16), Gaussian density f(v; μi, σi), garbled in extraction; see PDF]. To remove outliers or noises, we propose a novel prior based on the confidence of Gaussian distributions for improving robustness.

<!-- src: S051 + S052 (merged; Eq. (17) readable; "channelminimized" line-break artifacts fixed) -->
According to the unified framework as shown in Fig. 3, we propose a confidence prior I^m1_b, defined as: I^m1_b(i) = μi − λσi (17), where λ is a ratio parameter that adjusts confidence degrees. For example, if λ is set to 1, we have the confidence of 68.3% channel-minimized values that are in the range [μi − σi, μi + σi]. In fact, the color ellipsoid prior is equal to our confidence prior with λ equal to 1, as shown in Fig. 4(e). If λ is set to 2 and 3, channel-minimized values with the confidences of 95.4% and 99.7% are in the ranges [μi − 2σi, μi + 2σi] and [μi − 3σi, μi + 3σi], respectively. Increasing the confidence ratio λ magnifies the risk of introducing outliers and noises into the confidence prior. Fig. 4(e), (f) and (g) show our prior results by three different confidence ratios, and Fig. 4(k), (l) and (m) illustrate corresponding dehazed images for these priors. As we can see, a larger ratio λ generates smaller priors, and preserves more details. Corresponding dehazed images by smaller prior values are more similar to the original image.

<!-- src: C009 (body prose mislabeled as caption; restored to body) -->
Fig. 6(a) and (b) show the histograms of I^m1 for real world images in Fig. 6(c) and (d), respectively. Pixel values in most patches approximately satisfy Gaussian distributions. In addition, the distribution of I^m1 can be more accurately fitted by Gaussian mixture models (GMM), but computations are also more complicated. Therefore, we just use one Gaussian function to fit the histogram of I^m1. Fig. 6(e) and (f) show the histograms of two nearby blocks. Even if the two blocks are near to each other in the same image, they also have totally different histograms. As shown in Fig. 6(g) and (h), the two patches denoted by two rectangles contain the sky and tree branches.

<!-- src: S053 -->
Unlike the above-mentioned priors, we use a confidence ratio λ to statistically control the removal degree of outliers to obtain a more reliable prior I^m1_b. The position of I^m1_b is determined by λ. We can empirically specify a range for the ratio λ. As shown in Fig. 5, our confidence prior I^m1_b is within the prior range specified by λ = 1 and λ = 2. We can select a ratio λ to achieve an appropriate confidence prior for all local patches. In the case of Fig. 5, we specify the confidence prior I^m1_b by setting λ to 1.8. The ratio λ should not be set to the same value, since different patches may have different distribution of pixel values. Therefore, we propose to use a learning method, such as linear regression, logistic regression and neural networks, to adaptively estimate a confidence ratio λi for each patch centered at pixel i. So, we rewrite Eq. (17) as:

<!-- src: S054 + S055 (Eqs. (18)–(19) readable) -->
I^m1_b(i) = μi − λi·σi (18). To compensate the fitting errors by one Gaussian, a constant p (0 < p < 1) is introduced into Eq. (18). Hence, Eq. (18) can be expressed as: I^m1_b(i) = p(μi − λi·σi) (19). The above modification allows us to adaptively preserve a small amount of haze for distant objects to reduce the loss of depths brought by human perception. Fig. 7 shows the haze removal results with different parameters p. A smaller p leads to a result with more remained haze, and corresponding dehazed image is clearer for a larger p. The main reason is that the parameter p be responsible for enhancing the perceptual depth.

### Adaptive estimation of confidence ratios

<!-- original heading: "Adaptive estimation of confidence ratios" (S056) -->

<!-- src: S057 + S058 (Eq. (20) garbled in text layer, flagged) -->
An appearance feature vector v̂i extracted from a patch Ωi is closely related to the confidence ratio λi for the patch Ωi. For the sake of simplicity, we use a linear regression to fit the relationship between λi and v̂i, formulated as: [Eq. (20) garbled in extraction: λi = f(v̂i) = v̂iᵀw + b, with expanded component form; see PDF] where v_ij denotes the value I^m1 of the jth pixel in the ith patch, D represents the number of pixels in the ith patch, w_j is a weight for v_ij, and b is a bias coefficient.

<!-- src: S059 + S060 (Eqs. (21)–(23) partially garbled, flagged) -->
To simplify notations, we use an augmented feature vector v_i = [v_i1 v_i2 … v_ij … v_iD 1]ᵀ and an augmented weight vector w = [w_1 w_2 … w_j … w_D b]ᵀ, so the linear regression can be rewritten as: λi = f(v̂i) = f(v_i) = v_iᵀw (21). We aggregate all appearance feature vectors from each patch of all images in a training dataset into a matrix, denoted as: V = [v_1 v_2 … v_i … v_K] (22), where K stands for the total number of patches for all images in the training dataset. To facilitate computation, the linear regression problem can be further expressed as below: f(V) = Vᵀw (23)

<!-- src: S061 -->
To learn the augmented weight vector w, we need a training dataset containing haze-free images, corresponding hazy images and transmission maps. It is very difficult to acquire these images, so we randomly selected 20 clean images and corresponding depth maps from the NYU Depth dataset [49] to generate synthesized training samples. We used the physical model of Eq. (5) to synthesize hazy images. We used a random atmospheric light A = {k, k, k} where k ∈ [0.7, 0.99], and a random scattering coefficient β ∈ [0.1, 0.5] for synthesizing hazy images.

<!-- src: S062 + S063 (Eq. (24) readable; Eq. (25) garbled, flagged) -->
Each training sample has a ground truth transmission t_i for pixel i. Combining Eqs. (8) and (19), we have the following equation for pixel i: t_i = 1 − p·(μi − λi·σi)/A^m1 (24), where A^m1 is the minimized channel of A. The ground truth t_i is known for a training image I, so we solve the above equation to obtain a confidence ratio λi for each pixel of the training image I: [Eq. (25) garbled in extraction: λi = μi/σi − (1 − t_i)·A^m1/(p·σi); see PDF]. From all patches on images of the training dataset, we use Eq. (25) to compute K confidence ratios λG = [λ1 λ2 … λK]ᵀ. Then we minimize the error between the ground truth ratio vector and the estimated ratio vector by the regression function (Eq. 23) with input appearance vectors V = [v_1 v_2 … v_K]. The Mean Squared Error (MSE) loss function l(w) is often used to measure the error:

<!-- src: S064 + S065 (Eqs. (26)–(29) garbled/reordered in text layer, flagged; "0.0 0 01" spacing artifact fixed) -->
[Eq. (26) garbled in extraction: l(w) = ‖λG − Vᵀw‖²₂ = (λG − Vᵀw)ᵀ(λG − Vᵀw); see PDF]. Our goal in this paper is to find an optimized weight vector w to minimize the loss function l(w): [Eq. (27) garbled in extraction: w = argmin_w (λG − Vᵀw)ᵀ(λG − Vᵀw); see PDF]. To solve the problem, we calculate the partial derivatives of l(w) with respect to w and make them to be equal to zero: ∂l(w)/∂w = −2V(λG − Vᵀw) = 0 (28). Solving Eq. (28), we can obtain w as: w = (V·Vᵀ + qE)⁻¹·V·λG (29), where q is a small positive value (typically 0.0001) to avoid division by zero, and E is an identity matrix. The learning framework of weights w is shown in Fig. 8. Once the regression weight vector w is learned, we can easily predict λi for any appearance vector w_i using Eq. (21).

<!-- src: S066 (Eq. (30) readable) -->
Several methods introduce a filter to preserve details and smooth images simultaneously. To process patches with abrupt depth jumps, we use a kernel to smooth predicted ratios. If the intensity of a pixel i is bigger than the average intensity of pixels in a patch centered at pixel i, λi will be prone to be a negative number, while confidence ratios tend to be large for pixels in smooth areas. Before convolving a filter with a map λ, we need to restrict each ratio λi to a range defined by a lower bound γ1 and an upper bound γ2, formulated as: λi = G ⊛ min(max(λi, γ1), γ2) (30), where ⊛ stands for a convolution operator, and G is a kernel. We choose the Gaussian kernel for smoothing. For every input image, the weight and size of kernel are the same. In our implementation, γ1 and γ2 are set to 0 and 3, respectively. The confidence ratio map λ becomes smooth after filtering by Eq. (30). In this way, we can significantly reduce halo phenomenon in final dehazed images.

<!-- src: S067 + S068 + S069 + S070 (merged across p6→p7 page break; Eqs. (31)–(32) readable) -->
According to the physical property of Eq. (1), we can derive that I^m1_air is subject to the following constraint: 0 < I^m1_air(i) = I^m1(i) − I^m1_att(i) < I^m1(i) (31). Therefore, I^m1_air should be positive and cannot be higher than the channel-minimized value I^m1. Combining Eqs. (19) and (31), we can estimate the final airlight I_air by: I^m1_air(i) = max(min(p(μi − λi·σi), I^m1(i)), 0) (32). The atmospheric light A can be directly estimated from hazy images, and then the transmission map can be obtained using Eq. (8).

<!-- src: C011 (body prose mislabeled as caption; restored to body) -->
Fig. 4(h) shows I^m1_air by our method with learned ratio λ, which is different from the results by our method with fixed ratios λ, as shown in Fig. 4(e), (f) and (g). Our prior with learned ratios preserves more details in regions with abrupt depths. Our prior is a little similar to He et al. [5]'s prior for such patches with small variance. In addition, Bui and Kim [4]'s prior is a special case of our method with λ = 1.

### Atmospheric light estimation

<!-- original heading: "Atmospheric light estimation" (glued to body in S071; unglued) -->

<!-- src: S071 (Eq. (33) readable) -->
In most dehazing algorithms, the atmospheric light A is considered as a global constant and obtained by the intensity of the most haze-opaque region. The atmospheric light A contains the diffuse reflections of the sky, sunlight and reflected light from the ground, as shown in Fig. 1. The atmospheric light by the most haze-opaque region is not always correct when the sunlight and other lights reflected by the ground cannot be ignored. According to Eq. (3), if a scene point is very far away from the camera, the depth d becomes very large, leading to a zero transmission t. In this case, the airlight I_air of pixels with a very large depth (d → ∞) can be regarded as the value of A: A = I_air(x) for d(x) → ∞ (33)

<!-- src: S072 -->
In addition, the intensity I(x) of a pixel with an infinity depth is equal to the airlight value I_air(x) of the pixel since t(x) = 0, i.e. I_air(x) = I(x).

<!-- src: S073 -->
Eq. (33) shows a simple way to estimate the atmospheric airlight A. In some cases, images do not contain very distant objects in practice, and the sunlight in different weathers and the light reflected by the ground cannot be ignored. Since white objects reflect all colors of lights, we can use the color of pixels in both white objects and haze-opaque regions to estimate the atmospheric airlight A. He et al. [5] selected a part of bright pixels in the dark channel as the airlight. In this paper, we select the top 0.1% brightest pixels in the channel-minimized map I^m1, then we regard the average color of these pixels as the atmospheric light A. Pixels marked in red color points provide a good approximation of A, as shown in Fig. 9(a) and (c).

### Haze removal

<!-- original heading: "Haze removal" (glued to body in S074; unglued) -->

<!-- src: S074 + S075 (merged across caption interruption; Eqs. (34)–(35) partially garbled, flagged) -->
Once the airlight term I^m1_air and the atmospheric light A are obtained, we can directly compute the transmission map t according to Eq. (8), and then adopt Eq. (5) to recover the scene radiance. To avoid noisy results by transmissions near to zero, we introduce a lower bound t1 to restrict the value of t(x), and then recover the scene radiance J(x), formulated as: t(x) = 1 − max(min(p(μi − λi·σi), I^m1(i)), 0)/A^m1 (34); J(x) = (I(x) − A)/max(t(x), t1) + A (35) [Eqs. (34)–(35) reconstructed from garbled text layer; see PDF].

<!-- src: S076 -->
We set t1 to 0.1 for all images in our implementation. Fig. 4(n) shows the dehazed result by our method with learned confidence ratios. Observing the dehazed images in Fig. 4, we can conclude that our method can remove haze and is robust to noises and outliers.

## Results

<!-- original heading: "Experiments" (S077) -->

<!-- src: S078 -->
To evaluate the performance of dehazing methods, we compared our method with recent state-of-the-art methods. The datasets for comparisons include both natural and synthetic images. We conducted qualitative assessments on synthetic and natural images. In addition, we performed quantitative evaluations on synthetic images. We compared our method with prior-based approaches that are DCP [5], CAP [26], DHL [27], PDN [28] and DDIP [29], and also with data-driven methods including OTSFDE [22], AODN [32], LPQC [36], GFN [34], cGAN [43], GCA [44], GridNet [39], EPDN [42] and MSBDN [51]. Note that PDN [28], DDIP [29], AODN [32], LPQC [36], GFN [34], cGAN [43], GCA [44], GridNet [39], EPDN [42] and MSBDN [51] are CNN-based methods. In our implementation, we set p to 0.85, and used local patches with a fixed size of 3 × 3 around each pixel. Local patches are used for computation of channel-minimized values and appearance vectors. In this paper, all results by our method share the same parameters.

### Comparisons on natual images

<!-- original heading: "Comparisons on natual images" (glued to body in S079; unglued; "natual" preserved as printed — suspected source typo) -->

<!-- src: S079 -->
We compared our method with fourteen excellent algorithms. Since these methods achieved good visibility of restoration on general outdoor images, we compared them with our method on challenging natural images [50] containing rich details, bright, and sky scenes. Fig. 10 shows the outcomes of 'animal', 'architecture', 'human', 'landscape' and 'plant' images by different dehazing methods.

<!-- src: S080 -->
DCP [5] produced clear and natural restored images. However, there still exist severe color distortions in bright regions. This is because the dark channel prior takes outliers into account and causes an over-estimation of transmission. In addition, DCP [5] is invalid in bright regions, such as sky, leading to color distortion, as shown in the sky of the 'plant' image in Fig. 10(b). Besides, the choice of the atmospheric light by DCP [5] has its own limitations, such as ignoring the influence of sunlight, and this method is prone to produce darker results.

<!-- src: S081 -->
To achieve the visibility recovery of hazy images, Zhu et al [26] proposed a powerful color attenuation prior (CAP) for depth estimation from a single input hazy image. As shown in Fig. 10(c), CAP maintains original colors, but it also retains a part of haze and loses textures in dark regions. However, CAP adopts a constant scattering coefficient β, leading to incorrect estimation of transmission.

<!-- src: C015 (body prose mislabeled as caption; restored to body) -->
Fig. 10(d) shows the results of DHL [27]. The 'haze-line' method proposed by Berman et al. [27] significantly reduces haze, but it also erodes and clips bright regions. The main reason is that the 'haze-line' prior cannot perfectly model the formation of haze in bright regions. This causes the results to be over-saturated in distant objects, such as the 'human' and the 'building' regions in Fig. 10(d). Obviously, there are oversaturations and color distortions in distant regions of these images.

<!-- src: C016 (body prose mislabeled as caption; restored to body) -->
Fig. 10(e) shows the dehazed results of OTSFDE [22] proposed by Ling et al. [22]. They first evaluated the fog density of a hazy image via a linear combination of three haze features, then modeled a physics-based mathematical relationship between transmission and fog density. However, as shown in Fig. 10, the method generates significantly over-enhanced images, and it is more prone to produce color distortion than other methods especially in 'animal' and 'human' regions.

<!-- src: S082; "hazefree" line-break artifact fixed -->
Li et al. [32] proposed a method based on CNNs by building a re-formulated atmospheric scattering model to obtain the haze-free image from hazy images directly. This method avoids estimating the transmission map and improves the object detection performance on hazy images. However, color distortion also exists in the face of the woman and haze remains in distant regions, as shown in Fig. 10(f).

<!-- src: S083 -->
Santra et al. [36] trained a CNN-based comparator (LPQC) and then adopted it to directly find the ideal transmission map for haze removal. As shown in Fig. 10(g), the method achieved good results for most hazy images. But like most deep learning based methods, the results remain some haze. This is because the transmission map is obtained by binary search rather than physically modeling of haze formulation.

<!-- src: S084 -->
PDN [28] uses CNNs to learn both dark channel and transmission priors for single image dehazing. The method can significantly remove hazes from images and restore high color contrasts. However, as shown in the sky region of the 'architecture' image in Fig. 10(h), PDN [28] cannot properly deal with sky regions and is prone to introduce artifacts.

<!-- src: S085 -->
GFN [34] is a deep learning network (Dehaze-net) using synthetic data for training. The approach achieves outstanding dehazing performance due to investigating haze relevant features. It cannot enhance the detail and visibility of images well, because it uses synthetic image patches for training. As shown in Fig. 10(i), the results still remain some fog.

<!-- src: S086 + S087 (merged across p9→p10 page break; dangling "Fig. 10 (k) shows" joined) -->
DDIP [29] treats the dehazing problem as a layer-separation problem, and uses a coupled 'deep image prior' network for haze removal. Fig. 10(j) shows restored images by DDIP. However, like the PDN [28], it also tends to produce exaggerated sky regions. Besides, DDIP [29] also produces over-enhancements and artifacts. cGAN [43] adopts a conditional generative adversarial network to directly estimate clear images from hazy images. Fig. 10(k) shows the dehazed results of cGAN [43]. Although cGAN [43] is able to reserve structural details of objects, it also has limitations to handle a dense haze scene, resulting in that the outputs are still hazy and dark. In addition, color shift also occurs in the sky region of the last image.

<!-- src: S088 -->
To avoid gridding artifacts, Chen et al. [44] used a smoothed dilated technique to propose a Gated Context Aggregation Network (GCA) for dehazing and deraining, which utilizes a gated subnetwork to fuse the features of different levels. As shown in Fig. 10, GCA [44] avoids the over-enhancement problem to some extent. However, haze residue and color distortion still exist in the dehazed results, as shown in the second image of Fig. 10(l).

<!-- src: S089; "attentionbased", "postprocessing" line-break artifacts fixed -->
GridNet [39] consists of pre-processing, backbone, and post-processing modules. The backbone one implements attention-based multi-scale estimation on a grid network, which allows efficient information exchange across different scales. As shown in Fig. 10, GridNet [39] succeeds in suppressing the halo artifacts to a certain extent.

<!-- src: S090 -->
EPDN [42] transforms the problem of image dehazing to the problem of image-to-image translation, and embeds a GAN in its architecture, which is followed by two well-designed enhancing blocks. As shown in Fig. 10, EPDN can remove haze effectively in heavily hazy scenes, while the method tends to cause severe color distortions (see the animal and the sky in Fig. 10(n)).

<!-- src: S091 -->
Dong et al. [51] proposed a multi-scale boosted dehazing network (MSBDN) with dense feature fusion based on the U-Net architecture. MSBDN adopts the principle of boosting and error feedback, so it can preserve structural details of the objects, as shown in Fig. 10(o).

<!-- src: S092 -->
As shown in Fig. 10(p), our method removed more haze and preserved clearer scenes than other methods. Our results are similar to those produced by LPQC [36] and MSBDN [51], but slightly more natural in sky regions as exhibited in the 'animal' image. The reason why our method can achieve more natural results is that our confidence prior can suppress outliers or noises.

<!-- src: S093 -->
To further demonstrate the effectiveness of our method, we also randomly selected 30 daytime images and 30 night images from the Real-world Task-driven Testing Set (RTTS) of RESIDEβ for comparisons. Figs. 11 and 12 show the comparison results. The selected daytime images have dense haze, which are challenging to remove. The hazy images are given in Fig. 11(a). DDIP still suffers severe color shift as shown in the red rectangle of Fig. 11(j), and the details of dehazed images by DDIP are still blurry. DHL and OTSFDE can increase visual visibility, but they cannot produce color-balanced results as illustrated in Fig. 11(d) and (e). Fig. 11(m) and (n) show the results by two variants of our method. The two variants have the same parameters but with different p. Obviously, as p gets larger, the dehazed image becomes clearer. However, artifacts are easily introduced in recovered results. From the Eq. (34), we can conclude that decreasing the constant p makes the value of transmission to be close to 1. Larger transmission causes J(x) ≈ I(x) − A + A. It means that the influence of the atmospheric light is weakened on the restored image. This is the main reason that using a lower p is able to obtain smoother images. On the contrary, increasing p makes the value of transmission close to 0, but a lower transmission for recovering haze-free images magnifies the global atmospheric light and introduces halo artifacts. The dehazed night image in Fig. 11(e) denotes that OTSFDE is not robust to night environment.

<!-- src: S094 -->
We also used the average fog density [20] as a quantitative image quality metric for realistic haze images. Table 1 shows the average fog densities of dehazed results. Our method surpasses the fourteen State-of-the-Art methods in terms of fog density. For night hazy images, our method also defeats most of them.

### Comparisons on synthetic images

<!-- original heading: "Comparisons on synthetic images" (glued to body in S095; unglued) -->

<!-- src: S095; "state-of-theart" and "Dhazy" line-break artifacts fixed; block ends mid-sentence ("…RESIDE/IN and RESIDE/OUT are from"), continuation (description of RESIDE subsets and the seventh dataset hazeRD) lost in extraction -->
In order to evaluate the performance of the proposed method, we compared our results with the results by several state-of-the-art methods on synthetic hazy images with ground truth images. These synthetic images include seven datasets. The first and second dataset are 30 indoor images (I-HAZE dataset [52]) from the NTIRE2018 dehazing challenge [53] denoted as NTIRE/IN, 45 outdoor images (O-HAZE dataset) from NTIRE2018 as NTIRE/OUT. The third dataset including 23 images of the D-Hazy dataset. The D-hazy [54] dataset is synthesized from Middlebury [55] and NYU dataset [49]. The images for comparisons in this paper are synthesized from Middlebury. The fourth dataset is 66 images from Foggy Road Image Database (FRIDA) [56]. The FRIDA dataset consists of FRIDA and FRIDA2. The images used for comparisons are uniform fog (U080) of FRIDA2. We also used the recent large-scale RESIDE (REalistic Single Image DEhazing) dataset for comparisons. The fifth and sixth datasets denoted as RESIDE/IN and RESIDE/OUT are from [continuation lost in extraction — see PDF].

<!-- src: C027 (body prose mislabeled as caption) + S096 (merged across p12→p13 page break; hyphenated "im-/age" joined); "halo aircrafts" preserved as printed — suspected source typo -->
Fig. 13 shows the results of DHL [27], OTSFDE [22], DDIP [29], GridNet [39], MSBDN [51] and our method. DDIP [29]'s results have the color shift problem and the over-saturation problem. DHL [27] is prone to produce halo aircrafts, as shown in the bright region of the first row of Fig. 13(b). OTSFDE [22] leads to bad results on edges and severe color distortion. As we can see from Fig. 13(c), OTSFDE [22]'s results are quite different from the ground truth images. As shown in Fig. 13(f), our results are a little similar to MSBDN [51]'s results, but our method removes more haze than MSBDN [51], such as distant regions in the fourth image. As shown in the fifth and sixth rows of Fig. 13(e), Dehazed images by GridNet [39] are most similar to corresponding ground truths on the datasets of RESIDE/IN and RESIDE/OUT, but there are artifacts and obviously remained haze in dehazed images for other datasets. Our confidence prior has better generalization performance on most of the test datasets.

<!-- src: S097 + S098 (merged; Table-2 header debris "DCP CAP DHL … Ours" removed from end of S097) -->
Then, we quantitatively assess our confidence prior. The indicators for evaluation are the average peak signal-to-noise ratio (PSNR) and the structural similarity (SSIM). PSNR and SSIM are widely used in image objective evaluation. Higher PSNR and SSIM usually means better quality, but it is based on the pixel-wise error between dehazed image and corresponding ground truth. In some cases, it is inconsistent with human perceptional quality assessment. Table 2 shows comparisons of average PSNRs. Our method achieves very good PSNR results. Our method cheeringly ranks in the first position for hazeRD, and it has the best performance of haze removal in term of the SSIM metric on the hazeRD dataset. Although our method is not the best one on other datasets, our method outperforms most methods, and average PSNRs and SSIMs of our method are very similar to the best results. It is worth mentioning that our method exceeds almost all traditional methods on the seven datasets. In addition, our method even outperforms most of deep learning dehazing methods.

<!-- src: S099 + S100 (merged across column break; "CIEDE20 0 0" spacing artifact fixed) -->
To further validate the superiority of our method, we used CIEDE2000 [57], Universal Quality Index (UQI) [58] and Learned Perceptual Image Patch Similarity (LPIPS) [59] as dehazed performance metrics. Smaller CIEDE2000 and LPIPS mean better dehazed performance, while a larger UQI means a better result. The comparison results are listed in Tables 3–5. Our method achieved the highest UQI on the D-HAZY, and FRIDA datasets. Our method has the best performance in the LPIPS metric on the HAZERD, D-HAZY and FRIDA datasets.

<!-- src: S101 -->
We used the same comparison methods on noisy hazy images to demonstrate dehazing sensitivity to noises. Fig. 19 shows the report of average PSNRs obtained by the fourteen methods as the sensitivity indicator. LPQC [36] fails in dealing with heavy noisy images due to its specific mechanism of estimating transmission. Our method almost yields the best results among traditional methods (DCP [5], CAP [26], HLD, OTSFDE [22]) for all datasets with different-level noises. Although we do not achieve the best results among the seven CNN-based methods, we obtain high PSNR values that are very near to the best values. According to the quantitative comparisons on noisy images, we find that our results are very similar to the ground truths and have less noises than those of many methods. This indicates that our method is more robust to noises.

## Discussion

<!-- No standalone Discussion heading in the source; discussion-type content was merged into the ends of Experiments (S102) and Conclusions (S105). Split out here per canonical scheme. -->

<!-- src: S102 (final paragraph of Experiments in source) -->
Extensive experiments on both natural and synthetic images validate that our method achieves significantly better performance than state-of-the-art methods. In summary, our method significantly outperforms most of existing methods, including deep learning methods. However, our method needs to compute features of local patches, so it has high computational complexity. We can design efficient feature extraction algorithms or adopt GPUs to speed up our method in the future.

<!-- src: S105 (limitations paragraph inside Conclusions in source; Table-header debris "DCP CAP DHL … Ours" removed from end; final sentence truncated at "on night…" (likely "night hazy images") -->
Although our confidence prior achieves excellent results for haze removal, there are still some common problems to be solved. Firstly, the hyperparameter p in our method highly depends on experiences and is set to be constant in our implementation. A constant hyperparameter p is not suitable in inhomogeneous atmospheric conditions, since different image patches possess different feature distributions. Therefore, dehazing algorithms are prone to obtaining incorrect transmissions in some cases. Although the parameter selected by experiences can obtain outstanding dehazing effects, a more flexible method to estimate the hyperparameter p is highly desired. Secondly, the dehazed results by the proposed method still have much remaining haze and noise for dense haze images. Thirdly, although our method outperformed most existing methods, it did not obtain the best performance on night [sentence truncated in extraction; table-header debris removed].

## Conclusion

<!-- original heading: "Conclusions" (S103) -->

<!-- src: S104 -->
Due to tiny particles suspended in the air, images taken in outdoors usually have low contrast and poor visibility. To obtain clear images from hazy images, many image dehazing methods have been proposed in recent years. Existing methods usually assume some priors that hazy images have special properties. However, these priors are not always robust enough, and most of them often fail in some cases due to high brightness of some regions, outliers or noises. To better understand these priors, we first generate a curve of sorted channel-minimized values computed in a local patch, and then put the values of several well-known priors on the curve to propose a framework for unifying them. Then we propose a novel prior under the framework by specifying a ratio, which is used to adjust the confidence degree of channel-minimized values in local patches. Thus we can freely remove the influence degree of outliers or noises. In addition, we adopt a regression method to adaptively learn the relationship between patch appearance and confidence ratios for all pixels. Thus, we can solve the problem on heterogeneity of pixel values and abrupt jumps of scene depths in hazy images. To further improve robustness of the estimated confidence ratios, we use a kernel for smoothing. We conducted very extensive experiments on both natural and synthetic images. Experimental results also show that our method achieves significantly better performance than existing state-of-the-art methods. In addition, we can adjust the ratios to control the removal degree of outliers or noises. In this way, we make a good balance between dehazing quality and noise suppression.

## Acknowledgments

<!-- original heading: "Acknowledgments" (S107) -->

<!-- src: S108 -->
This work was partially supported by the National Natural Science Foundation of China (61862029, 62062038), the Natural Science Foundation of Jiangxi Province (20192BAB207011), and Science Technology Application Project of Jiangxi Province (GJJ190279).

## References

<!-- original heading: "References" (S109). src: S110.
     Reader condensed the reference list; full entries NOT recoverable from the bilingual reader. Do not use this stub as reference-style evidence. -->

[References condensed by the bilingual reader: entries [1]–[60] appear in full only in the source PDF (Pattern Recognition 119 (2021) 108076). Key cited works include He et al. dark channel prior [5], Tarel filtering prior [6], Bui color ellipsoid prior [4], and recent learning-based dehazing methods [27]–[51].]

## Other

### Keywords

<!-- src: S006 -->
Keywords: Regression; Classification; Image dehazing; Confidence prior; Appearance feature

### Declaration of Competing Interest

<!-- original heading glued to body in S106; unglued -->
The authors declared that they have no conflicts of interest to this work. We declare that we do not have any commercial or associative interest that represents a conflict of interest in connection with the work submitted.

### Author biographies

<!-- src: S112–S116; OCR spacing "20 04" → "2004", "Xi ׳an" → "Xi'an" fixed -->
Feiniu Yuan received his B.Eng. and M.E. degrees in mechanical engineering from Hefei University of Technology, Hefei, China, in 1998 and 2001, respectively, and his Ph.D. degree in pattern recognition and intelligence system from University of Science and Technology of China (USTC), Hefei, in 2004. From 2004 to 2006, he worked as a post-doctoral researcher with State Key Lab of Fire Science, USTC. From 2010 to 2012, he was a Senior Research Fellow with Singapore Bioimaging Consortium, Agency for Science, Technology and Research, Singapore. From 2006 to 2018, he worked as a full professor with School of Information Technology, Jiangxi University of Finance and Economics. He is currently a full professor with College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, Shanghai 201418, China. His research interests include deep learning, image processing, pattern recognition, and 3D modeling. He is a Senior Member of IEEE and CCF.

Yu Zhou was born in 1994, and received the B.E. degree in software engineering from East China Jiaotong University, Nanchang, China, in 2016 and the M.E. degree in computer technology from Jiangxi University of Finance and Economics, Nanchang, China, in 2019. Her research interests include computer vision, image processing, and machine learning. Now, she is a PhD candidate with School of information science and engineering, East China University of Science & Technology, Shanghai, P.R.China

Xue Xia received the B.E. degree in Film & TV Arts and Technology and the M.E. degree in Communication and Information Engineering from the Shanghai University, Shanghai, in 2011 and 2014, respectively. She is currently a Ph.D. candidate with School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, China. Her research interests include 3D display technology, image processing and pattern recognition.

Xueming Qian received the B.S. and M.S. degrees in Xi'an University of Technology, Xi'an, China, in 1999 and 2004, respectively, and the Ph.D. degree in the School of Electronics and Information Engineering, Xi'an Jiaotong University, Xi'an, China, in 2008. From 1999 to 2001, he was an Assistant Engineer at Shannxi Daily. From 2008 to 2011, he was an assistant professor, from 2014 till now, he was an full professor of the School of Electronics and Information Engineering, Xi'an Jiaotong University. His research interests include Social mobile multimedia mining learning and search. He is the director of SMILES LAB. He has authored or co-authored over 70 papers in journals and conferences. His research is supported by Microsoft, NSFC, etc. He was awarded Microsoft fellowship in 2006. He was a visit scholar at Microsoft research Asia from Aug. 2010 to March 2011. He was TPC member of ICME, Multimedia Modeling, ICIMCS, and he is the session chairs/organizers of VIE08, ICME14, MMM14. He is a member of IEEE, ACM and Senior member of CCF.

Jian Huang is a Professor in the School of Management Science and Engineering at Nanjing University of Finance and Economics. He received his Ph.D. in Management Science and Engineering from Nanjing University in 2007. His current research focuses on information management, E-business, optimization and operations. He has published over 30 research papers in IIE Transactions, European Journal of Operational Research, Decision Sciences, Nonlinear Analysis: Theory, Methods & Applications, and others.

### Figure and table captions

<!-- src: C001, C003, C005–C008, C010, C012–C014, C017–C026, C028–C030; genuine captions only (body prose that had been mislabeled as captions was moved into Methods/Results above) -->
Fig. 1. The airlight model.
Fig. 2. The overall processing flowchart of our method.
Fig. 3. Prior points of different methods under the unified framework of sorted channel-minimized values in a local patch.
Fig. 4. Priors and corresponding dehazed images. (a) An input hazy image. Images of (b) minimized-channel values, (c) DCP [5], (d) FP [6], (e) CEP [4] that is actually our confidence prior with λ equal to 1, (f) our confidence prior with λ equal to 2, (g) our confidence prior with λ equal to 3, and (h) our confidence prior with learned λ. Dehazed images by (i) DCP [5], (j) FP [6], (k) CEP [4] equivalent to our method with λ equal to 1, (l) our method with λ equal to 2, (m) our method with λ equal to 3, and (n) our method with learned λ.
Fig. 5. The distribution analysis of priors in a local region.
Fig. 6. Histograms of I^m1 for whole images or local patches.
Fig. 7. Recovered images using different parameter p. (a) input image. (b) p = 0.75. (c) p = 0.85. (d) p = 0.95.
Fig. 8. Learning procedure of confidence ratios.
Fig. 9. Estimation of the atmospheric light. (a) Input image. (b) Channel-minimized values. (c) Dehazed image by our approach.
Fig. 10. Comparison results of haze removal methods on natural images. (a) Hazy images. Dehazed results of (b) DCP [5], (c) CAP [26], (d) DHL [27], (e) OTSFDE [22], (f) AODN [32], (g) LPQC [36], (h) PDN [28], (i) GFN [34], (j) DDIP [29], (k) cGAN [43], (l) GCA [44], (m) GridNet [39], (n) EPDN [42], (o) MSBDN [51], and (p) our method.
Fig. 11. Comparison results of haze removal methods on realistic dense haze images. (a) Hazy images. Dehazed results of (b) DCP [5], (c) CAP [26], (d) DHL [27], (e) OTSFDE [22], (f) AODN [32], (g) LPQC [36], (h) PDN [28], (i) GFN [34], (j) DDIP [29], (k) cGAN [43], (l) GCA [44], (m) our method with p = 0.85, and (n) our method with p = 0.95.
Fig. 12. Comparison results of haze removal methods on realistic night images. (a) Hazy images; dehazed results of (b) DCP [5], (c) CAP [26], (d) DHL [27], (e) OTSFDE [22], (f) AODN [32], (g) LPQC [36], (h) PDN [28], (i) GFN [34], (j) DDIP [29], (k) cGAN [43], (l) GCA [44], (m) our method with p = 0.85, and (n) our method with p = 0.95.
Fig. 13. Results of dehazing methods on synthetic images. (a) Synthetic hazy images. Results of (b) DHL [27], (c) OTSFDE [22], (d) DDIP [29], (e) GridNet [39], (f) MSBDN [51], (g) our method, and (h) Ground truth images.
Fig. 14. Comparison results of dehazing methods on noisy images. (a) Noisy images. Results of (b) DHL [27], (c) DDIP [29], (d) GridNet [39], (e) MSBDN [51], and (f) our method.
Fig. 15. Comparison results of dehazing methods on noisy images. (a) Noisy images. Results of (b) DHL [27], (c) DDIP [29], (d) GridNet [39], (e) MSBDN [51], and (f) our method.
Fig. 16. Comparison results of dehazing methods on noisy images. (a) Noisy images. Results of (b) DHL [27], (c) DDIP [29], (d) GridNet [39], (e) MSBDN [51], and (f) our method.
Fig. 17. Comparison results of dehazing methods on noisy images. (a) Noisy images. Results of (b) DHL [27], (c) DDIP [29], (d) GridNet [39], (e) MSBDN [51], and (f) our method.
Fig. 18. Comparison results of dehazing methods on noisy images. (a) Noisy images. Results of (b) DHL [27], (c) DDIP [29], (d) GridNet [39], (e) EPDN [42], and (f) our method.
Fig. 19. Sensitivity to different noises over synthetic images with ground truths. Comparisons (a) on Ntire/IN, (b) Ntire/OUT, (c) D-Hazy, (d) FRIDA, (e) RESIDE/IN, (f) RESIDE/OUT, and (g) hazeRD.
Table 1. Quantitative comparisons of average fog densities.
Table 3. Quantitative comparisons of average CIEDE2000s.
Table 4. Quantitative comparisons of average UQIs.
Table 5. Quantitative comparisons of average LPIPSs.
