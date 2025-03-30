# 4) Create a program that opens camera , captures a photo and saves it and close
# camera window.

import cv2

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("error")
    exit()

while True :

    ret , frame = cap.read()

    if not ret:
        print("could not caputure frame")
        exit()

    cv2.imshow("front camera",frame)

    if cv2.waitKey(1)& 0xFF == ord("s"):
        cv2.imwrite("Capture_img.jpg",frame)
        print("Picture is saved successfully")
        break
    elif cv2.waitKey(1) & 0xFF == ord("q"):
        exit()

cap.release()
cv2.destroyAllWindows()
