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
<br>
<b>Linear Filter: Cross-Correlation:</b> Give a kernel of size (2k+1) x (2k+1)<br>
<b>Correlation defined as:</b>It can also be told sum of the values of image.<br><br>
G(i,j) = (1/(2k+1)<sup>2</sup>) * &Sigma;<sub>(u=-k to k)</sub>&Sigma;<sub>(v=-k to k)</sub> I(i+u,j+v)
<br><br>
Looping over pixels in considered neighbourhood around I(i,j) and dividing it with uniform weight to each pixel.
<br><br>
Now <b>Cross-Correlation</b> is defined as:<br><br>
G(i,j) = &Sigma;<sub>(u=-k to k)</sub> &Sigma;<sub>(v=-k to k)</sub> H(u,v) I(i+u,j+v) <br>
Here there are non-uniform weights to each pixel in the kernel/filter, take that weight through the H(u,v) function.<br><br>
Cross - correlation is denoted by:
G = H &otimes; I <br><br>
<b>This can be viewed as a "dot product" between local neighbourhood and kernel for each pixel.</b><br><br>
<li>Entires of kernel or mask H(u,v) called filter co-efficients.</li>
Example: <br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/147b8aa3-dfdb-46b4-8dbd-7b82f359d0c1)

<br>
Moving average filter example:<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/2f3b1259-a719-424d-9533-1ed3d68f1094)

<br>
If we want nearest neighbouring pixels to have the most influence on the input <br>
H(u,v) would be:<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/d1f0721e-7d3f-45cf-bf07-cde6bf0e1a47)

<br>
This kernel is an approximation of a 2D gaussian function.<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/ca910185-e88b-4ec4-9925-40a414afa66f)

Edge filter: <br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/104ebc1f-5482-42e7-b6d9-a3d0e8cbec38)

<br>

Impulse signal with Arbitrary Kernel H: <br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/e2dc7be6-b8b4-4775-938d-59b42d97aae6)


The output is a double flipped kernel instead of a direct kernel, this problem is modified by introducing Convolution instead of Cross-correlation.<br><br>
<b>Convolution:</b>
<br>
G(i,j) = &Sigma;<sub>(u=-k to k)</sub>&Sigma;<sub>(v=-k to k)</sub> H(u,v) I(i-u,j-v) <br>
While calculating the product itself, instead of the cross-correlation's I(i+u,j+v), the function already double flips through i-u and j-v. This handles the problem we got earlier.<br>
<br>
Equivalent to flip the filter in both directions(bottom to top and right to left) and apply cross-correlation.<br>
Denoted by: G = H * I <br>
<br>
<b>Linear Shift-Invariant Operators</b>
Both correlation and convolution are Linear Shift-Invariant operators, which obey: <br>
<b>Linear(or Superposition):</b> <br>
I&circo;(h<sub>0</sub> + h<sub>1</sub>) = I&circo;h<sub>0</sub> + I&circo;h<sub>1</sub> <br>
<br>
<b>Shift-invariance :</b><br>
Shifting or translating a signal commutes with applying the operator<br>
g(i,j) = h(i+k,j+l) <=> (f&circo;g)(i,j) = (f&circo;h)(i+k,j+l)<br>
<br>
This is equivalent to saying that the effect of the operator is the same everywhere. Why do we need this in computer vision? To understand the properties of Convolution and use them. <br>
<b>Properties of Convolution: </b><br>
<li>Commutative: a*b = b*a</li>
<li>Associative: a*(b*c) = (a*b)*c - Applying filters one after the other is the same as a cumulative filter.</li>
<li>Distributive over addition: a*(b+c)= (a*b) + (a*c) - combine the responses of a signal over two or more filters by combining them.</li>
<li>Scalars factor out: ka*b = a*kb = k(a*b)</li>
<li>Identity: Unit impulse e = [.....,0,0,1,0,0,....], a*e = a</li>
<b>Separability: </b>
<li>Convolution operator requires k<sup>2</sup> operations per pixel, where k is the width(and height) of a convolution kernel.</li>
<li>Costly. Reducing cost - for certain filters, can be sped up by performing a 1D horizontal convolution followed by a 1D vertical convolution, requiring 2K operations => conv kernel is separable.</li>
K = vh<sup>T</sup>, where v, h are 1D kernels and K is the 2D kernel.<br><br>
Example:<br>
(1/16)*
<table>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>1</td>
  </tr>
  <tr>
    <td>2</td>
    <td>4</td>
    <td>2</td>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>1</td>
  </tr>
</table>
=> v = h = 1/4*
<table>
  <tr>
    <td>1</td>
  </tr>
  <tr>
    <td>2</td>
  </tr>
  <tr>
    <td>1</td>
  </tr>
</table>
<br>
Example - 2:<br>
(1/8)*
<table>
  <tr>
    <td>-1</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>-2</td>
    <td>0</td>
    <td>2</td>
  </tr>
  <tr>
    <td>-1</td>
    <td>0</td>
    <td>1</td>
  </tr>
</table>
=> 
v = (1/4)*
<table>
  <tr>
    <td>-1</td>
  </tr>
  <tr>
    <td>-2</td>
  </tr>
  <tr>
    <td>-1</td>
  </tr>
</table>
and
h=(1/2)*
<table>
  <tr>
    <td>1</td>
  </tr>
  <tr>
    <td>0</td>
  </tr>
  <tr>
    <td>1</td>
  </tr>
</table>
<br>
<b>Separable Convolution:</b>
How do we know if a given K is separable?
<li>Visual inspection.</li>
<li>Analytically, look at SVD and if only one singular value is non-zero,=> separable</li>
K = U&Sigma;V<sup>T</sup> = &Sigma;<sub>i</sub> &sigma;<sub>i</sub>u<sub>i</sub>v<sub>i</sub><sup>T</sup><br>
where &Sigma; = diag(&sigma;<sub>i</sub>) <br>
and sqrt(&sigma;<sub>1</sub>u<sub>1</sub>) and sqrt(&sigma;<sub>1</sub>v<sub>1</sub>) are the vertical and horizontal kernels<br>
<br>
<b>Practical Issues:</b>
<li>Ideal size> - The bigger the mask - the more neighbours contribute, smaller noise variance of output, bigger noise spread, more blurring and more expensive to compute.</li>
<li>Without padding, we lose out information at the boundaries. We can use a variety of strategies such as zero padding, wrapping around, copy the edge.</li>
<br>
<b>Different padding strategies:</b><br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/24b0901e-b3af-4398-856c-eeba124c933d)

<br>
<b>Is Correlation still useful?</b>
<br>
<li>Can be used for Template matching.</li>
<li>Filters look like objects they are intended to find and then we use the normalized cross-correlation score to find the pattern in an image.</li>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/10e6682d-5864-4c85-b137-36f149c48569)

<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/43a01bc4-acc4-4681-9f5f-0eba7a501a3d)

<br>

<b>Non-linear filters:</b>
<li>Different types of noise in images</li>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/54554c41-108b-4a35-9cc4-28b215bb1fb9)

<li>Reducing Salt-and-pepper noise using gaussian filters.</li>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/6a0de31d-8de3-4914-b06d-ad66d540e521)

<br>
<br>

<b>Median filter </b>- Replace each pixel with MEDIAN value of all pixels in the neighbourhood.
<li>Non-linear</li>
<li>Does not spread noise</li>
<li>Can remove spike noise</li>
<li>Robust to outliers, but not good for Gaussian noise.</li>
<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/4d52ebd6-e602-4ba8-836b-5521c6d93c7e)

<br>
<b>Non-Linear filters: Bilateral filtering</b><br>
<li>Noise removal comes at expense of image blurring at edges.</li>
<li>Bilaterial filtering - simple, non-linear edge-preserving smoothing.</li>
<li>Rejects pixels whose values differ too much from the central pixel value.</li>

<li>Output pixel value is weighted combination of neighbouring pixel values.
g(i,j) = $\frac{\Sigma_{k,l} I(k,l)w(i,j,k,l)}{\Sigma_{k,l} w(i,j,k,l)}$ </li>

<li>Data-dependent bilateral weight function composed of domain and range kernel: 
  w(i,j,k,l) = exp($\frac{- [(i-k)^2 + (j-l)^2] }{2\sigma_d^2}$ - $\frac{|| I(i,j) - I(k,l)^2||^2}{2\sigma^2_r}$)
</li>

Example of Bilateral filters:<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/e69f9429-bc2c-4700-a1e3-39544ed92da3)

<br>


