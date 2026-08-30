## III. THE PROPOSED METHOD

Fig. 2 shows the overall framework of our Classificationassisted Gated Recurrent Network (CGRNet), which mainly contains four important modules, including an Xception network [66] for basic feature extraction, a semantic segmentation module with four branches, a classification module for assisting segmentation, and a fusion module.

### A. Basic Feature Extraction Module

[...] with 126 layers. This is mainly due to the usage of depthwise separable convolutions, which can greatly reduce the number of network parameters without obviously reducing performance.

### B. Semantic Segmentation Module

As shown in Fig. 2a, we propose a semantic segmentation module mainly consisting of four branches. Each branch acquires feature maps with different scales. Multi-scale features extracted in encoding stages of the segmentation module are fused in a bottom-to-up manner. Encoding stages embed abundant semantic information about scenes into feature maps, while decoding stages of the segmentation module are responsible for re-interpreting semantic information to produce final segmentation results. Low-level features learned by shallow layers have high resolution but lack semantic information. High-level features from deep layers contain rich semantic information but seriously lack spatial detail information. A common way for improving performance is to combine different level features.

Low-level features are of high resolution, but often contain too much noisy or interferential information, leading to instability of providing abundant high-resolution semantic guidance [68]. Aiming at solving this problem, we propose to add high-level features of Stage 4 to decoding layers of low-level stages, i.e. Stages 1, 2, and 3, as illustrated by dash lines in Fig. 2a. In this way, we improve decoding stability of semantic information by combining low-level and high-level features.

1) Attention Convolutional GRU: To enhance the ability of feature representation in decoding stages, we propose an Attention Convolutional Gated Recurrent Unit (Att-ConvGRU) to fuse features from different levels, as shown in Fig. 3. To preserve the spatial correlation of 2D features, we propose the Att-ConvGRU by first replacing all fully connected layers of the 1D GRU [3] with convolutional ones and then connecting the input signal Xt with the hidden state Ht−1. Convolutional layers are shared to reduce the number of parameters and computational complexity. The proposed Att-ConvGRU can be mathematically described as follows:

Zt = σ(Wz ∗ [Ht−1, Xt] + bz)    (1)

Rt = σ(Wr ∗ [Ht−1, Xt] + br)    (2)

At = σ(Wa ∗ GlobalAvgPool([Ht−1, Xt]))    (3)

X′t = At ⊙ Xt    (4)

H′t = tanh(Wh ∗ [Rt ⊙ Ht−1, X′t] + bh)    (5)

Ht = λ((1 − Zt) ⊙ Ht−1 + Zt ⊙ H′t)    (6)

where σ is the sigmoid function, [], ∗ and ⊙ denote operations of concatenation, convolution and Hadamard product, respectively, and λ is a learnable parameter with an initial value of 1. Like the original GRU, Zt is the update gate, Rt is the reset gate, Xt is the input of the current GRU, Ht−1 is the hidden layer status and the output of the previous GRU, and Ht is the hidden layer status and the output of the current GRU. By learning the inherent semantic relationship of features, our Att-ConvGRU can iteratively generate more highquality feature maps in a coarse-to-fine manner for enhancing robustness.

[...] attention module that uses previous state Ht−1 to guide current decision. By introducing an attention mechanism into the convolutional GRU, our method can mine the inherent semantic relations of fused features and learn the spatial dependence between different feature maps. High-level information effectively guides the bottom-to-up feed forward processing of data. The structure of our attention module is shown in Fig. 4.

2) Multi-Stage Stacking of Att-ConvGRUs: To extract more powerful features, we stack several Att-ConvGRUs together to construct a deeper network sharing the same weights during the cycles. The internal structure of Att-ConvGRU is complicated, so too many cycles will seriously reduce computational efficiency. By making a tradeoff between accuracy and efficiency, we connect only two Att-ConvGRUs in each stage for our CGRNet, as shown in Fig. 2a. A 1 × 1 convolutional layer first maps the output features of four encoding stages to features with 128 channels, each of which is then sent to the input layer of the first Att-ConvGRU at each stage. The output of the first Att-ConvGRU layer is used as the input of the next Att-ConvGRU layer at the same stage. To fuse features from different levels, we conduct similar operations for Att-ConvGRUs in adjacent stages, i.e. the output of the nth stage Att-ConvGRU as the input of the (n-1)th stage Att-ConvGRU. In addition, we use the output of MCCL in Stage 4 as the input of Att-ConvGRUs to deal with the problem of inconspicuous objects and large between-class similarity.

Table I lists a detailed description of the inputs for each AttConvGRU in our model. The input Ht to each Att-ConvGRU in Stage 4 is null, so the computation is slightly different from Att-ConvGRUs in other stages. In other words, the computation of Att-ConvGRUs in Stages 1 to 3 is described by Eq. 1 to Eq. 6, while each Att-ConvGRU in Stage 4 is formulated as follows:

Zt = σ(Wz ∗ Xt + bz)    (7)

At = σ(Wa ∗ GlobalAvgPool(Xt))    (8)

X′t = At ⊙ Xt    (9)

H′t = tanh(Wh ∗ X′t + bh)    (10)

Ht = Zt ⊙ H′t    (11)

To further enhance spatial details, we add a spatial attention module at the end of the multi-stage stacked structure of two-layer Att-ConvGRUs, as shown in Fig. 2b. The spatial attention module performs the average and max pooling operations on the input feature map along the channel direction, and then sends the sum of the two feature maps to a 3 × 3 sigmoid convolutional layer to generate a spatial attention map, which is pixel-wisely multiplied with the input feature map to obtain the spatially weighted features.

3) Multi-Scale Context Contrasted Local Feature: Highlevel features tend to contain more abstract and global information about the whole image, so most deep segmentation algorithms have achieved good results for the dominated objects in the image. However, natural images often contain many inconspicuous objects. Local and context information is more important for detecting them. To solve this problem, Ding et al. [18] proposed a Context Contrasted Local (CCL) model to compute a contrast between the separated context and local information. The model achieved satisfactory results for inconspicuous objects.

Most smoke can be viewed as inconspicuous objects, since smoke areas are often small and inconspicuous for early fire, and smoke is usually semi-transparent and of low contrast. We modify the network structure of CCL[18] to propose a Multi-scale Context Contrasted Local (MCCL) for our semantic segmentation module, as shown Fig. 5. CCL uses several context-local blocks in tandem and each block just enhances contrast between the outputs of atrous convolutions with rate = 1 and rate = 5. The number of scales is too less and not effective for inconspicuous objects with multiple scales. Higherlevel features are more beneficial to semantic segmentation, so MCCL is placed in Stage 4. To effectively process the output feature map with a size of 16∗16, the maximum dilation rate of atrous convolutions is set to 6. To further aggregate multi-scale context contrasted local features, we expand the rates of atrous convolutions to the range of 1, 2, 4 and 6, and then concatenate the contrast feature maps computed from every two of them.

To further extract multi-scale information, we propose a novel Dense Pyramid Pooling Module (DPPM) for our MCCL. Our MCCL has more rates for atrous convolutions and fewer parameters than the CCL, and it can extract multi-level and multi-scale context contrasted local features for inconspicuous smoke segmentation.

4) Dense Pyramid Pooling Module: There exists a common problem of ambiguous categories for image segmentation tasks. It is extremely challenging for most methods to segment objects with similar appearance. To solve the appearance ambiguity problem, Zhao et al. [31] proposed a Pyramid Pooling Module (PPM) to fuse features from four different pyramid scales by pooling operations with several kernels of different strides. The appearance ambiguity problem also exists for smoke segmentation. For example, clouds, haze and smoke share very similar visual patterns, so existing methods cannot discriminate them.

Therefore, we modify PPM to propose a Dense Pyramid Pooling Module (DPPM), as shown in Fig. 6. Inspired by the idea of DenseNet [28], we expand PPM to the dense style and cancel the concatenation operation of input and output features. Compared with PPM, our DPPM can generate features including larger receptive fields but with fewer parameters. Our DPPM actually extracts more context information in a more efficient manner. Different from DenseASPP [29], our DPPM upsamples feature maps at each stage, and also concatenates feature maps from different stages to obtain multi-scale features.

### C. Classification and Fusion Module

Another highlight of our method is that we use classification results to assist the segmentation module to improve segmentation accuracy. The structure of the classification assistance module is shown in the bottom row of Fig. 2a. Global information of input signals is very important for classification. The global average pooling [28], [69] is commonly used, and it summarizes spatial information of features to obtain global contextual knowledge about objects. The global max pooling usually preserves the most important and dominant information from features. Therefore, we collect the feature maps of the last separable convolution layer of the Xception network in the feature extraction module, and then use both a global average pooling and a global max pooling to generate discriminative features.

Discriminative features are first fused by a concatenation operation, and then divided into two classification branches p1 and p2. The design of branch p1 is inspired by the Squeeze-and-Excitation Network (SENet) [70], which can effectively improve the network representation ability by a Squeeze and Excitation block (SE). Its purpose is to model the inter-dependence between convolutional feature channels. We use a fully connected layer to learn the global information of corresponding features, which are used to selectively emphasize beneficial features and suppress useless ones. Then, we directly multiply the classification result of the p1 branch with the output of the segmentation module to refine segmentation results at image level. In this way, the p1 branch provides global information to implicitly distinguish objects with similar appearance. In addition, the p2 branch can directly produce the classification result of the input image for explicitly eliminating misclassified smoke-like objects. To better illustrate the benefit of our improvements, we perform extensive ablation experiments to verify our strengths in the experimental section.

### D. Loss and Final Result

Smoke segmentation is actually a dense classification problem of two categories over each pixel, so we adopt a binary cross-entropy loss, defined as:

l1 = −(1/N) Σ_k (1/Mk) Σ_j [gk_j log pk_j + (1 − gk_j) log(1 − pk_j)]

where N is the image number of the train set, Mk is the pixel number of the kth image, and pk_j and gk_j are the values of the jth pixel in the predicted map and the ground truth map of the kth image, respectively.

Similarly, a binary cross-entropy loss is also used for image classification over the whole image instead of each pixel, formulated as:

l2 = −(1/N) Σ_k [gk log pk + (1 − gk) log(1 − pk)]

where pk and gk are the predicted smoke probability and the label of the kth image, respectively.

The final objective function is defined as the weighted sum of the above two losses:

L = l1 + α · l2 + λ · ∥W∥2

where α is the weight of l2, and λ is a regularizer weight. To evaluate the importance of α for training, we conduct several experiments in the next section to show the impact of different α values.
