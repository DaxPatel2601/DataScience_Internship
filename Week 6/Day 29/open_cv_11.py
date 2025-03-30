import cv2 as cv

# 2.  Open the front camera in a mirrored mode.

cep = cv.VideoCapture(0)

if not cep.isOpened():
    print("Error")
    exit()

while True:
    ret,frame =cep.read()

    new_frame=cv.flip(frame,1)
    cv.imshow("Front camera",new_frame)
    if not ret:
        print("could not capture image")
        exit()

    key = cv.waitKey(1) & 0xFF

    if key==ord("q"):
        exit()

cep.release()
cv.destroyAllWindows()

