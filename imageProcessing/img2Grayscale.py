# installed opencv-python
#  this script converts image to grayscale
import cv2

color = cv2.imread('imageProcessing/child.jpg', 0)
cv2.imwrite('imageProcessing/child.jpg', color)