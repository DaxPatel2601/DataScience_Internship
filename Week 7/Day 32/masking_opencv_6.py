# 6.  Use Haar cascades to detect a face in an image and isolate it using a mask.

import cv2
import numpy as np

image = cv2.imread('images/group 1.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) > 0:
    x, y, w, h = faces[0]

    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

    result = cv2.bitwise_and(image, image, mask=mask)

    cropped_face = result[y:y + h, x:x + w]
    cv2.imshow('Isolated Face', cropped_face)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No face detected")