## Results

### IV. Experiments

#### A. Datasets

To better evaluate the performance of our network, extensive experiments were carried out on four public skin lesion segmentation datasets. We downloaded three publicly available skin lesion segmentation datasets from the International Skin Imaging Collaboration (ISIC), including ISIC 2016 dataset [48], ISIC 2017 dataset [49], and ISIC 2018 dataset [50]. There are a total of 1279 skin lesion RGB images in the ISIC 2016 dataset, where 900 images are used for training and 379 ones for testing. The ISIC 2017 dataset contains 2000 training images, 150 validation images and 600 testing images, respectively. The ISIC 2018 dataset contains 2594 skin lesion RGB images. We randomly divide them into 1815 images as a training set, 259 images as a validation set and the remaining 520 images as a testing set. The last one is PH2 [72] from the dermatology services of Pedro Hispano hospital, Matosinhos, and Portugal. It contains 200 dermoscopic images with a resolution of 768×560 pixels. Following [42], we randomly divided them into 140 instances for training, 20 instances for validation and 40 instances for evaluation.

#### B. Implementation Details

We implemented our BiFBA-Net by PyTorch, and tested it on a PC with a NVIDIA RTX 3090Ti GPU. We uniformly resized all images to 224×224. The weighting coefficients for loss functions were empirically set to 0.6. We follow the data augmentation techniques in TransFuse [51] during training, including random rotation, horizontal flipping, color jittering and so on. Our model was trained for 150 epochs using the Adam optimizer and the batch size of 8. The initial learning rate was set to 7e-5 and the rate decay was set to the cosine scheduling.

#### C. Evaluation Metrics

Jaccard Index (or Intersection Over Union, IoU) is a common indicator for ranking the methods of skin lesion segmentations. We also applied other two widely used metrics for evaluation, i.e. the accuracy (ACC) and the dice coefficient (Dice). The three metrics are defined as follows:

ACC = (TP + TN) / (TP + TN + FN + FP)    (13)

Dice = 2 · TP / ((TP + FP) + (TP + FN))    (14)

IoU = TP / (TP + FN + FP)    (15)

where TP, TN, FP and FN are the abbreviations for True Positive, True Negative, False Positive and False Negative, respectively. Specifically, TP means the number of skin lesion pixels correctly classified as skin lesion ones, and TN is the number of background pixels correctly classified as background ones. Similarly, FP means the number of background pixels falsely classified as skin lesion ones, and FN is the number of skin lesion pixels mis-classified as background.

[NOTE: Eqs. (13)–(14) were scrambled in the source: Eq. (13) printed as "ACC = F N + T P / T P + T N + F N + F P" and Eq. (14)'s denominator printed as "(T P + F P) + (T N + F N)". Both have been normalized to the standard definitions of accuracy and Dice; the numerator order and the "TN" in Eq. (14)'s denominator appear to be extraction/OCR artifacts.]

#### D. Ablation Studies

To evaluate the effectiveness of the proposed modules, we conducted ablation studies by varying the designs of the backbone and different modules. The ISIC 2018 dataset was used for testing, and the results were recorded in mean Dice (mDice), mean IoU (mIoU) and ACC. We used an encoder-decoder architecture as our baseline, which consists of a dual encoder following the designs of ResNet-50 [15] and ViT [14]. In the baseline, we use a simple fusion module that adds CNN and Transformer feature maps directly after alignments, a parallel decoder using a progressive up-sampling strategy, and skip connections. In ablation experiments, data augmentations and training strategies are the same as all methods.

> TABLE I. Experiments on ISIC 2018 by the variants of BiFBA-Net with different structures. [NOTE: table contents not present in extracted text.]

> TABLE II. Experiments on ISIC 2018 by the variants of fusion module with different structures. [NOTE: table contents not present in extracted text.]

We obtained several variants of our model by removing, adding or replacing some components with our designed modules in the baseline network. The variants of our method with different designed modules are validated on the dataset of ISIC 2018. The detailed comparison results are illustrated in TABLE I. Compared with the results by the baseline network, the statistical results of these variants demonstrate that the proposed modules are able to enhance the performance of our network. According to TABLE I, the variants of Baseline+Bi-AG, Baseline+BAD and Baseline+PD outperform the baseline model by 0.36%, 0.44%, and 0.32% in terms of Dice on the ISIC 2018 dataset, respectively. Furthermore, given the same backbone with different composition settings, our method equipped with all designed modules achieves the best performance among all the variants. The experimental results indicate that our BiFBA-Net obtains better improvements of about 0.68%, 1.47% and 1.2% than the backbone network in terms of ACC, IoU and Dice.

To validate the effectiveness of our bi-directional fusion method, we adjusted our Bi-AG with dual outputs to a fusion module with a single output to obtain two variants, named AG_CNN and AG_TRAN, respectively. The AG_CNN variant only uses CNN features to calibrate Transformer features, and its output is transmitted to next Transformer and CNN layers. Reshaping operations are employed when necessary. The AG_TRAN variant is similar to the AG_CNN one, but it uses Transformer features to prune CNN features. We conducted validation experiments on the ISIC 2018 dataset, as shown in TABLE II. Our Bi-AG outperforms the AG_CNN variant by 0.24%, 0.58%, 0.51% in terms of ACC, IoU and Dice. It also gets the improvements of 0.22% ACC, 0.88% IoU, 0.65% Dice than the AG_TRAN variant. The results demonstrate the advantage of our bi-directional fusion method.

As shown in Fig. 4, we also conducted visual comparisons on some typical cases to perceive which regions are attended by our progressive decoders. By observing the visualized attention maps produced by boundary aware, partial and CNN decoders, we find that the CNN decoder can retain the spatial details of objects and suppress the background simultaneously, as shown in Fig. 4d. The major reason may be that the CNN encoder accepts the Transformer output of our Bi-AG by fusing both CNN and Transformer features. Similar visualized results by the partial decoder are also observed, because the partial decoder receives the CNN features of our Bi-AG that contain the global cues from the Transformer encoder (Fig. 4c). This testifies that our Bi-AG plays an important role in improving accuracy. By observing Fig. 4e∼h, we find that the medium predictions of our BAD are progressively refined by using RA modules to process features from CNN and PD decoders. Hence, our BAD is a key module for improving accuracy.

> Fig. 4. Visual comparisons of different attention maps extracted by our proposed three decoders. (a) Input images; (b) Ground truth maps; The outputs of Partial Decoder (c) and CNN decoder (d); (e) The first outputs, (f) the second outputs, (g) the third outputs, and (h) the last outputs of the Boundary Aware Decoder.

#### E. Results on the ISIC 2016 Dataset

On the ISIC 2016 dataset, our BiFBA-Net outperforms several state-of-the-art methods. For the sake of fairness, we tested all compared methods using the same computing environments and data augmentation strategy. The quantitative results are listed in TABLE III. Our method achieves prominent results on three indicators. For example, it gets a mIoU increase of 2.22% compared to FAT-Net [42]. To intuitively show the merits of our BiFBA-Net, we visualize the segmented results of several typical challenging cases in the ISIC 2016 dataset, which are generated by U-Net [5], AttU-Net [23], CPFNet [56] and FAT-Net [42].

> TABLE III. Comparisons with state-of-the-art methods on ISIC 2016. [NOTE: table contents not present in extracted text.]

As shown in Fig. 5, red curves denote the ground truth contour of backgrounds, and green curves are the boundaries of segmentation results. The green lines by our method almost coincide with the red lines of ground truths. For objects with complex and tortuous boundaries (the second row of Fig. 5), both FAT-Net [42] and our method can achieve satisfactory results, but other methods need further improvements. Although other four methods do not work well on the indistinct and small protuberances of skin lesions (the 1st and 3rd rows of Fig. 5), our network still maintains good performance. As for tiny objects, CNN based methods tend to produce overly segmented results and some Transformer methods wrongly segment objects, but our method achieves more accurate results. In addition, our method also works well in the case of partial occlusions by hair. Our BiFBA-Net obtains the best results even for challenging cases with low contrasts and complicated illuminations.

> Fig. 5. Visual comparisons with different methods on the ISIC 2016 dataset. (a) Input images, and (b) corresponding ground truth masks. The results by (c) Attention U-Net, (d) CPFNet, (e) FAT-Net, (f) U-Net, and (g) our method. The red curves are ground truth contours, and the green ones denote the boundaries of segmented results. The IoU, Accuracy and Dice values for the different segmentations are also displayed.

#### F. Results on the ISIC 2017 Dataset

We evaluated our BiFBA-Net on the ISIC 2017 dataset, as shown in TABLE IV. Our network outperforms CNN-based methods by large margins, and it achieves increases of about 1.87%, 4.76% and 3.5% more than FAT-Net [42] in ACC, IoU and Dice metrics. Our method does not adopt any pretraining. The visual comparisons indicate that our BiFBP-Net has superior learning ability, because its Bi-AG effectively emphasizes important features and restrain irrelevant ones. Our BiFBA-Net does not encounter the problem of over-segmentation, which often persecutes existing methods in cases of tiny skin lesions and other non-skin lesion marks, as shown in the 1st and 5th rows of Fig. 6. Unlike compared methods, our method also does not under-segment large objects that almost occupy the entire image, as shown in the 2nd and 3rd rows of Fig. 6. In addition, it can also alleviate the problem of under-segmentation in segmenting objects with fuzzy boundaries, as shown in the 4th row of Fig. 6. Visual comparisons validate the significance of our boundary aware supervision strategy. [NOTE: "BiFBP-Net" appears as printed in the source; presumably BiFBA-Net.]

> TABLE IV. Comparisons with state-of-the-art methods on ISIC 2017. [NOTE: table contents not present in extracted text.]

> Fig. 6. Visual comparisons with different methods on the ISIC 2017 dataset. (a) Input images. (b) Ground truths. The results by (c) Attention U-Net, (d) CPFNet, (e) FAT-Net, (f) U-Net, and (g) our method. The red curves are ground truth contours, and the green ones are the contours of segmented results. The IoU, Accuracy and Dice values for each visualized segmentation image are also displayed.

#### G. Results on the ISIC 2018 Dataset

The proposed BiFBA-Net is compared with thirteen state-of-the-art methods on the ISIC 2018 dataset. These compared methods are listed in TABLE V. FTL [52], ERU [53], DAGAN [26], CKDNet [54], FAT-Net [42] and ACCPG-Net [64] are specially designed for the skin lesion segmentation task, while the rest compared methods are outstanding models for general medical image segmentation. As shown in TABLE IV, our method outperforms FAT-Net [42], which employs the pre-trained networks of DeiT [55] and ResNet [15] as its backbone. Our method achieves 96.26%, 83.00%, 89.72% in terms of ACC, IoU and DICE, respectively.

> TABLE V. Comparison with state-of-the-art methods on ISIC 2018. [NOTE: table contents not present in extracted text.]

To validate that the results by our method are convincing, we also conducted visual comparisons with several excellent methods on several typical challenging cases from the ISIC 2018 dataset. Fig. 7 shows the visualized results generated by four most representative methods, including U-Net [5], AttU-Net [23], CPFNet [56] and FAT-Net [42]. The results by our BiFBP-Net are more similar to corresponding ground truths than these compared methods. As shown in Fig. 7e, FAT-Net [42] apparently produces more artifact and uncontrollable results. For small objects, the predictions by U-Net [5] and AttU-Net [23] are less satisfactory than others due to inadequate guidance on long-range dependencies. Comparing to other dual or multiple encoder methods, our BiFBP-Net produces significantly less artifacts and uncontrollable effects, and achieves the best results among them, especially for the skin lesions with relatively small scales and irregular shapes. Experimental results indicate that our proposed method is able to capture finer information about object structures and produce more accurate predictions.

> Fig. 7. Visual comparisons with different methods on the ISIC 2018 dataset. (a) Input images. (b) Ground truth. The results by (c) Attention U-Net, (d) CPFNet, (e) FAT-Net, (f) U-Net, and (g) our method. The red curves denote ground truth contours, and the green ones are the contours of segmented results. The IoU, Accuracy and Dice values for each visualized segmentation image are also displayed.

#### H. Results on the PH2 Dataset

To further verify our BiFBA-Net, we conducted experiments on PH2. Unlike three aforementioned datasets with large data distribution, various scales and blurry boundaries, the PH2 dataset only contains hundreds of dermatoscopy images and the contrast of samples is relatively obvious. We compared our BiFBA-Net with thirteen methods. The results are listed in TABLE VI. The results illustrate that our method achieves the best values, which are 97.52% (ACC), 95.32% (DICE), and 91.19% (IoU). The results highlight the robust generalization ability of our method. As shown in Fig. 8, our BiFBA-Net is able to capture finer structural information and produce more accurate edges. The main reasons are that our method creates a dual-encoding structure with Transformers and CNNs, and designs Bi-AG to bi-directionally fuse features. These reasons make our method to have more robustness to noises and achieve better accuracy.

> TABLE VI. Comparison with state-of-the-art methods on PH2. [NOTE: table contents not present in extracted text.]

> Fig. 8. Visual comparisons with different methods on the PH2 dataset. (a) Input images. (b) Ground truth. The results by (c) Attention U-Net, (d) CPFNet, (e) FAT-Net, (f) U-Net, and (g) our method. The red curves denote ground truth contours, and the green ones are the contours of segmented results. The IoU, Accuracy and Dice values for each visualized segmentation image are also displayed.
