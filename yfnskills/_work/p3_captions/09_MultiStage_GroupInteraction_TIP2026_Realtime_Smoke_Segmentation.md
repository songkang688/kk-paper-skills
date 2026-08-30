Fig. 1. Samples of two smoke datasets from (a) SYN70K and (b) SFS3K.
Fig. 2 illustrates the architecture of the Multi-stage Group Interaction and Cross-domain Fusion Network (MGICFN). The proposed MGICFN consists of five core modules: CIAM, GCBAM, MGIM, GFM, and EEM. These modules work collaboratively to form a lightweight network with low computational complexity, specifically designed for smoke segmentation. MGICFN effectively addresses challenges such as the loss of light smoke and blurred segmentation boundaries, enhancing overall segmentation performance.
Fig. 2. Overall framework of our MGIFN. [NOTE: "MGIFN" appears as printed in the source caption; presumably MGICFN.]
Fig. 3. Details of cross-domain interaction attention module.
Fig. 4. Group convolutional block attention module.
Fig. 5. Multi-stage group interaction module.
Fig. 6. Group fusion module.
Fig. 7. Edge enhancement module.
Fig. 8. Some examples from our SFS3K. (a) Images, (b) Labels.
TABLE I. Details of different variants. [NOTE: table contents not present in extracted text.]
TABLE II. Segmentation results of various variants on different datasets. [NOTE: table contents not present in extracted text.]
Fig. 9 shows visualized segmentation comparisons of different variants on the SFS3K dataset (images 1, 2, and 3) and the SYN70K dataset (images 4, 5, and 6). The baseline model exhibits several limitations: (1) insufficient refinement of edge details, particularly evident in images 1 and 3; (2) poor discrimination between foreground smoke and background regions, observed in images 2, 4, and 6; and (3) significant segmentation errors, as seen in image 5. To address these issues, we progressively optimize the encoder, decoder, and skip connections, resulting in four variant models (Model 1 to Model 4). Notably, our model (Model 4) achieves the best overall performance.
Fig. 9. Visualization of different variants on the SFS3K and SYN70K test sets. (a) Smoke images, (b) Labels, (c) Baseline, (d) Model 1, (e) Model 2, (f) Model 3, and (g) Model 4 (Ours).
TABLE III. Ablation study of CBAM and GCBAM. [NOTE: table contents not present in extracted text.]
TABLE IV. Ablation study of different loss function. [NOTE: table contents not present in extracted text.]
TABLE V. Segmentation results of different lightweight method. [NOTE: table contents not present in extracted text.]
Fig. 10. Visualization of different lightweight methods on the SYN70K test sets. (a) Smoke images, (b) Ground truth, (c) UNet, (d) BiSeNet V2, (e) MALUNet, (f) EIUNet, (g) SwiftFormer, (h) PIDNet, (i) ULite, and (j) MGICFN (Our method).
Fig. 11. Visualization of different lightweight methods on the SFS3K test sets. (a) Smoke images, (b) Ground truth, (c) UNet, (d) BiSeNet V2, (e) MALUNet, (f) EIUNet, (g) SwiftFormer, (h) PIDNet, (i) ULite, and (j) MGICFN (Our method).
TABLE VI. Comparative results on SYN70K with different smoke segmentation methods. [NOTE: caption reconstructed; source text was garbled as "COMPARATIVE RESULTS ON SYN70K WITH DIFFERENT SSmoke SEGMEN...TATION METHOD". Table contents not present in extracted text.]
TABLE VI shows the performance comparison results of different methods. SAGINN achieves an mIoU of 83%, but it has significantly larger model size with 101.1M. In contrast, our MGICFN obtains an mIoU of 78.7% while maintaining an extremely lightweight architecture with only 0.73 million parameters that are 138× fewer parameters than SAGINN. Notably, when the classification auxiliary branch is removed from SAGINN, its mIoU drops to 79.9%, which is only marginally higher than our model's performance, highlighting MGICFN's strong efficiency-accuracy trade-off. LSSNet is another lightweight method for smoke segmentation. Our MGICFN shows more obvious advantages. MGICFN not only reduces parameters by 0.15M, but also increases mIoU by 5.5%.
TABLE VII. Real-time performance evaluation results. [NOTE: table contents not present in extracted text.]
Fig. 12. Segmentation of different lightweight models on a real-world smoke video. (a) UNet, (b) MALUNet, (c) PIDNet, (d) LSSNet, and (e) our MGICFN.