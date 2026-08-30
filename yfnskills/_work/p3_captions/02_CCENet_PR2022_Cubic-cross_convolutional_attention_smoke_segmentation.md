Fig. 1. Cubic-cross convolutional attention module.
Fig. 2. The equivalent cubic-cross kernel for a kernel of 3×3.
Fig. 3. Count prior embedding.
Fig. 4. The generation of an ideal count map.
Fig. 5. The overall architecture of our CCENet.
Fig. 5 illustrates the overall architecture of our network. The backbone of CCENet is the ResNet for feature encoding. The encoded feature maps are then fed to the module of cubic-cross convolutional attention described in Section 3.1. At last, we use the module of count prior embedding presented in Section 3.2 to further improve feature representation and output a final segmentation result.
Table 1. Comparisons with different combinations of modules.
Table 2. Comparison with different attention modules.
Table 3. Comparison results with the state-of-the-art methods on the PASCAL VOC2012 validation dataset.
Table 4. Comparisons of methods using standard convolution and our cubic-cross convolution.
Fig. 6. Test results on synthetic data. (a) Synthetic images. (b) Corresponding ground truths. Results of (c) FCN, (d) SegNet, (e) SMD, (f) TBFCN, (g) DeepLab v1, (h) ESPNet, (i) HG-Net 2, (j) HG-Net 8, (k) W-Net, and (l) our method.
Fig. 7. Test results on realistic data. (a) Realistic images. Results of (b) FCN, (c) SegNet, (d) SMD, (e) TBFCN, (f) DeepLab v1, (g) ESPNet, (h) HG-Net 2, (i) HG-Net 8, (j) W-Net, (k) DSS, and (l) our method.
Table 5. Comparison results with the state-of-the-art methods on the three synthetic test datasets.
Fig. 8. Visualized results on real smoke scenes. (a) Real smoke images. Visualized results by (b) DSS, (c) W-Net, and (d) our method.
Table 6. Quantitative results on real smoke scenes.
Fig. 9. Test results on realistic smoke videos. (a) Original frames from videos. Results of (b) SMD, (c) TBFCN, (d) LRN, (e) DeepLab v1, (f) ESPNet, (g) HG-Net2, (h) HG-Net8, (i) DSS, (j) W-Net, and (k) our method.