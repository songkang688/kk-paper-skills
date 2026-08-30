## Results

### IV. Experiments and Results

#### A. Experimental Datasets

Smoke has some dynamic natures, such as its constantly changing shape and ambiguous boundary. These natures make pixel-level manual annotation of real smoke images extremely challenging. Consequently, many researchers have turned to synthetic smoke datasets for model training. For example, the SYN70K dataset used in [1], [3], [6], and [46] generates diverse and realistic smoke samples, providing valuable support for training and evaluation. In this study, we conducted relevant experiments on synthetic datasets (SYN70K) and our newly constructed real-world Smoke and Fire Segmentation dataset (SFS3K). To facilitate further research in smoke and fire segmentation, we will publicly release the SFS3K dataset at https://github.com/KL0319/SFS3K. Some examples of the SFS3K datasets as shown in Fig. 8.

> Fig. 8. Some examples from our SFS3K. (a) Images, (b) Labels.

#### B. Experimental Settings

All experiments were conducted on a workstation equipped with an Intel i9-10900K CPU and an NVIDIA GeForce RTX 2080Ti 11GB GPU. Models were implemented using the PyTorch [47] deep learning framework. We trained the models with a batch size of 32 for 100 epochs, and used the AdamW [48] optimizer with an initial learning rate of 0.002.

#### C. Evaluation Metrics

To comprehensively evaluate the performance of the smoke segmentation method, we adopt several key metrics: Accuracy (Acc), Dice coefficient (Dice), and Intersection over Union (IoU). Accuracy measures the proportion of correctly predicted pixels relative to the total number of pixels, reflecting the model's overall classification performance. Dice coefficients quantify the overlap similarity between the predicted segmentation and the ground truth annotations. IoU calculates the ratio of the intersection to the union between the predicted and true regions, providing a robust measure of spatial alignment. In addition to segmentation accuracy, we evaluated the efficiency of compared models using the following metrics: the number of parameters, Floating Point Operations (FLOPs in G), and Frames Per Second (FPS).

#### D. Ablation Experiments

In this paper, we adopt a UNet [17] architecture with channel configurations of [16, 32, 64, 128, 256] as the baseline for our ablation experiments. We modify key components, such as the encoder, decoder and skip connections, to investigate the impact of our proposed modules on model performance in smoke segmentation. TABLE I provides detailed descriptions of the various model variants, while TABLE II presents a comparative analysis of their segmentation performance on the SFS3K and SYN70K datasets.

> TABLE I. Details of different variants. [NOTE: table contents not present in extracted text.]

> TABLE II. Segmentation results of various variants on different datasets. [NOTE: table contents not present in extracted text.]

As shown in TABLE II, replacing the baseline encoder with our proposed encoder (Model 1) results in only a marginal increase of 0.03M parameters (from 1.94 M to 1.97 M). However, it achieves a significant reduction in computational cost, with FLOPs decreasing from 2.63G to 0.74G. Importantly, this modification also improves segmentation accuracy, with mIoU increasing by 2.25% on SFS3K and 2.28% on SYN70K. When the standard convolutions in the short connection path of UNet are replaced with GCBAM (Model 2), the number of parameters drops by 0.55 M, and FLOPs are further reduced to 0.71G, while segmentation performance improves notably. Next, we replaced the skip connection of UNet with GFM or MGIM (Model 3) for substantially reducing parameters to 0.91M and FLOPs to 0.62G. It is nearly an order of magnitude smaller than the original. This modification significantly reduces computational overhead while preserves high segmentation accuracy. Finally, replacing the U-Net decoder with EEM (Model 4) yields the best overall performance. The model achieves the lowest complexity with only 0.73M parameters and 0.30G FLOPs. Compared to the baseline, mIoU increases by 3.58% on SFS3K and 3.44% on SYN70K, demonstrating superior efficiency and segmentation capability.

By incrementally refining individual components within the UNet architecture, we systematically reduced both the number of parameters and computational complexity, and simultaneously improve segmentation performance. Among all evaluated variants of our model, our final model (Model 4) achieves an optimal trade-off between model scale and accuracy.

Fig. 9 shows visualized segmentation comparisons of different variants on the SFS3K dataset (images 1, 2, and 3) and the SYN70K dataset (images 4, 5, and 6). The baseline model exhibits several limitations: (1) insufficient refinement of edge details, particularly evident in images 1 and 3; (2) poor discrimination between foreground smoke and background regions, observed in images 2, 4, and 6; and (3) significant segmentation errors, as seen in image 5. To address these issues, we progressively optimize the encoder, decoder, and skip connections, resulting in four variant models (Model 1 to Model 4). Notably, our model (Model 4) achieves the best overall performance.

> Fig. 9. Visualization of different variants on the SFS3K and SYN70K test sets. (a) Smoke images, (b) Labels, (c) Baseline, (d) Model 1, (e) Model 2, (f) Model 3, and (g) Model 4 (Ours).

We conducted an ablation experiment to evaluate the effectiveness of GCBAM by replacing it with CBAM. As shown in TABLE III, our GCBAM reduces the parameter number by 0.01M compared to the CBAM. This reduction is attributed to its grouping strategy and the shared CBAM design, which together optimizes the model structure. Although the computational complexity (FLOPs) remains comparable, GCBAM demonstrates superior performance in key metrics such as mIoU. Specifically, on the SFS3K dataset, GCBAM improves mIoU from 80.48% (with CBAM) to 81.16%, an increase of 0.68%. On the SYN70K dataset, the mIoU increases from 78.04% to 78.68%, representing a 0.64% improvement. These improvements indicate that GCBAM enhances feature modeling capability and reduces redundant computation, significantly boosting model performance without incurring additional computational cost.

> TABLE III. Ablation study of CBAM and GCBAM. [NOTE: table contents not present in extracted text.]

To evaluate the effectiveness of the joint loss function, we conducted experiments with models, which were trained using the weighted Binary Cross-Entropy loss (l^ω_BCE), the weighted Intersection over Union loss (l^ω_IoU), and their combination, respectively.

As shown in TABLE IV, the two loss functions yield the comparable mIoU performance on the two smoke segmentation datasets. In contrast, the joint function of the two losses significantly improves the model's performance. Specifically, its mIoU reaches 81.16% on the SFS3K dataset, which outperforms the best result of two single losses by 0.48%. Similarly, its mIoU increases to 78.68% on the SYN70K dataset, leading to a gain of 0.54% compared to the best result.

> TABLE IV. Ablation study of different loss function. [NOTE: table contents not present in extracted text.]

The superior performance of the joint loss can be attributed to its complementary optimization effects. l^ω_BCE ensures pixel-wise classification accuracy, while l^ω_IoU enhances global structural consistency. Their combination promotes a balance between local detail and global information, leading to more robust segmentation performance across diverse datasets.

#### E. Comparison With State-of-the-Art Methods

To validate the State-Of-The-Art performance of our MGICFN in lightweight smoke segmentation tasks, we conducted extensive comparative experiments with several mainstream lightweight architectures on the SFS3K and SYN70K datasets. These architectures include UNet [17], BiSeNet V2 [36], MALUNet [39], EIUNet [40], SwiftFormer [41], PIDNet [49], and ULite [50].

> TABLE V. Segmentation results of different lightweight method. [NOTE: table contents not present in extracted text.]

According to the results in TABLE V, our MGICFN achieves outstanding segmentation accuracy across both datasets. On the SYN70K dataset, our MGICFN attains a Dice score of 87.30%, an accuracy of 92.95%, and a highly competitive mIoU of 78.68%. Similarly, our method obtains a Dice score of 88.70%, an mIoU of 81.16%, and an accuracy of 91.93% on the SFS3K dataset. In addition, our MGICFN exhibits a remarkable advantage in terms of parameters and computational complexity. With only 0.73M parameters, it is the most lightweight model among all compared methods. In terms of computational cost, our method requires only 0.30G FLOPs, which is merely 1/35 of that required by UNet (10.48G FLOPs). Our method also achieves an excellent balance between segmentation performance and computational efficiency. Although ULite also has a low parameters and computational load, our method outperforms it across all key metrics, particularly mIoU and accuracy.

To crossly verify the quantitative analysis results, we further conducted qualitative comparisons of mainstream lightweight models on the synthetic smoke dataset (SYN70K) and the real-world smoke dataset (SFS3K). The visualized results are shown in Fig. 10 and Fig. 11.

> Fig. 10. Visualization of different lightweight methods on the SYN70K test sets. (a) Smoke images, (b) Ground truth, (c) UNet, (d) BiSeNet V2, (e) MALUNet, (f) EIUNet, (g) SwiftFormer, (h) PIDNet, (i) ULite, and (j) MGICFN (Our method).

> Fig. 11. Visualization of different lightweight methods on the SFS3K test sets. (a) Smoke images, (b) Ground truth, (c) UNet, (d) BiSeNet V2, (e) MALUNet, (f) EIUNet, (g) SwiftFormer, (h) PIDNet, (i) ULite, and (j) MGICFN (Our method).

By analyzing visualized results, we find some important observations. Most methods exhibit commendable performance in the case of large smoke objects. It shows they have good adaptation to large objects. The major reason is their ability to capture abstract information about prominent objects. Our method has the advantage in complex scenarios and diverse smoke patterns, because it exhibits more stable and superior performance than others. Taking the second and fourth samples in Fig. 10 as examples, our method considerably reduces the proportion of false positive regions, and achieves a higher accuracy of predicted edge details under challenging conditions where smoke regions are significantly sparse or low in concentration.

As shown in the third and fourth samples of Fig. 11 with small or visually less salient smoke, existing methods commonly suffer from missed detection, but our method still accurately identifies these regions. Specifically, in the fifth sample with thin smoke in a forest scenario, our MGICFN is able to segment smoke contours that are more complete than other models. In the sixth sample with a low-light environment complicated by fire, our method obtains satisfactory segmentation. Although minor false segmentation occurs in the sky region, our error level is significantly lower than that of other comparative methods, and it remains within an acceptable range.

In addition, we report the total training time of several models using a batch size of 32 and 100 epochs on the SYN70K dataset. As shown in the "Time (h)" column of TABLE V, our method requires 11.5 hours, which represents a significant advantage compared to UNet (19.5 hours). Compared to some of lightweight methods, our MGICFN spends the relatively longer training time on training. The primary reason is the computational cost associated with the Fourier transform in the encoder. This can maintain higher initial feature resolutions to improve segmentation accuracy, particularly for capturing subtle and structural details in smoke regions. Despite the additional time cost, our MGICFN offers superior performance with the lowest parameter count and FLOPs among all compared methods.

On the other hand, we compared state-of-the-arts smoke segmentation methods on the SYN70K dataset in recent years, including DSS [1], W-Net [46], Fizzi [9], TANet [3], LSSNet [10], SmokeSeger [5], FoSp [4], and SAGINN [6].

> TABLE VI. Comparative results on SYN70K with different smoke segmentation methods. [NOTE: caption reconstructed; source text was garbled as "COMPARATIVE RESULTS ON SYN70K WITH DIFFERENT SSmoke SEGMEN...TATION METHOD". Table contents not present in extracted text.]

TABLE VI shows the performance comparison results of different methods. SAGINN achieves an mIoU of 83%, but it has significantly larger model size with 101.1M. In contrast, our MGICFN obtains an mIoU of 78.7% while maintaining an extremely lightweight architecture with only 0.73 million parameters that are 138× fewer parameters than SAGINN. Notably, when the classification auxiliary branch is removed from SAGINN, its mIoU drops to 79.9%, which is only marginally higher than our model's performance, highlighting MGICFN's strong efficiency-accuracy trade-off. LSSNet is another lightweight method for smoke segmentation. Our MGICFN shows more obvious advantages. MGICFN not only reduces parameters by 0.15M, but also increases mIoU by 5.5%.

#### F. Real-Time Inference Performance

To evaluate the inference efficiency of our method in real-world scenarios, we compared several lightweight methods on a smoke video dataset. These methods include UNet [17], MALUNet [39], PIDNet [49], LSSNet [10], and our MGICFN. For the sake of comparisons, all evaluations were conducted under consistent conditions using a 480 × 480 resolution, and the performance metrics including average FPS and latency were evaluated on the first 100 frames of the same video.

> TABLE VII. Real-time performance evaluation results. [NOTE: table contents not present in extracted text.]

According to TABLE VII, our method achieves competitive performance with only 0.73M parameters and 1.35G FLOPs. It demonstrates significantly higher efficiency than other methods. Our method obtains a frame rate of 57.4 FPS. Although our frame rate is slightly lower than other methods, our method has higher resolutions and accuracy than others. Unlike most methods using 1/4 original resolutions in early stages, our MGICFN maintains 1/2 original resolutions to preserve spatial details. This strategy slightly reduces throughput, but it significantly improves segmentation accuracy for thin and semi-transparent smoke. In addition, our method uses the Fourier transform to improve accuracy, but it incurs substantial computational cost at high resolutions.

As shown in Fig. 12, we randomly selected three samples from video frames for visual comparisons, and predicted regions are annotated with red contours. It can be observed that our method significantly outperforms UNet and MALUNet in terms of foreground awareness. Specifically, in the upper-left region of the video sequence, our method effectively avoids erroneous segmentation artifacts present in other approaches. Compared to PIDNet and LSSNet, our method demonstrates noticeably superior segmentation performance, exhibiting more consistent and clearer boundary depiction. Although PIDNet achieves slightly better segmentation results in the second sample, our method shows higher overall performance and greater robustness in the other two samples than others.

> Fig. 12. Segmentation of different lightweight models on a real-world smoke video. (a) UNet, (b) MALUNet, (c) PIDNet, (d) LSSNet, and (e) our MGICFN.
