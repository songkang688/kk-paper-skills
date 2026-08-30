## 3. The proposed methods

### 3.1. Architecture overview

Inspired by the powerful representation abilities of CNNs and Transformers, we propose a CNN and Transformer Complementary Network (CTC-Net). As shown in Fig. 2, our CTC-Net consists of four main branches, including a CNN encoder, a Transformer encoder, a Feature Complementary Module (FCM) and a Transformer decoder. The main differences of our method from existing architectures are that we design two different encoders to produce complementary features, and propose a cross-domain complementary fusion module.

Our motivation of using both CNN and Transformer encoders is that CNN encoders are mutually complementary to Transformer encoders. On the one hand, there are relatively small or thin organs in medical images, so deeper CNN architectures may result in severe loss of small or thin objects. It is very difficult for decoders to recover lost small and narrow objects, leading to failures in small and narrow objects. On the other hand, Transformer encoders can capture more dependencies between long and narrow organs in human bodies, such as TransUnet [40]. Long-range information is very useful for improving segmentation accuracy of long and narrow objects. Therefore, we specially propose the multi-scale Feature Complementary Module (FCM) for fusing features from both CNN and Transformer encoders.

Finally, we design the Transformer decoder, which directly accepts the feature maps from the Transformer encoder for progressively recovering feature maps. In addition, our FCM produces different level complementary information from CNN and Transformer decoders, which is also fed into the Transformer decoder by skip connections. The complementary features are very important for restoring small and narrow objects commonly existing in human bodies.

### 3.2. The Transformer encoder

Alexey et al. [9] proposed the Vision Transformer (ViT), which is the first Transformer model for vision tasks. In a standard Transformer, pixel values in each patch are concatenated to produce a token feature vector, which is required to calculate the attention with all other tokens in the whole image, directly leading to the quadratic computational complexity with respect to the image size. To solve this problem, the Swin Transformer [11] performs self-attention only in each local window, thus the computational complexity is linearly proportional to the image size.

We stack Swin Transformer Blocks (STB) and patch operations [11] to construct the main feature encoding path, named as Transformer encoder (Fig. 2c). Each Swin Transformer block (Fig. 2e) is composed of two successive sub-blocks. The first sub-block consists of Layer Normalization (LN), Window based Multi-head Self Attention (W-MSA), Multi-Layer Perceptron (MLP) and residual additions. The second one has almost the same operations, but replaces W-MSA with Shifted Window based MSA (SW-MSA) [11].

We also use patch merging [11] to down-sample feature maps. Common down-sampling methods used in CNNs are pooling and de-convolution. Similarly, Transformer based methods also need to perform down-sampling operations for aggregating contextual features. To obtain the same ability, Swin Transformer [11] merges adjacent 2 × 2 patches into a large patch by concatenating these 4 small patches along the channel direction. This procedure is called patch merging.

According to spatial resolutions, the Transformer encoder can be divided into four levels, as shown in Fig. 2c. The first level has a patch embedding layer and two Swin Transformer blocks for feature encoding. The second to fourth levels have a patch merging for down-sampling, and two Swin Transformer blocks for extracting long-range dependencies.

Suppose that the input RGB image x has the size of H × W × 3, and the output y of our CTC-Net is H × W × N where N is the category number for segmentation. The 2D outputs of the Transformer encoder in the four levels are denoted by g1, g2, g3, and g4, which have the sizes of (H/4 × W/4) × C, (H/8 × W/8) × 2C, (H/16 × W/16) × 4C, (H/32 × W/32) × 8C, respectively. According to the Swin Transformer [11], a RGB image patch with size of 4 × 4 is regarded as a token, so the feature dimension C of each token is equal to 4 × 4 × 3 = 48, i.e. C = 48.

### 3.3. The CNN encoder

To obtain contextual features and maintain certain spatial details by convolutional neural networks, we use the four encoding blocks of ResNet34 [17] to build a CNN encoder, as shown in Fig. 2a. The four blocks of ResNet34 [17] are denoted by Conv1x, Conv2x, Conv3x and Conv4x, each of which performs down-sampling operations by a rate of 2.

To make the feature map size of the CNN encoder to be exactly consistent with that of the transformer encoder, we adopt Conv1x and Conv2x to down-sample feature maps twice in Level 1. For the sake of consistency, the channel C of the 3D feature map f1 for Level 1 is set to 48. Hence, the CNN encoder generates an output feature map f1 with size of H/4 × W/4 × C for the first level, which has the same pixel number as the first level output of the Transformer encoder. For the second level, the Conv3x block is used to process f1 to generate another 3D feature map f2, which has the size of H/8 × W/8 × 2C. Next, we use Conv4x to filter f2 obtain the third 3D feature map f3 with H/16 × W/16 × 4C for Level 3. Our CNN encoder has only three levels to produce three feature maps. These three maps, i.e. f1, f2 and f3, contain abundant spatial details and contextual semantics for improving the representation of the Transformer decoder.

### 3.4. Feature complementary module

Transformer based methods originally proposed for NLPs are different from CNN based ones for vision tasks. These two kinds of methods have totally different feature extraction manners, and also have completely diverse purposes for applications. The features by the Transformer encoder and the CNN encoder are generated in different domains. To obtain mutually complementary information, we propose a feature complementary module by designing four blocks, as shown in Fig. 3.

The first block is called Cross-domain Fusion Block (CFB). Our CFB is responsible for cross-wisely fusing and enhancing features from two different domains of Transformer and CNN encoders. Specifically, the feature maps from the Transformer and CNN encoders are denoted by gi and fi, respectively. Suppose that the 2D feature map gi has the size of (h × w) × c, and the 3D CNN feature map has the size of h × w × c. To implement cross-domain fusion, we first apply Global Average Pooling (GAP) on these two maps to generate two feature vectors with size of (1 × 1) × c. Then, we concatenate the Transformer input gi with the globally pooled feature vector of the CNN input fi along the first axis for producing a larger 2D feature map g1i with size of (h × w + 1) × c. Then the concatenated map is fed into a Swin Transformer Block (STB) for feature fusion. Thus we can obtain a powerfully fused 2D feature map g2i with size of (h × w) × c, which is reshaped into its 3D version g3i with size of h × w × c. On the other hand, we also concatenate the CNN input fi with the pooled feature vector of the Transformer input gi along the first axis for producing another larger 2D feature map f1i with size of (h × w + 1) × c. Similarly, we use a Swin Transformer Block to process the concatenated feature map for producing another cross-domain fused feature map f2i, and reshape it to obtain a 3D feature map f3i. Finally, we concatenate the two cross-domain fused 3D feature maps and use a 1 × 1 convolution to generate a cross-domain fusion feature map si with size of h × w × c. The processing for our CFB is formulated as follows:

g1_i = cat(GAP(f_i), g_i), (1)

f1_i = cat(GAP(g_i), f_i), (2)

g3_i = reshape(STB(g1_i)), (3)

f3_i = reshape(STB(f1_i)), (4)

s_i = conv(cat(g3_i, f3_i)), (5)

where GAP, cat, STB, reshape and conv stand for Global Average Pooling, concatenation, Swin Transformer Block, reshaping, and convolutions, respectively.

Eq.s 1 and 2 perform the intensive cross-domain fusion of features from two different domains. In addition, the Swin Transformer Blocks in Eq.s 3 and 4 can further enhance the feature representation abilities of long-range dependencies. Eq. (5) finally fuses the features from two kinds of cross-wise ways.

The second block is the Correlation Enhancement Block (CEB). Our CEB is proposed to model the cross-domain correlation between features from two transformation domains of Transformer and CNN encoders. We first reshape the 2D Transformer feature map gi to obtain its 3D version g0i, and then point-wisely multiply g0i by fi to produce a cross-domain correlation feature map ei with size of h × w × c. In fact, our CEB is a special kind of attention mechanisms, which can enhance important information and suppress unremarkable features among the two feature maps. By using CEB, we extract mutually salient features in both CNN and Transformer branches for further improving accuracy.

The third one is the Channel Attention Block (CAB). The original Swin Transformer block has a built-in self-attention mechanism for modeling long-range dependency. To further enhancing attention features, we apply a channel attention [42] commonly used by CNNs to the Transformer features. In this way, we efficiently implement a mixture of channel and self-attention attentions to obtain a dual attention feature map ai with size of h × w × c. In other words, our CAB is factually a mixed attention mechanism.

The last one is Feature Fusion Block (FFB). We concatenate the cross-domain feature map si, the correlation feature map ei and the dual attention feature map ai to obtain a feature map m1i with size of h × w × 3c, and use residual and reshaping operations to generate the output feature map mi with size of h × w × c for our FCM, formulated as:

m1_i = cat(s_i, e_i, a_i), (6)

m_i = reshape(conv(m1_i) + CBR(m1_i)), (7)

where CBR is a block with convolutions (Conv), batch normalization (BN) and rectified linear unit (ReLU) to fuse the concatenated features and reduce the number of parameters at the same time.

### 3.5. The Transformer decoder

Swin Transformer blocks have been proven quite qualified for serving as either encoders or decoders [8]. Just contrary to patch merging, patch expanding [11] is often used to up-sample feature maps. Following the idea of [11], we stack Swin Transformer blocks and patch expanding operations to create a four-level decoding path. To fuse features from both Transformer and CNN encoders, we also feed the cross-domain fused features from the Transformer and CNN encoders to the Swin Transformer block. As shown in Fig. 2d, our Transformer decoder has four levels. In each level, reinforced short connections between the Transformer decoder and the two encoders are proposed for compensating lost spatial details and long-range dependency information.

The fourth decoding level only adopts a patch expanding operation to up-sample feature maps at a rate of 2. In the third and second decoding levels, we first adopt two Swin Transformer blocks to fully fuse the cross-domain enhanced feature map from its corresponding feature complementary module and the up-sampled features from its adjacent high level, and then use patch expanding to up-sample the fused feature map. In the first decoding level, we also adopts two Swin Transformer block for feature fusion and extraction of long-range dependencies. Besides, we use a final patch expanding block to up-sample the feature map for generating the output mask with the same size as the input image. In the final patch expanding block, we use a patch expanding with a rate of 4 for recovering the size of the 2D feature map, a 1 × 1 convolution for adjusting its channel number to the category number N, and a reshaping operation to convert the 2D map into a 3D feature map that is just the output of our CTC-Net. According to the descriptions of Fig. 2d, the data processing in the Transformer decoder can be briefly formulated as follows:

v_k = STB(STB(u_k, m_k)), (8)

u_{k-1} = PE(v_k), (9)

where k is the level index, and STB and PE denote Swin Transformer and patch expanding blocks, respectively.
