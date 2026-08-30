Fig. 1. Some samples of smoke image.
Fig. 2. (a) Input image; (b) DANet+BCE; (c) DANet+SAL; (d) CCNet+BCE; (e) CCNet+SAL; (f) SAGINN+BCE; (g) SAGINN+SAL.
Fig. 3. The overall framework of SAGINN.
Fig. 4. The detailed structure of GINL.
Fig. 5. Pyramid pooling reshape (PPR).
Fig. 6. The framework of PHSA.
Fig. 7. Details of non-overlap depthwise convolution.
Fig. 8. Samples of (a) Synthetic image, (b) Real image, and (c) Real video.
Table II. Ablation study of GINL.
Table III. Ablation study of PPR.
Table IV. Results of different high-level semantics.
Table V. Results of different fusion modes.
Table VI. Ablation study of softmax.
Fig. 9. Visualization of spatial attention maps. (a) Image, (b) input of PHSA in SAGINN, (c) output of PHSA in SAGINN. Best viewed in color.
Fig. 10. Spatial attention maps of the output of PHSA. (a) Image, (b) None, (c) 8 × 8, (d) 4 × 4 and 8 × 8, (e) 2 × 2, 4 × 4 and 8 × 8 (SAGINN). Best viewed in color.
Table VII. Comparisons of three methods with different loss.
Table VIII illustrates the results of different loss function. Single-loss-A and single-loss-B only supervise the segmentation with SAL, but the difference lies in that the former completely removes the classification branch in the model, while the latter just cancels the supervision of classification without making any changes on the architecture. We observe that multi-task joint training can achieve better performance, which is higher than single-loss by about 3%. Another finding is that with the same structure, the performance of multi-loss is significantly better than that of single-loss, which contributes to 1.2∼1.5% improvement. This verifies the common belief that effective classification supervision can help PHSA learn more excellent high-level semantics to assist the model to make better decisions.
Table IX. Ablation study of different α.
Table X. Results of different training strategies.
Table XI. Smoke segmentation performance on SYN70K.
Table XII. Smoke segmentation performance on SMOKE5K.
Figure 11 provides some typical qualitative results of synthetic smoke images, which can support quantitative findings by visually assessing the predictions of compared methods. To highlight the difference between segmentation masks, we mark the samples with different lines, in which the solid blue line reflects the accuracy of edge prediction, and the dotted red line displays the segmentation ability on the difficult smoke area. We have the following observations. Firstly, most method can achieve better results on smoke occupying large area in the images, which mainly because most methods have a bias to capture abstract information about salient objects. Secondly, our model still consistently outperforms other methods for different smoke patterns and a variety of complex scenes. For example, for the second and third samples, our method shows absolute superiority in edge prediction, which is not only smoother, but also closer to corresponding GT. Thirdly, as for challenging smoke, most methods have more obvious incorrect segmentation except for our model, like the first, fourth and fifth samples, many methods either misclassify similar backgrounds as smoke or miss areas of thin smoke, which accredit to both the strong generalization ability of the model, and the priority of SAL-induced parameters modification. Figure 12 and 13 depict segmentation results of real images and videos, which are basically consistent with the synthetic images, and SAGINN further shows evident advantage. In addition to getting more accurate positioning and more detailed boundaries, SAGINN achieves more impressive results on challenging objects, such as the last example in Fig. 12 and the white smoke video in Fig. 13.
Fig. 11. Results on synthetic images. (a) Test images, (b) GT. Segmentation results of (c) Deeplab v1, (d) PSPNet, (e) DSS, (f) CMNet, (g) CGRNet, (h) DANet, (i) CCNet, (j) Segmenter, (k) Segformer, (l) Twins, (m) Swin, (n) our SAGINN. Best viewed in color.
Fig. 12. Results on real images. (a) Test images. Segmentation results of (b) Deeplab v1, (c) PSPNet, (d) DSS, (e) CMNet, (f) CGRNet, (g) DANet, (h) CCNet, (i) Segmenter, (j) Segformer, (k) Twins, (l) Swin, (m) our SAGINN.
Fig. 13. Results on real videos: white smoke and black smoke. (a) Test frames. Segmentation results of (b) Deeplab v1, (c) PSPNet, (d) DSS, (e) CMNet, (f) CGRNet, (g) DANet, (h) CCNet, (i) Segmenter, (j) Segformer, (k) Twins, (l) Swin, (m) our SAGINN. Best viewed in color.
Fig. 14. Results on real images. (a) Test images. Segmentation results of (b) Deeplab v1, (c) PSPNet, (d) DSS, (e) CMNet, (f) CGRNet, (g) DANet, (h) CCNet, (i) Segmenter, (j) Segformer, (k) Twins, (l) Swin, (m) our SAGINN.