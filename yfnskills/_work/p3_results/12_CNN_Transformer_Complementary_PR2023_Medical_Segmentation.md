## 4. Experiments and discussion

### 4.1. Datasets

To evaluate the performance of our method for medical image segmentation, we compared our method with existing state-of-the-art networks on two widely used medical image datasets, which are the Synapse dataset (Synapse) and the Automatic Cardiac Diagnosis Challenge (ACDC) dataset. The Synapse and ACDC datasets are available via https://www.synapse.org/#!Synapse:syn3193805/wiki/217789, and https://www.creatis.insa-lyon.fr/Challenge/acdc/, respectively. More details about the two datasets are described as follows:

#### 4.1.1. Synapse

Synapse includes 30 CT scans on abdominal organs for multi-organ segmentation. Following TransUnet [40], we selected 18 cases as a training set, and regarded the rest 12 cases as a test set. We report the average Dice Similarity Coefficient (DSC) and the average Hausdorff Distance (HD) on 8 categories of 2211 2D slices extracted from the 3D volumes. The 8 classes are aorta, gallbladder, spleen, left kidney, right kidney, liver, pancreas, and stomach.

#### 4.1.2. ACDC

ACDC aims to evaluate the segmentation performance of left ventricle (LV), right ventricle (RV) and myocardium (MYO) for automated cardiac diagnosis. The dataset includes MRI images of 100 different patients. We divided the dataset into a training set with 70 samples, a validation one with 10 samples and a test one with 20 samples. We report the average DSC on the 3 classes mentioned above.

### 4.2. Implementation details

Our CTC-Net was implemented using Python 3.8 and Pytorch 1.7.1. All experiments were conducted on an Intel i9 PC with an Nvidia GTX 3090 of 24GB memory. We used the pre-trained weights of Swin Transformer on ImageNet to initialize the Transformer encoder and decoder our CTC-Net, and adopted a pre-trained ResNet34 to initialize the parameters of our CNN encoder. The batch size is set to 24, the maximum iteration number is set to 13,950, and the optimizer is SGD with basic learning rate 0.01, momentum 0.99 and weight decay 3e-5. The decay strategy of learning rate lr can be described as follows:

lr = base_lr · (1 - iter_num / max_iterations)^0.9, (10)

where base_lr is a basic learning rate, max_iterations is a maximum iteration number, and iter_num is iteration index.

The overall loss of our model is defined as the weighted sum of a cross entropy loss and a dice loss. The two loss functions and the weight ratios between them can be described as follows:

L = (1 - α) ℓ_ce + α ℓ_dice, (11)

where ℓ_ce denotes the cross entropy loss, ℓ_dice stands for the dice loss, and α is a related importance weight empirically set to 0.6.

Human organs often have very smooth surfaces. To prevent the output results being noisy, we add a post-processing method on the segmentation results by our CTC-Net. There are several post-processing methods that can be adopted for removing noise, such as morphological operators and median filtering. For the sake of simplicity and computation efficiency, we use median filtering to obtain more smooth results. Subsequent experiments also validate that the results processed by median filtering are more accurate than the original results of our network. The reason may be that human organs have inherent smooth surfaces.

Two evaluation metrics are the average Dice Similarity Coefficient (DSC) and the average Hausdorff Distance (HD). They both indicate the similarity between a predicted segmentation and its ground truth. DSC is used to evaluate the overlapping degree between a segmentation prediction P and its corresponding ground truth G, and HD measures the overlapping quality of segmentation boundaries. The two metrics are defined as follows:

DSC = 2|P ∩ G| / (|P| + |G|), (12)

HD(P, G) = max[D(P, G), D(G, P)], (13)

D(P, G) = max_{p∈P} min_{g∈G} ||p - g||, (14)

where ∩ stands for an intersection operator for two sets, p and g are coordinate vectors of two pixels, |S| is the pixel number of a set S, ||v|| is the l2 norm of a vector v, and P and G denote the coordinate sets of the segmentation prediction and the ground truth, respectively. A larger DSC or a smaller HD means a better segmentation.

Other detailed parameter settings of our CTC-Net are summarized in Table 1. As shown in Table 1, Depth_encoder and Depth_decoder denote the depth of each Swin Transformer layer in the Transformer encoder and decoder, Num_heads stands for the number of attention heads in the Transformer encoder and decoder, and Num_heads_FCM is the number of attention heads in FCM.

### 4.3. Experiments on Synapse

Table 2 lists the results of our method and twenty state-of-the-art CNN semantic segmentation models on the Synapse dataset. We compared our CTC-Net with these 20 methods, including pure Transformer based models, pure CNN based ones, and CNN and Transformer combined ones. We used the average Dice Similarity Coefficient (DSC) as our main evaluation metrics.

According to Table 2, experimental results demonstrate that our proposed CTC-Net achieves the highest average DSC of 78.41% among all the compared methods. Compared with any of the above models, our CTC-Net outperforms them on at least half of all the eight categories. All compared methods always achieve the comparatively low accuracies on pancreas segmentation due to the particularly large deformation of the pancreas from case to case and its blurred boundary. Thanks to the efficient combination of local details and global interactions in a cross-domain manner, our CTC-Net produces the best results on pancreas among all the methods. As for Kidney (R) and Kidney (L), our CTC-Net achieves the highest DSC and the second highest DSC among twenty-one methods, respectively. These existing methods have achieved state-of-the-art results, so it validates that our method is powerful.

For the sake of simplicity, Table 3 presents the average Hausdorff Distances (HDs) achieved by some of the excellent models in Table 2. Experimental results show that our CTC-Net achieves accurate segmentations on both large organs, and long and narrow ones, such as kidney and pancreas. Its CNN and Transformer encoders provide complementary features that are helpful for medical image segmentation. Our FCM can effectively fuse these two kinds of features in different scales. Due to effective fusion of complementary features, our CTC-Net has a powerful ability to extract robust feature representations for large, narrow or long-shaped organs, such as kidney, liver and pancreas. The long-range dependency of Transformer enables our network to segment large organs well, such as kidney and liver. The local details by CNNs make our network produce more accurate boundaries. The combination of CNN and Transformer features boosts the overall segmentation performance. Although our method only surpasses TransUNet by 1% in term of DSC, it improves nearly 10% in the HD metric and is well ahead of other models. According to Table 3, our CTC-Net obtains the best result among them. Furthermore, we even achieve a HD of 19.19% in our ablation studies, which is much better than our current architecture. Fig. 4 shows the visual comparisons between the results of our CTC-Net and compared methods. Our method achieves very pleasing segmented results.

### 4.4. Experiments on ACDC

To evaluate the generalization and robustness of our CNN and Transformer complementary model, we also performed related experiments on the ACDC dataset, which contains entirely different modalities and body parts. Table 4 presents the average DSC metric, and our method also achieves the highest average DSC on the ACDC dataset among these state-of-the-art methods. In addition, our method surpasses all the compared methods on two classes of right ventricle (RV) and left ventricle (LV). As for the category of myocardium (MYO), our method obtains the second highest DSC of 85.52%. These experiments effectively validate that our method outperforms the state-of-the-art methods of medical image segmentation.

### 4.5. Ablation studies

In order to prove the rationality of our CTC-Net and the interpretability of each module, we conducted ablation studies on the Synapse dataset.

#### 4.5.1. Evaluation of FCM

To validate the effectiveness of our FCM, we obtain several variants of our CTC-Net by replacing it with other existing modules or removing certain key blocks of FCM.

One straightforward idea is to simply concatenate two feature maps from the CNN and Transformer encoders, and adopt 1 × 1 convolutions to fuse them. In this way, we obtain the first variant of our CTC-Net for validating the importance of our FCM, denoted by "concat + conv".

Inspired by the success of [40], we replace the proposed FCM with a transformer decoder to perform the cross attention between the features from the CNN and Transformer encoders. The query matrix of the cross attention is from the CNN encoder, and the matrices of the key and value pair are generated based on the Transformer encoder. This is the case for one aspect. In the other aspect, the query matrix and the matrices of the key and value pair are reversely from the Transformer and CNN encoders, respectively. The final output is obtained by convolving the outputs from two aspects. Thus, the second variant is generated, and it is named as "cross attention".

The purpose of Channel Attention Block (CAB) is to emphasize channel related information for improving feature robustness. To validate the importance of CAB on the CNN branch, we add channel attention blocks in both CNN and Transformer paths to produce the third variant of our network, named as "Dual CAB". It seems reasonable that we would achieve better results by adding channel attentions in both CNN and Transformer branches. However, enabling channel attentions in both CNN and Transformer branches does not produce better results, as shown in Table 5.

In addition, we also performed three conventional ablation experiments to observe the performance of some blocks in our FCM. The fourth variant of our method is obtained by deleting the Channel Attention Block (CAB), and it is named as "without CAB". We remove the Cross-domain Fusion Block (CFB) from the FCM to produce the fifth variant of our method, named as "without CFB". Furthermore, we remove Correlation Enhancement Block (CEB) from our FCM to verify its effectiveness, named as "without CEB".

The experimental results for ablation studies are listed in Table 5. According to the average DSCs, our method can outperform the five variants by very large margins. In addition, our method achieves the highest DSCs on five categories among all variants. Although the second variant uses a cross attention method for cross-wisely fusing features from Transformers and CNNs, its DSC is far lower than that of our method. That's proofed that the FCM plays a very key role in our network.

#### 4.5.2. Evaluation of encoders

Our CTC-Net has two important encoders, which are Transformer and CNN ones. The Transformer encoder is the major branch for extracting long-range dependencies. The CNN encoder serves as an auxiliary branch to compensate for contextual features and spatial details. To explore the importance of the CNN encoder, we remove it to obtain a variant of our method, which is a pure transformer architecture. The variant has an encoder and a decoder, and both of them are composed of Swin Transformer blocks. The experimental results are shown in Table 6. Our method achieves the average DSC of 78.41%, which is significantly better than that of 76.38% by the variant. In addition, our method also obtains better results on six out of eight categories than the variant. It proves that the CNN encoder is a key branch in our network.

#### 4.5.3. Evaluation of decoders

Most of existing U-shaped networks have approximately symmetric structures. We know by intuition that symmetric networks may achieve excellent results. However, our CTC-Net has two encoders but one decoder, so it is obviously asymmetric. Why not design two decoders for our method?

To answer the above question, we need to evaluate the symmetric variant of our method with two decoders, denoted by "CTC-Net with two decoders". We add a traditional CNN decoder widely used in U-shaped networks to our CTC-Net. The CNN decoder directly accepts feature maps from the CNN decoder of the original CTC-Net as the input, and adopts de-convolutions for gradually up-sampling the feature maps in a learnable manner. To improve spatial details, we also use skip connections between different levels of encoders and decoders. The variant produces two outputs by the Transformer and CNN decoders. Finally, we fuse the two outputs for the variant. As shown in Table 7, the symmetric variant cannot achieve better results than our asymmetric CTC-Net with only one decoder. Obviously, the results are contrary to our intuitions. There may be two main reasons for explaining the results. The first one is that adding a CNN decoder greatly increases network parameters, leading to possible overfitting. Another one is that the two decoders recover feature maps independently and they lack adequate information interchanging.

In addition, we replace the Swin Transformer Block with our self-designed Swin Transformer Decoder to produce another variant, named as "CTC-Net with cross attention". By the way, the cross attention [40] has achieved significant improvements for image segmentation. The variant only differs only in the part of attention calculation from our CTC-Net. We apply cross attention on features from skip connections and up-sampled features at each up-sampling stage, where the query matrix is from skip connection and the matrices of the key and value pair are the up-sampled features. The experimental results are shown in Table 7. The variant with cross attention achieves far better results than the variant with two decoders, but it cannot surpass our CTC-Net.
