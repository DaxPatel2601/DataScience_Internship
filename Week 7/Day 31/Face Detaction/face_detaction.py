# image detection

import cv2 as cv

cep = cv.VideoCapture(0)

if not cep.isOpened():
    print("Error")
    exit()

haar_cascade=cv.CascadeClassifier("haar_face.xml")


while True:

    ret , frame = cep.read()
    gray_frame=cv.cvtColor(frame,cv.COLOR_RGB2GRAY)

    faces_rect=haar_cascade.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=3)
    person_count=len(faces_rect)

    for (x,y,w,h) in faces_rect:
        xframe=cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
        xxframe=cv.flip(xframe,1)
        new_frame=cv.putText(xxframe,f"{person_count}",(20,80),cv.FONT_HERSHEY_SIMPLEX,2,(20,25,100),5)
        cv.imshow("output",new_frame)

    if not ret:
        print("Could not capture frame")
        exit()

    key = cv.waitKey(1) & 0xFF

    if key==ord("q"):
        exit()

cep.release()
cv2.destroyAllWindows()


