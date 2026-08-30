

=========== 21 DISCUSSION
## Discussion

### 6. Discussion

The algorithm can detect the presence of smoke in a video with the size of 320×240 at about 10 frames per second (fps). It cannot obtain real time processing frame rates (above 25 fps). The algorithm needs a training image set. In fact, the positive and negative images used in the algorithm are impossible to cover all kinds of smoke and non-smoke objects. Therefore, detection and false alarm rates of the system highly depend on the training image set. The algorithm performs well on several videos we captured. If a video contains too many objects which are not included in the training set, the system performance will drop obviously. So we do not know the performance on unknown videos. That is the lower limit of smoke detection of the video system. Solution to the above mentioned problems is to create a representative image database and improve the algorithm itself.

=========== 11 DISCUSSION
## Discussion

Extensive experiments on both natural and synthetic images validate that our method achieves significantly better performance than state-of-the-art methods. In summary, our method significantly outperforms most of existing methods, including deep learning methods. However, our method needs to compute features of local patches, so it has high computational complexity. We can design efficient feature extraction algorithms or adopt GPUs to speed up our method in the future.

Although our confidence prior achieves excellent results for haze removal, there are still some common problems to be solved. Firstly, the hyperparameter p in our method highly depends on experiences and is set to be constant in our implementation. A constant hyperparameter p is not suitable in inhomogeneous atmospheric conditions, since different image patches possess different feature distributions. Therefore, dehazing algorithms are prone to obtaining incorrect transmissions in some cases. Although the parameter selected by experiences can obtain outstanding dehazing effects, a more flexible method to estimate the hyperparameter p is highly desired. Secondly, the dehazed results by the proposed method still have much remaining haze and noise for dense haze images. Thirdly, although our method outperformed most existing methods, it did not obtain the best performance on night [sentence truncated in extraction; table-header debris removed].

=========== 08 Limitations subsection (inside Results)
of our method

Although our method has achieved good results, there is a long way to reach perfect effects. The main reasons are as follows. First, smoke has very large variations of features: texture, shape, color, etc., and these features appear in many forms and are also varying even if they are produced from the same fire source. Second, the edge of smoke is very blurry compared to other objects, and smoke precise edges are hard to get. Third, many objects, such as fog and clouds, share the same visual appearance as smoke. It is very difficult to discriminate them. As shown in Fig. 8, there are several examples of false positives produced by the comparing methods and the proposed method. Except for FCN, our method only misclassified a small number of fog and cloud pixels as smoke compared to other methods. This also proves that our proposed method not only has certain advantages in accuracy, but also has a strong competitive effect on false positives. Moreover, real-time performance is a very important requirement for application of smoke segmentation. Therefore, another limitation of our method is that the test speed needs to be further improved.
