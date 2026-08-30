## V. EXPERIMENTAL RESULTS

In this section, we will describe our experimental datasets (Sec. A) and implementation details (Sec. B), evaluate our model on three synthetic test smoke datasets and one real smoke dataset in quantitative and qualitative manners (Sec. C), explain the importance of each part of the model by ablation experiments (Sec. D), and finally show the limitations of the proposed model (Sec. E).

### A. Image datasets

We created three synthetic smoke image datasets and one real smoke image dataset for comparisons. These datasets are very challenging due to large variations in texture, shape, color and scales. All test images were not used in the training process, and even the smoke backgrounds are totally different from the training samples.

Each synthetic dataset contains 1000 composited smoke images of size 256*256, which were generated in the same way as the training data described in Section III. But the background images for generation of the three synthetic test datasets were selected from CBCL StreetScenes [43], Pascal Visual Object Classes [44] and Baidu people segmentation dataset [45], respectively. For the sake of clearness, the three synthetic test datasets with different background images are named DS01, DS02 and DS03, respectively. Fig. 4 shows some synthetic smoke images and corresponding ground truths of alpha channels from the three synthetic data sets. To create the real smoke dataset, we manually collected several smoke images from the internet. Due to lack of ground truths for real images, the real image dataset was used only for qualitative analysis.

### B. Implementation details

We implemented our proposed network using Tensorflow and Keras. The proposed model was trained end-to-end using a single NVIDIA GeForce GTX1080Ti with 11 GB RAM. A well-known problem with network training is the initialization of network parameters. If the initialization parameters of network are not suitable, it is easy to get the network into local optimal solutions. Related work has shown that this problem can be overcome by using pre-trained parameters of some famous networks to initialize the network. Therefore, for the encoder, 13 convolutional layers were initialized with the weights of the VGG16 network pre-trained on ImageNet. The parameters of the decoder were randomly initialized by truncated normal distributions. Since the network does not use smoke images for further training, it is unable to perform smoke segmentation. Therefore, we trained our network on the smoke training datasets with stochastic gradient descent (SGD) [42] with a fixed learning rate of 0.001, a momentum of 0.9 and a weight decay of 1e-5.

After our proposed network is trained, we can perform smoke segmentation on test datasets. We deal with synthetic and real datasets in different ways. Synthetic smoke images have binary ground truths that can be directly computed from alpha channels of pure smoke images. For the sake of convenient comparisons, we perform a binary process on the results for synthetic smoke images, since all comparing methods perform binary segmentation. The binary process regards a prediction value greater than 0.5 as smoke with label "1", and a value less than 0.5 as background with label "0". For real smoke images, we directly retain predicted results without any process for visual accessments because there is no ground truth.

We calculated two widely used measures: mean Intersection over Union (mIoU) and Mean Square Error (Mse). The larger the value of mIoU is, the better the segmentation is, while the smaller the value of Mse is, the better the result is.

The value of mIoU can well reflect the accuracy of segmentation results. The mean of Intersection over Union (mIoU) is defined as

mIoU = (1/n) Σ_i (PR_i ∩ GT_i) / (PR_i ∪ GT_i)    (6)

where PRi is the predicted segmentation result of the ith image, and GTi is corresponding ground truth, and n is the number of images in a dataset.

Msei is defined as the average per-pixel square difference between the prediction result PR and its ground truth GT for the ith test image:

Mse_i = (1/(h_i w_i)) Σ_k (PR_i(x_k) − GT_i(x_k))^2    (7)

where hi and wi are the height and width of the ith test image, and xk is the coordinates of the kth pixel in the ith test image. In our experiments, we compute the average Mse on a test dataset for performance evaluation:

mMse = (1/n) Σ_i Mse_i    (8)

### C. Performance comparisons

Since there is no algorithm for smoke segmentation using deep learning, in order to illustrate performance of the proposed method, we compared the experimental results with multiple classical segmentation algorithms based on deep learning, including FCN [14], SegNet [29], Text-Block FCN [31] denoted as TBFCN, and static map detection method [16] denoted as SMD. We used the network code of the authors and trained these comparing methods on the same smoke training data. In comparisons, there are several points that need to be explained. First, we only compared the first path segmentation results of TBFCN because the method was designed for text segmentation and the work of the second path was proposed to locate the text center point, and it is not needed for smoke segmentation. Second, the method in [16] was proposed for video object segmentation and used dynamic information. For fair comparisons, we only used the static segmentation results of this method for comparisons.

(1) Qualitative comparisons

Qualitative comparisons of our method with other deep learning methods on the smoke test datasets are shown in Fig. 5. The first column shows test images, the second column shows corresponding ground truths, and other columns show the segmentation results of different methods. Fig. 6 shows experimental results of real smoke images collected from the internet. Except that the real smoke images do not have corresponding ground truths, the other columns in Fig. 6 are the same as those in Fig. 5. As we can see, our method exhibits excellent segmentation performance on both synthetic smoke images and real smoke images. Indeed, our method separates smoke with sharper edges and more accurate locations compared to other methods.

(2) Quantitative analysis

We performed quantitative evaluation experiments on the three synthetic smoke test datasets (DS01, DS02 and DS03). The quantitative results on the three test datasets are given in Table 4 to Table 6. As we can see, our method significantly outperforms other methods on all synthetic datasets. Our method achieves the highest mIoU among all the comparing methods, indicating that our prediction segmentation is the closest to its ground truth. At the same time, our method achieves the lowest mMse among them.

Moreover, we have found that the performance of SegNet is the lowest among them. We think that there are two main reasons. The first reason is that SegNet does not adopt the same skip layers as other methods. The second one is that SegNet does not use the pre-trained weights of VGG16 to initialize the network. Network initialization using pre-trained parameters on large image datasets is very favorable in the case of relatively few training samples. Therefore, we can draw some conclusions that skip architectures and pre-trained weights can greatly improve the prediction performance of the proposed model.

### D. Ablation analysis

In order to analyze the importance and necessity of each part of the proposed network, we conducted a series of ablation experiments. We compared the proposed network with three variants of the proposed network by removing the skip structures of path 2 (-Rs), the entire network of path 2 (-R), and the entire network of path 2 and the skip structures of path 1 (-R-Cs). Ablation experiments will show that skip structures and the second shallow encoder-decoder network play a very important role in smoke segmentation.

We also performed ablation experiments on the three synthetic datasets. Quantitative results are listed in Table 6 to Table 8. According to the quantitative results on DS01, we can find that mIoU increases from 64.64% to 71.04% by adding the network of path 2, so it shows that the second network is very important for improvement of accuracy. In addition, the mIoU of the proposed method with skip architectures in both paths is about 4 to 5 percentage higher than those without skip layers. That proves the effectiveness of skip layers. This phenomenon also happens on DS02 and DS03. Therefore, we can see that skip structures and the second refinement network play a very important role in our network.

Meanwhile, the networks with skip layers in the two paths, i.e. Variant 2 (-R) and our complete method, are better than the methods without skip layers that are Variant 1 (-R-Cs) and Variant 3 (-Rs).

We visually evaluated the results of the three variants and the proposed complete method on real images. Qualitative experimental results are shown in Fig. 7. From Fig. 7, we can clearly observe that the final results of the proposed method are significantly better than the coarse results of Variant 2 (-R).

Since the method of [31] used deconvolution and add operations to fuse features from different layers, we want to verify that upsampling and concatenation operations used in our proposed method is more appropriate and effective than deconvolution and add operations used in [31]. Therefore, we replace unsampling and concatenation operations by deconvolution and add layers to produce a new variant of the proposed method, denoted as Variant 4 (deconvolution+add). We compared the proposed method with Variant 4 on the three synthetic smoke datasets under the same condition. The experimental results are shown in Table 10. We can find that unsampling and concatenation operations unanimously achieve better performance than deconvolution and add ones on DS01, DS02, and DS03.

### E. Test on videos

We tested our method on the same four videos as [46]. The four videos are two smoke videos and two non-smoke videos, respectively. The first video is a black smoke video produced by burning diesel oil. Our method achieved accurate segmentation for each frame, as shown in Fig. 9. The second video is a white smoke video by cotton ropes, as shown in Fig. 10. The white smoke video has poor image quality, leading to inaccurate segmentation results. The third is a non-smoke video containing waving leaves, and the fourth is a basketball court video with some students playing basketball. Fig. 11 shows two frames from the two non-smoke videos. We are pleased that our method did not misclassify any pixel as smoke on the two nonsmoke videos, so we do not illustrate segmentation masks.

Based on the segmentation results of our method, we can easily make the whole image smoke recognition. For the sake of simplicity, we simply count the number of pixels classified as smoke in an image, and classify the image as a smoke one if the number of pixels classified as moke is greater than a threshold.

We used the above segmentation based smoke recognition method to detect smoke on the four videos, and compared our method with LBP_LBPV [46] and Toreyin's method [47]. Table 11 lists the results of the three methods. Our method detected smoke at the first frame of the two smoke videos. Apparently, our method can detect smoke much earlier than other two methods. In addition, our method did not raise any false alarms on the two non-smoke videos, and we do not use any post-processing techniques to further reduce false alarms.

### F. Limitations of our method

Although our method has achieved good results, there is a long way to reach perfect effects. The main reasons are as follows. First, smoke has very large variations of features: texture, shape, color, etc., and these features appear in many forms and are also varying even if they are produced from the same fire source. Second, the edge of smoke is very blurry compared to other objects, and smoke precise edges are hard to get. Third, many objects, such as fog and clouds, share the same visual appearance as smoke. It is very difficult to discriminate them. As shown in Fig. 8, there are several examples of false positives produced by the comparing methods and the proposed method. Except for FCN, our method only misclassified a small number of fog and cloud pixels as smoke compared to other methods. This also proves that our proposed method not only has certain advantages in accuracy, but also has a strong competitive effect on false positives. Moreover, real-time performance is a very important requirement for application of smoke segmentation. Therefore, another limitation of our method is that the test speed needs to be further improved.
