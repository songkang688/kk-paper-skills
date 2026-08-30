<!--
FnyPro-1 Stage 00 Wave 3 Agent G clean corpus
Paper_ID: 07_CGRNet_TIP2021_Gated_Recurrent_Smoke_Semantic_Segmentation
Source: /workspace/07_CGRNet_TIP2021_Gated_Recurrent_Smoke_Semantic_Segmentation.md (**Original:** blocks only)
Fixes applied: title/byline de-interleaved (S001+S009); IEEE drop-cap "D/EEP" normalized (S010/S011);
dangling-fragment joins (S013->S014, S041->S042, S072->S073, S079->S080, S088->S089); table captions
moved out of body (S045, S075, S086, S087); equations (1)-(6) and (7)-(11) and the loss/metric formulas
reconstructed from garbled fragments and FLAGGED inline - verify against PDF before quantitative use.
"[...]" marks text lost at column/page boundaries in the extraction (starts of several paragraphs).
Excluded: Chinese text, reader nav/glossary, first-page footnotes S004-S008 (manuscript history,
funding, affiliations - see section map; funding note lives in footnote S004, no Acknowledgments
section exists in this paper), reference entries (S094-S095: flagged uncertain, truncated at [13]).
No grammar rewriting; authorial wording preserved.
-->

# A Gated Recurrent Network With Dual Classification Assistance for Smoke Semantic Segmentation

Feiniu Yuan, Senior Member, IEEE, Lin Zhang, Xue Xia, Qinghua Huang, and Xuelong Li, Fellow, IEEE

## Abstract

Abstract—Smoke has semi-transparency property leading to highly complicated mixture of background and smoke. Sparse or small smoke is visually inconspicuous, and its boundary is often ambiguous. These reasons result in a very challenging task of separating smoke from a single image. To solve these problems, we propose a Classification-assisted Gated Recurrent Network (CGRNet) for smoke semantic segmentation. To discriminate smoke and smoke-like objects, we present a smoke segmentation strategy with dual classification assistance. Our classification module outputs two prediction probabilities for smoke. The first assistance is to use one probability to explicitly regulate the segmentation module for accuracy improvement by supervising a cross-entropy classification loss. The second one is to multiply the segmentation result by another probability for further refinement. This dual classification assistance greatly improves performance at image level. In the segmentation module, we design an Attention Convolutional GRU module (Att-ConvGRU) to learn the long-range context dependence of features. To perceive small or inconspicuous smoke, we design a Multi-scale Context Contrasted Local Feature structure (MCCL) and a Dense Pyramid Pooling Module (DPPM) for improving the representation ability of our network. Extensive experiments validate that our method significantly outperforms existing stateof-art algorithms on smoke datasets, and also obtain satisfactory results on challenging images with inconspicuous smoke and smoke-like objects.

Index Terms—Smoke semantic segmentation, Dense Pyramid Pooling, Gated Recurrent Network, dual classification assistance, convolutional neural network.

## I. INTRODUCTION

Deep convolutional neural networks (DNN) [1] have achieved great success in recent years in computer vision tasks, such as image classification, object detection, and segmentation. Deep learning based smoke segmentation aims at directly separating smoke regions from a single image. Segmented smoke regions not only provide an important clue for fire detection, but also accurately indicate the location of fire. It is very important for realizing automatic fire detection in intelligent robots to avoid casualties of firefighters.

DCNNs belong to a kind of feed-forward networks and usually have no recurrent structures. Recurrent structures are especially useful for processing sequential data and extracting long-range dependency. Due to lack of recurrent modules, DCNNs have some limitations to some applications. The most serious problem is that with the deepening of networks, it is very difficult to guarantee that the context dependent information of learned features is distinguishable. In recent years, many recurrent structures have been proposed to solve these problems, such as Recurrent Neural Networks (RNN) [2], [3]. However, RNNs also have several inherent problems, such as vanishing or exploding gradients. Long-term dependence is easily implemented by repeating structures with short-term dependence, so many subsequent methods use the Long ShortTerm Memory (LSTM) [2] to replace RNNs. The LSTM is also difficult to train due to its complex internal structure. Gated Recurrent Units (GRU) [3] have lower computational complexity than LSTMs [4], and GRUs can achieve the same performance as LSTMs. The original GRU is mainly used to process one-dimensional sequential data. To better capture spatial correlation and context dependent information of twodimensional features, we propose an attention convolutional GRU module by converting the original GRU into a convolutional GRU and designing an attention mechanism to enhance the ability of the network to extract distinguishable features.

It is a very challenging task to accurately separate smoke from a single image. The main reason may be inconspicuousness of small smoke, highly complicated texture by blending semi-transparent smoke and different background, multiple scales of smoke at fire different evolving stages, and disturbance of smoke-like objects, such as haze and clouds. Some challenging examples for smoke segmentation are shown in Fig. 1. To reduce loss of lives and properties caused by fires, detection methods should find smoke as early as possible [5], [6]. In other words, detection methods should detect smoke when it is very small or inconspicuous at its early evolving stage.

In this paper, we mainly focus on semantic segmentation of small, semi-transparent or multi-scale smoke, and discrimination between smoke, haze and clouds. For small, semi-transparent or inconspicuous smoke as shown in Fig. 1 (a) and (b), we propose a Multi-scale Context Contrasted Local (MCCL) model to capture locally discriminative features, which are computed from the contrast features between multi-scale feature maps filtered by the atrous convolutions with different rates. There are many real objects that share similar appearances to smoke, as shown in Fig. 1(c) and (d). To discriminate between smoke and haze, we propose a Dense Pyramid Pooling Module (DPPM) to incorporate local and global features, and design two classification branches to assist segmentation. For multi-scale smoke as shown in Fig.1 (b) and (e), we follow the way of methods [7]–[10] to fuse features from middle layers, but these methods ignore the fact that different features make different contributions to the task. To address this problem, we propose to use one classification branch to learn weights, which can reflect the interdependence between different channels of convolutional features for robustness improvement.

Extensive experiments show that our method achieves stateof-the-art performance on both synthetic and real smoke images. In summary, the main contributions of our method are listed as follows:

• We propose a smoke segmentation strategy with the dual assistance of image classification. One classification assistance supervises a cross-entropy classification loss in the training stage to explicitly regulate the segmentation module for accuracy improvement at image level. Another one is to multiply the segmentation result with a classification output for further refinement. This strategy significantly improves accuracy of smoke segmentation at image level, since the image classification module can greatly reduce misclassification of smoke-like objects, such as clouds.

• [...] module for the convolutional GRU. As far as we know, this is the first time to apply the attention convolutional GRU to image semantic segmentation.

• To perceive small or inconspicuous smoke, we carefully design two modules for smoke segmentation, including a Multi-scale Context Contrasted Local Feature structure (MCCL) and a Dense Pyramid Pooling Module (DPPM). The MCCL adopts four scales to compute feature differences for enhancement of low contrast smoke. The DPPM is proposed to further provide more context information for our MCCL module.

• We propose an objective function with weighted losses of classification and segmentation for joint optimization of our network. In this way, we can efficiently train the proposed network end-to-end. Besides, we use the Xception network to extract powerful features that are shared by our segmentation and classification modules. Thus we can greatly reduce network parameters and computational complexity.

The remainder of this paper is organized as follows. Related work on semantic segmentation is given in Section II-A, smoke segmentation in Section II-B, and recurrent networks in computer vision in Section II-C. The proposed method is introduced in Section III. In Section IV, experimental results are shown to evaluate the performance of our method. Conclusions are drawn in the last section.

## II. RELATED WORK

### A. Object Semantic Segmentation

1) Multi-Scale Features: There are many ways to obtain multi-scale features. The most common way is to directly extract and combine multi-scale feature maps from different convolutional layers for semantic segmentation, such as FCN [1], OSVOS [11]. These methods usually use encoderdecoder structures, and directly connect the features of encoders to those of decoders. These methods can be further subdivided into two categories. Some methods directly send features from encoder layers without any processing to the corresponding decoder layers, such as U-Net [7], CTN [12], SegFlow[13], methods in [14], [15] and [8]. The others use specially designed modules to process the encoded features, such as GCN and BR of LKM [9], RefineNet [10], EA [16], MMF and RefineNet [17], and CCL and Gated sum [18]. The MSCI [19] uses a special feature fusion method, which adopts an LSTM [2] to intertwine two sets of scaleadjacent features together in a bidirectional and recurrent fashion.

Another way is to make use of the atrous convolution with different rates, which was originally proposed in [20]. Its advantage is to expand receptive fields without changing the size of feature maps. To achieve the same receptive field as VGG16 [21], the atrous convolutions with dilation rates of 2 and 4 are used in the Deeplab v1 [22] for the last three convolutional layers and the first fully connected layer. Subsequently, the Atrous Spatial Pyramid Pooling (ASPP) was proposed in the Deeplab v2 [23], in which multiple parallel atrous convolutional layers with different sampling rates are used to achieve robust segmentation of objects at multiple scales. Jain et al. [24] and Ci et al. [25] directly embedded ASPPs into their models. The Deeplab v3 [26] adopts Batch Normalization (BN) [27] in the ASPP and substitutes a 1∗1 convolution for the atrous convolution with a dilation rate of 24. By borrowing the idea of DenseNet [28] to improve the ASPP, Yang et al. [29] proposed DenseASPP to achieve larger receptive fields. To reduce the number of parameters, Chen et al. [30] replaced the ordinary atrous convolution with the atrous separable convolution. The Pyramid Pooling Module (PPM) [31] combines the features of four different scales generated by pooling operations with different kernels for scene parsing.

2) Multi-Label Semantic Segmentation: Multiple labels usually appear in multi-task applications. The mask R-CNN [32] simultaneously outputs object labels, bounding boxes and semantic segmentation results, so it requires multiple labels to supervise network training. Of course, multiple labels can also be used in single-object tasks. Alshaikhli et al. [33] selected foreground and background labels to segment brain tumors. Payer et al. [34] and Chen et al. [35] proposed similar methods for multi-label tasks. They all designed twostage localization structures by firstly enabling subsequent segmentation networks to focus on object areas and then utilizing multiple labels from different parts of objects to complete segmentation. The M-Net [36] was proposed for a simultaneous multi-label segmentation task of optic discs and cups. The method in [37] was significantly different from the above mentioned methods in a supervised manner. Since it is very expensive to generate per-pixel label maps, Luo et al. [37] proposed to use image-level labels and a small number of per-pixel label maps to complete semi-supervised semantic segmentation. Souly et al. [38] utilized the Generative Adversarial Network (GAN) [39] to perform semisupervised semantic segmentation, in which noise and class labels were used to generate fake segmentation images, while unlabeled data, image-level and pixel-level labels were used to discriminate images generated by the generative network.

Inspired by these methods, we also use segmentation and classification labels for performance improvement in this paper. However, the main difference is that we design several special modules for smoke and use a fully supervised endto-end training method, since we can use fluid simulation methods to generate photo-realistic smoke images with pixellevel and image-level labels for training.

### B. Smoke Semantic Segmentation

[...] a single image by training a foreground smoke dictionary and a background non-smoke one, but which deeply depend on training data. Lin et al. [50] estimated fire contours by proposing a Kalman filter-based method.

With the rapid development of deep learning in recent years, deep neural network based methods for smoke semantic segmentation have been proposed. Deep smoke semantic segmentation methods combine feature extraction and classification without complicated hand-crafted feature designs. Kaabi et al. [51] directly adopted a deep belief network to classify every pixel as a smoke object or a non-smoke one. Li et al. [52] proposed a 3D parallel full CNN to segment smoke regions in video. Yuan et al. [53] proposed a Waveshaped deep neural Network (W-Net) for smoke density estimation. It is actually a method for soft segmentation of smoke, but more challenging than hard smoke segmentation.

### C. Recurrent Networks for Computer Vision

Recurrent networks were originally proposed to process 1D sequential data with chained structures. It is obviously unsuitable for them to process 2D images, because images have no chained connections. Early recurrent methods usually transform feature maps generated by CNNs into chained forms, and then feed them into a recurrent structure to learn context dependence. Zou et al. [54] transformed 2D features into four 1D sequences by scanning a feature map in four directions. Byeon et al. [55] constructed a 2D LSTM layer containing four directional 1D LSTM blocks. Visin et al. [56] proposed a layer composed of four GRUs by dividing the scanning in four directions into two steps. Directly converting 2D features into 1D sequences inevitably loses spatial information of images, so Shuai et al. [57] used Undirected Cyclic Graphs (UCGs) to represent spatial connections between image units, and then adopted four Directed Acyclic Graphs (DAGs) to overcome the problem that UCGs cannot be expanded into acyclic sequences.

Aiming at solving the defect that recurrent networks can only process 1D sequence data, Shi et al. [58] proposed a convolutional LSTM by replacing all connected layers in traditional LSTMs with convolutional layers to encode spatial information. Lin et al. [19] adopted a bi-directionally connected convolutional LSTM to fuse feature maps of adjacent scales. Liu et al. [59] and Li et al. [60] used convolutional LSTMs for text-based instance segmentation. A multi-model convolutional LSTM was proposed to encode the sequential interaction between a single word, visual information and text information, and a convolutional LSTM was used to recursively improve the coarse segmentation regions obtained by CNNs and LSTMs. Ventura et al. [61] adopted convolutional LSTMs in both spatial and temporal dimensions to complete video object segmentation. Piao et al. [62] combined the convolutional LSTM with spatial and channel attention to learn the intrinsic semantic relevance of fused features. Yao et al. [63] proposed a convolutional GRU based on convolutional LSTMs. In addition to the normal input, Nilsson and Sminchisescu [64] used optical flow information as an [...]

Inspired by the success of GRU based methods, we also propose an attention convolutional GRU module to learn the spatial correlation and long-range context dependence of smoke. This is the first time the attention convolutional GRU has been used for image semantic segmentation.

## III. THE PROPOSED METHOD

Fig. 2 shows the overall framework of our Classificationassisted Gated Recurrent Network (CGRNet), which mainly contains four important modules, including an Xception network [66] for basic feature extraction, a semantic segmentation module with four branches, a classification module for assisting segmentation, and a fusion module.

### A. Basic Feature Extraction Module

[...] with 126 layers. This is mainly due to the usage of depthwise separable convolutions, which can greatly reduce the number of network parameters without obviously reducing performance.

### B. Semantic Segmentation Module

As shown in Fig. 2a, we propose a semantic segmentation module mainly consisting of four branches. Each branch acquires feature maps with different scales. Multi-scale features extracted in encoding stages of the segmentation module are fused in a bottom-to-up manner. Encoding stages embed abundant semantic information about scenes into feature maps, while decoding stages of the segmentation module are responsible for re-interpreting semantic information to produce final segmentation results. Low-level features learned by shallow layers have high resolution but lack semantic information. High-level features from deep layers contain rich semantic information but seriously lack spatial detail information. A common way for improving performance is to combine different level features.

Low-level features are of high resolution, but often contain too much noisy or interferential information, leading to instability of providing abundant high-resolution semantic guidance [68]. Aiming at solving this problem, we propose to add high-level features of Stage 4 to decoding layers of low-level stages, i.e. Stages 1, 2, and 3, as illustrated by dash lines in Fig. 2a. In this way, we improve decoding stability of semantic information by combining low-level and high-level features.

1) Attention Convolutional GRU: To enhance the ability of feature representation in decoding stages, we propose an Attention Convolutional Gated Recurrent Unit (Att-ConvGRU) to fuse features from different levels, as shown in Fig. 3. To preserve the spatial correlation of 2D features, we propose the Att-ConvGRU by first replacing all fully connected layers of the 1D GRU [3] with convolutional ones and then connecting the input signal Xt with the hidden state Ht−1. Convolutional layers are shared to reduce the number of parameters and computational complexity. The proposed Att-ConvGRU can be mathematically described as follows:

<!-- Eqs. (1)-(6) reconstructed from garbled extraction fragments (S043); bracket placement and the
label of Eq. (3)/(6) inferred from standard GRU form and the surrounding prose - verify against PDF. -->

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

<!-- Eqs. (7)-(11) reconstructed from garbled extraction fragments (S049); label of Eq. (11) inferred - verify against PDF. -->

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

<!-- Loss/metric formulas below reconstructed from fragmentary extraction (S060, S061, S062, S068, S069) - verify against PDF. -->

l1 = −(1/N) Σ_k (1/Mk) Σ_j [gk_j log pk_j + (1 − gk_j) log(1 − pk_j)]

where N is the image number of the train set, Mk is the pixel number of the kth image, and pk_j and gk_j are the values of the jth pixel in the predicted map and the ground truth map of the kth image, respectively.

Similarly, a binary cross-entropy loss is also used for image classification over the whole image instead of each pixel, formulated as:

l2 = −(1/N) Σ_k [gk log pk + (1 − gk) log(1 − pk)]

where pk and gk are the predicted smoke probability and the label of the kth image, respectively.

The final objective function is defined as the weighted sum of the above two losses:

L = l1 + α · l2 + λ · ∥W∥2

where α is the weight of l2, and λ is a regularizer weight. To evaluate the importance of α for training, we conduct several experiments in the next section to show the impact of different α values.

## IV. EXPERIMENTAL RESULTS

### A. Datasets and Implementation Details

Our method generates the final segmentation result by a segmentation module and a classification one. In the segmentation module, we extract four sets of feature maps from the middle layers of the Xception network pre-trained on the ImageNet dataset. The sizes of feature maps are 16 × 16, 32 × 32, 64×64 and 128×128, respectively. The classification module has two branches. One branch is used to implicitly refine the segmentation branch, and another one explicitly regulates the final loss of our method.

[...] synthetic test datasets (DS01, DS02, DS03) and one real smoke test dataset. These datasets are very challenging due to large variations in texture, shape, color, transparency and scales. Among the three synthetic test datasets, DS02 contains more sparse smoke, so it has more complicatedly mixed texture of background color, shape, and texture. We used Python and Tensorflow to implement our method, and trained it using stochastic gradient descent (SGD). The parameters of learning rate, momentum and weight decay are set to 0.001, 0.9 and 1e-5, respectively. The optimized weight α of the classification loss is set to 0.25. It took about 2 days to train our network, and our method spent less than 15 seconds to process 1000 images, including the time for reference and image loading.

### B. Evaluation Metrics

We report all segmentation results in terms of Intersection over Union (IoU) and Mean Square Error (Mse), which are widely used to evaluate the overall performance of semantic segmentation algorithms. The IoU reflects the degree of coincidence between a predicted result and its corresponding ground truth. For the sake of fairness, we use the average value of IoUs on the three synthetic test datasets, defined as:

mIoU = (1/N) Σ_k (Pk ∩ Gk) / (Pk ∪ Gk)

where Pk and Gk are the predicted map and corresponding ground truth map for the kth image, respectively.

Complementary to mIoU, the average value of Mses on the test datasets is used as another quantitative evaluation criterion, defined as:

mMse = (1/N) Σ_k (1/Mk) Σ_j [P(xk_j) − G(xk_j)]^2

where xk_j is the 2D coordinates of the jth pixel in the kth image. Apparently, a larger mIoU means higher accuracy, and the lower the mMse, the better the performance of the method.

### C. Performance Comparisons

To evaluate the effectiveness of our framework, we tested our method on the three synthetic datasets and one real smoke dataset, and compared it with several outstanding semantic segmentation methods based on deep learning, including static map detection method (SMD) [73], Text-Block FCN (TBFCN) [74], label refinement network (LRN) [75], Deeplab v1 [22], HG-Net [76], large kernel matters (LKM) [9], RefineNet [10], PSPNet [31], CCL[18], DFN [77], DSS [71], and W-Net [53]. To objectively and fairly evaluate the performance of each method, we used the same dataset and configurations to train all the comparison methods.

Table II lists quantitative comparison results on the three synthetic datasets. Our method achieved the highest mIoU and the lowest mMse on all the test datasets. In other words, our method obtained the best performance in terms of both mIoU and mMse among the comparison methods. By observing the experimental results, our method is better than other methods, such as RefineNet and PSPNet. The main reason is that our method upsamples feature maps to the size of original images before final prediction. Due to the ambiguous edges of smoke, downsampling the final prediction causes significantly jagged edges, resulting in accuracy reduction. This phenomenon is also observed in the results by LRN that is a multi-prediction model. The test accuracy of LRN is not high mainly because it down-samples ground truths to the sizes of feature maps, directly resulting in blurry edges of smoke objects. In addition, our CGRNet also outperforms our previous work, including DSS [71] and W-Net [53]. Different from previous methods, our CGRNet uses multi-stage stacking of Att-ConvGRUs to fuse multi-scale features in different levels, and at the same time increases spatial attention and long-range dependency. These techniques greatly improve the representation ability of our network. In addition, we propose MCCL to effectively alleviate the erroneous segmentation of inconspicuous objects. Combination of DPPM and classification branches greatly reduces the possibility of misclassifying smoke-like objects as smoke. We will also validate this conclusion in the subsequent ablation experiments.

Fig. 7 and Fig. 8 show segmented results of some synthetic and real images by the comparison methods, respectively. To better illustrate the functionality of each module proposed in our method, we selected some representative examples from the synthetic test datasets for analysis.

[...] the PSPNet, especially on inconspicuous smoke images. For the last two test samples, there is a large difference between predicted results by the PSPNet and corresponding ground truths. Meanwhile, the edges of smoke regions segmented by the PSPNet have more obvious block effects due to the eight times upsampling of predictions.

Segmentation results on the real smoke images are basically consistent with those on the synthetic images. Results predicted by our CGRNet are visually similar to the input real images. For images with inconspicuous smoke and smoke-like objects, as shown in the fourth to seventh columns of Fig. 8, our CRGNet obtains more accuracy. In particular, the test image in the last column is a very typical sample containing both inconspicuous and large between-class similarity problems. Many methods either failed to detect smoke, such as SMD, TBFCN and PSPNet, or they mis-classified all smokelike clouds and fog as smoke, such as HG-Net2 and HG-Net8.

In addition to synthetic and real images, we also performed experimental comparisons on real videos. Fig. 9 shows results segmented by comparison methods on real smoke videos. We selected three frames with large smoke variance from the two smoke videos to illustrate the robustness of our method. By observing all predicted results, it can be found that the segmentation results of all methods on the black smoke video are better than the white smoke video, mainly because the white smoke video is of low image quality. Compared with other methods, our CGRNet achieves the best performance on all video frames, and especially on images with inconspicuous smoke and large between-class similarity problems. For example, in the second frame of the black smoke video, the smoke in the upper left corner is very similar to the background, so most comparison methods produced incorrect segmentation, i.e. the smoke was misclassified as the background. As shown in Fig. 9, the smoke in some regions of the white smoke video is very sparse and inconspicuous. Many methods fail to segment such inconspicuous smoke objects.

In addition, to further enhance the performance of CGRNet on real images, we specifically involve an extra real smoke dataset [78] in our training dataset. This dataset includes 416 smoke images, in which 143 images have pixel-level labels (GT). We re-trained the model on the 143 images together with our training dataset, and then tested on the remaining 273 images without labels. Fig. 10 shows the visualization results of our method on some challenging samples. For the first two samples with inconspicuous problem of small smoke objects, our method was not heavily disturbed by the background and obtained good segmentation results. Although there obviously exists an ambiguous problem of similar categories in the third to sixth samples with smokelike objects, such as snow, cloud and fog, our method does not produce obvious wrong segmentation. The seventh sample has both problems and is even difficult to distinguish by human, but our method achieves acceptable results.

<!-- Subsection heading for the ablation study (Section IV-D) was lost in extraction; the following
paragraphs are the ablation discussion. -->

[...] experiments by removing each part or replacing some parts with other structures, and we have nine variants of our method, as described in Table III. The comparison results by the nine variants are shown in Table IV. According to the experimental results, we have several important conclusions.

First, removing the classification module from our method greatly reduces the overall prediction accuracy by about 6%. The main reason is that without the assistance of the classification module, our method is changed from the multi-task joint training to the single-loss training, directly resulting in slow convergence of network training.

Second, the removal of stacked Att-ConvGRUs causes a performance degradation of approximately 3%, so it means that the multi-stage stacking of Att-ConvGRUs plays an important role in learning effective features.

Third, increasing channel attention in the convolutional GRU can learn the intrinsic nature of the features, and effectively improve the quality of features.

Finally, since the number of samples with inconspicuous smoke and smoke-like objects in the three test datasets is small, the impact of DPPM and MCCL is not obvious.

[...] function by setting α to an appropriate non-zero value. Observing Fig. 11, we find that the multi-loss function can make our method converge more quickly and stably than the single-loss one. To find an optimized weight, we experimented with a range of the classification loss weight α between 0 and 1, as shown in Table V. Since our network is proposed for the purpose of segmentation, we theoretically needs to pay more attention to the segmentation module than the classification one. In other words, the weight for the classification loss should be relatively smaller than that for the segmentation loss. Experimental results also validate that a relative small weight (α = 0.25) achieved the best performance. In the case of α = 0, the accuracy of our algorithm significantly decreases as the training loss function degenerates into a single objective loss function. The accuracy with α = 1 decreases by approximately 2.5%.

### E. Segmentation of Images With Large Between-Class Similarity

Both PSPNet and our CGRNet can effectively solve the problem of large between-class similarity. To validate the performance of our method, we selected some challenging images for visual comparisons, and results are shown in Fig. 12. As shown in the samples of columns 1 and 2, the PSPNet has wrong segmentation results, but our CGRNet avoids this situation very well. This is mainly because the smoke probability of the two samples classified by our CGRNet is 1.01×e−5 and 0.0871, which help our method to avoid misclassifying smokelike objects as smoke. For samples containing smoke, cloud and fog at the same time, as shown in columns 3 and 4, our CGRNet has obviously better segmentation performance than the PSPNet. Since smoke and fog have very overlapped visual appearance, the PSPNet cannot correctly discriminate between smoke and fog at all, resulting in erroneous segmentation. Visual comparisons prove that our CGRNet is superior to the PSPNet for smoke-like objects with large between-class similarity.

## V. CONCLUSION

[...] the long-range and context-dependent information of objects and enhance the ability of network to extract distinguishable features, we introduce convolutional GRUs into smoke semantic segmentation, and design a channel attention mechanism to mine the inherent semantic relationship of features. To improve the segmentation performance of inconspicuous smoke objects, we propose to use the contrast of multiple atrous convolutions with different rates to obtain useful context information, and also focus on local information of inconspicuous objects at the same time. For the problem of smoke-like objects, we propose a module with dual classification assistance branches to improve discriminative ability. The main idea of one classification branch is to extract the global category information of the input image to avoid misclassifying smoke-like objects as smoke. On the other hand, the output of another classification branch is used to multiply the weights of the segmentation module for recalibrating the features of segmentation. Compared with other excellent semantic segmentation algorithms, our method consistently outperformed state-of-the-arts algorithms on three synthesis smoke datasets and real smoke images. In addition, our method does not require complicated training for images with inconspicuous objects and smoke-like objects with large between-class similarity problems.

## REFERENCES

<!-- Reference entries omitted from clean corpus: the extraction carries only entries [1]-[13]
(S094-S095), flagged [uncertain]/medium in translation_notes.md, with the remainder of the list
missing. Consult the source PDF for the full reference list. -->

## Appendix: Figure and Table Captions (segregated from body)

Fig. 1. Some challenging images. (a), (b), and (e) are smoke; (c) and (d) are haze.

Fig. 2. The framework of our network.

Fig. 3. Detailed diagram of the proposed Att-ConvGRU.

Fig. 4. The attention module in the proposed Att-ConvGRU.

Fig. 5. Multi-scale context contrasted local module.

Fig. 6. Dense Pyramid Pooling Module (DPPM).

Fig. 7. Results on synthetic smoke images. (a) Synthetic smoke images. (b) Ground truth. Segmented results by (c) SMD, (d) TBFCN, (e) LRN, (f) Deeplab v1, (g) HG-Net2, (h) HG-Net8, (i) LKM, (j) RefineNet, (k) PSPNet, and (l) our CGRNet.

Fig. 8. Results on real smoke images. (a) Real smoke images. Segmented results by (b) SMD, (c) TBFCN, (d) LRN, (e) Deeplab v1, (f) HG-Net2, (g) HG-Net8, (h) LKM, (i) RefineNet, (j) PSPNet, and (k) our CGRNet.

Fig. 9. Results on real smoke videos. (a) Frames from videos. Segmented results by (b) SMD, (c) TBFCN, (d) LRN, (e) Deeplab v1, (f) HG-Net2, (g) HG-Net8, (h) LKM, (i) RefineNet, (j) PSPNet, and (k) our CGRNet.

Fig. 10. Results of our CGRNet on some real smoke images from [78].

Fig. 11. Training error curves of different loss function.

Fig. 12. Images with large between-class similarity. (a) Original images. Segmented images by (b) PSPNet, and (c) CGRNet.

TABLE I DETAILED DESCRIPTION OF THE INPUTS FOR EACH ATT-CONVGRU

TABLE II SEGMENTATION RESULTS OF DIFFERENT METHODS ON THE THREE SYNTHETIC TEST DATASETS

TABLE III DETAILED DESCRIPTION OF OUR VARIANTS

TABLE IV COMPARISON RESULTS OF OUR VARIANTS

TABLE V RESULTS WITH DIFFERENT α
