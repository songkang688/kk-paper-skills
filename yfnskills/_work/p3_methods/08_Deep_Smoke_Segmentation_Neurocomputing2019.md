## III. DATASET GENERATION FOR SMOKE BINARY SEGMENTATION

One of the great obstacles to smoke segmentation based on deep learning is the lack of adequate annotated training data. Although we can easily acquire a huge number of smoke images, it is extremely time-consuming, boring and difficult to manually segment smoke objects from an image since smoke has fuzzy edges and translucent property.

As far as we know, there is no image dataset for smoke segmentation. It is of great significance to create image datasets for smoke segmentation in both research and industry communities of visual smoke detection. We first used computer graphics to virtually generate 8162 pure smoke images, denoted as a PureSmoke dataset. Then, we adopted a linear color composition method to synthesize a random background image and a pure smoke image to construct a training dataset and three test datasets. Each test dataset has 1000 synthesized smoke images for comparisons.

Some pure smoke samples are shown in Fig. 1. Each image is an RGBA image containing 4 channels, i.e., three RGB color channels (S) and one alpha channel (α). We use the linear color composition of a pure smoke image (S and α) and a background RGB image B to generate a new smoke RGB image I, which is expressed as follows:

I = (1 − α)B + αS    (1)

where the alpha α is actually a blending parameter in the range [0, 1] representing the transparency of smoke.

To make the training samples diverse, we use the Places365Standard dataset [41] as background images. In the synthesis process, we randomly select a background image from the Places365-Standard dataset and a pure smoke image from the PureSmoke dataset, then combine the two images to generate a synthesized smoke image. To further perform data augment of smoke images, we change the alpha values of pure smoke images to control the concentrations of smoke images, which is expressed as:

I_R = (1 − βα)B_R + βαS_R    (2)

I_G = (1 − βα)B_G + βαS_G    (3)

I_B = (1 − βα)B_B + βαS_B    (4)

where β is a linear coefficient with range (0,1) used to control the concentration of smoke, IR, IG and IB are the red, green and blue channels of a pixel in an observed smoke RGB image I, respectively, SR, SG and SB are respectively the red, green and blue channels of the pixel in a pure smoke RGBA image (S and α), and BR, BG and BB are respectively the red, green and blue channels of the same pixel in a background RGB image B.

In this way, we can easily generate a large number of training samples. Fig. 2 shows some training images for smoke segmentation. Our synthesizing method avoids the difficulty in manually annotating ground truths of smoke images. We threshold the alpha channel of a pure smoke image to generate a binary mask for smoke regions, and then the binary mask is regarded as the ground truth of a synthesized image blended by the pure smoke image and any other background image.

## IV. TWO-PATH FULLY CONVOLUTIONAL NETWORKS

Ideally, we require our deep smoke segmentation network to have the following advantages: accurate segmentation, small network size, and a fast test speed. The overall structure of the proposed method is shown in Fig. 3. This network is called a two-path FCN since it consists of two paths. The first path is a deep fully convolutional network with asymmetrical structures, which is used for global segmentation prediction. The second one is a refinement path that produces a more detailed prediction on the basis of global prediction. Then we will describe the two paths in more detail in following sections.

### A. A deep network for global context information

The first path aims at gaining global context information for generation of a coarse smoke segmentation map. The network of this path takes a single RGB image as input and produces an prediction map with the same size of the input. The detailed structure of the network is shown in the bottom row of Fig. 3. Apparently, the network is a typical encoder-decoder FCN. To speed up training, there are many segmentation algorithms [14][31][37][38][39] that adopt the convolutional blocks of the VGG16 network [26] to achieve remarkable results. We also utilize the first five blocks of the VGG 16 network as the basis of the encoding phase of path 1, which contains 13 convolutional layers and 4 max-pooling layers, and we remove the fully connected layers to reduce the number of trainable parameters.

To further reduce the number of network parameters and improve the training speed, we use an asymmetric structure in the decoding phase. Besides two concatenation layers, the decoder network only includes 9 convolutional layers and 4 upsampling layers. Finally, a convolutional layer with a 1×1 kernel and a sigmoid activation function, which is called prediction phase, is added at the end of the decoder network to predict a coarse segmentation map for input. The detailed hyper-parameters of the network are shown in Table 1.

The first path network leverages a binary cross-entropy loss with weight decaying regularization as a loss function, which can be expressed as:

L(P, G) = −Σ_i [g_i log p_i + (1 − g_i) log(1 − p_i)] + λ∥W∥^2    (5)

where pi is the probability of a pixel i classified as smoke in the predicted map P, pi ∈ [0,1], gi is the probability of the pixel i in the corresponding ground truth map G, and gi is equal to 1 for a smoke pixel and 0 for non-smoke.

In order to obtain multi-scale features and retain detailed spatial information, we increase the network depth and add skip structures between encoding and decoding phases of the network. Zhang et al. [31] and Hou et al. [19] verified that deeper layers can capture more global information. Learned from the above idea, we propose to incorporate the last three blocks of the encoding phase into the decoding phase to increase the network depth for capturing more global information. The output feature maps of convolutional layers in the encoding phase are extracted, and then these feature maps are upsampled to the size of the feature maps of corresponding decoder layers to perform feature concatenation operations.

### B. A shallow network for local fine information

As mentioned earlier, smoke is hard to segment because it has very blurry edges and translucent property. In the first path of our network, we obtain global information to generate a coarse segmentation of smoke, but we lost detailed spatial information for smoke localization. Therefore, the goal of the second path is to capture details of smoke.

In addition to proving that deeper layers can capture more global information, Zhang et al. [31] and Hou et al. [19] also verified that shallower layers can capture rich local information and object details. According to this idea, we propose to use a shallow encoder-decoder network using the first three blocks of VGG16 with two max-pooling layers to retain more details of the input. The detailed structure of the shallow network is shown in Fig. 3. The network is just an encoder-decoder structure that includes 7 convolutional layers and 2 maxpooling layers in the encoding phase, and 4 convolutional layers and 2 upsampling layers in the decoding phase. The hyperparameters of the second path network are given in Table 2.

Similar to the network of the first path, the second network also adopts skip structures for capturing scale information. We extract the outputs of two convolutional layers in the encoding phase, and then upsample the extracted feature maps to the size of the feature maps in corresponding decoder layers to complete concatenation operations. Finally, we obtain the detailed segmentation map of smoke through two ReLu convolutional layers and one sigmoid convolutional layer.

### C. A fusion network of two paths

The overall goal of this work is to gain an accurate smoke segmentation map. Therefore, we merge the coarse prediction result at path 1 and the detailed spatial information at path 2 to generate the final accurate result. We first add up the network outputs of the two paths, and then feed the summed segmentation map into a convolutional layer with a 1*1 kernel and a sigmoid activation function to produce the final prediction map, as shown in Table 3.

Although we have borrowed some inspirations from the method proposed by zhang et al. [31], our method is obviously different from the method. First, we only use the feature information of the last three blocks in VGG16, and zhang et al. [30] used all the first five blocks of VGG16. Second, we use upsampling and concatenation operations to replace deconvolution and summation layers [30]. Thirdly, our method includes decoding phases with multiple unsampling and convolutional layers. Fourth, we propose a shallow encoderdecoder network with skip layers to produce finer segmentation results.

Our method can be efficiently trained end-to-end because we use the fusion network and skip structures. However, the method in [27] adopts a complicated updating strategy for training. It first updates the parameters of the first path network by removing the second path network. Once the first path is converged, it fixes the first path parameters and then updates the second path network without the first network. After the second path is converged, it fine-tunes the whole network again using the same training method. Apparently, our method is more efficient and appropriate for simultaneous optimization of all network parameters.
