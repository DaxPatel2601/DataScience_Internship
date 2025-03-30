# 1.  Write a program to detect a face in a static image using a Haar cascade.

import cv2 as cv

import cv2
from cv2.data import haarcascades


def detect_face(image_path):
    # Load the Haar cascade for face detection
    haar_cascade = cv.CascadeClassifier("Face Detaction/haar_face.xml")
    # cv2.imshow("trd",image_path)

    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv.imshow("f",gray)

    # Detect faces
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    person_count = len(faces)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.putText(image, f"{person_count}", (20, 80), cv.FONT_HERSHEY_SIMPLEX, 2, (20, 25, 100), 5)

    # Show the result
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Provide the path to your image
detect_face("images/images.jpeg")


