import cv2 as cv

# 6.  Store  10  images  in  the  input_images  folder.  Load  all  images  using  a  loop  or  any
# other logic, convert them to grayscale, and store them in the gray_images folder.


for i in range(1,11):
    img = cv.imread(f"Images/car{i}.jpg")
    img2 = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.imwrite(f"Output_img/car{i}.jpg", img2)



