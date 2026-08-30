# 前向生成测试 — 目标风格版（按 final_skill/SKILL.md 生成）

## Introduction（节选）

Pavement cracks provide the earliest visible evidence of structural deterioration, and failing to find them in time leads to costly reconstruction and to traffic accidents. Manual inspection requires closing lanes and depends on the experience of inspectors, so it cannot be repeated at the frequency that maintenance planning needs. Vision-based inspection can be classified into two categories: patch-level crack recognition and pixel-level crack segmentation. Segmentation offers more information than recognition, because it delineates the extent of every crack, but it is far more challenging when images are captured at night.

It is a challenging task to segment cracks from night-time pavement images. The reasons are three folds: 1) cracks are only a few pixels wide and their contrast against pavement is low, 2) illumination from vehicle headlamps is highly uneven within a single frame, and 3) shadows and oil stains share the elongated dark appearance of cracks.

Existing segmentation methods aggregate multi-scale features by concatenation, so the continuity of a thin structure along its own direction is not modelled. Channel attention reweights feature maps in a global manner, and therefore local directional evidence is discarded. In addition, these methods treat every image identically, so image-level illumination information is not involved at all.

To recover the directional continuity, we propose a Directional Aggregation Attention (DAA) module. To embed image-level illumination information, we propose an Illumination Prior Embedding (IPE) structure, and we impose a regression loss on the predicted illumination map so that the structure is forced to extract this information correctly. To combine the two kinds of responses, we design an Adaptive Fusion Block (AFB). The main contributions of this paper are summarized as follows:

1) We propose a Directional Aggregation Attention (DAA) module. Four strip kernels with different orientations are convolved with the input, and the dominant orientation is selected in a channel-wise manner, so the receptive field is concentrated along the crack rather than spread over background pixels.

2) To make the network aware of uneven headlamp illumination, we propose an Illumination Prior Embedding (IPE) structure. A regression loss is imposed on the predicted illumination map and the mean-luminance map computed from the input, thus we can guarantee that the structure really encodes image-level illumination.

3) By integrating DAA, IPE and an Adaptive Fusion Block (AFB) on a ResNet-18 backbone, we propose a lightweight network for night-time crack segmentation with only 2.1 M parameters.

## Methods（节选）

### Directional Aggregation Attention

To recover the directional continuity that concatenation-based fusion discards, we propose a Directional Aggregation Attention (DAA) module. A crack extends along one dominant orientation while its cross-section is only a few pixels wide, so an isotropic kernel spends most of its capacity on background pixels. For an input feature tensor X ∈ R^{C×H×W}, we first convolve X with four strip kernels oriented at 0°, 45°, 90° and 135° to obtain four directional responses, then take a channel-wise maximum over these responses to produce a dominant-orientation map, and finally weight X by the sigmoid of the map so that the output keeps the same size as the input.

    A = σ( max_{d∈D} ( W_d ∗ X ) ),   X_out = X ⊙ A    (1)

where D is the set of the four orientations, W_d is the strip kernel of orientation d, σ(·) is the sigmoid function, ∗ denotes convolution, and ⊙ denotes element-wise multiplication.

### Illumination Prior Embedding

To embed image-level illumination information, we propose an Illumination Prior Embedding (IPE) structure. Headlamp illumination changes sharply across a single frame, so a network trained without any illumination cue tends to interpret a dark background region as a crack. We predict a single-channel illumination map from the highest encoding stage, and then broadcast it over the decoded features. To ensure that the predicted map really carries illumination information, we impose a regression loss between the map and the mean-luminance map directly computed from the input image.

### Loss function

Our objective function contains two terms. A cross-entropy loss supervises the final segmentation output, and a regression loss supervises the illumination map produced by IPE. The two terms are weighted by α, which is set to 0.3 in our implementation.

## Results（节选）

### Ablation studies

To validate the contribution of each module, we removed them one at a time from the full model, as shown in Table 2. As shown in Table 2, we find that removing DAA reduces mIoU by 3.4%, so it means that directional aggregation plays an important role in preserving the continuity of thin cracks. The main reason is that the strip kernels concentrate the receptive field along the crack direction instead of spreading it over background pixels. Removing IPE reduces mIoU by 1.1% on the two synthetic sets, but by 2.9% on RN-800. The reason may be that the illumination of the real images varies far more strongly within a single frame than the synthetic rendering reproduces. Removing AFB reduces mIoU by 0.6%.

### Comparisons with state-of-the-art methods

Table 3 lists quantitative comparison results on the three datasets. Our method achieves the highest mIoU of 74.8% on SYN-N1, while X-Net, the strongest compared method, obtains 73.9%. X-Net achieves slightly higher F1 of 75.1% than our 74.6% on SYN-N2, but our model is obviously lighter, with approximately 11× fewer parameters than X-Net, and it reaches 41 FPS at 8.7 GFLOPs.

## Conclusion（节选）

Cracks in night-time pavement images are only a few pixels wide, and headlamp illumination is highly uneven within a single frame. These properties lead to a challenging task of crack segmentation. To recover the directional continuity that concatenation-based fusion discards, we propose a Directional Aggregation Attention module, in which four strip kernels select the dominant orientation of a crack in a channel-wise manner. To embed image-level illumination information, we propose an Illumination Prior Embedding structure supervised by a regression loss. By integrating the two modules with an Adaptive Fusion Block on a ResNet-18 backbone, we propose a lightweight network with only 2.1 M parameters. Experiments on two synthetic datasets and a real one show that our method outperforms existing state-of-the-art methods while running at 41 FPS.

Although our network achieves encouraging accuracy, it degrades on cracks narrower than two pixels. The main reason may be that our decoder starts to recover feature maps from the quarter-resolution stage, where such thin structures have already been merged into the background. In the future, we will explore decoding paths that maintain full resolution for the thinnest structures.

## 图注（节选）

Fig. 4. Ablation analysis. (a) the plain encoder-decoder baseline; (b) the baseline with DAA; (c) the baseline with DAA and IPE; (d) the proposed network with DAA, IPE and AFB.

Fig. 6. Visual comparisons on the RN-800 dataset. (a) Input images. (b) Ground truth masks. The results by (c) U-Net, (d) DeepCrack, (e) X-Net, and (f) our method. The blue outlines indicate the annotated cracks, while the yellow ones show the predictions of each method.

TABLE III Comparisons with state-of-the-art methods on the three night-time crack datasets
