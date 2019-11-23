import cv2
import numpy as np


img1 = cv2.imread("res_old.jpg",2)
img2 = cv2.imread("res_new2old.jpg",2)

ret1, bw_img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
ret2, bw_img2 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)


cv2.imwrite("bi_old.jpg", bw_img1)
cv2.imwrite("bi_new.jpg", bw_img2)


