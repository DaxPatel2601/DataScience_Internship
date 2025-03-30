import cv2
import cv2 as cv

# 3.  Open the front camera with a frame displaying your name in the frame.


cep = cv.VideoCapture(0)

if not cep.isOpened():
    print("Error")
    exit()

while True:
    ret, frame=cep.read()
    new_frame=cv.putText(frame,"DAX",(0,100),cv.FONT_HERSHEY_SIMPLEX,1,(20,25,100),2)
    cv.imshow("front",new_frame)

    if not ret:
        print("could not capture frame")
        exit()

    if cv.waitKey(1) & 0xFF==ord("q"):
        exit()

cep.release()
cv2.destroyAllWindows()


