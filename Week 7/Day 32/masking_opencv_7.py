# 7.  Create a program to highlight yellow objects in an image (e.g., traffic signs).


import cv2
import numpy as np


image = cv2.imread('images/colorful_1.jpg')  # Change to your image

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

highlighted = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("original image",image)
cv2.imshow('Highlighted Yellow Objects', highlighted)
cv2.waitKey(0)
cv2.destroyAllWindows()