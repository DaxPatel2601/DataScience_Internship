import cv2 as cv

# 5.  Allow  the  user  to  enter  the  height  and  width  of  an  image.  Resize  the  image
# accordingly and store it in a folder called output_images.

width=int(input("Enter The Width:"))
height=int(input("Enter The Height:"))

img=cv.imread("Images/2016_mini_cooper_convertible-HD.jpg")

img2=cv.resize(img,(width,height))
cv.imwrite("Output_img/resize_img.jpg",img2)

