import cv2 as cv

# 4.  Create an image filter program that:
# ○  Loads an image from the input_images folder.
# ○  Applies three filters:
# ■  Gaussian Blur (7x7)
# ■  Median Blur (5)
# ■  Bilateral Filter (9, 75, 75)
# ○  Saves all three processed images in the filtered_images folder.

img=cv.imread("Images/car1.jpg")
cv.imwrite("gaussian_blur.jpg",cv.GaussianBlur(img,(107,107),10))

cv.imwrite("median_blur.jpg",cv.medianBlur(img,5))

cv.imwrite("bilateral.jpg",cv.bilateralFilter(img,9,75,75))