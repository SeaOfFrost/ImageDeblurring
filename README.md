Image Deblurring
Application that tests an image for bluriness and deblurs the image 

This project aims to be an application that does two major things -- check if an image is a blurry and if so, deblur the image. 
Hence, there are two steps.

Setup/Usage
======
1. Blur Detection and Deblur
To just run the blur detection and deblurring, use the detect_blur_image file, with the path of the image as an argument

```python
python detect_blur_image.py --image PATH 
```
2. Train Network
If you wish to train the network and then run the program, do the following.

⋅⋅⋅First get the images that you wish to blur and save it in the folder called 'inputs.' Then add the Gaussian blur to your own set of images using

```python
python ../src/detect_blur_image.py --image PATH 
```
⋅⋅⋅To train the network, run the following. Change the number of epochs according to your requirements
```python
python deblur_train.py --epochs 50 
```

Blur Detection
======
The blur detection here is based on the magnitude of the Fast Fourier Transform as explained in [this paper](http://www.cse.cuhk.edu.hk/leojia/all_final_papers/blur_detect_cvpr08.pdf). The code for the same is based on the helpful tutorial shown [over here](https://www.pyimagesearch.com/2020/06/15/opencv-fast-fourier-transform-fft-for-blur-detection-in-images-and-video-streams/).

Image Deblurring using SRCNN
======
Once it is detected that the image is blurry, we then use a slightly modified version of the SRCNN model as described [here](https://www.researchgate.net/publication/221364186_Image_super-resolution_as_sparse_representation_of_raw_image_patches). 

The model is trained using images from this [Kaggle blur dataset](https://www.kaggle.com/kwentar/blur-dataset), for images that have Gaussian blur. The code is based on the tutorial on [this website](https://debuggercafe.com/image-deblurring-using-convolutional-neural-networks-and-deep-learning/)  