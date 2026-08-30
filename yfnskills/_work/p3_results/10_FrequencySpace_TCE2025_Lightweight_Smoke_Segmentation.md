## Results

### IV. Experiments and Results

#### A. Experimental Datasets

The dynamic characteristics of smoke, including its varying shapes and indistinct boundaries, make pixel-level accurate annotation of real smoke images extremely challenging. To address this issue, the synthetic smoke dataset SYN70K [12] was introduced and has been widely used in [14], [15], [16], and [17]. SYN70K consists of approximately 70,000 images, each with a resolution of 256×256 pixels. We divide these images into training and validation sets in an 8:2 ratio. The test set includes the DS01, DS02, and DS03 subsets of SYN70K, totaling 3,000 images. We combined DS01, DS02, and DS03 for consistent evaluation into a unified SSS test set.

SMOKE5K [25] is a mixed smoke dataset comprising 5,400 images, which include 4,000 synthetic smoke images obtained from SYN70K and 1,400 real-world smoke images. Among them, 5,000 images are designated for training, while 400 images are reserved for testing. The real smoke images in this dataset face several challenges, such as sparse smoke, small targets, and similar backgrounds, which make the smoke segmentation task particularly difficult. In the examples shown in Fig. 6, we have highlighted the smoke regions with red boxes. To ensure consistency in processing, we resize each image to 480×480 pixel.

> Fig. 6. Smoke examples. (a) Synthetic smoke images. (b) Real smoke images.

#### B. Experimental Settings

All training, validation, and testing experiments were conducted on a system equipped with a single NVIDIA 2080Ti GPU, and under the PyTorch [49] framework. During the training process, we employed the standard AdamW optimizer and adopted the CosineAnnealingLR [50] scheduler to adjust the learning rate, and used a maximum of 50 iterations and a minimum learning rate 1e-5.

For the SYN70K dataset, the initial learning rate and the batch size were set to 2e-3 and 32, respectively. The model was trained for 50 epochs. For the SMOKE5K dataset, the initial learning rate and the batch size were set to 1e-3 and 6, respectively. The model was trained for 100 epochs.

#### C. Evaluation Metrics

To evaluate the proposed method's performance, we selected Intersection over Union (IoU) as the primary metric for segmentation accuracy. We measured the overall performance of the model by calculating the mean IoU (mIoU) over the test dataset. Additionally, we conducted a comparative analysis of the parameter numbers for each model and compared their Floating Point Operations (FLOPs) to assess computational complexity.

For the SMOKE5K dataset, we adopted the same performance metrics [15] and [25], including Mean Square Error (MSE) and F-Measure (Fβ), to ensure the consistency and comparability. The MSE calculates the average of the squared differences between predicted values and true labels. The formula for calculating MSE is as follows:

MSE = (1/N) Σ_{i=0}^{N−1} (y_i − ŷ_i)^2    (20)

where y_i represents the ground truth, ŷ_i represents the predicted value, and N is the total number of pixels. In practical testing, we calculate the average of MSE for all test data to obtain the mean Mean-square error (mMse). The mMse reflects the model's overall performance.

The Fβ serves as a supplementary metric to the mMse, and it is the mean of precision and recall for effectively balancing the evaluation of both accuracy and recall.

#### D. Ablation Experiments

We conducted ablation experiments on the SSS test set of SYN70K, with the input image resolution set to 256×256 pixels for FLOPs evaluation.

To explore the impact of the channel dimension on model performance, we constructed five models of different scales by adjusting the channel width: FSIHAN-Tiny (T), FSIHAN-Small (S), FSIHAN-Base (B), FSIHAN-Middle (M), and FSIHAN-Large (L). These experiments systematically analyze the specific impact of different architectural scales on task performance. The related experimental results are presented in TABLE I.

> TABLE I. Performance under different channel configurations. [NOTE: table contents not present in extracted text.]

According to the results presented in TABLE I, an increase in channel dimension leads to a significant rise in both the number of parameters and FLOPs. While the performance metric (mIoU) also improves accordingly, the increasing gains are relatively modest. Based on this observation, we focus our analysis on the performance of FSIHAN-T, FSIHAN-B, and FSIHAN-L variants. FSIHAN-T contains 0.12M parameters and requires 0.11G FLOPs, and it achieves a mIoU of 76.62%. With the smallest number of channels and parameters, FSIHAN-T offers high computational efficiency, making it suitable for resource-constrained devices. FSIHAN-B, with 0.46M parameters and 0.39G FLOPs, achieves an improved mIoU of 78.58%. Compared to the Tiny variant, the Base model significantly enhances performance by increasing channel width, and this demonstrates the effectiveness of channel expansion. FSIHAN-L reaches the highest performance with 1.77M parameters, 1.46G FLOPs, and a mIoU of 79.38%, indicating further gains from broader channel configurations.

In summary, FSIHAN-T represents a lightweight setup focused on efficiency, FSIHAN-B serves as the balanced baseline with a trade-off between accuracy and complexity, and FSIHAN-L corresponds to the full-scale configuration for offering optimal performance when computational resources are sufficient.

To accelerate experimental validation, we selected an encoder configuration with channel combinations {16, 32, 64, 128} as the baseline model, which was subsequently used for ablation studies. To validate the effectiveness of the network constructed with Frequency-Space Interaction Block (FSIB), Group Multi-Dilated Fusion (GMDF) and Hierarchical Feature Aggregation Module (HFAM), we progressively added the proposed modules to the baseline model, resulting in six variant models. The experimental setups and results are detailed in TABLE II.

> TABLE II. Segmentation performance of different components on the SSS test set. [NOTE: table contents not present in extracted text.]

According to the experimental results in TABLE II, the baseline model achieves a mIoU of 76.41% with only 0.378M parameters and 0.316 GFLOPs, effectively demonstrating the efficacy of FSIB in smoke feature extraction while maintaining a low-complexity encoder design. As GMDF and HFAM modules are progressively introduced, the model's segmentation performance significantly improves. These results indicate that each module contributes positively to performance enhancement, validating the effectiveness of our model design. On the other hand, from the baseline model to Variant 6, mIoU steadily increases from 76.41% to 78.58%. Although the number of modules leads to a slight increase in computational complexity and parameters, the performance improvement far outweighs the additional computational cost, making it negligible. Therefore, the model effectively balances computational complexity and segmentation performance.

To further investigate the specific contributions of the proposed modules, particularly in terms of the model's attention regions and feature extraction, we conducted a heatmap analysis of the results from each variant. The heatmaps in Fig. 7 illustrate the differences in the model's attention when processing the same input. For instance, in the second image of Fig. 7, the baseline model successfully extracts smoke features and localizes them well, due to FSIB. However, the heatmap indicates that the model overly focuses on the wheel region, resulting in mis-segmentation. After incorporating GMDF, this issue is mitigated by expanding the receptive field of features by the multi-dilated structure. Further improvements are observed with the addition of HFAM. The mis-segmentation in the wheel area is reduced, and the heat intensity significantly decreases. Ultimately, as we stack additional layers of HFAM, the mis-segmentation in the wheel region is satisfactorily resolved.

> Fig. 7. Heat map visualizations of some samples in the SSS test sets. (a) Images; outputs of (b) Variant 1, (c) Variant 2, (d) Variant 3, (e) Variant 4, (f) Variant 5, and (g) Variant 6.

To verify the effectiveness of the GMDF module, we conducted comparative experiments with ASPP in terms of parameters, computational complexity, and segmentation performance. The experimental results are shown in TABLE III.

> TABLE III. Ablation study of ASPP and GMDF. [NOTE: table contents not present in extracted text.]

The results demonstrate that GMDF outperforms ASPP in several aspects: the GMDF's parameters are reduced by 50%, effectively lowering memory consumption; computational complexity is decreased by 0.13 GFLOPs, significantly improving the model's computational efficiency; and mIoU is increased by 0.46%, indicating that GMDF has a clear advantage in fine-grained feature extraction and segmentation accuracy.

#### E. Comparisons With State-of-the-Art Methods

In the subsequent comparative experiments, we selected three representative models from the FSIHAN family (FSIHAN-T, FSIHAN-B, and FSIHAN-L) to evaluate their performance against current SOTA methods. The selection of models is mainly based on two considerations. The first one is to ensure the conciseness of tables and highlighting key comparative results. The second one is to evaluate models of different scales to comprehensively validate the adaptability and effectiveness of the proposed method under various computational resource constraints.

To fully evaluate the proposed method, we conducted systematic comparisons between our model and several mainstream lightweight approaches on two widely adopted benchmark datasets for smoke segmentation, including SYN70K and SMOKE5K. The compared methods include UNet [7], BiseNetV2 [38], MALUNet [39], LPS-Net [40], SwiftFormer [41], PIDNet [51], and ULite [52].

To ensure the fairness and comparability of results, we conducted reproducibility experiments on mainstream lightweight models under the same experimental environment. All models were trained from scratch on the SYN70K and SMOKE5K datasets, with strict consistency in parameter settings and training procedures. The input resolution is 256×256 for SYN70K and 480×480 for SMOKE5K to test FOLPs. TABLE IV presents the quantitative analysis of results by different lightweight models.

> TABLE IV. Segmentation results of different lightweight method. [NOTE: table contents not present in extracted text.]

Based on the experimental results presented in TABLE IV, the proposed method demonstrates optimal performance. We performed a detailed comparative analysis on the SYN70K dataset. As a classic encoder-decoder architecture, UNet performs well in segmentation tasks. However, UNet has high computational complexity with 13.68G FLOPs. In contrast, FSIHAN-T, an extremely lightweight model, has a computational complexity of only 0.11G, which is approximately 1/124 of UNet's FLOPs, and the mIoU of FSIHAN-T is 76.62% that is 0.03% higher than that of UNet. This substantial reduction in computational overhead makes FSIHAN-T an efficient solution for real-time or resource-constrained environments. The segmentation performance of FSIHAN-B is comparable to that of PIDNet, but the former has significantly reduced parameters and FLOPs compared to the latter. As for FSIHAN-L with only 1.77M parameters, it is much smaller than most other models (except for ULite). FSIHAN-L achieves a mIoU of 79.38%, making it suitable for high-precision application scenarios. Its performance on the SMOKE5K dataset is similar to that on SYN70K, validating the consistency of our proposed model across different datasets. These experimental results highlight the advantages of our method in optimizing segmentation performance and resource consumption, making it an ideal choice for real-time segmentation tasks in resource-constrained environments.

In addition, to further validate the quantitative analysis presented in TABLE IV, we conducted a qualitative evaluation of the performance of different segmentation methods on the SYN70K and SMOKE5K datasets. We selected representative samples for visual demonstration, as shown in Fig. 8 and Fig. 9.

> Fig. 8. Visualization comparisons with different lightweight methods on SYN70K dataset. The green and red curves represent the ground truth and prediction mask, respectively.

> Fig. 9. Visualization comparison with different lightweight methods on SMOKE5K dataset.

In the visual comparison, we chose FSIHAN-B for our analysis. To facilitate intuitive comparison, we used red curves to mark the regions of predicted segmentation and green ones to denote the ground truth. This approach allows for a clear evaluation of the model's segmentation performance. Compared to the other seven methods, our approach demonstrates the best segmentation results on synthetic smoke images, with the predicted contours closely matching the ground truth. For instance, in the second image of Fig. 8, the appearance of smoke and background objects are highly similar. Although other methods can identify and locate the smoke region, they exhibit significant over-segmentation. In contrast, our method delineates the shape of smoke and effectively avoids mis-segmentation, showcasing higher accuracy.

Fig. 9 demonstrates the segmentation results on the SMOKE5K dataset, where we conduct a qualitative analysis on the more challenging real images. Consistent with its performance on synthetic images, FSIHAN-B further exhibits significant advantages on real images. In addition to achieving better localization accuracy and boundary details, FSIHAN-B also delivers more impressive results in tasks involving distant and small smoke. As shown in the third and fourth images in Fig. 9, even in the presence of complex background interference, our model can accurately segment the smoke, including details that are difficult for the human eye to distinguish.

On the other hand, we conducted a comparative analysis of our model against the current SOTA smoke segmentation models on the SYN70K and SMOKE5K datasets. These models include DSS [12], W-Net [13], Frizzi [14], TANet [53], LSSNet [45], SmokeSeger [16], FoSp [15], SAGINN [17], MIFNet [27], and Trans-BVM [25], most of which have large parameter sizes and complex network architectures.

To ensure the optimal performance of compared methods, the segmentation results are from their original papers, as shown in TABLE V and TABLE VI. It is particularly important to note that the segmentation results in TABLE V represent the average mIoU score across the three test sets, DS01, DS02, and DS03, i.e., (mIoU_DS01 + mIoU_DS02 + mIoU_DS03)/3.

> TABLE V. Results on SYN70K with different smoke segmentation method. [NOTE: table contents not present in extracted text.]

TABLE V indicates that the FSIHAN variants demonstrate significant competitive advantages over current SOTA smoke segmentation methods in terms of both parameter efficiency and segmentation performance. Specifically, FSIHAN-T, the most lightweight variant in the FSIHAN family, achieves a segmentation accuracy of 76.6% with only 0.12M parameters. Compared to SmokeSeger, FSIHAN-T not only achieves higher segmentation accuracy but also utilizes over 280 times fewer parameters, demonstrating exceptional efficiency under extreme resource constraints. FSIHAN-B further improves performance, i.e., achieving 78.6% mIoU with just 0.46M parameters.

LSSNet, a lightweight smoke segmentation model, achieves a mIoU of only 73.2% while utilizing 0.88M parameters. These results indicate that FSIHAN-B outperforms LSSNet in segmentation accuracy and model compactness, underscoring the effectiveness of our architectural design. FSIHAN-L, the largest model in the FSIHAN series, obtains a 79.4% mIoU with only 1.77M parameters. FSIHAN-L performs competitively with SAGINN*, which achieves a 79.9% mIoU without classification assistance but relies on a heavy ResNeXt 101 [56] backbone. Compared to SAGINN (101.1M parameters), FSIHAN-L achieves comparable performance with approximately 57x fewer parameters. Moreover, compared to other recent high-performing models, such as FoSp and MIFNet, FSIHAN-L still exhibits clear advantages in parameters. FoSp achieves an 82.5% mIoU but requires 47.5M parameters, while MIFNet achieves an 81.6% mIoU with 24.6M. Although these models slightly outperform FSIHAN-L in accuracy, their parameters are 13x to 27x larger.

We conducted a comparative evaluation of existing state-of-the-art models for smoke segmentation, including methods such as Trans-BVM, FoSp, and SAGINN. Detailed quantitative results are shown in TABLE VI.

> TABLE VI. Segmentation results on the test set of SMOKE5K. [NOTE: table contents not present in extracted text.]

Compared to FoSp, FSIHAN-L reduces the number of parameters approximately 27x, while only showing a marginal difference of 0.001 in mMse and 0.002 in Fβ. Overall, our model significantly reduces the parameters, and maintains the accuracy nearly identical to FoSp. Our FSIHAN-L overtakes SAGINN in Fβ metric. These results demonstrate that FSIHAN-L achieves performance comparable to SOTA methods while maintaining high efficiency.

#### F. Experimental Results in Real-World Scenarios

To address the complex variations across different real-world scenarios, we collected three types of smoke videos: dense smoke, diffuse smoke, and translucent smoke. We provided the test results of several existing lightweight models, including UNet [7], BiseNetV2 [38], MALUNet [39], LPS-Net [40], and PIDNet [51], as well as the proposed FSIHAN-B.

As illustrated in Fig. 10, our proposed method achieves the best overall performance in smoke segmentation across three different types of test videos. In scenarios involving dense smoke, most models produce satisfactory segmentation results. However, when these models process diffused and semi-transparent smoke, the results are less than satisfactory. Although BiseNetV2, PIDNet, and our FSIHAN model demonstrate comparable performance, FSIHAN exhibits superior capability in capturing fine-grained edge details, significantly outperforming other methods. In addition, we find that pure white smoke (as illustrated in the second and third rows) poses a significant challenge to most models.

> Fig. 10. Visual segmentation results of different lightweight models on three types of real-world smoke videos.

To evaluate the real-time inference performance in realistic smoke video scenarios, we selected the first 100 frames from a video. We measured the total inference time and the number of frames per second (FPS). All input frames were resized to a resolution of 480×480.

> TABLE VII. Real-time performance evaluation on real smoke video. [NOTE: table contents not present in extracted text.]

Based on TABLE VII, the proposed FSIHAN variants demonstrate significant compactness advantages in terms of parameter count and model size. Specifically, the lightweight FSIHAN-T contains only 0.12M parameters and requires only 0.60 MB of storage, which is substantially smaller than all baseline models, highlighting its large advantage in model size and resource consumption. Combined with the quantitative analysis results on the SYN70K and SMOKE5K datasets in TABLE IV, the FSIHAN models achieve a good trade-off between segmentation accuracy and resource usage.

In particular, FSIHAN-T, the smallest model, achieves 54.1 FPS, so it sufficiently meets the demands of most real-time applications, although it is still slower than LPS-Net (97.1 FPS) and BiseNetV2 (82.1 FPS). As the model size increases, FSIHAN-B and FSIHAN-L show further improvements in segmentation accuracy, but the inference latency also increases, reaching 24.4 ms (41.0 FPS) and 33.8 ms (29.6 FPS), respectively.
