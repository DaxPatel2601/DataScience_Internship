# 4.  Write  a  program  to  mask  and  display  a  rectangular  area  (e.g.,  a  car's  license
# plate).


import cv2
import numpy as np


def mask_rectangle_region(image_path, top_left, bottom_right):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    # Create a mask with the same dimensions as the image, filled with zeros (black)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    # Draw a white filled rectangle on the mask to define the region of interest
    cv2.rectangle(mask, top_left, bottom_right, 255, -1)

    # Bitwise-AND the mask and the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image and the masked rectangular region
    cv2.imshow("Original Image", image)
    cv2.imshow("Masked Rectangular Region", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = "images/cover_3.jpeg"  # Replace with your image path
top_left = (100, 200)  # Replace with the top-left coordinates
bottom_right = (300, 250)  # Replace with the bottom-right coordinates
mask_rectangle_region(image_path, top_left, bottom_right)
