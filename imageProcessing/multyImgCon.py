import os
import cv2


images = os.listdir('imageProcessing/img/')
for image in images:
    gray = cv2.imread(f'imageProcessing/img/{image}', 0)
    cv2.imwrite(f'imageProcessing/grayImages/gray-{image}', gray)