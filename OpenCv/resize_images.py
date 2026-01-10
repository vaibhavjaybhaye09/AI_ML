import cv2
## croping Images
img = cv2.imread('images/bus.jpg')
crop_img = img[0:200,200:500]
cv2.imshow('output',img)
cv2.imshow('crop_output',crop_img)
cv2.waitKey(0)