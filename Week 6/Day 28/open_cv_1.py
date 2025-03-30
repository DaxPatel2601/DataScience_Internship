import cv2
## 1) Open front camera.

cap= cv2.VideoCapture(0)

if not cap.isOpened():
    print("error")
    exit()

while True:

    ret,frame = cap.read()

    if not ret:
        print("fail to capture frame")
        exit()

    cv2.imshow('Front Camera',frame)

    if cv2.waitKey(1)& 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()




