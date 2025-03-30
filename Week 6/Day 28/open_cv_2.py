##2) Open front camera in grayscale ( black and white mode )

import cv2

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error")
    exit()

while True:

    ret , frame = cap.read()

    if not ret:
        print("Frame Could not be Captured")
        exit()

    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Front Camera",gray_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        exit()

cap.release()
cv2.destroyAllWindows()

