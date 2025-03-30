# 1. Ask the user for their choice:
# ○ 1 → Capture Image
# ○ 2 → Record Video
# ○ 3 → Open Live Feed
# ○ 4 → Exit

import cv2 as cv

cep = cv.VideoCapture(0)


def user_input():
    user_choice=int(input("(1:Capture Image,2:Record Video,3:Open Live Feed,4:Exit)"))
    return user_choice

def capture_image(cep):
    while True:
        ret , frame=cep.read()
        cv.imshow("Front Camera",frame)

        if not ret:
            print("could an error in capturing frame")
            exit()
        print("Enter S for save the image and Q for exit the code")
        if cv.waitKey(1) & 0xFF == ord("s"):
            cv.imwrite("Output_img/Captured_img.jpg", frame)
            exit()
        else:
            exit_code()

def record_video(cep):
    while True:
        ret, frame = cep.read()
        cv.imshow("Front Camera", frame)
        fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Codec for AVI format
        out = None
        recording = False

        if not ret:
            print("could not capture frame")
            exit()

        key = cv.waitKey(1) & 0xFF
        if key == ord('s') and not recording:
            out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
            recording = True
            print("Recording started...")
        elif key == ord('e') and recording:
            recording = False
            if out is not None:
                out.release()
                out = None
            print("Recording stopped.")
        elif key == ord('q'):
            exit_code()


def exit_code():
    key= cv.waitKey(1) & 0xFF
    if key==ord("q"):
        exit()

def main():
    if not cep.isOpened():
        print("Error!!")
        exit()

    user_choice=user_input()

    if user_choice==1:
        capture_image(cep)
    elif user_choice==2:
        record_video(cep)



main()
cv.waitKey(0)
cep.release()
cv.destroyAllWindows()


