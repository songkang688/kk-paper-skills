table content), and Fig. 3 pipeline labels (S037, figure content). Figure/table captions segregated into
Fig. 3 shows processing flow of HOG, where we need to estimate the gradient of an image, and compute the magnitude and orientation of the gradient. We can use Sobel operators or central differences of an image f(x,y) to compute the gradient (fx, fy) of the image. Then we use Eq. (7) and (8) to calculate the magnitude and orientation of the gradient.
Fig. 4(d) and Fig. 4(h) respectively show gradient magnitudes of "lena" and "smoke" based on Hamming distances of LBP codes, which are estimated by Eq.(10).
Table 2. Preserved verbatim. -->
Table 4 method-description rows. -->
Fig. 1. Neighborhood types. (a) Rectangular neighborhood; (b) Circular neighborhood
Fig. 2. Distance measures. (a) the local direction order; (b) the differences between the central LBP code and the LBP codes in its rectangular neighborhood.
Fig. 3. Processing flow of HOG.
Fig. 4. Comparisons for LBP codes and gradients based on Hamming distance. (a) The image named "lena"; (b) The gradient magnitude of "lena"; (c) The LBP code map of "lena"; (d) The gradient magnitude of "lena" based on Hamming distances of LBP codes; (e) The image named "smoke"; (f) The gradient magnitude of "smoke"; (g) The LBP code map of "smoke"; (g) The gradient magnitude of "smoke" based on Hamming distances of LBP codes. [Note: the second "(g)" is in the original caption; it should read "(h)".]
Fig. 5. Gradient computation over LBP maps. (a) coordinate system for computing gradient in traditional HOG; (b) coordinate system for computing gradient in traditional HOG after the LBP map is rotated 45°; (c) two coordinate systems in our approach; (d) two coordinate systems in our approach after LBP map is rotated 45°.
Fig. 6. Framework of feature extraction.
Fig. 7. Smoke samples and non-smoke samples. (a) Smoke samples. (b) Non-smoke samples.
Fig. 8. Visualization of experimental performance.
Fig. 9. Falsely classified samples of smoke (a) and non-smoke (b).
Fig. 10. Some samples of Brodatz album.
Table 1. The image datasets for training and classifying
Table 2. Summary of some texture detection methods
Table 3. Experimental results
Table 4. Summary of some texture detection methods
Table 5. comparison with other LBP variants on Brodatz