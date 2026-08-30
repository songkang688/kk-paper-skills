## Methods

### III. The Proposed Method

#### A. The Overall Structure

Fig. 2 illustrates the network structure of our BiFBA-Net for medical image segmentations. Inspired by the success of combining local and global features, we design a CNN encoder and a Transformer one to create a dual encoding structure. To reduce semantic gaps between them, we propose a Bi-directional Attention Gate module (Bi-AG) to fully exchange information from the two encoding paths. In particular, for an input dermoscopy image with the size of H × W, a stem part containing resampling, normalizing, convolution and pooling layers is first used to generate an initial feature map. Then, patch embedding techniques are adopted to produce visual tokens for the Transformer encoder to extract long-distance features. The CNN encoder uses ResNet [15] to capture more local features. Different from existing dual encoders, we design the Bi-AG to exchange information from the two encoders for fully fusing local and global features. Our BiFBA-Net has three decoders, including a CNN decoder, a Partial Decoder (PD), and a Boundary Aware Decoder (BAD). The CNN decoder mainly restores spatial information that is fed into a partial decoder [44] for further processing. Finally, the partial decoded features, CNN decoded and encoded features are fed into BAD for decoding boundary aware features.

> Fig. 2. The overall framework of the proposed BiFBA-Net.

#### B. Dual-Encoding Structure With Bi-Directional Fusion

##### 1) Transformer Encoder

The Transformer encoder has twelve Transformer blocks to extract global feature representations. The original feature map is first divided into 14 × 14 non-overlapping patches, which are embedded to produce tokens. Patch embedding is implemented by a linear projection. By using the bi-directional fusion module, we force the output features of the Transformer encoder to frequently interact with the features of the CNN encode at different levels. Since both local features and spatial localization information are automatically encoded by the CNN encoder, the positional embedding usually used in Transformers is no longer indispensable in our network. In our implementation, we adopt positional embedding for Transformers. Each Transformer block consists of a Multi-head Self-Attention (MSA) and a Multi-Layer Perception (MLP). As a key component of Transformers, the MSA block employs multiple attention heads to calculate attention. It captures information from different subspaces and updates embedded patch features by globally aggregating information, formulated as follows:

SA(Q, K, V) = softmax( QK^T / √d_k ) V
Q = X_l W_Q, K = X_l W_K, V = X_l W_V    (1)

MSA = Concat(head_1, head_2, . . . , head_h) W_O
head_i = SA(Q_i, K_i, V_i)    (2)

where X_l is the output of the l-th Transformer block, matrices Q, K and V are obtained by respectively multiplying X_l with three trainable transformation matrices W_Q, W_K and W_V, embedding dimension d_Xl and feature dimension d_k are respectively the lengths of rows and columns in matrix K, Concat represents concatenation operation, head_i represents the i-th attention head, W_O is the learnable weight matrix for the linear transformation, and h is the number of attention heads. In our implementation, d_Xl = 576 and h = 9, so we use d_k = d_Xl/h = 64 for each head.

[NOTE: Eq. (1) was fragmented in the source ("QK T", "SA (Q, K, V ) = sof tmax", "√dk" as separate blocks); reassembled per the standard scaled dot-product attention form.]

The results by multiplying Q with K factually denote the correlation between them. The greater the correlation, the greater the self-attention coefficients for weighting the value matrix V. The MLP block is designed as a feed forward network with two fully connected layers, the GELU activation function and a dropout layer. Its first full connection layer increases the number of input nodes and its second full connection layer restores the number of original nodes. Layer Normalization (LN) and residual connections are used in Transformer blocks.

Different from other Transformer encoders, our Transformer encoder is designed as the branch crossly fused with the CNN decoder in dual directions. The output of each Transformer block is sent to the Bi-AG module for fully interacting with the CNN encoder, and then its next Transformer block accepts the fused feature map of the Bi-AG module as its input.

##### 2) CNN Encoder

The encoding part of ResNet [15] is used as the CNN Encoder of our network. The whole CNN encoder can be split into four stages. In subsequent stages, feature maps are convoluted, activated and down-sampled repeatedly. The spatial resolution of feature maps decreases, but the channel number of feature maps often increases. In the CNN encoder, we design k bottlenecks for convolution blocks, and other operations are just the same as the ResNet [15]. Concretely, the original feature map is extracted in Stage C1, and the resolution of the original feature map is just one quarter of the input image. In the following i-th stage {Ci, i = 2,...,5}, the resolution of the extracted feature map is the size of H/2^i × W/2^i. The CNN encoder is more likely to preserve spatial details in the extracted local features since convolution kernels slide over feature maps in an overlapping way. The object features and approximate locations are progressively extracted by convolutional encoder blocks.

##### 3) Bi-Directional Attention Gate

The CNN and Transformer encoders respectively produce 2D feature maps and 1D patch embedding features, so they are not aligned. Apparently, this kind of misalignment is reflected not only in the semantic gap but also in feature dimensionality. To solve this problem, we propose a Bi-directional Attention Gate (Bi-AG) module to effectively interchange relevant features between the CNN and Transformer encoders in an interactive and crossly-fusing way.

In terms of feature dimensionality, a CNN feature map has the size of C × H × W, where C, H and W denote its channel number, height and width. The batch size is not changed in each branch, so it is unnecessary to discuss it. A patch embedding has the size of (K + 1) × E, where K, 1 and E stand for the number of patches, one positional embedding feature vector and the token dimensionality. In fact, E is just the dimension of Transformer features. To align CNN features with Transformer ones, we first adopt a 1 × 1 convolution to adjust the channel dimension of CNN features to E in each stage. Subsequently, a down-sampling projection and a reshaping operation (flattening) are performed to alter the spatial dimension for making convolutional features to be suitable for the Transformer blocks. Similarly, each patch embedding vector is first adjusted in sequence length and then reshaped to match the size of a convolutional feature map. Then, a 1 × 1 convolution is used to align the number of channels with those of convolutional features. Finally, we employed an up-sampling operation to incorporate spatial structures into the Transformer features.

Traditional methods directly concatenate or add the aligned features for information fusion, but both concatenation and addition inevitably introduce noisy information. To solve this problem, we adopt two Attention Gates to reduce feature redundancy for bi-directional fusion. A single Attention Gate (AG) filters the encoded features by skip connections, but it may lead to a noisy spatial map. As it is found in [16], combining two AGs in parallel has the potential for improving the robustness of segmentation. We think that this parallel structure is equivalent to an ensemble model. It collects low-level and high-level feature maps, then simply uses two identical AGs to produce two identical spatial attention maps and concatenates them to produce the final output. However, compared to using the query features to calibrate the low-level key features in the same branch, two different kinds of encoding branches provide more abundant information for calibrations.

Specifically, our mutual Bi-AG based fusion module exploits two AGs in parallel to obtain two different pixel-wise gating coefficients α and β from the 2D CNN features x_CNN and the 1D Transformer features x_Tran. As shown in Fig. 3, the top row branch of Bi-AG generates a hidden feature vector h1, and an attention gate accepts the feature vector h1 and the Transformer feature vector x_Tran as the inputs to generate a weighted attention feature vector α · h1. Similarly, the bottom branch produces a hidden feature map h2, and another attention gate accepts the feature map h2 and the CNN feature map x_CNN as the inputs to obtain a weighted attention feature map β · h2. In this way, the attention coefficients α and β are multiplied with CNN and Transformer features for cross and hybrid calibrations. Cross attention gates of our Bi-AG play a key role in pruning noisy or unimportant features, and keeping more contextual information, as shown in Fig. 3. By ablation studies in Section IV, we validate that variants with Bi-AG achieve unanimously better results than ones without Bi-AG. Furthermore, the operations of Layer Normalization (LN) and Batch Normalization (BN) [46] are used to normalize features for accelerating learning. The outputs of our Bi-AG based fusion module, y_Tran and y_CNN, are calculated as follows:

h1 = LN(Reshape(Down(ϕc(x_CNN))))
h2 = BN(Up(ϕc(Reshape(x_Tran))))    (3)

α = σ(ϕc(ReLU(ϕc(h1) + ϕc(x_Tran))))    (4)

β = σ(ϕc(ReLU(ϕc(x_CNN) + ϕc(h2))))    (5)

y_Tran = α · h1 + x_Tran
y_CNN = β · h2 + x_CNN    (6)

where ϕc means a 1 × 1 convolution with c output channels followed by batch normalization, and c varies depending on the specific situation, Down and Up denote the modules of down-sampling and up-sampling, respectively, and σ corresponds to the sigmoid activation function.

[NOTE: Eqs. (3)–(5) were shattered into isolated one-token fragments in the source ("ϕc (xCNN) h1 = LN", "Reshape", "Down", "α = σ", "ReLU", etc.); they have been reassembled following the alignment procedure described in the surrounding text (1×1 conv → down-sample → reshape for the CNN branch; reshape → 1×1 conv → up-sample for the Transformer branch) and the standard additive attention-gate form. The exact nesting order inside Eq. (3) is a best-effort reconstruction. The two stray NUL bytes in the source file occurred inside these broken formula blocks.]

> Fig. 3. The Bi-Attention Gate fusion module. (a) Details of the proposed Bi-AG based fusion module. (b) A single attention gate block.

#### C. Progressive Decoding Structure With Boundary Aware

To extract and recover discriminative feature maps, our network has three decoders that are a CNN decoder, a Boundary Aware Decoder (BAD) and a Partial Decoder (PD) [44].

We design the CNN decoder to process the 1D feature vector y_Tran of Bi-AG instead of the 2D CNN features y_CNN of Bi-AG, thus we generate a rough prediction P6 but with more long-range dependency. To further fuse the feature maps from the CNN encoder and the fusion module, we adopt the partial decoder to filter the 2D CNN features y_CNN for producing another coarse prediction P5 with more spatial details. The boundary aware decoder combines the features of the fusion module and the CNN encoder, and the two above-mentioned predictions for producing the final prediction P0.

##### 1) CNN Decoder

The CNN decoder is mainly responsible for generating feature maps with abundant spatial details due to local weight sharing properties of CNNs. We adopt the strategy of Progressive UP-sampling (PUP) in SETR [45], and totally apply four consecutive decoding blocks to recover the spatial resolutions and generate the final segmentation results. The CNN decoder receives the 1D feature vector y_Tran produced from the Bi-AG fusion module as input, so it's necessary to reshape the 1D feature vector into a 2D feature map before upsampling. The Bi-AG fusion module combines the features of the Transformer and CNN encoders, so the output of the CNN decoder also contains long-range dependency and spatial details.

##### 2) Partial Decoder

Compared with high-level contextual information, low-level feature maps usually contribute less to the accuracy performance. Inspired by the idea of Receptive Field Blocks (RFB) in the cascaded partial decoder [44], we adopt a memory efficient Partial Decoder (PD) to aggregate high-level features with higher semantic confidences. We also discard the low-level features of the first two stages in the fusion module for the partial decoder to efficiently aggregate the features of the remaining three stages, resulting in the prediction map P6. [NOTE: the source text here attributes P6 to the Partial Decoder, whereas the section overview above attributes P6 to the CNN decoder and P5 to the Partial Decoder; this inconsistency exists in the original text and is preserved as printed.]

##### 3) Boundary Aware Decoder

CNN and partial decoders produce coarse predictions P5 and P6, which are not yet satisfactory to medical applications. Therefore, we design the Boundary Aware Decoder (BAD) to further restore the finer structural features, as shown in Fig. 2. It is widely known that deeper layers of neural networks extract more advanced semantic information but lose more spatial details. The most prevailing remedy method is to fuse multi-level features from different layers, so that complementary cues can be captured. However, the predictions of deep layers often degrade when they are directly combined with shallow ones. Besides, most of prevailing deep encoders unintentionally concentrate on high-response regions during residual learning, as they are typically fine-tuned from image classification networks. This makes it is struggling for them to capture residual details [47]. To solve this problem, we use residual learning along with several Reverse Attention (RA) modules to extract dense features for pixel-wise predictions. In addition, the reverse attention module boosts the representation ability of residual learning, so it helps the network mine the missed skin lesions. Starting with the 2D feature map output from the last Bi-AG block and the coarse saliency map produced by the partial decoder, we adopt several RA modules and residual structures to progressively generate multi-scale feature maps, denoted as P1, P2, P3, and P4.

The reverse attention module is inspired by the idea of erasing foreground objects progressively in saliency detection. The reverse attention emphasizes salient objects. Taking the second RA module as an example, P4 is upsampled and reversed to weight its adjacent shallow features, and this procedure efficiently guides the residual learning of undetected regions. We adopt RAs to gradually recognize and progressively refine skin lesion regions in the multi-scale feature maps P1, P2, P3, P4, P5 and P6, resulting in a more precise prediction P0. The reverse attention coefficients are adaptively learned from the corresponding level features of the CNN encoder and the output features of the adjacent RA block rather than aggregating features of all levels. Specifically, we multiply the features {f_i, i = 1, 2, 3, 4} by the reverse attention coefficients a_i to obtain the reverse attention features r_i, formulated as follows:

r_i = f_i ⊙ a_i    (7)

The reverse attention weight a_i can be expressed as:

a_i = 1 − σ(UP(P_{i+1}))    (8)

where UP means an up-projection operation, σ is the sigmoid function, and 1 denotes a feature map with all elements being 1. Fig. 2 shows the details of the RA module.

[NOTE: the argument of σ(UP(·)) in Eq. (8) was lost at a column break in the source ("ai = 1 −" followed by an empty block); reconstructed as the adjacent deeper prediction map following the standard reverse-attention formulation and the surrounding text.]

#### D. Deep Supervisions

To achieve better performance, we utilize a hybrid loss to calculate the errors between the predicted segmentation map of a dermoscopic image and its ground truth map G. In general, each ground truth map was manually annotated by medical experts. The hybrid loss is composed of a weighted binary cross-entropy loss ℓce and a weighted IoU loss ℓiou, formulated as follows:

ℓ(G, P_i) = δ ℓce(G, P_i) + (1 − δ) ℓiou(G, P_i)    (9)

ℓce(G, P_i) = − Σ_j [ G^j ln P^j_i + (1 − G^j) ln(1 − P^j_i) ]    (10)

ℓiou(G, P_i) = −ln( ∩(G, P_i) / ∪(G, P_i) )    (11)

where P^j_i is the j-th pixel value of the i-th prediction map P_i, G^j is the j-th pixel value of its ground truth map G, ∩(G, P_i) is the pixel number of intersection between the i-th prediction map and its ground truth map, ∪(G, P_i) is the pixel number of union between them, and δ is a weighting coefficient. To correctly compute medium losses, P1, P2, P3 and P4 are all upsampled to the same size as its ground truth. The overall loss function is formulated as follows:

L_overall = ℓ(G, P1) + ℓ(G, P2) + ℓ(G, P3) + ℓ(G, P4) + ℓ(G, P5) + ℓ(G, P6)    (12)

[NOTE: Eq. (10) was fragmented in the source ("i ) + G j ln P j", "(1 −G j) ln(1 −P j"); reassembled per the standard binary cross-entropy form.]
