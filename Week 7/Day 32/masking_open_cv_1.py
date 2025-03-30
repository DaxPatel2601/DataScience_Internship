# 1.  Write  a  program  to  detect  and  highlight  only  blue  regions  in  an  image  using
# masking.

import cv2 as cv
import numpy as np

image=cv.imread("images/group 2.jpg")


img2=cv.cvtColor(image,cv.COLOR_RGB2HSV)

lower_blue = np.array([100, 150, 50])  # Adjust values as needed
upper_blue = np.array([140, 255, 255])

mask=cv.inRange(img2,lower_blue,upper_blue)

result=cv.bitwise_and(image,image,mask)

# cv.imshow("color change",img2)
cv.imshow("mask",image)
cv.imshow("Result",result)

cv.waitKey(0)

