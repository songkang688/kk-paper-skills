# 前向生成测试 — 通用学术英语 baseline 版（刻意不套用任何风格规则）

同一组夹具事实，用普通计算机视觉论文的写法生成，作为对照组。

## Introduction（节选）

Crack detection has attracted increasing attention in recent years because of its importance in infrastructure maintenance. With the rapid development of deep learning, many methods have been proposed and have achieved promising results. However, the performance of existing methods is still limited, especially for images captured at night, where the illumination is complex. Cracks are thin and have low contrast, which makes the task difficult. Moreover, shadows and oil stains may cause false positives.

In this paper, we propose a novel network for night-time crack segmentation. The proposed network is based on ResNet-18 and consists of three modules, namely DAA, IPE and AFB. DAA is a directional aggregation attention module. It uses four strip kernels to extract directional features. IPE is an illumination prior embedding module. It predicts an illumination map, which is supervised by a regression loss. AFB is an adaptive fusion block used to fuse the features from DAA and IPE. Our contributions are that we propose the DAA module, the IPE module and the AFB module, and that our network is lightweight.

## Methods（节选）

### The DAA module

The DAA module is shown in Fig. 2. It contains four strip convolutions with orientations of 0°, 45°, 90° and 135°. The four responses are combined by a channel-wise maximum operation, and a sigmoid function is applied to generate the attention map. The attention map is then multiplied with the input feature. This module can capture directional information of cracks, which is helpful for segmentation.

### The IPE module

The IPE module predicts an illumination map from the highest encoding stage. The map is broadcast over the decoded features. A regression loss is used for supervision. This module makes the network aware of the illumination.

### Loss function

The total loss is the weighted sum of a cross-entropy loss and a regression loss, with α set to 0.3.

## Results（节选）

### Comparisons with state-of-the-art methods

We compare our method with several state-of-the-art methods on three datasets. The results are given in Table 3. Our method achieves 74.8% mIoU on SYN-N1, which is better than X-Net (73.9%). On SYN-N2, the F1 of X-Net is 75.1% and ours is 74.6%. Our model has 2.1 M parameters and 8.7 GFLOPs, and runs at 41 FPS, while X-Net has 24 M parameters. These results demonstrate the effectiveness and efficiency of the proposed method.

### Ablation studies

We conduct ablation studies to verify the effectiveness of each module. As can be seen in Table 2, the mIoU decreases by 3.4% without DAA, by 1.1% on synthetic sets and 2.9% on RN-800 without IPE, and by 0.6% without AFB. This demonstrates that all the three modules are effective.

## Conclusion（节选）

In this paper, we proposed a lightweight network for night-time crack segmentation. The network consists of a DAA module, an IPE module and an AFB module. Extensive experiments on three datasets demonstrate that the proposed method achieves state-of-the-art performance with only 2.1 M parameters. In the future, we will further improve the performance of our method.
