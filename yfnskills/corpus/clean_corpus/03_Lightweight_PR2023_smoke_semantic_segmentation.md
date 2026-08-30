# A lightweight network for smoke semantic segmentation

**Paper_ID:** 03_Lightweight_PR2023_smoke_semantic_segmentation
**Authors:** Feiniu Yuan (co-first), Kang Li (co-first), Chunmei Wang, Zhijun Fang (corresponding author, zjfang@sues.edu.cn)
**Affiliations:** a) College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, Shanghai 201418, China; b) Research Base of Online Education for Shanghai Middle and Primary Schools, Shanghai Normal University, Shanghai 201418, China; c) School of Computer Science and Technology, Donghua University, Shanghai 201620, China; d) Mathematics and Science College, Shanghai Normal University, Shanghai 200233, China; e) Key Innovation Group of Digital Humanities Resource and Research, Shanghai Normal University, Shanghai 200234, China; f) Shanghai Engineering Research Center of Intelligent Education and Bigdata, Shanghai Normal University, Shanghai 201418, China
**Venue:** Pattern Recognition 137 (2023) 109289
**Article history:** Received 27 January 2022; Revised 8 December 2022; Accepted 31 December 2022; Available online 5 January 2023

## Abstract

To obtain real-time performance on computation limited devices, we propose a lightweight network for smoke segmentation. To enhance the ability of feature encoding, we first propose an Attention Encoding Module (AEM) by designing a Channel Split and Shuffle Attention Module (CSSAM), which can extract powerful features and reduce computations simultaneously. CSSAM adopts Channel split and shuffle to greatly reduce learnable parameters for improving computation speed, and uses attention mechanism to focus on salient objects to enhance the effectiveness of features. In addition, AEM repeatedly stacks CSSAM in different encoding stages to achieve scale invariance. For the middle-level features of encoding stages, we propose a Spatial Enhancement Module (SEM) to boost the representation ability of spatial details. SEM concatenates feature maps produced by average and maximum pooling to achieve dominant and global responses, which are then weighted by the activated output of global average pooling to generate attention features. In the highest level of encoding stages, we present a Channel Attention Module (CAM) to explicitly model interdependency between channels. By reshaping 2D features into 1D features, we use element-wise matrix multiplications to reduce computation complexity for extracting channel-related information. Finally, we design a Feature Fusion Module (FFM) and a Global Coefficient Path (GCP) to fuse the outputs of SEM and CAM in an attention way for further improving robustness of final features. Experiments show that our method is significantly superior to existing state-of-the-art algorithms in smoke datasets, and also obtains excellent results in both synthetic and real smoke datasets. However, our method has less than 1 M network parameters.

**Keywords:** Smoke semantic segmentation; Deep learning; Attention mechanism; Lightweight network; Channel split and shuffle

## Introduction

### 1. Introduction

Semantic segmentation is a basic and challenging task in computer vision. Deep convolutional neural networks (DCNNs) [1] have achieved great successes in many computer vision tasks, such as object detection [2], medical image analysis [3]. Smoke segmentation based on deep learning aims to accurately separate smoke regions from a single image. Smoke segmentation not only provides an important clue for fire detection, but also offers abundant pixel-level information for fire simulation and human evacuation. Intelligent robots for fire detection need to precisely find the source of fires, and then guide firefighters to extinguish the fires as soon as possible. Smoke segmentation is very important for early fire detection that can avoid casualties and property losses. In addition, some leaky chemical substances may produce colored smoke, so smoke segmentation methods can help guide inspection devices to precisely locate the leaky point of chemical substances, and visually assist the staff to amend the corresponding equipment.

It is a main trend to construct deeper and wider convolutional neural networks (CNNs), such as FCN [4], ResNet [5] and Deeplab [6]. Deepening and widening is an effective and simple way to improve accuracy of networks. To achieve higher accuracy, some CNN based segmentation methods even design hundreds of convolutional layers and thousands of feature channels, leading to billions of FLOPs. However, higher accuracy is achieved at the expense of computation time and memory consumption. For example, FCN [4] and DANet [7] have made great progresses in image semantic segmentation tasks, but these networks consume huge memory and increase inference time. That limits these models to be applied in mobile or computation-limited devices, so it is necessary to develop lightweight, efficient and real-time semantic segmentation methods for such devices. With the continuous improvement of smart city, intelligent surveillance has widely been penetrated into all corners of modern cities. Fully utilizing video surveillance devices for fire monitoring [8,9] can help solve the problem of fire detection in open or large spaces at a low cost. Video fire detection techniques have the advantages of lower costs, quicker response and wider monitoring coverage than traditional fire detectors. Video surveillance devices produce a huge number of sequential images every day, so it is urgently necessary for researchers to develop lightweight models for rapid analysis of videos. Lightweight smoke segmentation networks can be deployed in mobile devices and surveillance cameras for greatly reducing the computational overload of backend severs.

Accurately separating smoke from a single image is a challenging task. The main reasons may be unremarkable objects of small smoke, complex textures of translucent smoke mixed with complicated backgrounds, multi-scale smoke at different stages of fire evolution, and interference of haze, cloud and other smoke-like objects. To suppress disturbed objects, image dehazing methods [15,16] and other enhancement ones [17] can be performed before smoke segmentation.

Reducing learnable parameters of neural networks is a key way to achieve fast inference speed and reduce memory consumption. It is an exploring trend that is suitable for mobile or memory-limited devices. Using factorized convolutions to build efficient light-weighted networks is a scalable approach, which can more easily balance accuracy, network size, inference speed, and efficiency. Many methods have achieved promising results and potential applications, such as ENet [10], BiSeNet [11], ERFNet [12], LEDNet [13] and DFANet [14]. However, ERFNet [12] and LEDNet [13] fail to properly balance factorized convolution and long-range dependency features, while DFANet [14] makes up for these defects but lacks extraction of texture features. Although these methods have achieved satisfactory results in street scene segmentation, they may not achieve good performance for smoke semantic segmentation. To solve these problems, we propose a light-weighted Channel Split and Shuffle Attention Module (CSSAM) to extract long-range dependency and texture features for reducing redundant information.

In this paper, we mainly focus on semantic segmentation of small, semi-transparent or inconspicuous smoke, as well as recognition of hazes and clouds. To extract more powerful features, we propose an attention encoder by designing a channel split and shuffle attention module. In addition, we propose a spatial enhancement module to capture detailed features for representing small, semi-transparent or inconspicuous smoke. It is very difficult to distinguish between smoke and clouds, because they share a very similar visual appearance. We design a channel attention module to extract interdependence information across channels. Finally, we design a feature fusion module to combine features from different stages or modules to obtain final segmentation maps. Extensive experiments show that our method achieves the state-of-the-art performance on both synthetic and real smoke images. The main contributions of our method are summarized as follows:

- We propose an Attention Encoding Module (AEM) to enhance the representation ability of the encoding module. A Channel Split and Shuffle Attention Module (CSSAM) is first designed to extract powerful features and reduce computation complexity simultaneously. Channel split and shuffle techniques can greatly reduce learnable parameters, and attention mechanism improves feature robustness to compensate for possible decrease in performance due to reduction of learnable parameters. To obtain scale invariance, CSSAM is repeatedly stacked in different encoding stages of AEM.
- We propose a Spatial Enhancement Module (SEM) and a Channel Attention Module (CAM) to improve robustness of encoding features with different levels. SEM learns dominant and global responses of the middle level features, while CAM explicitly models interdependency between channels of the highest level features. By transforming 3D feature tensors into 2D ones, CAM accelerates computation of interdependency between channels. SEM and CAM are responsible for capturing local spatial details and global semantic contexts at middle and high levels, respectively.
- We propose a Feature Fusion Module (FFM) to aggregate the features of SEM and CAM, and design a Global Coefficient Path (GCP) to further improve the representation ability of the aggregated features. GCP produces more global semantic information by deepening the network structure of AEM, and a squeezing and activating manner is used to generate powerful attention coefficients for weighting the aggregated features.
- By fully integrating AEM, SEM, CAM and FFM, we propose an efficient lightweight network for semantic smoke segmentation with less than 1 M network parameters, which achieves excellent performance.

## RelatedWork

### 2. Related work

#### 2.1. Semantic segmentation

There are a lot of FCN based segmentation methods proposed in recent years. To obtain more accurate results, some of them [18,19] adopt structured prediction modules for refining outputs, such as conditional random fields [20]. To capture contextual information, several state-of-the-art methods [7] have designed specific segmentation heads with dilated convolutions [21] for improving segmentation performance. Non-local operators [22] for modelling self-attention mechanisms [23] have been proposed to obtain global contexts in image levels. To include some prior knowledge, Luo et al. [24] propose a novel segmentation-to-classification scheme by adding the segmentation-based attention (SBA) information to the deep convolution network (DCNN) for breast tumors classification. Although these methods achieve state-of-the-art results on some standard benchmarks of Cityscapes [25] and PASCAL VOC [26], direct usages of them may not achieve good performance on smoke segmentation benchmarks due to adverse properties of smoke, such as semi-transparency and blurry edges. In addition, most of existing methods have a large number of network parameters leading to high computational complexity, so they are not suitable for hardware constrained devices. To fully utilize long-range dependency, Transformers [27] have widely been used for vision tasks in recent years. Dosovitskiy et al. [28] partitioned an image into several blocks for encoding sequential features to propose a Vision Transformer (ViT). To segment urban ground scenes with large-scale variances, Yi et al. [29] proposed a novel composite transformer network for urban scenes segmentation of UAV image. Yuan et al. [30] proposed an effective CNN and Transformer complementary network for medical image segmentation. This method fully utilizes the advantages of CNN and Transformers.

Some vision applications need to be deployed on hardware limited or mobile devices, for examples, unmanned aerial vehicles. These devices usually have no powerful computation capability or specialized deep learning architectures. Therefore, it is necessary to develop lightweight semantic segmentation models for achieving real-time segmentation. Many lightweight models have been proposed, such as BiSeNet [11], DFANet [14] and CGNet [31]. The aim of lightweight models is to reduce memory consumption and network parameters for accelerating inference speed, and also to achieve satisfactory accuracy at the same time.

There are several main methods to improve computational performance, such as network pruning, convolution factorization and channel reduction. Model pruning requires more time to obtain a training target, and probably causes the loss of details. Convolution factorization decomposes large convolutional kernels into two or more small kernels to obtain the same receptive fields. ENet [10] reduces the number of channels to cut down computation and memory consumption. LiteSeg [32] uses a deep atrous spatial pyramid pooling module to improve segmentation performance. ICNet [33] proposes an image cascade network for real-time semantic segmentation, which utilizes low-resolution semantic information and high-resolution image details. DFANet [14] maximizes multiscale receptive fields by modifying the Xception [34] network structure, increasing channel attention in full convolutional layers, and fusing low-level and high-level features. BiSeNet [11] adopts the dual-path model to fuse features extracted from the two paths in semantic segmentation. Inspired by existing methods, we also design a lightweight network in a similar style to achieve the goal of real-time visual smoke segmentation.

#### 2.2. Smoke semantic segmentation

Traditional smoke segmentation methods mainly depend on hand-designed features. Early methods extract color features in different color spaces, such as CIE, RGB and HIS, to obtain suspicious smoke areas. Dimitropoulos et al. [35] filtered non-smoke pixels by applying background subtraction and color analysis. Zhao [36] and Zhang et al. [37] adopted a rough set of color features for smoke segmentation. Filonenko et al. [38] used both shape and color features, and accelerated computations using CUDA. In [39] and [40], the authors used motion features for smoke detection and segmentation. Tian et al. [41] separated smoke regions from a single image by training a foreground smoke dictionary and a background one, but this algorithm is highly dependent on training data.

With the rapid development of deep learning in recent years, several smoke semantic segmentation methods based on deep neural networks have been proposed. Deep learning methods combine feature extraction and classification without designing hand-crafted features. Kaabi et al. [42] directly used Deep Belief Networks (DBN) for classifying each pixel into smoke or nonsmoke objects. Li et al. [43] proposed a three-dimensional parallel full convolutional neural network to segment smoke regions in videos. Yuan et al. [44] and Frizzi et al. [45] proposed deep smoke segmentation methods based on CNNs. The network by [44] uses a stepwise up-sampling way to restore feature maps to the input image size, while the one by [45] adopts a deconvolution method to recover segmentation feature maps. Yuan et al. [46] repeatedly stacked encoders and decoders to propose a Wave-shaped deep neural Network (W-Net) for smoke density estimation, which is factually a soft segmentation of smoke. Wang and Hu [47] proposed gated recurrent connections to improve performance by introducing gates, which can avoid inconsistency with biological facts. Yuan et al. [48] also used gated units to propose a Classification-assisted Gated Recurrent Network (CGRNet) for smoke semantic segmentation. CGRNet designs an Attention Convolutional GRU module (Att-ConvGRU) to learn the long-range contextual dependence of features, and uses a strategy of dual classification assistance to reduce false segmentation of smoke-like objects, such as clouds. However, most of abovementioned smoke segmentation methods are based on powerful but large backbones, such as VGG16 [49], ResNet [5]. Although these networks have achieved excellent results in smoke segmentation, the computational complexity of networks and the number of model parameters have increased significantly. Large models are not suitable for hardware limited or mobile devices. Yuan et al. [50] utilized three directional convolutions and the ratio of smoke to non-smoke pixels for improving segmentation accuracy. The pixel ratio can supervise erroneous segmentations in image levels.

#### 2.3. Factorized convolution

Traditional standard convolution adopts a two-dimensional kernel to convolve all channels of the input to compute each pixel value of the output. Therefore, the number of learnable parameters for convolution is determined by the 2D kernel size, the input channel number and the output channel number. If the width and height of the kernel, the channel numbers of the input and output are large, the number of convolution parameters is very huge.

To reduce learnable parameters, Xception [34] and MobileNet [51] adopt a depthwise separable convolution by combining depthwise convolutions and pointwise convolutions. The depthwise convolution learns local spatial relations within each channel for reducing computations, while the pointwise convolution learns features across channels for swapping information. Both depthwise and pointwise convolutions reduce parameters and computations. ShuffleNet [52] adopts a strategy of channel split and shuffle to reduce parameters and computations. In this strategy, a standard convolution can be divided into two convolutions on two groups of split channels, and a channel shuffle operation helps information exchange between the two groups. Factorizing a large 2D convolution kernel into two small 2D convolution kernels is another method to reduce network parameters. There are some lightweight methods [12,13] adopting this approach and obtaining good performance. Inspired by these ideas, our Channel Split and Shuffle Attention Module (CSSAM) also utilizes these strategies to construct a light-weighted, efficient and powerful network structure.

#### 2.4. Attention models

Attention mechanism simulates the human visual perception system, which can capture long-range dependencies. In recent years, many attention modules have been proposed in many computer vision tasks. Position attention and channel attention are two important mechanisms. SENet [53] adopts a squeeze-and-excitation method to enhance the robustness of features and extract the relationship between channels. Chen et al. [54] used several attention masks to fuse feature maps or predictions from different branches. Wang et al. [55] proposed a non-local attention module by reshaping feature maps to simulate matrix multiplication that is similarly to non-local mean. DANet [7] uses self-attention mechanism to capture contextual information. Channel attention module has been widely applied in semantic segmentation, including some light-weighted methods of DFANet [14] and CGNet [31]. Spatial attention methods have been proposed for semantic segmentation in recent years, but they are rarely explored in light-weighted semantic segmentation. In this paper, we construct spatial enhancement module and channel attention module, which are applicable to lightweight networks and can effectively extract powerful smoke features.

## Methods

### 3. The lightweight smoke segmentation network

Fig. 1 shows the overall framework of our network, which consists of an attention feature extraction encoder and a feature fusion decoder. The encoder is constructed by our Attention Encoding Module (AEM). As shown in Fig. 2, we stack several Channel Split and Shuffle Attention Modules (CSSAM) in different stages of our AEM. Fig. 3 shows the detailed structure of CSSAM. The decoder network mainly contains three important modules, which are a Spatial Enhancement Module (SEM), a Channel Attention Module (CAM), a Global Coefficient Path (GCP) and a Feature Fusion Module (FFM), as shown in Fig. 1. Finally, we add two segmentation heads for training.

> Fig. 1. The overall architecture of our network.

> Fig. 2. Attention Encoding Module (AEM).

> Fig. 3. Channel Split and Shuffle Attention Module (CSSAM).

#### 3.1. Encoding stages

##### 3.1.1. The overall structure of encoder

As show in Fig. 2, we use a ResNet-style structure of three stages to form the encoder. We use the same down-sampling unit as the ENet [10] network for conversion between two adjacent stages. The down-sampling unit consists of two parallel operations that are a 3 × 3 convolution layers with a stride of 2 and a maxpooling layer, and then it concatenates the outputs of the two layers together for its final output. This concatenation structure of two parallel down-sampling layers easily enables deeper networks to gather more contextual information. To efficiently extract attention features, we propose a Channel Split and Shuffle Attention Module (CSSAM), and repeatedly apply CSSAM in different encoding stages, as shown in Fig. 3.

##### 3.1.2. Channel split and shuffle attention module

Our CSSAM is a light-weighted and efficient feature extraction module. It adopts the same channel split and shuffle scheme as the ones used in LEDNet [13] and DFANet [14]. Similarly, we also use dilated convolutions with two asymmetric kernels of 1 × 3 and 3 × 1 to further speed up computation for each path of divided channels. The usage of dilated convolutions [6] enables our architecture to have large receptive fields for improving accuracy.

Splitting channels is a common method to achieve light-weighted models for semantic segmentation, since reducing channel numbers can greatly cut down learnable parameters. Dilated convolution is used to enlarge receptive fields and is also important for semantic segmentation models. The receptive field produced by one convolution with a 3 × 3 kernel is almost the same as the one generated by two convolutions with a 3 × 1 kernel and a 1 × 3 kernel, but the parameter number of the latter is significantly less than that of the former.

> Table 1. The detailed configuration of our encoder network. "r" denotes the dilation rate.

| Stage | Operation | Output size |
|---|---|---|
| Stage 1 | Downsampling Unit | 128 × 128 × 32 |
| Stage 1 | 3 × CSSAM | 128 × 128 × 32 |
| Stage 2 | Downsampling Unit | 64 × 64 × 64 |
| Stage 2 | 2 × CSSAM | 64 × 64 × 64 |
| Stage 3 | Downsampling Unit | 32 × 32 × 128 |
| Stage 3 | CSSAM (r = 1), (r = 2), (r = 5), (r = 9), (r = 2), (r = 5), (r = 9), (r = 17) | 32 × 32 × 128 each |

As shown in Fig. 3, our CSSAM divides the input feature map into two small feature maps, each of which has only half the channels of the input feature map. Then, we use one dilated convolution with a 3 × 1 kernel followed by another dilated one with a 1 × 3 kernel to filter one small feature map, and also adopt two dilated convolutions but with a different sequence of kernel sizes for another small feature map. The sequential kernel sizes are 1 × 3 and 3 × 1 instead of 3 × 1 and 1 × 3. Apparently, we adopt an asymmetrical scheme of kernel sizes, and the purpose is to perceive objects with irregular shapes for different processing paths. After the two small feature maps are processed by two sets of convolution, batch normalization (BN) and activation (ReLU) operations, we directly concatenate the results generated from two small feature maps, so the concatenated feature map has the same channel number as the input feature map. The concatenated feature map is processed again by convolution, BN and ReLU.

Another path from the input is squeezed and activated to generate attention coefficients by a global max-pooling with kernel size 3 × 3, a 1 × 1 convolution, a BN layer and an activation layer of sigmoid. Each attention coefficient is multiplied with each channel of the processed concatenated feature map, and the multiplied result is element-wisely added to the processed concatenated feature map to generate attention features. Finally, the channel shuffle operation in ShuffleNet [52] is used to realize information swapping between two split paths.

##### 3.1.3. Attention encoding module

Convolution kernels with large dilation rates can obtain complex or spatially informative long-range features for recognizing large-scale objects, while kernels with small dilation rates are used to capture short-range features for perceiving small or inconspicuous objects. Therefore, we repeatedly apply our CSSAM on three scales of feature maps, as show in Fig. 2. In Stage 1, we stack three CSSAMs to obtain contextual information. Two CSSAMs are put in Stage 2. In Stage 3, we use eight CSSAMs for deeply extracting global and local features by carefully designing different dilation rates. We performed several experiments to obtain the best results using the sequence of dilation rates that is {1,2,5,9,2,5,9,17}. Thus, we obtain multi-scale features. Table 1 lists a detailed configuration of each stage in the attention encoder.

#### 3.2. Decoding stages

As shown in Fig. 1, our decoder is a pixel-wise classifier enhanced by our spatial enhancement module, channel attention module and feature fusion module, and refines the output by a segmentation head. Each module acquires feature information from different levels of the encoding stages. Low-level features in shallow layers have higher resolutions but lack abundant semantic information [56]. Higher level features in deep layers contain rich semantic information, but lack spatial details. A common way to capture abundant spatial details and semantic information is to combine features from different levels.

To solve this problem, we propose to use Spatial Enhancement Module (SEM) at the lower-level decoding layer (Stage 2) to obtain rich spatial detail features, and then acquire rich semantic information and contextual features by Channel Attention Module (CAM) at the high-level decoding layer (Stage 3). The decoding stability of semantic information is improved by combining low-level features with high-level features in a fusion manner. Finally, the output is refined by a segmentation head.

##### 3.2.1. Spatial enhancement module

Pooling operations can not only reduce model sizes and accelerate computations, but also improve the robustness of features. Different pooling types have unique characteristics. Max-pooling retains major and dominant responses of features, and extracts non-linear and robust information. Average-pooling tends to preserve more overall or low-frequency information about objects, so the result by global average pooling is a good prior knowledge of global context.

In early stage of fires, smoke is often small, translucent or of low contrast. In other words, early smoke usually behaves like inconspicuous objects. Max-pooling and average-pooling operations are suitable for capturing local dominant details and global contexts of inconspicuous smoke objects, respectively. To obtain complementary information about local details and global contexts, we design two parallel paths of max-pooling and average-pooling operations. As shown in Fig. 1, the input is first processed by a set of convolution, BN and ReLU layers, and then the results of max-pooling and average-pooling are concatenated, convolved, batch-normalized, and activated by ReLU. In addition, another path uses global average pooling, convolution, batch normalization, sigmoid activation to generate attention coefficients for weighting the parallel pooling results. Finally, we add the weighted feature map to the input for producing the final output of our Spatial Enhancement Module (SEM).

##### 3.2.2. Channel attention module

High-level features tend to contain more abstract and global information, which is helpful for smoke segmentation. Each channel of a high-level feature map is regarded as a class-specific response. In fact, different semantic responses are often related to each other. By fully mining the interdependence between channels, we need to extract interdependent channel information for improving the feature representation abilities of inconspicuous smoke objects. Therefore, we design a specialized Channel Attention Module (CAM) to explicitly model these interdependencies between channels for improving robustness, as shown in Fig. 1. The computational complexity of large matrix multiplication is very high, so we abandon the operation of matrix multiplication adopted in DANet [7]. Reducing spatial resolutions can greatly decrease computation complexity, so we perform matrix multiplication in Stage 3. To further improve computational efficiency, we use 1D convolutions to reduce the channel number of a feature map to one-kth of the original channel number.

As shown in Fig. 1, the input with C × H × W to our CAM is processed by 2D convolution and batch normalization to obtain a channel-reduced feature map with C/k × H × W, which is then reshaped to produce a 2D feature map F8 with size C/k × N (N = H × W). Another path uses 2D convolution and batch normalization to obtain a feature map of size C × H × W, which is finally reshaped to generate a feature map of size C × N (N = H × W). The feature map is then reduced to C/k × N by a 1D convolution. We use the softmax activation function to generate a 2D coefficient map F9 for weighting the 2D feature map F8 by element-wise multiplication. We use 1D convolution to increase the channel number of the 2D weighted feature F10 to a feature map F11 of C × N, and reshape it to C × H × W, and use 2D convolution and BN to generate a feature map F12. Finally, we add the feature map F12 and the input F3 together to generate the output F13 of our CAM.

##### 3.2.3. Feature fusion module

Another highlight of our method is that we design a Feature Fusion Module (FFM) to integrate the outputs of our spatial enhancement module and channel attention module to improve segmentation accuracy. The structure of our FFM is shown in the upper right of Fig. 1. The outputs of our SEM and CAM have different resolutions, so our FFM can generate multi-scale features.

In addition, we use attention mechanism to further enhance representation capability of features. Hou et al. [57] verify that deeper network layers can capture more semantic information. Therefore, we design a Global Coefficient Path (GCP) to generate an attention coefficient map that contains more global and contextual information, as shown in the bottom of Fig. 1. In GCP, we further down-sample the output of Stage 3 to deepen our network, and use convolution, BN, ReLU, global average pooling and sigmoid to generate global coefficients. Finally, we use these coefficients to weight the concatenated features from our SEM and CAM for producing an attention feature map as the output of our FFM. In this way, our model generates more robust features to prevent overfitting and improve accuracy.

#### 3.3. Segmentation head

In order to further improve segmentation accuracy and refine prediction results, we design an enhanced training strategy by supervising the medium output and the final output simultaneously. Thus, we can improve the representation abilities of both encoding and decoding features in the training phase, but in the testing phase, we abandon the auxiliary supervision path and only use the final output for prediction. Fig. 4 shows the details of the segmentation head.

> Fig. 4. The details of the segmentation head.

#### 3.4. Loss function

As shown in Fig. 1, we use two Cross Entropy losses to supervise both the final output of our network and a medium output. The feature map of the last encoding stage is followed by our segmentation head to generate the medium output. The cross-entropy loss on the final output is defined as:

l1 = −(1/N) Σ_{k=1}^{N} (1/M_k) Σ_{j=1}^{M_k} Σ_{i=1}^{C} g^{k,j}_i log(p^{k,j}_i)  (1)

where N is the image number of the train set, M_k is the pixel number of the kth training image, C is the number of object categories, p^{k,j}_i is the ith channel value of the jth pixel in the kth final predicted map, and g^{k,j}_i is the ith channel value of the jth pixel in the kth ground truth map.

Similarly, the cross-entropy loss on the medium output is defined as:

l2 = −(1/N) Σ_{k=1}^{N} (1/M_k) Σ_{j=1}^{M_k} Σ_{i=1}^{C} g^{k,j}_i log(p^{m,k,j}_i)  (2)

where p^{m,k,j}_i is the ith channel value of the jth pixel in the kth medium predicted map, and g^{k,j}_i is the ith channel value of the jth pixel in the kth ground truth map.

The final objective function is defined as the weighted sum of the above two losses:

ℓ = l1 + α · l2 + λ · ‖W‖²₂  (3)

where α is the relatively important coefficient for l2, and λ is a regularizing coefficient.

## Results

### 4. Experimental results

#### 4.1. Datasets and implementation

##### 4.1.1. Experimental datasets

Yuan et al. [44] created virtual smoke datasets with accurate semantic annotations using techniques of computer simulation and volume rendering. Extensive experiments [44] also validated that these virtual smoke images can cover most visual appearances of smoke, and their models trained on these virtual datasets have achieved good results on both virtual and real smoke images. There are great differences between training and test virtual samples. The training dataset has 70,632 smoke images with RGB channels synthesized by blending virtual smoke images with real background images, and each synthesized smoke image has the size of 256 × 256. The training images are divided into a training set and a verification one at a ratio of 8 to 2. Specifically, there are 56,505 and 14,127 images in the training and validation datasets, respectively. We have three virtual test datasets, named DS01, DS02 and DS03, for comparisons. Each test dataset is composed of 1000 RGB smoke images. Each sample from test datasets has 256 × 256 pixels and an annotation mask. Among the three synthesized test datasets, DS02 contains more sparse smoke, leading to more complicated mixtures of virtual smoke and background textures.

Fig. 5 shows composited smoke images of the three test datasets, corresponding ground truths, binarized density maps, and predicted images by our methods. Each original ground truth in the test datasets is a gray-scale density map with 8 bits. Following [44], we binarize the density maps of the test datasets for all experiments. The pixel-wise conversion is simply formulated as:

g_j = 1 if a_j ≥ Th; 0 else  (4)

where a_j is the jth pixel of an original ground truth image, g_j is its corresponding binary version, and Th is a predefined threshold. In our implementation, we also adopt Th = 50/255 ≈ 0.2, i.e., if a pixel has more than a smoke density of 0.2, we regard the pixel as a smoke object, otherwise it is viewed as a non-smoke one.

> Fig. 5. Some images from the three test datasets. (a) Composited smoke images, (b) Density maps, (c) Ground truths by binarizing density maps, and (d) our predicted images.

##### 4.1.2. Experimental setting

We implemented our method using Python and PyTorch with batch normalization, and trained it using the Stochastic Gradient Descent (SGD). The learning rate, momentum and weight attenuation parameters are set to 0.01, 0.9 and 1e-5, respectively. The optimized weight α for the auxiliary loss is set to 0.5.

#### 4.2. Evaluation metrics

To evaluate the performance of our model, we adopt the mean Intersection over Union (mIoU) as the evaluation index of segmentation results. In addition, we also use the parameter number, the model size, the Floating-point operations (FLOPs) and the Frames Per Second (FPS) for efficiency comparisons, which are widely used to evaluate the timing performance of lightweight semantic segmentation algorithms. To be specific, the mIoU reflects the degree of coincidence between a predicted result and its corresponding ground truth. The number of model parameters and the model size can measure memory consumption and computation complexity. The mean Intersection over Union (mIoU) is defined as:

mIoU = (1/C) Σ_{i=1}^{C} p_ii / (Σ_{j=1}^{C} p_ij + Σ_{j=1}^{C} p_ji − p_ii)  (5)

where p_ij is the pixel number of class i predicted as class j, and C is the number of classes. The FPS is defined as:

FPS = N / Σ_{i=1}^{N} T_i  (6)

where N is the number of images, and T_i represents the seconds for processing the ith image by the algorithm.

#### 4.3. Ablation experiments

##### 4.3.1. Ablation study for modules

To verify the importance of our modules, we conduct a series of ablation experiments by removing some modules or replacing some with other network structures. Therefore, six variants of our method are designed, as described in Table 2. The comparison results by the six variants are shown in Table 3. According to the experimental results, we have several important conclusions.

> Table 2. Detailed description of our variants.

| Method | Description of our variants |
|---|---|
| Model1 | Replace the CSSAM in our method with the SS-nbt in the LEDNet |
| Model2 | Replace the decoder in our method with the APN in the LEDNet |
| Model3 | Replace the spatial enhancement module with the SPM in DANet |
| Model4 | Replace the channel attention module with the CAM in DANet |
| Model5 | Remove the spatial enhancement module from our method |
| Model6 | Remove the seghead branch (l2) from our method |

> Table 3. Comparison results of our variants.

| Method | DS01 mIoU (%) | DS02 mIoU (%) | DS03 mIoU (%) |
|---|---|---|---|
| Model1 | 69.8 | 68.2 | 68.3 |
| Model2 | 70.6 | 68.7 | 68.1 |
| Model3 | 71.2 | 69.1 | 69.9 |
| Model4 | 71.6 | 69.5 | 69.1 |
| Model5 | 70.1 | 67.8 | 68.0 |
| Model6 | 72.5 | 70.8 | 70.9 |
| Our method | 74.2 | 72.5 | 72.8 |

First, replacing the CSSAM in our method with other module greatly reduces prediction accuracy by about 4.5%. The main reason is that our CSSAM module provides a large amount of smoke texture information, which effectively decreases useless information. Second, removing the Spatial Enhancement Module (SEM) causes the performance of our method directly decreases by about 3%, indicating that our SEM plays an important role in learning effective features.

##### 4.3.2. Ablation study for loss weights

In addition, we explore the influence of the auxiliary branch on network segmentation accuracy. To find an optimized weight α for regulating the relative importance of the two losses, we experiment with a set of regulation weights ranging between 0 and 1, as shown in Table 4. In the case of α = 0, the accuracy of the algorithm is reduced by about 2% as the training loss function degenerates into a single target loss function. We achieve the best performance when α = 0.5.

> Table 4. Results with different α.

| The weight of α | DS01 mIoU (%) | DS02 mIoU (%) | DS03 mIoU (%) |
|---|---|---|---|
| 0 | 72.5 | 70.8 | 70.9 |
| 0.25 | 73.8 | 71.9 | 72.0 |
| 0.5 (our method) | [row values truncated in source] | | |

#### 4.4. Comparisons with other methods

To evaluate the performance of our network, we tested our method on three synthetic datasets and one real smoke dataset, and compared the results of our method with those of several excellent semantic segmentation methods based on deep learning. These comparison networks include some light-weight semantic segmentation networks, such as ERFNet [12], LEDNet [13], DFANet [14], CGNet [31], and several smoke segmentation networks, such as DSS [44], Frizzi [45], W-Net [46]. For the sake of fairness, we used the same dataset and configuration to train all the comparison methods.

Table 5 lists the quantitative results of these comparison methods on the three synthetic datasets. Our method achieves satisfying performance on the three synthetic datasets. Our method already surpasses most of existing segmentation networks, no matter what mIoU, parameter numbers or model sizes. Due to the blurry edge of smoke, the prediction with final large upsampling is prone to leading to obviously jagged edges and lower accuracy, such as LEDNet [13] and DFANet [14]. To avoid these problems, our method not only supervises the final prediction, but also imposes a loss on the middle feature map with the smallest resolution containing more global contexts. The mIoUs achieved by our method on DS01 are 3.2%, 3.8% and 1.1% higher than those by DSS [44], Frizzi [45] and W-Net [46], respectively. Our method achieves the highest accuracy among these comparison methods on DS01.

> Table 5. Comparisons of different methods on the three synthetic test datasets.

| Methods | DS01 mIoU (%) | DS02 mIoU (%) | DS03 mIoU (%) | #Parameters (M) | Model size (MB) | FLOPs | FPS |
|---|---|---|---|---|---|---|---|
| ERFNet [12] | 69.9 | 67.9 | 68.7 | 2.06 | 15.8 | 3.69 G | 60.5 |
| LEDNet [13] | 69.0 | 67.8 | 68.5 | 0.91 | 7.18 | 1.44 G | 58.9 |
| DFANet [14] | 63.2 | 59.4 | 61.8 | 2.18 | 16.9 | 0.45 G | 32.4 |
| CGNet [31] | 68.6 | 65.5 | 67.2 | 0.49 | 3.94 | 0.87 G | 53.0 |
| DSS [44] | 71.0 | 71.0 | 69.8 | 29.9 | – | – | 32.5 |
| Frizzi [45] | 70.4 | 70.0 | 70.7 | 57.0 | – | – | 60.4 |
| W-Net [46] | 73.1 | 74.0 | 73.4 | 31.1 | 127 | – | – |
| Our method | 74.2 | 72.5 | 72.8 | 0.88 | 6.88 | 1.15 G | 68.8 |

The FLOPs of networks is approximately proportional to the number of parameters and the model size, and the FPS of networks is inversely proportional to the parameter number, model size and FLOPs. Our method obtains the second highest mIoUs on DS02 and DS03 among all compared methods. According to Table 5, our method has only 0.88 M parameters that are smaller than other methods. W-Net [46] achieves slightly higher mIoUs on DS02 and DS03 than our method. However, our method has far less parameters than W-Net [46]. The first reason for the high efficiency of our method is that we do not use large networks as the backbone network for encoding, such as ResNet [5], VGG16 [49] and Unet [58]. Another reason may be that our method does not use learnable de-convolutions to restore the size of feature maps, leading to great decreasing of computational complexity and memory consumption. Although our model ranks in the middle position in term of FLOPs, our segmentation accuracy significantly exceeds those of other lightweight models. In other words, our method achieves excellent performance of both accuracy and computation, and it is more qualified for real-time smoke segmentation applications than other methods.

Fig. 6 shows visualized segmentation results of synthetic smoke images by these compared methods. In order to better illustrate the superiority of our method, we select some segmentation results of representative examples for analysis. It can be found that the segmentation results by our network on all selected samples are significantly better than other comparison methods, especially on challenging images that are very difficult for human to distinguish. For images with smoke obviously different from the background, as shown in the second to fifth rows of Fig. 6, some methods produced obviously incorrect segmentation and inaccurate smoke edges, but most methods obtained the relatively accurate localization of smoke. As for inconspicuous smoke, as shown in the second and last two rows of Fig. 6, most comparison methods generated seriously wrong segmentations. However, our network obtains more accurate location and obviously clearer edge details of smoke regions, especially on inconspicuous smoke images.

> Fig. 6. Results on synthetic smoke images. (a) Synthetic smoke images. (b) Density maps by computer simulation. (c) Ground truths by binarizing density maps. Segmented results by (d) LEDNet, (e) CGNet, (f) DFANet, (g) ERFNet and (h) our methods.

Fig. 7 shows the visualized segmentation results by comparison methods on the real smoke dataset [59]. The 143 real smoke images of the dataset were manually annotated. Most methods achieve good segmentation results on real smoke images, which are basically consistent with real smoke regions. By visually comparing these results, we find that our method obtains the best results. For images with inconspicuous smoke and smoke-like objects, our network also obtains higher accuracy than other methods, as shown in the third rows of Fig. 7. DFANet misclassifies smoke-like clouds as smoke. In addition, we also conduct quantitative comparisons on the 143 annotated real smoke images, and the mIoUs by these compared methods are shown in Table 6. It is worth mentioning that our method was only trained on the synthetic smoke dataset. According to Table 6, our method achieves the highest mIoU on the 143 real smoke images among all compared methods.

> Fig. 7. (a) Visualized results on real smoke images. Segmented results by (b) LEDNet, (c) CGNet, (d) DFANet, (e) ERFNet and (f) our methods.

> Table 6. Comparisons of different lightweight semantic segmentation methods on the 143 annotated real smoke images.

| Methods | ERFNet | LEDNet | DFANet | CGNet | Our method |
|---|---|---|---|---|---|
| mIoU% | 60.3 | 57.7 | 54.3 | 57.6 | 65.2 |

In addition, to further enhance the performance of our network on real images, we specifically involve a small real smoke dataset [59] into the training dataset. The real dataset includes 416 smoke images, in which 143 images have pixel-level labels (ground truth). We first use data augmentation to expand 143 images and labels, and integrate the augmented real smoke dataset into the synthetic smoke training dataset to produce a real and synthetic mixed dataset. Then we re-train our model using the mixed dataset, and test the remaining 273 images without labels. Fig. 8 shows the visualization results of our method on some challenging samples. Our method is not seriously disturbed by the background and obtains excellent segmentation results. There are obvious background blurring problems in the second to fourth samples with smoke-like objects, such as clouds. Some regions of smoke in the third sample are even hard to distinguish by humans, but our method achieves acceptable results.

> Fig. 8. Results of our method on some real smoke images.

## Conclusion

### 5. Conclusions

In this paper, we propose a light-weighted real-time smoke segmentation network to solve the challenging task of smoke semantic segmentation on mobile or computation limited devices. The proposed method achieves an effective balance between segmentation accuracy and inference speed. In order to achieve powerful features and fast processing speed, we propose a Channel Split and Shuffle Attention Module based on a ResNet-Style encoder to extract long-range information for effectively representing smoke texture features and reducing useless information. To improve the segmentation performance of small or inconspicuous smoke objects, a spatial enhancement module is proposed to learn the spatial interdependence of smoke features, and the channel attention module is designed to capture the inter-channel interdependence. By establishing these rich contextual dependencies on features, the results of smoke segmentation are significantly improved. On the other hand, we design a feature fusion module to enhance feature representation by fusing spatial enhancement and channel attention modules. Finally, the fused result is multiplied by the output of a global coefficient path to refine the smoke segmentation results of our network. Compared with existing state-of-the-art semantic segmentation algorithms, our method consistently outperforms these comparison algorithms on three synthetic smoke datasets and real smoke images, and its parameters are less than 1 M.

## Acknowledgments

This work was partially supported by the National Natural Science Foundation of China (62272308), Capacity Construction Project of Shanghai Local Colleges (23010504100), the Joint Key Fund of National Natural Science Foundation of China (U2033218), and the Major Project of New Generation Artificial Intelligence for Scientific and Technological Innovation 2030 (2020AAA0109300).

## References

[1] L. Yann, L. Bottou, Y. Bengio, P. Haffner, Gradient-based learning applied to document recognition, Proc. IEEE 86 (11) (1998) 2278–2324.
[2] A. Borji, M. Cheng, Q. Hou, H. Jiang, J. Li, Salient object detection: A survey, Comput. Vis. Media 5 (2) (2019) 117–150.
[3] O. Ronneberger, P. Fischer, T. Brox, U-net: convolutional networks for biomedical image segmentation, in: Proceedings of the International Conference on Medical image computing and computer-assisted intervention, 2015, pp. 234–241.
[4] L. Jonathan, S. Evan, D. Trevor, Fully convolutional networks for semantic segmentation, IEEE Trans. Pattern Anal. Mach. Intell. 39 (4) (2017) 640–651.
[5] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, in: Proceedings of the Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 770–778.
[6] L.C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, A.L. Yuille, Deeplab: semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected CRFs, IEEE Trans. Pattern Anal. Mach. Intell. 40 (4) (2018) 834–848.
[7] J. Fu, J. Liu, H. Tian, Y. Li, Y. Bao, Z. Fang, H. Lu, Dual attention network for scene segmentation, in: Proceedings of the Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 3141–3149.
[8] F. Yuan, Video-based smoke detection with histogram sequence of LBP and LBPV pyramids, Fire Saf. J. 46 (3) (2011) 132–139.
[9] F. Yuan, A double mapping framework for extraction of shape-invariant features based on multi-scale partitions with AdaBoost for video smoke detection, Pattern Recognit. 45 (12) (2012) 4326–4336.
[10] A. Paszke, A. Chaurasia, S. Kim, E. Culurciello, "ENet: a deep neural network architecture for real-time semantic segmentation," arXiv preprint arXiv:1606.02147, 2016.
[11] C. Yu, J. Wang, C. Peng, C.X. Gao, G. Yu, N. Sang, BiSeNet: bilateral segmentation network for real-time semantic segmentation, in: Proceedings of the European Conference on Computer Vision (ECCV), 2018.
[12] E. Romera, J.M. Álvarez, L.M. Bergasa, R. Arroyo, ERFNet: efficient residual factorized ConvNet for real-time semantic segmentation, IEEE Trans. Intell. Transp. Syst. 19 (1) (2018) 263–272.
[13] Y. Wang, Q. Zhou, J. Liu, J. Xiong, L.J. Latecki, LEDNet: a lightweight encoder-decoder network for real-time semantic segmentation, in: Proceedings of the IEEE International Conference on Image Processing (ICIP), 2019, pp. 1860–1864.
[14] H. Li, P. Xiong, H. Fan, J. Sun, DFANet: deep feature aggregation for real-time semantic segmentation, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 9514–9523.
[15] F. Yuan, Y. Zhou, X. Xia, X. Qian, J. Huang, A confidence prior for image dehazing, Pattern Recognit. 119 (2021) 1–16.
[16] S. Yin, X. Yang, Y. Wang, Y.H. Yang, Visual attention dehazing network with multi-level features refinement and fusion, Pattern Recognit. 118 (2021) 108021.
[17] X. Liu, W. Ma, X. Ma, J. Wang, LAE-Net: a locally-adaptive embedding network for low-light image enhancement, Pattern Recognit. 133 (2023) 109039.
[18] G. Lin, C. Shen, A. van den Hengel, I. Reid, Efficient piecewise training of deep structured models for semantic segmentation, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 3194–3203.
[19] S. Zheng, S. Jayasumana, B. RomeraParedes, V. Vineet, Z. Su, D. Du, C. Huang, P. Torr, Conditional random fields as recurrent neural networks, in: Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2015, pp. 1529–1537.
[20] J. Lafferty, A. McCallum, F. Pereira, Conditional random fields: probabilistic models for segmenting and labeling sequence data, in: Proceedings of the Eighteenth International Conference on Machine Learning, 2001, pp. 282–289.
[21] F. Yu, V. Koltun, Multi-scale context aggregation by dilated convolutions, in: Proceedings of the International Conference on Learning Representations (ICLR), 2016.
[22] X. Wang, R. Girshick, A. Gupta, K. He, Non-local neural networks, in: Proceedings of the Conference on Computer Vision and Pattern Recognition (CVPR), 2018.
[23] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. Gomez, Ł. Kaiser, I. Polosukhin, "Attention is all you need," in: Neural Information Processing Systems (NeurIPS), 2017.
[24] Y. Luo, Q. Huang, X. Li, Segmentation information with attention integration for classification of breast tumor in ultrasound image, Pattern Recognit. 124 (2022) 108427.
[25] M. Cordts, M. Omran, S. Ramos, T. Rehfeld, M. Enzweiler, R. Benenson, U. Franke, S. Roth, B. Schiele, The cityscapes dataset for semantic urban scene understanding, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 3213–3223.
[26] M. Everingham, L. Gool, C. Williams, J. Winn, A. Zisserman, The pascal visual object classes (VOC) challenge, Int. J. Comput. Vis. (2010) 303–338.
[27] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, L. Kaiser, I. Polosukhin, "Attention is all you need," in Advances in Neural Information Processing Systems, pp. 5998–6008, 2017.
[28] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, N. Houlsby, An image is worth 16x16 words: transformers for image recognition at scale, in: Proceedings of the International Conference on Learning Representations, 2021.
[29] Shi Yi, Xi Liu, Junjie Li, Ling Chen, UAVformer: a composite transformer network for urban scene segmentation of UAV images, Pattern Recognit. 133 (2023) 109019.
[30] F. Yuan, Z. Zhang, Z. Fang, "An effective CNN and transformer complementary network for medical image segmentation", Pattern Recognition, online, 30 November 2022, 109228, 10.1016/j.patcog.2022.109228.
[31] T. Wu, S. Tang, R. Zhang, J. Cao, Y. Zhang, CGNet: a light-weight context guided network for semantic segmentation, IEEE Trans. Image Process. 30 (2021) 1169–1179.
[32] T. Emara, H.E.A.E. Munim, H.M. Abbas, LiteSeg: a novel lightweight ConvNet for semantic segmentation, in: Proceedings of the Digital Image Computing: Techniques and Applications (DICTA), 2019, pp. 1–7.
[33] H. Zhao, X. Qi, X. Shen, J.P. Shi, J.Y. Jia, "ICNet for real-time semantic segmentation on high-resolution images," arXiv preprint arXiv:1704.08545, 2017.
[34] F. Chollet, Xception: deep learning with depthwise separable convolutions, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 1800–1807.
[35] K. Dimitropoulos, P. Barmpoutis, N. Grammalidis, Higher order linear dynamical systems for smoke detection in video surveillance applications, IEEE Trans. Circuits Syst. Video Technol. 27 (5) (2017) 1143–1154.
[36] Y. Zhao, Candidate smoke region segmentation of fire video based on rough set theory, J. Electr. Comput. Eng. 2015 (2015) 1–8.
[37] N. Zhang, H. Wang, Y. Hu, A smoke image segmentation algorithm based on rough set and region growing, J. Front. Comput. Sci. Technol. 11 (8) (2015) 1296–1299.
[38] A. Filonenko, D.C. Hernandez, K.-H. Jo, Fast smoke detection for video surveillance using CUDA, IEEE Trans. Ind. Inform. 14 (2) (2018) 725–733.
[39] Y. Jia, G. Lin, J. Wang, J. Fang, Y. Zhang, Early video smoke segmentation algorithm based on saliency detection and Gaussian mixture model, Comput. Eng. 42 (2) (2016) 206–209.
[40] Y. Luo, L. Zhao, P. Liu, D. Huang, Fire smoke detection algorithm based on motion characteristic and convolutional neural networks, Multimed. Tools Appl. 77 (12) (2018) 15075–15092.
[41] H. Tian, W. Li, P.O. Ogunbona, L. Wang, Detection and separation of smoke from single image frames, IEEE Trans. Image Process. 27 (3) (2018) 1164–1177.
[42] R. Kaabi, M. Sayadi, M. Bouchouicha, F. Fnaiech, E. Moreau, J.M. Ginoux, Early smoke detection of forest wildfire video using deep belief network, in: Proceedings of the 4th International Conference on Advanced Technologies for Signal and Image Processing (ATSIP), 2018, pp. 1–6.
[43] X. Li, Z. Chen, Q.M.J. Wu, C. Liu, 3D Parallel fully convolutional networks for real-time video wildfire smoke detection, IEEE Trans. Circuits Syst. Video Technol. 30 (1) (2020) 89–103.
[44] F. Yuan, L. Zhang, X. Xia, B. Wan, Q. Huang, X. Li, Deep smoke segmentation, Neurocomputing 357 (2019) 248–260.
[45] S. Frizzi, M. Bouchouicha, Ginoux Jean-Marc, E. Moreau, M. Sayadi, Convolutional neural network for smoke and fire semantic segmentation, IET Image Process. 15 (6) (2021) 634–647.
[46] F. Yuan, L. Zhang, X. Xia, Q. Huang, X. Li, A wave-shaped deep neural network for smoke density estimation, IEEE Trans. Image Process. 29 (2020) 2301–2313.
[47] J. Wang, X. Hu, Convolutional neural networks with gated recurrent connections, IEEE Trans. Pattern Anal. Mach. Intell. (2021) online, doi: 10.1109/TPAMI.2021.3054614.
[48] F. Yuan, L. Zhang, X. Xia, Q. Huang, X. Li, A gated recurrent network with dual classification assistance for smoke semantic segmentation, IEEE Trans. Image Process. 30 (2021) 4409–4422.
[49] K. Simonyan, A. Zisserman, Very deep convolutional networks for large-scale image recognition, in: Proceedings of the International Conference on Learning Representation, 2014.
[50] F. Yuan, Z. Dong, L. Zhang, X. Xia, J. Shi, Cubic-cross convolutional attention and count prior embedding for smoke segmentation, Pattern Recognit. 131 (2022) 108902.
[51] A.G. Howard, M.L. Zhu, B. Chen, D. Kalenichenko, W.J. Wang, T. Weyand, M. Andreetto, H. Adam, "Mobilenets: efficient convolutional neural networks for mobile vision applications," arXiv preprint arXiv:1704.04861, 2017.
[52] X. Zhang, X. Zhou, M. Lin, J. Sun, ShuffleNet: an extremely efficient convolutional neural network for mobile devices, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2018, pp. 6848–6856.
[53] J. Hu, L. Shen, S. Albanie, G. Sun, E. Wu, Squeeze-and-excitation networks, IEEE Trans. Pattern Anal. Mach. Intell. 42 (8) (2020) 2011–2023.
[54] L.C. Chen, Y. Yang, J. Wang, W. Xu, A.L. Yuille, Attention to scale: scale-aware semantic image segmentation, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 3640–3649.
[55] X. Wang, R. Girshick, A. Gupta, K. He, Non-local neural networks, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2018, pp. 7794–7803.
[56] C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens, Z. Wojna, Rethinking the inception architecture for computer vision, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 2818–2826.
[57] Q.B. Hou, M.M. Cheng, X.W. Hu, A. Borji, Z.W. Tu, P.H.S. Torr, Deeply supervised salient object detection with short connections, IEEE Trans. Pattern Anal. Mach. Intell. 41 (4) (2019) 815–828.
[58] O. Ronneberger, P. Fischer, T. Brox, U-Net: convolutional networks for biomedical image segmentation, in: Proceedings of the International Conference on Medical image computing and computer-assisted intervention, 9351, Cham, Springer, 2015, pp. 234–241.
[59] Smoke Semantic Segmentation. Accessed: Feb. 2, 2021. [Online]. Available: https://github.com/rekon/Smoke-semantic-segmentation

## Other

### Footnotes

E-mail address: zjfang@sues.edu.cn (Z. Fang). 1 Co-first authors.

### Declaration of Competing Interest

The authors declared that they have no conflicts of interest to this work. We declare that we do not have any commercial or associative interest that represents a conflict of interest in connection with the work submitted.

### Data availability

Data will be made available on request.

### Author biographies

Feiniu Yuan received his B. Eng. and M. Eng. degrees in mechanical engineering from Hefei University of Technology, Hefei, China, in 1998 and 2001, respectively, and his Ph.D. degree in pattern recognition and intelligence system from University of Science and Technology of China (USTC), Hefei, China, in 2004. From 2004 to 2006, he worked as a post-doctor with State Key Lab of Fire Science, USTC. From 2010 to 2012, he was a Senior Research Fellow with Singapore Bioimaging Consortium (SBIC), Agency for Science, Technology And Research (A∗STAR), Singapore. He is currently a professor, a PhD supervisor and a vice dean with College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, China. His research interests include deep learning, image segmentation, pattern recognition and 3D modeling.

Kang Li received his B.Eng. degrees in information and communication engineering from Huaibei Normal University, Huaibei, China, in 2018. He is currently an M.E. candidate with College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, Shanghai, China. His research interests include deep learning, image segmentation.

Chunmei Wang received her B. Eng. and M. Eng. degrees in electronic engineering from Inner Mongolia University, Hohhot, China, in 1991 and 2001, respectively, and her Ph.D. degree in pattern recognition and intelligence system from East China University of Science and Technology (ECUST), Shanghai, China, in 2011. She is currently an associate professor, a Master supervisor with College of Information, Mechanical and Electrical Engineering, Shanghai Normal University, China. Her research interests include deep learning, image segmentation, pattern recognition, signal processing and application.

Zhijun Fang is a professor and the dean of School of Electronic and Electrical Engineering, Shanghai University of Engineering Science. He obtained his PhD degree in Shanghai Jiaotong University and was a visiting scholar in University of Washington. He is a senior member of IEEE/ACM/CCF/CAAI/CSIG. His current research interests include image & video processing, machine vision, and intelligent data analysis.
