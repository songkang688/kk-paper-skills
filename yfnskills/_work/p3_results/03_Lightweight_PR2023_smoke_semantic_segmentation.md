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
