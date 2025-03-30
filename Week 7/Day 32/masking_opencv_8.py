# 8.  Write  a  program  to  generate  an  inverted  mask,  where  the  selected  region  is
# hidden, and everything else is visible.


import cv2
import numpy as np


def inverted_mask(image_path, top_left, bottom_right):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    # Create a mask with the same dimensions as the image, filled with white (255)
    mask = np.ones(image.shape[:2], dtype=np.uint8) * 255

    # Draw a black filled rectangle on the mask to define the hidden region
    cv2.rectangle(mask, top_left, bottom_right, 0, -1)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image and the masked result
    cv2.imshow("Original Image", image)
    cv2.imshow("Inverted Masked Region", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = "images/colorful_1.jpg"  # Replace with your image path
top_left = (100, 100)  # Replace with the top-left coordinates of the hidden region
bottom_right = (300, 300)  # Replace with the bottom-right coordinates of the hidden region
inverted_mask(image_path, top_left, bottom_right)
