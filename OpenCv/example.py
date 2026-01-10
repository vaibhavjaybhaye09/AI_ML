import cv2
import numpy as np

img = cv2.imread("images/bus.jpg") # its our metrix
print(img.shape)

#cap = cv2.VideoCapture("") # video its: collection of multiples frame
#convert to gray scale


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#convert the image color
                                               #SigmaX (auto-calculated by OpenCV)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0) #To blur a grayscale image, you must use Gaussian Blur.
                                       #Kernel size (must be odd numbers)


#Canny Edge Detection is a highly popular, multi-stage algorithm used to identify a wide range of edges in images by detecting sharp changes in pixel intensity.
img_canny = cv2.Canny(img_blur, 100,100)
print("img_gray: ",img_gray)
print("img_gray: ",img_gray.shape)
print("output", img)
print("original :",img.shape)


cv2.waitKey(0)