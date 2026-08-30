# Cubic-cross convolutional attention and count prior embedding for smoke segmentation

**Paper_ID:** 02_CCENet_PR2022_Cubic-cross_convolutional_attention_smoke_segmentation
**Authors:** Feiniu Yuan, Zeshu Dong, Lin Zhang, Xue Xia, and Jinting Shi
**Affiliations:** a) College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, Shanghai 201418, China; b) School of Mathematics and Computer Science, Jiangxi Science and Technology Normal University, Nanchang, Jiangxi 330038, China; c) School of Information Technology, Jiangxi University of Finance and Economics, Nanchang, Jiangxi 330032, China; d) Vocational School of Teachers and Technology, Jiangxi Agricultural University, Nanchang, Jiangxi 330045, China; e) Research Base of Online Education for Shanghai Middle and Primary Schools, Shanghai 201418, China
**Venue:** Pattern Recognition 131 (2022) 108902
**DOI:** 10.1016/j.patcog.2022.108902

## Abstract

It is very challenging to accurately segment smoke images because smoke has some adverse properties, such as semi-transparency and blurry boundary. Aiming at solving these problems, we first fuse convolutional results along different axes to equivalently produce a cubic-cross convolutional kernel, which enlarges receptive fields at affordable computational costs for capturing long-range dependency of smoke pixels, and then we propose a Cubic-cross Convolutional Attention (CCA). To embed global category information, we propose a count prior structure to model and supervise the count of smoke pixels. To ensure the network can correctly extract a count prior map, we impose a regression loss on the count prior map and corresponding ideal count map directly calculated from its ground truth. Then we multiply the reshaped input by the count prior map to produce a Count Prior Attention (CPA) map, which is upsampled to generate the final output. A cross entropy loss is used to supervise the final segmentation. Finally, we use ResNet50 for feature encoding, and stack CCA and CPA together to propose a Cubic-cross convolutional attention and Count prior Embedding Network (CCENet) for smoke segmentation. Experiments on both synthetic and real smoke datasets show that our method outperforms existing state-of-the-art methods.

**Keywords:** Smoke segmentation; Information embedding; Cubic-cross convolutional attention; Count prior attention

## Introduction

### 1. Introduction

Different from other disasters, fires exhibit very clear visual cues, such as smoke and flame. In most cases, fires develop slowly and probably last for a long time at early stages before flames burst out. Therefore, smoke detection provides far earlier fire alarms than flame detection, and it allows firefighters to have enough time to extinguish fires. In many applications, smoke detection effectively reduces damages caused by fires. Traditional smoke detection techniques are usually based on sensing temperatures or particles. These sensors are not effective in large or open spaces. Visual smoke detection methods utilize computer vision techniques to recognize smoke from images, and they are more suitable for smoke surveillance in open and large scenes than traditional sensors.

Fully Convolutional Networks (FCN) have rapidly been developed and applied in many vision tasks. Inspired by the successes of FCNs, there are several FCN based methods that have been proposed for smoke segmentation. Like general segmentation tasks, it is also difficult for existing smoke segmentation methods to capture sufficient contextual information and high-resolution spatial details simultaneously. The main reason is the contradiction between local spatial details and global semantic information. The first way of aggregating multi-scale contexts and capturing long-range dependencies has been widely used for solving the contradiction. One effective way is to fuse multi-scale feature maps from different levels. For example, some methods fuse the results by Atrous convolutions with different dilation rates and pooling operations with different strides to extract multi-scale features. Others use skip and concatenation operations to fuse features from encoding and decoding stages. Another way is to use attention mechanisms. In recent years, many attention methods have been proposed for image segmentation by designing special network structures to extract spatial or channel correlations. To extract non-local information, some attention methods often adopt complex data operations, such as matrix multiplication, but it inevitably increases computational burdens. Other methods achieve contextual information by fusing spatial and channel attentions that are separately calculated. However, fusing attention features may not fully model relations between space and channels very well. Extracting highly coupled information across spatial and channel data plays a key role in capturing local and global information.

In fact, smoke segmentation is a dense binary classification problem over each pixel. Smoke has some adverse visual properties, such as fuzzy edges and semi-transparency, directly leading to the difficulty in accurately segmenting smoke regions. Existing smoke segmentation methods do not fully utilize attention mechanisms and global information about the count of smoke pixels. To solve the above problems, we propose a Cubic-cross convolutional attention and Count prior Embedding Network (CCENet) to model long-range dependencies and global count prior for smoke segmentation. The main contributions of this paper are summarized as follows:

(1) We design a cubic-cross convolution to propose Cubic-cross Convolutional Attention (CCA) in an efficient and effective way. The fused results of three convolutions along different axes equivalently produce a cubic-cross shaped kernel with long extents, leading to enlarged receptive fields. Compared with existing attention methods, cubic-cross kernels effectively capture long-range dependency of smoke pixels at affordable computational costs. In addition, combining attention mechanism and cubic-cross convolution further improves performance.

(2) We propose a count prior embedding method to extract image-level information about the counts of smoke and non-smoke pixels. We first design a special network structure to generate a count prior map. Then a count loss is imposed on the count prior map and corresponding ideal count map directly calculated from its ground truth, thus we can guarantee that the count prior map can correctly extract global information about the count of smoke pixels.

(3) We propose a Cubic-cross convolutional attention and Count prior Embedding Network (CCENet) for smoke segmentation by stacking ResNet50, CCA and CPA. Specially, ResNet50 provides powerful feature encoding, CCA focuses on long-range dependency of pixels, and CPA embeds global information about the count of smoke pixels. Our CCENet is a robust but efficient method especially for smoke segmentation.

The remainder of this paper is organized as follows. Related work on context information embedding is given in Section 2.1, attention mechanism in Section 2.2, and smoke segmentation methods in Section 2.3. The proposed method is described in Section 3. Section 4 presents experimental results to evaluate the performance of our method. Conclusions are drawn in the last section.

## RelatedWork

### 2. Related work

#### 2.1. Context information embedding

Context information embedding plays a key role in semantic segmentation. In recent years, various methods have explored multi-scale context information to help the network efficiently capture contextual dependencies. Using image pyramids is a common way to obtain multi-scale context. FCN, SegNet and U-Net have an encoder-decoder architecture to fuse multi-scale feature maps from encoders and decoders. PSPNet adopts the pyramid pooling to extract multi-scale features from different regions and integrate these feature maps to enlarge receptive fields. Deeplab v3 uses the Atrous Spatial Pyramid Pooling, which is a combination of convolutions with different sized images, to embed context information directly from feature maps. However, these methods are supposed to fuse features in a spatial-wise manner. Compared to these methods, RecoNet uses the 3D low-rank tensor reconstruction to extract long-range dependencies. When the network uses global average pooling in order to adopt 3D operations, some features are abandoned. Recently, Huang et al. presented a novel Multi-Level Adversarial Network (MLAN), which aims to optimally address the domain inconsistency at both global image levels and local region ones. Wang et al. designed an Enhancement-Fusion Network (EFNet) by using input images to extract more diversified features, thus they boosted the task of pixel-wise labeling to produce multiple enhanced images.

#### 2.2. Attention mechanism

A lot of attention mechanism methods have been proposed and widely applied in computer vision fields, since attention mechanism was first proposed in natural language processing (NLP). Unlike convolutional and recurrent operations, Wang et al. presented non-local operations to capture long-range dependencies. Fu et al. proposed a Dual Attention Network (DANet) for scene segmentation to capture dependencies of positions and channels. SENet is a squeeze-and-excitation network for capturing channel-interdependencies. Yu et al. proposed a Bilateral Segmentation Network (BiSeNet) for real-time semantic segmentation. Li et al. proposed Expectation-Maximization Attention Networks (EMANet) for Semantic Segmentation. To reduce memory consumption and improve efficiency, other attention modules have been recently proposed, such as Double Attention Networks (A2Net). Yu et al. proposed Context Prior Layers by using explicit regularization with an affinity loss to supervise learning. Zhou et al. proposed a Co-Attention Network (CANet) to build sound interaction between RGB and depth features. Xiong et al. proposed an efficient framework to recognize RGB-D scenes by adaptively selecting important local features to capture the great spatial variability of scene images.

#### 2.3. Smoke segmentation

Traditional machine learning algorithms have been widely proposed for smoke detection and segmentation. Wang et al. proposed a smoke segmentation method based on fractal theory and regional growth. Zhang et al. calculated the upper approximation and the lower approximation of pixels in a color space to obtain a roughness histogram, and used the roughness histogram to adaptively select a threshold for rough segmentation.

With the rapid development of deep learning, neural networks have been used for smoke recognition and segmentation in recent years. Tao et al. implemented smoke recognition using the AlexNet. Yin et al. proposed a Deep Normalization and Convolutional Neural Network (DNCNN) for smoke detection by stacking convolutional, activation, batch normalization layers. Yuan et al. proposed an end-to-end smoke segmentation method by fusing coarse and fine convolutional paths, and used computer simulation to generate synthetic smoke images for training and testing. In recent years, synthetic datasets are also used in other applications to avoid manually annotating real data. Wang et al. developed a free data collector and labeler to generate synthetic crowd datasets with labels from computer game scenes, and they also proposed a weakly supervised adversarial domain adaptation to improve the segmentation performance from synthetic data to real scenes. Yuan et al. stacked convolutional encoder-decoder structures together to propose a Wave-shaped neural Network (W-Net), and achieved very good results of smoke density estimation due to specially designed losses and wave-shaped structures.

However, above-mentioned methods do not fully focus on segmentation of smoke boundaries and extraction of long-range dependencies. Inspired by the recent successes of attention models, we design a cubic-cross convolutional attention to efficiently capture long-range dependencies, a count prior attention to extract global information about the count of smoke pixels, and finally combine these two attention modules to jointly solve semi-transparency of smoke and long-range dependencies of smoke pixels.

## Methods

### 3. Cubic-cross and count prior attentions

#### 3.1. Cubic-cross convolutional attention

Contextual information has widely been explored in various methods and plays a crucial role in scene understanding. Existing methods usually adopt convolution, batch normalization, matrix multiplication and activation operations to extract contextual and attention features for capturing long-range dependencies. However, most methods do not balance well between feature robustness and computation efficiency simultaneously. To reduce computational complexity, we propose a Cubic-cross Convolutional Attention module (CCA) to efficiently model long-range dependencies of smoke pixels, as shown in Fig. 1.

> Fig. 1. Cubic-cross convolutional attention module.

##### 3.1.1. Multi-scale information extraction

Many methods have been proposed to capture multi-scale features in recent years. One method for multi-scale contextual features is to directly compute features from images with different sizes. Creating an image pyramid is a common way for this purpose. Another method is to use pyramid pooling to generate features with multiple scales. In this paper, we use the Pyramid Pooling Module (PPM) with the same pool sizes of [1–3,6] as prior work to extract multi-scale features. To keep the channel number unchanged, the number of feature maps by pyramid pooling is reduced to one fourth of the input channel number by convolutions. All feature maps generated by the pyramid pooling module are bilinearly interpolated to the input size and then concatenated together to generate the multi-scale feature map.

##### 3.1.2. Convolutions along different axes

To capture long-range dependencies of pixels, we propose a novel attention based on the fused convolutional results along three axes, including two spatial axes and one channel axis. We first use the pyramid pooling module to generate a multi-scale feature map with the size of h×w×C, then send the feature map into four different paths, as shown in Fig. 1. The first three paths are used to capture pixel dependencies along different convolutional axes. This procedure is equivalent to extracting dependencies in different convolutional planes. The last path is a short connection to produce attention maps.

For most deep learning frameworks, convolutions are usually performed in the width-height plane whose normal is just the channel axis of the 3D feature tensor. As shown in Fig. 1, Path 1 is just the convolution in the default plane defined by the width and height axes. If a 3×3 kernel is specified, the default convolution factually has the 3D kernel size of 3×3×C.

To capture pixel dependencies along the width axis, we first transpose the input feature tensor with the size of h×w×C to produce a new feature tensor with the size of h×C×w, then convolve the transposed tensor, and finally transpose the convolved tensor back to keep the same size as the input feature tensor. As shown in Fig. 1, Path 2 is the equivalent convolutional operation in the height-channel plane along the width axis. As for a 3×3 kernel, the actual convolutional kernel along the width axis has the shape of 3×3×w. Similarly, we first transpose the input feature tensor to obtain a new feature tensor with the size of C×w×h, then convolve the transposed tensor, and finally transpose the convolved tensor back to match the input size. As shown in Fig. 1, Path 3 is the convolutional operation in the channel-width plane along the height axis. As for a 3×3 kernel, the actual convolutional kernel along the height axis has the size of 3×3×h.

##### 3.1.3. Cubic-cross convolutional attention

To capture long-range dependencies of pixels along different axes, we fuse these feature maps convolved along three axes by point-wise addition. Then we activate the sum of the three convolved feature maps using the sigmoid function to generate a coefficient map for weighting the input feature map. The coefficient map is point-wisely multiplied by the input feature map to produce the output of our attention module, as shown in Fig. 1. In this way, we can efficiently obtain long-range contextual information with large receptive fields.

Compared with default convolutions, our fused convolution method produces an equivalent 3D kernel shape, which has larger receptive fields than traditional methods. Fig. 2 illustrates the equivalent 3D kernel of fused convolutions along the three axes for a kernel of 3×3. The equivalent 3D kernel is just like a cubic cross sign. Therefore, the equivalent of the fused convolutions along the three axes is called a cubic-cross convolution. Apparently, the cubic-cross convolution can generate long-range dependencies, since it has larger equivalent kernels.

> Fig. 2. The equivalent cubic-cross kernel for a kernel of 3×3.

In current implementation, we use two matrix transposition operations for convolutions along non-default axes since current popular deep learning frameworks do not directly realize convolutions along other axes. To speedup computation, we can implement convolutions along any axis using the CUDA programming specification in future work, thus we can avoid unnecessary data copying.

#### 3.2. Count prior embedding

It is a more challenging task to segment fluid objects than general ones because fluid objects have semi-transparency property, time-varying shapes, complicatedly mixed colors and textures. Smoke is a typical fluid, and it is difficult for existing methods to accurately distinguish between smoke and non-smoke pixels, especially in smoke boundary regions. The most adverse characteristic of smoke is the property of semi-transparency, which usually leads to very complicated mixture of background and smoke.

To solve the above-mentioned challenges, we design a special network structure to model a global count prior, as shown in Fig. 3. Inspired by the affinity matrix of prior work, we propose a count prior embedding method to extract global context of smoke pixels, and use the count prior to design a novel attention. In addition, we supervise the count prior to further improve the performance of our network. Although our method partially borrows an idea from prior work, the count prior is totally different: the count prior is defined as a matrix containing the numbers of negative and positive pixels in image levels; and we propose a novel attention module based on the count prior to further enhance contextual information about the global distribution of smoke and non-smoke pixels.

> Fig. 3. Count prior embedding.

To control the behavior of our network, we adopt a regression loss for supervising the count prior and a cross entropy loss for directly controlling segmentation accuracy. Existing methods often produce low confidence for boundary pixels that are ambiguous in labels and very difficult to be classified. The count prior loss guarantees that the network can correctly generate count prior maps for optimizing the challenging segmentation of smoke boundary regions, since it directly supervises the number of positive and negative pixels in each sample. If the ratio of positive and negative pixels in the generated count prior map is different from the one in its ground truth, the count prior loss becomes large to penalize the learning procedure. The count prior loss and attention mechanism can jointly rectify erroneous classification of smoke boundary pixels.

##### 3.2.1. Ideal count map

The number of smoke pixels varies for different images. In most cases, the number of smoke pixels is far less or far more than the one of non-smoke pixels. The count of smoke pixels is rarely equal to the number of non-smoke pixels. In other words, there exists a significant imbalance between positive and negative pixels in most training images. In addition, smoke images often have blurry boundaries, but boundary pixels are ambiguous and very difficult to be distinguished. The counts of smoke and non-smoke pixels in an image are important information for correcting erroneous classification of boundary pixels. Therefore, we propose a count loss to reduce misclassification of pixels on the image level.

To supervise the count of smoke pixels in the learning stage, we need to construct an Ideal Count Map (ICM) Zi for each ground truth map Y. As shown in Fig. 4, we use the one-hot encoding scheme to transform each ground truth to obtain a 3D tensor G with the size of H×W×C, where H, W, and C denote height, width and the number of classes, respectively. The c-th channel of the 3D ground truth tensor G is reshaped into a column vector gc with the dimension of HW. By stacking gc at the c-th column, we obtain the following 2D label matrix L, defined as

L = {g1, ..., gC}  (1)

> Fig. 4. The generation of an ideal count map.

Then, we transpose the 2D label matrix L to obtain its transposed version L^T, and multiply L^T by L to produce an absolute count map Za with the size of C×C, formulated as

Za = L^T L  (2)

Given a ground truth mask map Y, each element value in the label matrix L is 1 or 0 since we adopt the one-hot encoding scheme. Obviously, the c-th diagonal element of the absolute count map Za is just the count of pixels belonging to the c-th class.

The height H and width W of the input image may be different from the height h and width w of the input feature map, so the pixel counts encoded in the absolute count map are not equal to the ones in an input image. Absolute counts may be very large, and it may lead to numeric computation instability in learning and testing stages. To avoid image resizing and numeric computation instability, the softmax function is used to activate the absolute count map to obtain an ideal count map Zi, formulated as

Zi = softmax(Za)  (3)

The diagonal elements of the ideal count map Zi store the normalized ratio of pixels belonging to each class.

##### 3.2.2. Count prior map

As for an input tensor with the size of h×w×C to our count prior embedding module, we also transpose and reshape the 3D input tensor to produce a 2D matrix of C×(h×w). Different from the computation of the ideal count map for a ground truth, we adopt a learning method to generate a count matrix that has the same size of the ideal count map. As shown in Fig. 3, the 2D matrix of C×(w×h) is first processed by convolutions with C kernels to produce a C×C map, and then the map is activated using the softmax function to produce a count prior map Zp. By imposing a count loss on the count prior map Zp and its corresponding ideal count map Zi, we can ensure the network to correctly learn a count prior map that contains the pixel ratio of each class. In this way, we can use a supervised learning method to generate a count prior map containing global image-level information. This processing can be mathematically formulated as

Zp = fW(X)  (4)

where X stands for a RGB input image, fW is a high-dimensional mapping function determined by a series of data operations. As described in the above sections, we use several complicated modules, such as ResNet, PPM, CCA and CPA, to produce the count prior map, so data operations for fW include convolution, batch normalization, activation, short connection, point-wise addition, point-wise multiplication, data reshaping and matrix transposition, and so on. Apparently, fW is a very complicated high-dimensional function, so it has the capability to learn the complex relationship between smoke and non-smoke pixels in an image under deep learning frameworks.

##### 3.2.3. Count loss

After we obtain the count prior map from an image and the ideal count map from its corresponding ground truth, we propose to use a regression loss to supervise the two maps, which is called the count loss. In this paper, the count loss is defined as the Mean Squared Error (MSE):

lC = (1/N) Σ_{k=1}^{N} || Zp_k − Zi_k ||_F^2  (5)

where N is the number of training images, ||Z||_F stands for the matrix Frobenius norm, and Zp_k and Zi_k are the count prior map and the ideal count map computed from the k-th training image Xk and its ground truth Yg_k, respectively.

##### 3.2.4. Count prior attention

Besides using the count loss for medium supervision, we fully utilize the count prior map to extract attention information for further improvement. As shown in Fig. 3, the reshaped version of the 3D input tensor is multiplied by the count prior map to produce a map of Count Prior Attention (CPA). Then the CPA map with the size of (h×w)×C is reshaped and upsampled to produce the final output with the size of H×W×C. At last, the output is supervised by a cross entropy loss, defined as:

lS = −(1/(NM)) Σ_k Σ_j [ y^g_{k,j} log(y^p_{k,j}) + (1−y^g_{k,j}) log(1−y^p_{k,j}) ]  (6)

where M is the pixel count of the k-th training image Xk, and y^p_{k,j} and y^g_{k,j} are the j-th pixel values of the output Yp_k and its corresponding ground truth mask Yg_k for Xk, respectively. Explicit supervision of the count loss and the count prior attention map can jointly encode the long-range relationship of pixels and the total ratio of positive pixels to negative ones. Therefore, we use a weighted sum of the two losses to generate the final loss, defined as:

ℓ = λS lS + λC lC  (7)

where λS and λC are the coefficients to control the relative importance of each loss. In our implementation, λS and λC are set to 1.0 and 0.4, respectively.

> Fig. 5. The overall architecture of our CCENet.

#### 3.3. Network architecture

Fig. 5 illustrates the overall architecture of our network. The backbone of CCENet is the ResNet for feature encoding. The encoded feature maps are then fed to the module of cubic-cross convolutional attention described in Section 3.1. At last, we use the module of count prior embedding presented in Section 3.2 to further improve feature representation and output a final segmentation result.

## Results

### 4. Experimental results

#### 4.1. Experimental datasets

Due to the fuzzy boundary phenomenon and semi-transparent characteristics of smoke, it is extremely difficult to label smoke regions in real images. Currently, there are several datasets for smoke segmentation in public. We used computer graphics and volume rendering to create smoke segmentation datasets for training and testing. Our datasets contain a large number of pure virtual smoke images with RGBA channels, including RGB channels for smoke color and an alpha channel for smoke transparency. We can randomly combine a pure smoke image with a background image to generate an observation image. In this way, a virtual smoke dataset containing a variety of smoke patterns was generated for training and validation. The virtual smoke dataset has a total of 70,632 images, and 90% of the dataset is used for training and 10% is used for validation.

#### 4.2. Implementation details

We implemented the proposed CCENet using Tensorflow, and adopted the ResNet as the backbone of our CCENet, which was pre-trained on the ImageNet. Following prior work, we, respectively, assign the dilation rates of 2 and 4 to the last two stages of the backbone network, and the output feature map is the 1/8 size of the input image. Our CCENet was trained on a PC equipped with a single NVIDIA GeForce GTX2080Ti card containing 11GB Video RAMs. The optimization algorithm is set to the Stochastic Gradient Descent (SGD) with an initial learning rate of 0.004, a momentum of 0.9 and a decay weight of 0.0001. For the sake of fairness, we use the same settings of hyper-parameters and training tricks for all experiments.

To evaluate performance, we tested our network on three smoke test sets of DS01, DS02 and DS03. Each test set consists of 1000 pictures with the size of 256×256. All pictures were composited by randomly selecting pure smoke and realistic background images. The alpha channel of a pure smoke image is converted to produce a binary ground truth for the pure smoke image, formulated as

β = 1 if α ≥ T; β = 0 if α < T  (8)

where T is a predefined threshold. Following prior work, we set T to 0.2. If a pixel has an alpha value that is equal to or more than 0.2, then the pixel is regarded as smoke, otherwise it is viewed as background. The evaluation metric is the mean of Intersection over Union (mIoU).

#### 4.3. Ablation studies

To validate effectiveness of each module, we performed ablation experiments with different combinations of separate modules in our method. Our CCENet mainly includes a ResNet50 module, a Cubic-cross Convolutional Attention module (CCA) and a Count Prior Attention module (CPA). Since our CCA module consists of a Pyramid Pooling Module (PPM) and a pure Cubic-cross Convolutional Attention (denoted as pCCA).

According to ResNet50, PPM, pCCA and CPA, we designed five variants of our method: ResNet50+pCCA; ResNet50+PPM; ResNet50+PPM+pCCA; ResNet50+PPM+CPA; and ResNet50+PPM+pCCA+CPA (CCENet). All ablation experiments are listed in Table 1.

> Table 1. Comparisons with different combinations of modules.

According to Table 1, variants of ResNet50+PPM+pCCA and CCENet are significantly better than ResNet50+PPM and ResNet50+PPM+CPA. Since both ResNet50+PPM+pCCA and CCENet contain a powerful module of pCCA, the pure CCA module plays a key role in improving performance. The main reason may be that CCA has cubic-cross convolutional kernels to produce large receptive fields. Comparing the results of the second and third variants, we find that the pure CCA module achieves better performance than the CPA module. The main reason may be that the CPA module is designed to assist pixel classification in the image level and the three test datasets do not contain smoke-like objects, such as cloud. The first variant is the only one without PPM, but it also surpasses the second and fourth variants with PPM.

> Table 2. Comparison with different attention modules.

Experiments show that our attention module outperforms all attention modules. As shown in Table 2, we find that a network capturing both spatial and channel information achieves better performance than one extracting single information. The main reason is that our attention module captures both spatial and channel information to perfectly model long-range dependency.

To validate the performance of our CCA on multi-class datasets, we designed a new variant of our method that includes ResNet and CCA modules. We first use the PASCAL VOC2012 augmented dataset for training, and then fine-tune the trained model on the PASCAL VOC 2012 original training set for all compared methods. The PASCAL VOC2012 augmented dataset contains 10582 training images, 1449 validation images and 1456 test images. We tested all compared methods on the PASCAL VOC 2012 validation dataset for performance evaluation. The pixel category proportion of each sample is used to supervise the count prior matrix. For binary classification tasks, the count prior matrix is a diagonal matrix of size 2×2, which can globally rectify the erroneous proportion of positive and negative predictions. In multi-category tasks, for example, the PASCAL VOC2012 dataset with 21 classes produces the count prior matrix with size of 21×21. Apparently, correcting the erroneous proportion of 21 categories is more complicated and far less effective than two categories. In other words, the count prior matrix for CPA is unsuitable for multiple classes. Therefore, we do not use CPA for multi-class segmentation.

> Table 3. Comparison results with the state-of-the-art methods on the PASCAL VOC2012 validation dataset.

As shown in Table 3, our method achieves the highest accuracy of 83.2% among compared methods while maintaining a relatively small number of parameters (46M).

> Table 4. Comparisons of methods using standard convolution and our cubic-cross convolution.

To demonstrate the efficacy of cubic-cross convolution, we compared our module with several other attention modules using standard convolutions (SE, CBAM, and CA). All methods used a MobileNetV2 backbone. The experiments on the PASCAL VOC 2012 validation set show that the cubic-cross convolution module (CCA) achieves the best accuracy.

#### 4.4. Comparison on synthetic datasets

We compared our CCENet with eleven state-of-the-art methods on the three smoke test datasets that are DS01, DS02, and DS03. These methods for comparisons include FCN-8S, SegNet, SMD, TBFCN, Deeplab v1, ESPNet, DSS, HG-Net2, HG-Net8, and W-Net. Table 5 shows comparison results of these twelve methods on the three synthetic smoke test datasets. According to Table 5, our CCENet obtains the best performance among these twelve methods.

> Fig. 6. Test results on synthetic data. (a) Synthetic images. (b) Corresponding ground truths. Results of (c) FCN, (d) SegNet, (e) SMD, (f) TBFCN, (g) DeepLab v1, (h) ESPNet, (i) HG-Net 2, (j) HG-Net 8, (k) W-Net, and (l) our method.

> Fig. 7. Test results on realistic data. (a) Realistic images. Results of (b) FCN, (c) SegNet, (d) SMD, (e) TBFCN, (f) DeepLab v1, (g) ESPNet, (h) HG-Net 2, (i) HG-Net 8, (j) W-Net, (k) DSS, and (l) our method.

> Table 5. Comparison results with the state-of-the-art methods on the three synthetic test datasets.

For visual clarity, only ten methods are shown in Fig. 6. Our method produces clearer smoke boundaries and fewer false alarms than compared methods on synthetic data. Fig. 7 further shows qualitative results on realistic composited smoke images.

#### 4.5. Experiments on real smoke scenes

To further evaluate generalization, we tested DSS, W-Net and our method on real smoke scenes. Real smoke datasets were downloaded from websites and manually selected. Fig. 8 shows visualized results on real smoke scenes.

> Fig. 8. Visualized results on real smoke scenes. (a) Real smoke images. Visualized results by (b) DSS, (c) W-Net, and (d) our method.

The 1st to 3rd rows of Fig. 8 show segmented results of real images with white smoke and blue skies. DSS achieves excellent results for a while, but our method obtains more complete smoke regions. From 7th to 9th rows of Fig. 8, there are white smoke real images with white skies and clouds, and visualized results segmented by the three methods. For the smoke image in the 8th row of Fig. 8, our method achieves the best results, and all the methods do not classify clouds as smoke. The 10th row of Fig. 8a shows a white smoke image with a white snow background. The three methods can clearly discriminate white smoke regions from snow. For tree leaves in later rows of Fig. 8, our method also surpasses others.

> Table 6. Quantitative results on real smoke scenes.

The real smoke datasets not only have black and white smoke images, but also contain many colorful smoke ones. For the sake of fairness, we selected comparable samples for comparisons. According to Table 6, our network also achieves the highest accuracy on real smoke images among the three compared methods.

#### 4.6. Experiments on sequential images of smoke videos

In order to further verify the performance of our model in actual scenarios, we performed comparative experiments on a black smoke video and a white smoke video. Fig. 9 shows test results on realistic smoke videos. Our method produces more temporally consistent and spatially complete smoke masks than compared methods on these sequential frames.

> Fig. 9. Test results on realistic smoke videos. (a) Original frames from videos. Results of (b) SMD, (c) TBFCN, (d) LRN, (e) DeepLab v1, (f) ESPNet, (g) HG-Net2, (h) HG-Net8, (i) DSS, (j) W-Net, and (k) our method.

## Conclusion

### 5. Conclusions

Smoke has properties of semi-transparency, fuzzy boundary, time-varying shapes and colors. These smoke properties lead to a challenging task of smoke segmentation. In this paper, we propose a Cubic-cross Convolutional Attention (CCA) to capture long-range dependencies of smoke pixels at affordable computational costs, and a Count Prior Attention (CPA) to embed global information about the count of smoke pixels. By stacking ResNet50, CCA and CPA, we propose a Cubic-cross convolutional attention and Count prior Embedding Network (CCENet) for smoke segmentation. Experimental results on both synthetic and real smoke datasets demonstrate that our method outperforms existing state-of-the-art methods.

## Acknowledgments

This work was partially supported by the Natural Science Foundation of China (61862029, 62062038), and Capacity Construction Project of Local Colleges of Shanghai Science and Technology Commission (22010503700).

## References

[Note: the source extraction condensed the reference list.] [1]–[46] Bibliographic entries covering smoke detection/segmentation, FCN/SegNet/U-Net/PSPNet/DeepLab, attention networks (non-local, DANet, SENet, BiSeNet, EMANet, A2Net, CANet), synthetic-data domain adaptation, W-Net density estimation, and related semantic segmentation baselines. Full fields remain in the PDF.

## Other

### Declaration of Competing Interest

The authors declared that they have no conflicts of interest to this work. We declare that we do not have any commercial or associative interest that represents a conflict of interest in connection with the work submitted.

### Author biographies

Feiniu Yuan received his B.Eng. and M.E. degrees in mechanical engineering from Hefei University of Technology, Hefei, China, in 1998 and 2001, respectively, and his Ph.D. in pattern recognition and intelligent systems from University of Science and Technology of China (USTC), Hefei, China. He is currently a professor. His research interests include smoke recognition, image processing, deep learning, and video analysis.

Zeshu Dong received his B.E. degree in communication engineering from Hohai University, Changzhou, China, in 2019. He is currently pursuing the M.E. degree. His research interests include image processing and deep learning.

Lin Zhang received her B.E. degree in computer science and technology from East China Jiaotong University, Nanchang, China, in 2004, and her degrees thereafter in related computing fields. Her research interests include image processing and pattern recognition.

Xue Xia received the B.E. degree in Film & TV Arts and Technology and the M.E. degree in Communication and Information Engineering from Shanghai University, and works on image analysis and smoke-related vision tasks.

Jinting Shi received the B.E. degree in computer science and technology from the Jiangxi Normal University, Nanchang, China, in 2003, and subsequent graduate degrees. Her research interests include computer vision and pattern recognition.
