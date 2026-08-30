## Conclusion

### V. Conclusion

To improve the performance of real-time smoke segmentation, we propose a Multi-stage Group Interaction and Cross-domain Fusion Network (MGICFN). We propose several novel modules to build our network, including the Cross-domain Interaction Attention Module (CIAM), Group Convolutional Block Attention Module (GCBAM), Multi-Stage Group Interaction Module (MGIM), Group Fusion Module (GFM), and Edge Enhancement Module (EEM). These modules together enhance feature representation, inter-scale interaction, and boundary refinement. Our MGICFN achieves significant improvements in computational cost and segmentation accuracy. Experimental results demonstrate that our MGICFN achieves state-of-the-art performance on the synthetic SYN70K and real-world SFS3K datasets and maintains a lightweight architecture simultaneously.

Notably, its inference speed is constrained by its high-initial-resolution design and the computational overhead of frequency-domain processing. In future work, we will focus on optimizing these components to improve computational efficiency, and also plan to expand the SFS3K dataset with more real-world scenarios and extend our MGICFN to related tasks such as joint fire and smoke detection.
