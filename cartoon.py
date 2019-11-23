import cv2
import numpy as np

img1 = cv2.imread("res_new2old.jpg")

img2 = cv2.imread("res_old.jpg")

# 1) Edges
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.medianBlur(gray1, 5)
edges1 = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray2 = cv2.medianBlur(gray2, 5)
edges2 = cv2.adaptiveThreshold(gray2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)



# 2) Color
color1 = cv2.bilateralFilter(img1, 9, 300, 300)

color2 = cv2.bilateralFilter(img2, 9, 300, 300)

# 3) Cartoon
cartoon1 = cv2.bitwise_and(color1, color1, mask=edges1)

cartoon2 = cv2.bitwise_and(color2, color2, mask=edges2)


# cv2.imshow("Image", img)
cv2.imwrite('cartoon_new.jpg', cartoon1)
cv2.imwrite('color_new.jpg', color1)
cv2.imwrite('edges_new.jpg', edges1)

cv2.imwrite('cartoon_old.jpg', cartoon2)
cv2.imwrite('color_old.jpg', color2)
cv2.imwrite('edges_old.jpg', edges2)

