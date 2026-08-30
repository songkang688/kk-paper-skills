## Conclusion

### V. Conclusion

Semantic segmentation has increasingly become the preferred technique for smoke detection. However, existing smoke segmentation models often suffer from high complexity and limited representational capacity. Therefore, developing an efficient and lightweight smoke segmentation framework is crucial for computation-limited devices. In response to this challenge, we propose a lightweight smoke segmentation method called FSIHAN. This approach introduces the Frequency-Space Interaction Module (FSIM) to facilitate efficient cross-domain feature fusion. The FSIM is integrated into the FSIB block along with a Multi-Layer Perceptron (MLP) to enhance the extraction of smoke-related features.

Additionally, during the transition from encoding to decoding, we introduce the Group Multi-Dilated Fusion (GMDF) module, which improves the efficiency of feature information propagation and fusion. In the decoding stage, we employ the Hierarchical Feature Aggregation Module (HFAM) module to enable fine-grained decoding across successive layers. Experimental results demonstrate that FSIHAN outperforms current state-of-the-art semantic segmentation algorithms on the SYN70K, SMOKE5K, and various real-world smoke image tests.

The FSIHAN models achieve a good balance between model size and segmentation performance, and particularly excel in edge detail preservation and complex smoke scenarios. However, our method remains a limitation of processing speed. In future work, we explore methods to further reduce computational latency, which is an ongoing challenge that needs to be addressed.
