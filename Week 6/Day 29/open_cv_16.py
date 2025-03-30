# 7.  Load  Image  from  folder  and  detect  edges  of  the  image  and  store  it  as  edge_image
# in folder.

import cv2
import cv2 as cv0

img=cv2.imread("Images/car1.jpg")

img2 = cv2.Canny(img,-120,300)

cv2.imwrite("car1.jpg",img2)


