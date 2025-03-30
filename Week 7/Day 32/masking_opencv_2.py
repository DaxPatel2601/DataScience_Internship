# 2.  Modify  the  previous  program  to  detect  and  highlight  red  and  green  areas
# simultaneously.

import cv2
import numpy as np

image = cv2.imread('images/colorful_2.jpeg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 50, 70])
upper_blue = np.array([130, 255, 255])

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

mask_combined = cv2.bitwise_or(mask_blue, cv2.bitwise_or(mask_red, mask_green))

result = cv2.bitwise_and(image, image, mask=mask_combined)

cv2.imshow('Original Image', image)
cv2.imshow('Color Mask', mask_combined)
cv2.imshow('Highlighted Regions', result)

cv2.waitKey(0)
cv2.destroyAllWindows()