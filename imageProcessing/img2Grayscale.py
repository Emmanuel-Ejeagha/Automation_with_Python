# installed opencv-python
#  this script converts image to grayscale
import cv2

color = cv2.imread('imageProcessing/img/child.jpg', 0)
cv2.imwrite('imageProcessing/img/child0.jpg', color)