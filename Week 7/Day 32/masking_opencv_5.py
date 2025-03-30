# 5.  Create  a  program  to  apply  a  mask  that  blurs  everything  except  a  selected  object
# (e.g., a face or a car) in an image.


import cv2
import numpy as np


def blur_except_region(image_path, top_left, bottom_right):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    # Create a blurred version of the image
    blurred = cv2.GaussianBlur(image, (25, 25), 0)

    # Create a mask with the same dimensions as the image, filled with zeros (black)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    # Draw a white filled rectangle on the mask to define the region of interest
    cv2.rectangle(mask, top_left, bottom_right, 255, -1)

    # Create an inverse mask
    inverse_mask = cv2.bitwise_not(mask)

    # Apply the mask to the original image (keep selected region unblurred)
    focused_region = cv2.bitwise_and(image, image, mask=mask)

    # Apply the inverse mask to the blurred image (blur everything else)
    blurred_background = cv2.bitwise_and(blurred, blurred, mask=inverse_mask)

    # Combine the focused region with the blurred background
    final_result = cv2.add(focused_region, blurred_background)

    # Display the original image and the final result
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Except Region", final_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = "images/colorful_2.jpeg"  # Replace with your image path
top_left = (100, 100)  # Replace with the top-left coordinates of the region to keep clear
bottom_right = (300, 300)  # Replace with the bottom-right coordinates of the region to keep clear
blur_except_region(image_path, top_left, bottom_right)
