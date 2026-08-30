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
