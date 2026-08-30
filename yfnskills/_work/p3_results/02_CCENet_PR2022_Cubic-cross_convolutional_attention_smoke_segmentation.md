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
