## Discussion

### 6. Discussion

The algorithm can detect the presence of smoke in a video with the size of 320×240 at about 10 frames per second (fps). It cannot obtain real time processing frame rates (above 25 fps). The algorithm needs a training image set. In fact, the positive and negative images used in the algorithm are impossible to cover all kinds of smoke and non-smoke objects. Therefore, detection and false alarm rates of the system highly depend on the training image set. The algorithm performs well on several videos we captured. If a video contains too many objects which are not included in the training set, the system performance will drop obviously. So we do not know the performance on unknown videos. That is the lower limit of smoke detection of the video system. Solution to the above mentioned problems is to create a representative image database and improve the algorithm itself.
