from PIL import Image
import numpy as np


# Load an image using Numpy and pillow and convert the image into grayscale Image.

img=Image.open("2016_mini_cooper_convertible-HD.jpg")
img.show()

# FLIP the Image.

img_2=img.transpose(Image.FLIP_LEFT_RIGHT)
img_2.show()

# Rotate the Image to 110 degrees.

img_3=Image.open("2016_mini_cooper_convertible-HD.jpg")
img_3.rotate(90).show()


# Save the image to New_image png
img_3.save("img_3.png")

# Load an image using NumPy and Pillow
original_size = img.size
resized_image = img.resize((original_size[0] // 2, original_size[1] // 2))
resized_image.save("resized_image_4.png")

# Resize the image to 50% of its original dimensions.
#
# Save the resized image as resized_image.png.
#
# Load an image using NumPy and Pillow
#
# Flip the image horizontally (left to right).
#
# Flip the image vertically (top to bottom)
#
# Save both flipped images as flipped_horizontal.png and
#
# flipped_vertical.png
#
# Load an image using NumPy and Pillow
#
# Apply a blur effect to the image
#
# Save the blurred image as blurred_image.png