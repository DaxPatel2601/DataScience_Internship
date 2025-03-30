# 3.  Create a program to extract a circular region (e.g., the car wheel) from an image.

import cv2
import numpy as np


def extract_circular_region(image_path, center, radius):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    # Create a mask with the same dimensions as the image, filled with zeros (black)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    # Draw a white filled circle on the mask to define the region of interest
    cv2.circle(mask, center, radius, 255, -1)

    # Bitwise-AND the mask and the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image and the extracted circular region
    cv2.imshow("Original Image", image)
    cv2.imshow("Extracted Circular Region", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = "images/colorful_1.jpg"  # Replace with your image path
center = (250, 250)  # Replace with the center of the circular region
radius = 100  # Replace with the desired radius
extract_circular_region(image_path, center, radius)
