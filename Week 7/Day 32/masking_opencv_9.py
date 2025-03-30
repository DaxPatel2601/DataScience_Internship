# 9.  Create  a  program  to  mask  and  extract  a  specific  color  (e.g.,  orange)  from  an
# image and convert the rest of the image to grayscale.


import cv2
import numpy as np


def extract_color_and_grayscale(image_path, lower_bound, upper_bound):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create a mask for the specific color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Extract the color region
    color_region = cv2.bitwise_and(image, image, mask=mask)

    # Convert the original image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert grayscale back to 3 channels
    grayscale_3channel = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2BGR)

    # Combine the grayscale image with the extracted color region
    final_result = np.where(mask[:, :, None] == 255, color_region, grayscale_3channel)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Color Extracted Image", final_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = "images/colorful_2.jpeg"  # Replace with your image path
lower_orange = np.array([10, 100, 100])  # Lower HSV bound for orange
upper_orange = np.array([25, 255, 255])  # Upper HSV bound for orange
extract_color_and_grayscale(image_path, lower_orange, upper_orange)
