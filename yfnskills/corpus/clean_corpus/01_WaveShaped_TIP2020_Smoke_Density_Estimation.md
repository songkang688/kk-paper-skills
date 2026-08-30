<!--
FnyPro-1 Stage 00 Wave 3 Agent G clean corpus
Paper_ID: 01_WaveShaped_TIP2020_Smoke_Density_Estimation
Source: /workspace/01_WaveShaped_TIP2020_Smoke_Density_Estimation.md (bilingual reader, **Original:** blocks only)
Content policy: English original text only. Excluded: all Chinese, reader navigation/glossary/reading notes,
running-header/venue line (S003), reference entries (S109-S111, reader-condensed, non-verbatim), and
author biographies (S112-S117, suspected reader condensation). Figure/table captions are segregated
into a trailing appendix instead of interrupting body paragraphs.
No grammar rewriting was performed; authorial wording preserved verbatim.
-->

# A Wave-Shaped Deep Neural Network for Smoke Density Estimation

Feiniu Yuan, Senior Member, IEEE, Lin Zhang, Xue Xia, Qinghua Huang, and Xuelong Li, Fellow, IEEE

## Abstract

Smoke density estimation from a single image is a totally new but highly ill-posed problem. To solve the problem, we stack several convolutional encoder-decoder structures together to propose a wave-shaped neural network, termed W-Net. Stacking encoder-decoders directly increases the network depth, leading to the enlargement of receptive fields for encoding more semantic information. To maximize the degrees of feature re-usage, we copy and resize the outputs of encoding layers to corresponding decoding layers, and then concatenate them to implement short-cut connections for improving spatial accuracy. The crests and troughs of W-Net are special structures containing abundant localization and semantic information, so we also use short-cut connections between these structures and decoding layers. Estimated smoke density is useful in many applications, such as smoke segmentation, smoke detection, disaster simulation. Experimental results show that our method outperforms existing methods on both smoke density estimation and segmentation. It also achieves satisfying results in visual detection of auto exhausts.

Index Terms— Deep neural network, W-Net, smoke density estimation, smoke segmentation, smoke simulation.

## I. INTRODUCTION

Smoke detection is necessary and important for public safety and security, since smoke always emerges before flame. Visual smoke detection provides earlier fire alarms, wider monitoring ranges and faster response than traditional fire detection methods based on photo-electricity or ionized atom sensors. Image smoke recognition is a fundamental problem for visual smoke detection since a video is composed of sequential images. It is a challenging task to recognize smoke from a single image. The reasons are four folds: 1) smoke seriously blurs images and decreases image contrast, 2) smoke appearance is easily affected by environments, 3) smoke usually has translucency property that makes smoke textures mixing with background ones, and 4) smoke boundaries are very fuzzy.

Visual smoke detection can be roughly categorized into traditional and deep learning-based methods. Traditional methods share a common framework including image partition, spatial or temporal feature extraction, smoke recognition for each patch, and final classification for the whole image. Traditional methods achieve smoke detection by judging whether the number of small patches classified as smoke in an image is more than a threshold. Traditional methods often design hand-crafted descriptors, but which may be unable to effectively extract semantic information. The reason is that feature extraction is a complex function of local geometry, structure, and context [1]. Deep learning based methods usually use convolutional neural networks (CNN) to implement an end-to-end method for smoke detection. In some cases, CNNs are also used to extract features. For example, high-level semantic features can be extracted from hierarchical structures in CNNs, which can shorten the semantic gap between objects and features. However, CNNs require a huge number of samples [2] for training to demonstrate better performance.

Smoke segmentation offers more information than smoke detection since it performs dense prediction over each pixel. It is a challenging task that aims at accurately separating smoke components from a single image. This task can be easily extended to videos. Sparse smoke usually appears translucent in observed scenes, so visual patterns of translucent smoke are heavily affected by background objects. This phenomenon also obscures optical flow based dynamic smoke segmentation [3]. A general framework of smoke segmentation views a smoky scene as a linear combination of semi-transparent smoke and background. Deep learning methods can be used to solve the problem in an end-to-end way.

Smoke density estimation provides more information than smoke segmentation, but it is far more challenging than smoke segmentation. The location and density of smoke provides more accurate and abundant information [3] for smoke detection or other applications, such as fire simulation and human evacuation. Smoke density contains different levels of smoke particles [4]. Different from traditional smoke density estimation by particle sensors [5], [6], our task not only performs pixel-wise smoke recognition, but also aims at predicting the smoke density of every pixel. This task requires accurate ground truths for supervised learning of smoke density estimation models. Data sets for smoke segmentation actually provide binary mask maps that indicate the location of smoke pixels instead of smoke density. Since smoke binary masks are very difficult to be segmented in a manual way, it is more extremely difficult to manually label smoke density.

To avoid the difficulty in manually labelling smoke density, we use 3D visualization techniques of particle scattering and emission models to simulate smoke behavior and generate a lot of translucent pure smoke images with RGBA channels. The alpha channel carries information about smoke density. To generate synthetic smoke density data sets for training, we linearly blend a pure smoke image with a real image as background to generate an observed image, and the alpha channel of the pure smoke image is regarded as the ground truth of the observed image. In this way, we avoid the challenging problem of manually labelling smoke density.

Synthetic images generated by our method are photo-realistic. By visually observing them, we can also find that these synthetic images are hardly distinguishable from real ones. Therefore, photo-realistic synthesized smoke images assure that our method can correctly learn a suitable model that applies to real images.

In this paper, we propose a wave-shaped deep neural network by stacking multiple encoder-decoders for smoke density estimation, and use synthetic data sets for training. The main contributions of this paper are as follows:

1) We propose an end-to-end smoke density estimation method using full convolutional networks (FCN). The proposed deep network can be trained end-to-end and used to estimate a smoke density map from an observed image of arbitrary size.

2) We stack several non-symmetric encoder-decoder networks together to propose wave-shaped structures, which greatly expands receptive fields of each neuron, and forms special wave structures, including troughs and crests. The troughs of wave structures consist of abundant semantic information for dense classification over all pixels, while the crests of wave structures contain more local or median-scale information for smoke localization. To improve accuracy, we use short-cut connections between troughs, crests and decoding layers.

3) We propose a complicated loss function that includes four errors of smoke density, smoke color, background color, and composited observed color. These four-error terms jointly regulate the training of our proposed network.

This paper is organized as follows. Section II describes related work on smoke detection and semantic segmentation. Section III describes the synthesizing method of smoke density images. In Section IV, we present our network in details. Extensive experiments are given in Section V. At last, we conclude the paper in Section VI.

## II. RELATED WORK

Early methods use motion, texture and color information for smoke detection. Calderara et al. [7] proposed a background model to obtain smoke regions, and took energy and color properties into account for smoke detection. Filonenko et al. [8] used background subtraction to extract foreground components, and distinguished smoke regions by analyzing color features of moving objects. Yuan [9] used the integral image to propose a fast accumulative motion orientation model for video smoke detection. Dimitropoulos et al. [10] proposed a dynamical model to capture the temporal evolution of pixels from the aforementioned regions in smoke sequences. These methods involve background subtraction and color analysis. Background models greatly depend on pre-specified thresholds, which vary in different scenes and burning materials, so the selection of thresholds greatly affects detection results [11]. Appana et al. [12] used frame differences to model smoke patterns. Spatio-temporal energy analysis and Gabor transforms were involved to extract smoke regions by frame differences. For slowly flowing smoke or normally flowing smoke captured in distant cameras, visual changes of smoke are very small and often imperceptible in several adjacent frames, so temporal differences between two consecutive frames may not be able to reflect smoke motion. In addition, it is also difficult to specify a suitable time interval for frame differences.

Smoke is a special kind of fluid. Fluid characteristics can be utilized for smoke detection, thus we may avoid the difficulty of parameter selection. Dense motion estimation of fluid relies on the assumptions of brightness constancy and the first-order smoothness [13], but it's difficult to accurately estimate motion of complex fluids, such as smoke. Chen et al. [14] proposed a smoke motion estimation method based on the prior that the global smoke density distribution changes little across frames. This method implements smoke segmentation and smoke mass transfer modeling without feature matching and brightness assumption. But the segmentation was conducted on smoke videos with black background, so the method may not be suitable for smoke motion estimation in real world scenes. In summary, video-based smoke methods suffer from two main obstacles: (1) background subtraction that needs thresholding, and (2) frame differencing that relies on sampling intervals.

Deep neural networks are used for smoke recognition and detection. Tao et al. [15] implemented smoke recognition by AlexNet [16]. The method achieved limited performance since AlexNet aims at recognizing digital numbers and is not for smoke classification, segmentation and density estimation. Yin et al. [17] proposed a deep normalization and convolutional neural network for image smoke recognition. Yuan et al. [18] proposed a convolutional neural network based on multi-scale additive merging layers for visual smoke recognition. Tian et al. [19] separated smoke components from a single image by constructing dual dictionaries for smoke and background components, and formulated the smoke separation task as a convex optimization. But the sparse learning for dual dictionaries was time-consuming and deeply dependent on training data. Zhang et al. [20] adopted faster R-CNN [21] without modification for smoke detection in the wild land. Xu et al. [22] proposed a saliency network for smoke detection, in which one encoder-decoder was involved.

CNNs have achieved significant successes in the fields of image classification, object detection and semantic segmentation. CNNs often use pooling layers to downsample the spatial resolutions of feature maps for computational efficiency and acquisition of spatial context. However, downsampling causes loss of spatial details, which finally decrease the spatial accuracy of pixel-wise segmentation. Solutions to this problem can be generally divided into three kinds of techniques: dilation filters, encoder-decoder structures and short-cut connections. Motivated by the success of spatial pyramid pooling (SPP) [23], Chen et al. [24] proposed the atrous SPP to implement multi-scale training and fully connected conditional random fields for accurate localization. Shelhamer et al. [25] adopted dilation filters in FCNs for dense semantic segmentation, and used short-cut connections to combine fine layers with coarse layers to improve segmentation accuracy. Peng et al. [26] achieved global convolution by using large kernels.

To reduce computational complexity, Badrinarayanan et al. [27] stored pooling indices to present an FCN-based pixel-wise segmentation network (SegNet). SegNet transfers max-pooling indices in encoder layers to corresponding decoders, so it can produce dense feature maps without increasing computational consumption. Ronneberger et al. [28] designed an encoder-decoder structure for medical image segmentation. The method resizes and copies feature maps in encoder layers to decoder ones, and concatenates them for short-cut connections, thus it can obtain precise localization. This kind of network yields a U-shaped architecture, termed U-Net. Lin et al. [29] fused features at different stages of convolutions to obtain high-resolution predictions and adopted residual connections to increase the depth of networks.

Several methods stack U-Net like structures for improvement. Newell et al. [30] proposed a U-Net like module termed hourglass and stacked several hourglass blocks to generate a deeper network for human pose estimation. Yuan et al. [31] recently proposed a deep FCN network with two encoder-decoder paths for hard smoke segmentation. The first path focuses on global context information while the second one captures local fine information. Sun et al. [32] stacked U-Nets with multiple outputs for road extraction.

In this paper, we propose W-Net for smoke density estimation, which involves more median information, captures features across multiple scales and increases more information reusage. To our knowledge, it's the first time to propose an end-to-end deep network for smoke density estimation.

## III. SYNTHESIZING METHOD OF SMOKE DENSITY DATA SETS

### A. Illumination Model of Smoke Particles

Smoke is usually composed of many tiny particles, which scatter and absorb lights from light sources or environmental reflections [33]. Lights gradually attenuate in the air, and finally enter into a camera to generate an image, as shown in Fig. 1. In the imaging model [34], the background light transmission t(d, x) for a given pixel x is computed as

t(d, x) = b(x) exp(-∫_0^d τ(v, x) dv)    (1)

where τ(v, x) is an attenuation coefficient at the position v along a viewing light for pixel x, d denotes the light travel length through smoke particles, and b(x) stands for the light intensity from scene background for pixel x.

The scattered intensity s(d, x) of smoke particles can be formulated as a light emission term, defined as:

s(d, x) = ∫_0^d g(u, x) exp(-∫_u^d τ(v, x) dv) du    (2)

where g(u, x) denotes the scattering color of smoke particles at a light travel position u. It is determined by several factors, such as particle densities, particle scattering spectrums, lighting conditions and viewing angles.

The final color of pixel x is the sum of the transmitted color of background and the scattered color of smoke.

i(x) = b(x) exp(-∫_0^d τ(v, x) dv) + ∫_0^d g(u, x) exp(-∫_u^d τ(v, x) dv) du    (3)

To simplify the integrals of the above equation, we define a translucency degree α(x) of smoke as:

α(x) = 1 − exp(-∫_0^d τ(v, x) dv)    (4)

It is quite complicated to directly compute the color intensity of smoke particles, so we replace the scattered color s(d, x) of smoke particles with the product of s(x) and α(x), where s(x) is defined as the color of smoke and α(x) is the translucency coefficient or the alpha channel of smoke. The observed intensity i(x) for pixel x is reduced to the following equation:

i(x) = b(x)(1 − α(x)) + s(x)α(x)    (5)

The above equation is just the linear color composition formula in image dehazing [35] and image matting [36], [23]. For the sake of simplicity, the translucency degree α(x) of smoke is approximately equivalent to the density of smoke. For RGB images, we apply Eq. (5) to red, green and blue channels, respectively. Therefore, we have three equations with seven unknowns, including RGB channels b(x) of background, RGB channels s(x) of smoke, and an alpha channel α(x) of density, so the inverse problem is highly ill-posed.

### B. Smoke Simulation by Computational Fluid Dynamics

Traditional methods usually impose some priors on the inverse problem, such as local consistency, dark channel [37]. However, these priors may not hold in some cases. In this paper, we propose a deep learning architecture to accurately and quickly solve the inverse problem, but we have no sufficient training data labelled for density estimation. It is impractical for us to manually label alpha channels of real images since each pixel of an alpha channel has 256 possible values. Labeling alpha channels is extremely laborious, costly, and inaccurate.

3D visualization techniques have achieved amazing results in simulation of fluid dynamics, elastic dynamics [38], [39]. Foster and Metaxes [40], [41] used 3D meshes to simulate smoke. Particle systems and volume rendering techniques are often used to simulate fluid dynamics [40]. The Navier-Stokes Equation [42] describes the motion of viscous fluid substances:

∂(ρv)/∂t + ∇·(ρv ⊗ v) = −∇·p I + ∇·τ + ρg    (6)

where ρ is the fluid density, v is the flow velocity, ∇ is the divergence operator, p is the pressure, t is time, I is an identity matrix, τ is Cauchy stress tensor, g represents body accelerations acting on the continuum, and ⊗ is the outer product. Stam [42] proposed a classic solution method for computational fluid dynamics.

### C. Generation of Smoke Density Data Sets

There are a lot of discrete methods to solve the above equation. We can use one of classic methods to solve the Navier-Stokes equation and adopt volume rendering methods to visualize simulated smoke to generate a huge number of pure smoke images with RGBA channels. Each pure smoke image has four channels, i.e. RGBA. The RGBA channels are decomposed into RGB channels for a smoke color vectors and an alpha channel for smoke density α. To obtain smoke images with large variance, we generate a variety of smoke with different shapes, densities and colors.

To facilitate the generation of smoke images with alpha channels, we use a third-party free 3D modeling software, Blender [43], to simulate and visualize smoke. Blender allows users to freely add wind, motion and gravity to greatly vary smoke appearance. We can use high-resolution 3D grids to generate high-quality smoke images, but it is time-consuming. To save time, we produce a large number of low-quality smoke images and a small number of high-quality smoke images. This tradeoff strategy does not influence the training of our model, since most of real smoke images are of low quality.

We used computer graphics to generate about 20k pure smoke images for composition of smoky images. To avoid overfitting, we also use data augment techniques, such as affine transformation, gamma correction and color jittering, to generate more smoke and background images.

Fig. 2 shows some pure smoke images generated using computational fluid dynamics. The first and second rows of Fig. 2 illustrate low-quality smoke, and the third row shows high-quality smoke. We can find that these simulated pure smoke images are very photo-realistic. Since each pure smoke image contains RGB channels s and an alpha channel α, we can use Eq. (5) to blend a pure smoke image (s and α) and a background one b to obtain a composited smoky image i. Fig. 3 illustrates two composited smoky images.

## IV. THE PROPOSED W-NET FOR SMOKE DENSITY ESTIMATION

### A. Basic Convolutional Blocks

To implement effective feature encoding for smoke density estimation, we design two down-sampling blocks: normal convolutional down-sampling and residual down-sampling blocks. Fig. 4a is a normal down-sampling block. Each normal convolutional down-sampling block consists of convolution (con), batch normalization (BN) and rectified linear unit (ReLU) layers. The convolution layer in the normal down-sampling block adopts a kernel of size 7x7 with step 2, so it down-samples feature maps by a factor of 2.

Residual networks have achieved excellent performance and are often used to increase the depth of networks for further improvements. We also design a residual block, which is the sum of two paths. As shown in Fig. 4c, the first path does not use any operation while the second path has a convolution with a 3 × 3 kernel of step 1 and batch normalization. Residual blocks can also be used for down-sampling if we add a pooling layer with step 2 and use the convolution also with step 2. Fig. 4d illustrates a residual down-sampling block.

In decoding stages, we need to gradually up-sample feature maps. Similarly, we also design two versions of up-sampling blocks. The first up-sampling block is implemented by deconvolution. Fig. 4b shows our normal convolutional up-sampling block, which consists of deconvolution (cont), batch normalization (BN) and rectified linear unit (ReLU). The deconvolution of the normal up-sampling block uses a 7x7 kernel with step 2 to implement up-sampling of factor 2. Fig. 4e is our residual up-sampling block. We use deconvolution layers with step 2 in the two paths. But the kernel size of deconvolution is different for scale invariance, thus we can involve different receptive fields for residual summing.

### B. Wave-Shaped Structures

Contracting and expanding paths are corresponding to encoding and decoding, respectively. A contracting path followed by an expanding path forms an encoder-decoder, as shown in Fig. 5. Encoder-decoder structures are the backbones of many deep neural networks for semantic segmentation, object detection, and other applications.

We stack several encoder-decoder structures to propose a wave-shaped network. Fig. 5 illustrates a typical wave-shaped network by stacking two encoder-decoder structures. Wave-shaped structures have the same advantages as encoder-decoder ones, such as global and localization information. Besides these advantages, wave-shaped structures further enlarge receptive fields of neurons and provide more important feature maps at the crests and troughs of wave structures. To fully utilize information from these important structures, a simple way is to concatenate features from wave crests and troughs with features at subsequent decoding layers. Experiments also validate that wave-shaped structures play an important role in improving accuracy of smoke density estimation.

The trough of a wave-shaped network lies in the most bottom layer of an encoding path, so it carries more abundant global context information about objects, which facilitates coarse semantic segmentation of objects. On the other hand, the crest of a wave-shaped network is in the most top layer of a decoding path. Apparently, it includes more local or medium features that favor localization of segmentation. These two structures are used together for improving segmentation accuracy of fuzzy objects, such as smoke, fog. Experiments show that increasing the number of encoder-decoder structures does not improve accuracy significantly. Therefore, we stack only two encoder-decoder structures to generate a wave-shaped network for computational efficiency in this paper.

### C. The Proposed Network

Smoke density estimation is a little similar to semantic segmentation that is a dense classification over all pixels, but smoke density estimation is actually a dense regression problem. In fact, our problem can be viewed as a fuzzy semantic segmentation of two classes while traditional object semantic segmentation belongs to hard segmentation of multiple classes. Smoke density estimation also faces an inherent tension between semantics and location: global information resolves what [25], which indicates features and contributes for classification, while local information resolves where [25], which indicates local spatial appearance and devotes for localization.

To accurately accomplish fuzzy semantic segmentation of smoke, we use basic convolutional blocks and wave-shaped structures to propose a Wave-shaped deep neural Network (W-Net) for smoke density estimation. Fig. 6 gives the overall structure of the proposed W-Net, which takes an observed RGB image as input and generates an output map with seven channels. The seven channels of the output map include an alpha channel for smoke density, three RGB channels for smoke color, and three RGB channels for background color.

To clearly describe the network framework, we first introduce six operations: linear color composition, normal down-sampling, normal up-sampling, residual down-sampling, residual up-sampling, and copying and resizing. Linear color composition is used just in the training stage to generate an observed RGB image in real time from a pure smoke RGBA image and an RGB background image. Each pure smoke RGBA image consists of a ground truth alpha channel and RGB color channels. Normal down-sampling is used in the first layer of our W-Net. Residual down-sampling operations are responsible for encoding features to extract global semantic information. The normal up-sampling operation is used in the last layer of our W-Net. Similarly, normal and residual up-sampling operations are used for decoding features from previous layers. The copying and resizing operations implement feature reusage and short-cut connections by concatenating resized features from encoding layers with features of decoded layers. The copying and resizing operations can greatly improve localization accuracy.

As shown in Fig. 6, to improve estimation accuracy, we use copying and resizing operations to implement several short-cut connections between encoder and decoder layers having the same resolution. Besides these short-cut connections between the same resolution layers, we also pass information from crests of the wave-shaped network to higher-resolution decoding layers. Since feature maps of crests may have different resolutions from decoder layers, we first need to resize feature maps of crests to the resolution of decoding layers, and then concatenate these feature maps together. We use wave-shaped structures and short-cut connection to expand receptive fields of neurons and maximize information re-usage, so we can simultaneously obtain global semantic information, local and median localization information.

### D. Loss Function

The proposed W-Net outputs seven channels from an input RGB image, including an alpha channel, an RGB image for pure smoke color, and another RGB image for background. Based on the seven channels, we compute four terms of physically meaningful errors between the seven channels and corresponding ground truths. Then we combine the four error terms to propose a special loss function for smoke density estimation, defined as:

L = L_α + w_s L_s + w_b L_b + w_c L_c    (7)

where L_α, L_s, L_b, and L_c denote the training errors of smoke alpha α, smoke color s, background color b and composited color c, and w_s, w_b and w_c are corresponding coefficients for controlling relative importance of each term.

Specifically, L_α is a training error between the ground truth alpha α_gt and the predicted alpha α, L_s denotes an error between the ground truth smoke RGB color s_gt and the predicted smoke RGB color s, and L_b stands for an error between the ground truth background color b_gt and the predicted background color b. To further regulate the loss function, we use Eq. (5) to dynamically generate a composited color c by blending the predicted background color b and the predicted smoke color s with the predicted alpha α, and then compute an error L_c between the observed color i and the composited color c. The alpha channel error L_α, smoke color error L_s, background color error L_b, and composited color error L_c are formulated as follows:

L_α = (1/2)||α − α_gt||_2^2    (8)

L_s = (1/2)||s − s_gt||_2^2    (9)

L_b = (1/2)||b − b_gt||_2^2    (10)

L_c = (1/2)||i − b(1 − α) − sα||_2^2    (11)

Minimizing the loss function in Eq. (7) is usually solved by stochastic gradient descent (SGD). We need to compute the gradients of the loss function for SGD. The gradients of L_α, L_s, L_b with respect to alpha α, smoke color s, and background color b are straight-forward. However, the gradients of L_c are more complicated since L_c is a linear combination of seven-channel parameters. We derived the gradients of L_c with respect to alpha α, smoke color s and background color b:

∂L_c/∂α = Σ_{k=r,g,b} [i_k − b_k(1 − α) − s_k α](b_k − s_k)    (12)

∂L_c/∂s_k = −[i_k − b_k(1 − α) − s_k α] α    (13)

∂L_c/∂b_k = −[i_k − b_k(1 − α) − s_k α](1 − α)    (14)

where k denotes r, g, b channels.

## V. EXPERIMENTAL RESULTS

### A. Synthetic Smoke Datasets

We first used the method in Section III to generate about 20k pure smoke images with RGBA channels. Then we divided a pure smoke RGBA image into an alpha image and an RGB smoke image, and used the alpha image to blend the RGB smoke image with a background RGB image to generate a composited smoky image. The composited smoky image is just regarded as an input image. The alpha image, the RGB smoke image and the background RGB image are the ground truth with seven channels for the input image. The background images for training were randomly selected from CBCL StreetScenes [44], Pascal Visual Object Classes [45] and Baidu people segmentation dataset [46]. The number of background images for training is about 60k. Fig. 7 shows some background images from the three image data sets.

To avoid overfitting, we randomly used affine transformation, gamma correction, random cropping and color jittering to augment the number of pure smoke and background images during training. In other words, each epoch has different training samples since we use data augmentation techniques to produce training data in real time. Thus, we can theoretically generate a huge number of composited smoky images when we use the large number of training epochs. For the sake of fair comparisons, we used data augment techniques to generate three test data sets, i.e. DS01, DS02, DS03 [31]. All images of test sets have the same resolution of size 256 × 256. Each set has 1000 composited smoky images with corresponding ground truth images. DS01, DS02 and DS03 were generated by blending pure smoke images and background images randomly selected from CBCL StreetScenes [44], Pascal Visual Object Classes [45], and Baidu human dataset [46], respectively. Since the three test sets were generated by randomly blending pure smoke and background images, 1000 composited smoky images have enough variance for testing.

We used C++ to implement our W-Net and wrote console programs for testing. Related data sets and programs can be downloaded from http://staff.ustc.edu.cn/~yfn/.

### B. Ablation Analysis of Network Structures

To validate the importance of wave-shaped structures and short-cut connections, we selectively remove some of short-cut connections and wave-shaped structures to produce several variants of our method, as shown in Fig. 8.

Fig. 8a is just an encoder-decoder network without any short-cut connections by removing a wave crest from our W-Net. Inspired by U-Net [28], we also use short-cut concatenation from encoder layers to decoder ones. Fig. 8b is just a U-Net with four short-cut connections. In Fig. 8c, we add a wave-shaped structure to Fig. 8b, but we do not reuse any information on crests and troughs of the wave structure, and remove the bottom short-cut connection due to the existing of the wave structure. Fig. 8d is the proposed W-Net, which adopts short-cut connections between crests, troughs and decoding layers.

To quantitatively evaluate our method, we also compute the mean squared error between predicted smoke density and corresponding ground truth, which is defined as

mMse = (1/N) Σ_n (1/(H_n W_n)) Σ_y Σ_x [α(x,y,n) − α_gt(x,y,n)]^2    (15)

where W_n and H_n are width and height of the nth image, N is the image number of a data set, and α(x, y, n) and α_gt(x, y, n) denote the predicted density and the ground truth at a pixel (x, y) of the nth image, respectively.

Table 1 lists the comparison results on the three test data sets (DS01, DS02, DS03). The proposed W-Net has the best performance among these variants because it fully utilizes wave-shaped structures and short-cut connections on both crests and troughs. From the results of Table 1, we can find that short-cut connections plus encoder-decoder structures have better performance than the pure encoder-decoder. If short-cut connections are performed on crests and troughs of wave structures, the performance will be further improved. Wave-shaped structures truly improve the prediction accuracy of smoke density estimation.

The average testing time is also listed in Table 1. We tested our W-Net on a PC with i7 CPU and Nvidia GeForce GTX 1080Ti. It took us an average time of 20.675 seconds to estimate smoke density for 1000 test images. The time includes image loading, network inferencing and MSE calculation. Although our W-Net has the most slowest speed, it is quite fast to process 1000 images in such a short time.

In addition, we also changed the output of W-Net to a single channel of smoke density for further ablation analysis, i.e. we set w_s, w_b and w_c in the total loss function of Eq. (7) to zero. However, the performance of W-Net becomes very worsened, so we enable the seven-channel output for W-Net.

### C. Smoke Density Estimation on Synthetic Images

To evaluate performance, we tested our method on DS01, DS02 and DS03. Fig. 9a and Fig. 9b show a composited smoky image and its corresponding ground truth from DS01, respectively. Fig. 9c is just the predicted smoke density map by our W-Net from the input image in Fig. 9a. Fig. 9d and Fig. 9e are a composited smoky image and its corresponding ground truth from DS02. Our W-Net accurately estimated a smoke density map shown in Fig. 9f from the composited image in Fig. 9d. Fig. 9g and Fig. 9h show a composited smoky image and its corresponding ground truth selected from DS03. Fig. 9i gives the predicted smoke density map by our W-Net for Fig. 9g. By visually comparing these predicted density maps with their ground truths, our W-Net achieves very accurate estimation of smoke density.

Once we obtain the results of smoke density estimation, we can easily make use of the density maps for hard segmentation, smoke recognition, smoke detection or other purposes. We will discuss them in subsequent sections.

### D. Hard Smoke Segmentation on Synthetic Images

Our W-Net is actually a soft segmentation method. After we use our W-Net to estimate a density map from an image, we can directly binarize the density map to produce a hard segmentation of the image. The pixel-wise conversion from soft segmentation to hard one is simply formulated as β = 1 if α ≥ Th; 0 otherwise (16), where Th is a predefined threshold. In our implementation, we set Th = 50/255 ≈ 0.2 by trials and errors. In other words, if a pixel has more than a smoke density of 0.2, we regard the pixel as a smoke one; otherwise it is viewed as a non-smoke one.

To quantitatively evaluate the performance of hard segmentation, we compute the mean Intersection over Union (mIoU) of segmented map and its ground truth: mIoU = (1/N) Σ_n (β_n ∩ β_n^gt) / (β_n ∪ β_n^gt) (17), where N is the image number of a data set, and β_n, β_n^gt are the predicted hard segmentation map and its binarized ground truth of the nth image, respectively.

We compared the hard segmentation variant of our W-Net with eight state-of-the-art methods, including FCN-8s [25], SegNet [27], Static Map Detection (SMD) [47], Text-Block FCN (TBFCN) [48], Deeplab v1 [49], ESPNet [50], Deep Smoke Segmentation (DSS) [31], and Stacked Hourglass Network (HG-Net) [30]. The hard segmentation experiments were performed on DS01, DS02 and DS03. To apply HG-Net to smoke segmentation, we added a sigmoid layer followed by a binarization layer, and an upsampling layer to match input size. We implemented HG-Net 2 and HG-Net 8 with two and eight hourglass blocks. Modifications of other comparison methods can be found in [31].

Table 2 lists the comparison results on DS01, DS02 and DS03. Our method achieved the highest mIoU among all comparison methods on the three data sets. Stacking more hourglass blocks for HG-Net [30] cannot obviously improve performance. The proposed W-Net even outperforms DSS [31] specially designed for hard smoke segmentation. Fig. 10 gives some synthetic smoky images and corresponding segmented images by these comparison methods. By visually comparing these results to corresponding binarized ground truths in Fig. 10b, we find that the results by our method are the most similar to ground truths, so our method achieved the best performance among these comparison methods.

### E. Hard Smoke Segmentation on Real Images

We used our method to segment real images, which were manually collected from the Internet. Since these real images have no ground truths, we perform visual comparisons. Fig. 11 illustrates the results by our method, FCN-8s [25], SegNet [27], Static Map Detection (SMD) [47], Text-Block FCN (TBFCN) [48], Deeplab v1 [49], ESPNet [50], and HG-Net [30]. By visually comparing these segmented images with each other, we find that our method achieved the best performance.

### F. Smoke Density Estimation on Real Videos

Our method was used to estimate smoke density on the same four videos as [51], including two smoke videos and two non-smoke videos. The first video is a black smoke video generated by burning diesel oil, the second one is a white smoke video by burning cotton ropes, the third one is a non-smoke video containing waving leaves, and the fourth one is a basketball court video consisting of several students playing basketball.

Fig. 12 shows estimated density maps for four frames of the black smoke video. Fig. 12a illustrates the four original frames from the video, Fig. 12b is the estimated smoke density maps for the four frames, and Fig. 12c show the overlapped display results of the four frames and corresponding estimated smoke density maps. By observing the overlapped results, we can find that our method estimated very accurate smoke density maps for the black smoke video. The accuracy is very high in both spatial locations and density levels.

Fig. 13a, Fig. 13b and Fig. 13c show four original frames, estimated smoke density maps and overlapped display results on the white smoke video. As we can see, the accuracy of estimated density maps on the white smoke video is good, but obviously lower than that on the black smoke video. The main reason may be that the white smoke video has very poor image quality. Fig. 14 shows two frames from the two non-smoke videos. Our method did not misclassify any pixel as smoke on the two non-smoke videos, so we do not illustrate estimation results.

According to the smoke density results estimated by our method, we can easily perform smoke binary segmentation, smoke detection, whole image smoke recognition, and fire spreading simulation. For the sake of simplicity, we first used Eq. (16) to produce binary segmentation of predicted maps, then counted the number of pixels classified as smoke in an image, and classified the whole image as smoke if the number of pixels classified as smoke is greater than a pre-specified threshold. We compared our method with LBP_LBPV [51] and Toreyin's method [52]. Table III lists the results of the three methods. Our method detected smoke at the first frame of the two smoke videos. Experimental results show that our method can detect smoke much earlier than other two methods. In addition, our method did not raise any false alarms on the two non-smoke videos, and we did not use any post-processing techniques to further reduce false alarms.

### G. Visual Detection of Auto Exhausts by Our Method

Auto exhausts become one of the main air pollution sources in metropolises. Traditional sensors achieve high accuracy for detection of auto exhausts, but they need to sample and analyze molecules of auto exhausts. It is very difficult and impractical to effectively sample auto exhausts of fast moving vehicles.

Our W-Net can be used to detect auto exhausts from images or videos. Fig. 15 shows results of auto exhausts detected from several images with different vehicle types, which were manually collected from the Internet. Fig. 15a, Fig. 15b, and Fig. 15c are original images, estimated density maps and overlapped displays of auto exhausts, respectively. The first row illustrates detection of white smoke generated by auto exhausts. The second one accurately detects heavy black smoke produced by a truck. The last one shows detected black smoke of a minibus. The results are quite accurate and appealing.

## VI. CONCLUSION

It is a highly ill-posed problem to estimate smoke density from a single image. To solve the challenging problem, we first use dynamic fluid simulation, computer graphics and color composition to virtually create smoke density datasets. Thus we easily avoid the difficulty in manually labelling the smoke density of images. To enlarge receptive fields for encoding more semantic information, we stack convolutional encoder-decoder structures together to propose a wave-shaped neural network (W-Net). To maximize data flow and feature re-usage degree, we resize and copy the outputs of previous encoding layers to corresponding decoding layers, and concatenate them together to implement short-cut connections for accuracy improvement. Crests and troughs of the proposed W-Net are special and important structures to refine abundant localization and semantic information. Experimental results show that our method outperforms existing methods on both smoke density estimation and smoke segmentation.

## REFERENCES

<!-- Reference entries omitted from clean corpus: the reader condensed/grouped them (S109-S111 flagged
[uncertain] in translation_notes.md; S111 tail is a non-verbatim summary "[38]-[42] Fluid simulation
and Navier-Stokes / Stam stable fluids; ..."). Consult the source PDF for verbatim entries. -->

## Appendix: Figure and Table Captions (segregated from body)

<!-- Verbatim "Original caption" strings from the reader; kept out of body paragraphs to avoid
caption/body mixing. Caption for Fig. 9 shows signs of reader condensation ("(d)-(f) DS02 sample
pair and prediction") — medium confidence. -->

Fig. 1. Imaging model of smoke particles.

Fig. 2. Pure smoke images with RGBA channels.

Fig. 3. Composition of pure smoke and background images.

Fig. 4. Down-sampling and up-sampling blocks. (a) Normal convolutional down-sampling, and (b) up-sampling blocks. (c) Residual block, (d) residual down-sampling block, and (e) residual up-sampling block.

Fig. 5. A wave-shaped network formed by two encoder-decoder structures.

Fig. 6. The overall deep wave-shaped network with a stack of encoder-decoder structures.

Fig. 7. Background images from (a) CBCL StreetScenes [44], (b) Pascal Visual Object Classes [45] and (c) Baidu people segmentation dataset [46].

Fig. 8. Ablation analysis. (a) an encoder-decoder network; (b) an encoder-decoder network with short-cut connections (U-Net); (c) wave-shaped structures with short-cut connections of encoder and decoder; (d) wave-shaped structures with short-cut connections of encoder, decoder, crests and troughs.

Fig. 9. Some images from the three test data sets. (a) A composited smoky image and (b) its corresponding ground truth from DS01, and (c) its predicted density map. (d)–(f) DS02 sample pair and prediction. (g)–(i) DS03 sample pair and prediction.

Fig. 10. Results of synthetic data. (a) Synthetic images. (b) Corresponding ground truths. Results of (c) FCN, (d) SegNet, (e) SMD, (f) TBFCN, (g) Deeplab v1, (h) ESPNet, (i) HG-Net 2, (j) HG-Net 8, and (k) our method.

Fig. 11. Segmentation results of real smoke images. (a) Real images. Results of (b) FCN, (c) SegNet, (d) SMD, (e) TBFCN, (f) Deeplab v1, (g) ESPNet, (h) HG-Net 2, (i) HG-Net 8, and (j) our method.

Fig. 12. Estimated smoke density maps on a black smoke video.

Fig. 13. Estimated smoke density maps on a white smoke video.

Fig. 14. A waving leaf video (left) and a basketball court video (right).

Fig. 15. Visual detection of auto exhausts.

TABLE I COMPARISONS FOR ABLATION ANALYSIS

TABLE II COMPARISONS OF HARD SEGMENTATION

TABLE III COMPARISON RESULTS OF SMOKE DETECTION ON VIDEOS
