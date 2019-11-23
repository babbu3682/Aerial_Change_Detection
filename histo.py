'''
Image Alignment 

Satya Mallick, LearnOpenCV.com
'''
from __future__ import print_function
import cv2
import numpy as np



refFilename1 = "new.jpg"
print("Reading reference image : ", refFilename1)
imReference1 = cv2.imread(refFilename1, cv2.IMREAD_COLOR)


refFilename2 = "old.jpg"
print("Reading reference image : ", refFilename2)
imReference2 = cv2.imread(refFilename2, cv2.IMREAD_COLOR)


# Convert images to grayscale
imReference1[:,:,0] = cv2.equalizeHist(imReference1[:,:,0])
imReference1[:,:,1] = cv2.equalizeHist(imReference1[:,:,1])
imReference1[:,:,2] = cv2.equalizeHist(imReference1[:,:,2])

# Convert images to grayscale
imReference2[:,:,0] = cv2.equalizeHist(imReference2[:,:,0])
imReference2[:,:,1] = cv2.equalizeHist(imReference2[:,:,1])
imReference2[:,:,2] = cv2.equalizeHist(imReference2[:,:,2])

cv2.imwrite("res_new.jpg", imReference1)

cv2.imwrite("res_old.jpg", imReference2)




