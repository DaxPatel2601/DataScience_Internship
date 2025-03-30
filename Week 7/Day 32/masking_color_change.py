import cv2 as cv
import numpy as np

image=cv.imread("images/WhatsApp Image 2025-03-05 at 09.42.03_2ad2b886.jpg")

image_hsv=cv.cvtColor(image,cv.COLOR_RGB2HSV)

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

mask=cv.inRange(image_hsv,lower_blue,upper_blue)

image[np.where(mask == 255)] = [0, 0, 255]


cv.imshow("HSV Image",image_hsv)
cv.imshow("mask",mask)
cv.imshow("Output Image",image)

cv.waitKey(0)
cv.destroyAllWindows()
