import cv2 as cv

# 1.  Open  the  front  camera  in  normal  mode.  Allow  the  user  to  press  'S'  to  capture  a
# selfie, but store the image in grayscale.


cap=cv.VideoCapture(0)

if not cap.isOpened():
    print("Error")
    exit()

while True:

    ret , frame=cap.read()
    cv.imshow("front camera",frame)

    if not ret:
        print("Could not capture frame")
        exit()

    if cv.waitKey(1) & 0xFF==ord("c"):
        new_frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        cv.imwrite("capture_img.jpg", new_frame)
        exit()
    elif cv.waitKey(1) & 0xFF==ord("q"):
        exit()

cap.release()
cv.destroyAllWindows()

