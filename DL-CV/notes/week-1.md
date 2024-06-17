## Week-1

<b>Computer Vision:</b> A field that seeks to automate and endow a computing framework with the ability to interpret images the way humans do. Sub-topic of AI.<br><br>
<b>Applications:</b> Autonomous vehicles, Surveillance, Factory Automation, Medical Imaging, Human-Computer Interaction, Visual Effects, Retail security, Structural Health monitoring, Document Understanding, Healthcare, Agriculture, Banking and Finance, Remote Sensing, Tele and Social Media, Augmented Reality etc.<br><br>
<b>Why is it harder?</b>
1) Optical Illusions:
<br>
Muller-Lyer Illusion - Which line is longer?
<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/72e12d6a-c951-46a8-b776-c730baaa362b)

<br>
<br>
Actually, both are of the same length.
<br>
Variation of Hermann grid Illusion: What do yu see at the intersections? <br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/09b77380-4929-4a0c-9a3d-318c2d996df8) <br>

<br>
Adelson's brightness constancy illusion: Which is brighter, A/B?
<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/00f48ce5-d89b-4492-90dd-267e1102d5dc)

<br><br>
Count the red Xs in both figures, which is harder?<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/0477710f-5610-4887-a294-782a27d86568)<br><br>

2) Many practical use cases are inverse model applications. 
<br> No knowledge of how an image was taken or camera parameters - but need to model the real world in which the picutre/video was taken => Need to almost always model from incomplete/partial noisy information.<br><br>
3) High-dimensional data = > Heavy computational requirements.<br><br>
4) Computer Vision is <b>AI-complete</b>: The computer cannot solve the problem on its own, it needs to be a human to do that.<br><br>
5) No complete models of the human visual system exist - Existing models largely related to subsytems, holistic. What is perceived and what is cognized?<br><br>
6) Verifiability of mathematical/physical models non-trivial: How should similarity/dissimilarity b/w representations be defined? How would a manipulation in a given environment behave, w.r.t the captured image/video? Can a physical model capture this?<br><br>

<b>Computer Vision: Topics</b>
<ol>
  <li>Learning-based Vision: Visual Recognition, Detection, Segmentation, Tracking, Retrieval etc.</li>
  <li>Geometry-based Vision: Feature-based Alignment, Image Stitching, Epipolar Geomtry, Structure from Motion, 3D Reconstruction etc.</li>
  <li>Physics-based Vision: Computational Photography, Photometry, Light-fields, Color spaces, Shape-from-X, Reflection, Refraction, Polarization, Diffraction, Interference etc.</li>
</ol>
<br><b>The first topic is the focus of the course.</b>
<br><br>

### History:
1959 - David Hubel and Torsten Wiesel's work on 'Receptive Fields of single neurons in the cat's striate cortex'. Showed simple and complex neurons exist and visual processing starts with simple structures such as oriented edges.<br><br>
1959 - World's first image - Russel Kirsch and his colleagues develop an apparatus to transform images to number grids. A grainy 5cm by 5cm photo og Russell's infant son.<br><br>
1963 - Lawrence Roberts' PhD thesis: Machine Perception of 3D Solids. 3D Information extraction from solid objects from 2D photographs of line drawings.<br><br>
1966 - Seymour Papert from MIT launched Summer Vision Project. A platform development to automatically segment background/foreground and extract non-overlapping objects from real-world images.<br><br>
1971 - Discern a shape in a line drawing by labeling lines as convex, concave and occluded.<br><br>
1973 - Pictorial structures model by Fischler and Elschlager. Given a visual object's description, find the object in a photograph.<br><br>
1971-'79 - Object recognition through shape understanding. MIT's SAIL offers a "Machine Vision" course.
1979-'82 - David Marr establed that vision is hierarchical. <i>A computational investigation into the human representation and processing of visual information.</i>. Marr's Representation Framework - A primal sketch of an image, 2+1/2D sketch representation where surfaces, information about depth, and discontinuities on an images are pieced together. First <b>ConvNet</b>. Also had convolutional layers with weight vectors (filters)<br><br>
<b>Towards Algorithms and Practice: Low-level understanding</b>
1981 - Optical Flow: Horn and Schunck develop method to estimate the direction and speed of a moving object across two images. Flow is formulated as a global energy functional which is minimized.<br><br>
1986 - Canny Edge Detector: Multi-stage edge detection operator, with a computational theory of edge detection. Well-defined method simple to implement, became very popular for edge detection.<br><br>
1987 - Recognition by Components Theory: Bottom-up process to explain object recognition. Object's component parts: geons, based on basic 3D shapes assembled to form the object.<br><br>
1988 - Snakes or Active Contour models: delineate an object outline from a possibly noisy 2D image. Widely used in Object tracking, shape recognition, segmentation, edge detection and stereo matching.<br><br>
1989 - Backprop for CNNs arrives. Applied to handwritten digit recognition provided by USPS. <br><br>
<b>Towards Algorithms and Practice: Next-level understanding</b>
1991 - Eigenfaces for face recognition<br>
1997 - Computational theories of object recognition and Perceptual grouping, Normalized Cuts<br>
1998 - Particle filters, Mean shift for tracking<br>
1999 - SIFT <br>
2001 - Viola-Jones face detection and Conditional Random Fields<br>
2005 - Pictorial structures revisited<br>
2006 - PASCAL VOC arrivies; Scene/panorama/location recognition methods grow.<br>
2007 - Constellation models<br>
2009 - Deformable part models<br>
<br>
<b>Deep Learning Era</b>
2010 - ImageNet arrives <br>
2012 - AlexNet wins the ImageNet challenge <br>
2013 - A CNN variant of ZFNet wins ImageNet challenge; R-CNNs for object detection arrive.<br>
2014 - InceptionNet, VGG models arrive, Human Pose Estimation CNNs; Deep generative models: GANs, VAEs.<br>
2015 - ResNet arrives; CNNs match human performance on ImageNet. FCN, SegNet and U-NET for semantic segmentation; COCO dataset arrives; VQA dataset arrives.<br>
2016 - YOLO and SSD for object detection; cityscapes dataset arrives, Visual Genome dataset arrives.<br>
2017 - Scene graph generation models<br>
2018 - VCR Dataset, panoptic segmentation<br>
<br>

### Image Representation
<b>If visible light spectrum is VIBGYOR, why RGB colour representation?</b>
<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/ffff8703-bbaa-4a12-9b87-ee76de6d0780)

<br>
Long(red), Mediumm(green), and Short(blue) cones, plus intensity rods are enough to cover the spectrum at specific wavelengths.<br>
<b>Image as a Matrix:</b>
Common to use one byte per value: 0=black, 255=white. One such matrix for every channel in colour images.<br>
<b>Image as a Function:</b>
We can think of a grayscale image as a function f:R<sup>2</sup> ->  R, giving the intensity at position (x,y). A digital image is a discrete(sampled, quantized) version of this function.<br>
If I(x,y) is the intensity function that gives the intensity value at the position x,y: <br>
I<sup>'</sup> (x,y) = I (-x,y) condition modifies the current image to it's mirror image.<br>
Also, I<sup>'</sup>(x,y) = I(x,y)+20 increases the intensity of the pixels at each position on the image. <br><br>
<b>Image Processing Operations: </b>
<b>Point Operations:</b> Output value at (m<sub>0</sub>,n<sub>0</sub>) is dependent only on the input value at the same coordinate. Constant complexity.<br>
<b>Local Operations:</b> Output value at (m<sub>0</sub>,n<sub<0</sub>) is dependent on input values in a p x p neighbourhood of that same coordinate. P<sup>2</sup> complexity.<br>
<b>Global Operations:</b> Output value at (m<sub>0</sub>,n<sub>0</sub>) is dependent on all the values in the input N x N image. N<sup>2</sup> complexity.
<br><br>
<b>Image Operations: Example</b>
Different types of image enhancement<br>
Contrast Reversing:<br>
I<sup>'</sup>(m<sub>0</sub>,n<sub>0</sub>) = I<sub>MAX</sub> - I(m<sub>0</sub>,n<sub>0</sub>) + I <sub>MIN</sub>. 
<br><br>
Contrast Stretching:<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/5e084951-361d-4c0a-807b-39077afc8ee5)

<br>
<b>Histogram Equalization:</b> is a method in image processing of contrast adjustment using the image's histogram.
Let I be the image with M X N pixels in total; I<sub>MAX</sub> be the maximum image intensity value (255); h(I) be the image histogram.<br>
Integrate h(I) to obtain the cumulative distribution c(I), whose each value c<sub>k</sub> = (1/MXN)(&Sigma;<sub>l=1 to k</sub>h(l)).<br>
The transformed image I'(i,j) = I<sub>MAX</sub> x c<sub>p<sub>ij</sub></sub><br>
<br>
<b>Use of Single Point Operations :</b>
<li>Single point's intensity is influenced by multiple factors, and may not tell us everything - Light source, direction, surface geometry, material and nearby surfaces.</li>
<li>Given a camera and a still scene, how do you reduce noise using point operations?</li>
<li>Take many images and average them.</li>
<li>You need local operations otherwise. Examples: Moving Average. </li>
<br>
<b>Global Operations Examples: Fourier transform, etc other transformations.</b>
<br>
<br>
<b>Image Filters: Linear Filter :- </b>
Modify the image pixels based on some function of a local neighbourhood of each pixel. E.g.
<table>
  <tr>
    <td>0</td>
    <td>5</td>
    <td>3</td>
  </tr>
    <tr>
    <td>4</td>
    <td>5</td>
    <td>1</td>
    </tr>
    <tr>
    <td>1</td>
    <td>1</td>
    <td>6</td>
    </tr>    
</table>
 => apply a function = mean of all values and replace it in the center element =>
<table>
 <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
    <tr>
    <td></td>
    <td>4</td>
    <td></td>
    </tr>
    <tr>
    <td></td>
    <td></td>
    <td></td>
    </tr>    
</table>

<b>Linear Filter: </b>
Replace each pixel by linear combination of neighbours.Linear combination called kernel, mask or filter.<br>
<table>
  <tr>
    <td>10</td>
    <td>5</td>
    <td>3</td>
  </tr>
    <tr>
    <td>4</td>
    <td>5</td>
    <td>1</td>
    </tr>
    <tr>
    <td>1</td>
    <td>1</td>
    <td>6</td>
    </tr>    
</table>
=> Kernel<br>
<table>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
    <tr>
    <td>0</td>
    <td>0.5</td>
    <td>0</td>
    </tr>
    <tr>
    <td>0</td>
    <td>1</td>
    <td>0.5</td>
    </tr>    
</table>
=>
<table>
  <tr>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
    <tr>
    <td> </td>
    <td>6.5</td>
    <td> </td>
    </tr>
    <tr>
    <td> </td>
    <td> </td>
    <td> </td>
    </tr>    
</table>
Modified image data.
<br>
