Table 8 shows that the average ranking of our method is superior to other methods. DMD and PRICoLBP compute features in local multi-scale coordinates. Our features are computed from fixed local coordinates, and the multi-scale information of our method comes from 3D difference computation. Consequently, we should improve our descriptor by learning a local difference selection strategy, thus we obtain more transform invariance.
Fig. 1. Examples of 3D sampling windows in image pyramid and scale space with r = 1 and K = 3.
Fig. 2. Calculation of 3D local differences.
Fig. 3. The calculation of the c th within-scatter matrix S_w^c.
Fig. 4. The calculation of between-scatter matrix S_b.
Fig. 5. The generation of 8 feature maps in the ith image.
Fig. 6. Feature extraction procedure of a layer. (a) Calculation of 3D differences. (b) Learning and projection. (c) Within-map and between-map encodings.
Fig. 7. Between-map encoding.
Fig. 8. Feature extraction of our method for texture classification. (A) Scale space construction and local difference calculation. (B) Projection matrix learning. (C) Projection, between-map and within-map encodings and weighted concatenation.
Fig. 9. The original framework of our method for learning, feature extraction and classification.
Fig. 10. An extension of our feature extraction method.
Fig. 11. Visualization of our learning-based projection and encoding results. (a) An input image. (b) and (c) Gaussian filtered images with different variances. (d) The cross-sign map LBP_0 from (f) in the between-map encoding way. (e) The cross-magnitude map LBP_mag obtained from (f) by between-map encoding. (f) The eight feature maps generated from (a), (b) and (c). (g) The original LBP maps, LBP_1, ..., LBP_8, computed from (f) by within-map encoding.
Fig. 12. Cross-sign and cross-magnitude maps obtained from sixteen feature maps. (a) The cross-sign map and (b) the cross-magnitude map generated from the top 8 feature maps. (c) The cross-sign map and (d) the cross-magnitude map computed by the 9th to 16th feature maps.
Fig. 13. The ROC curves of compared methods on Set2.
Fig. 14. The ROC curves of compared methods on Set3.
Fig. 15. The ROC curves of compared methods on Set4.
Table 1. Datesets for smoke recognition.
Table 2. Compared methods for smoke recognition.
Table 3. Experimental results for smoke recognition.
Table 4. Comparision results (%) of two learning-based methods.
Table 5. Compared methods on texture classification.
Table 6. Comparision results (%) using PRICoLBP's protocol.
Table 7. Comparision results (%) using DMD's protocol.
Table 8. Performance rankings for Table 7.