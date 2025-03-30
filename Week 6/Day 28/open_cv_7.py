# 7) Create a program that opens a camera, captures image and stores when user
# press C and close the camera screen when user press E.


# 5) Change the size of captured picture.

import cv2

# Open the camera (0 = default, 1 = front camera)
cap = cv2.VideoCapture(0)  # Change to 1 if you need the front camera

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()  # Capture frame
    if not ret:
        print("Failed to capture frame.")
        break

    cv2.imshow('Camera - Press SPACE to Capture', frame)  # Display camera feed

    key = cv2.waitKey(1) & 0xFF  # Wait for key press
    if key == ord("c"):  # Press SPACE to capture photo
        resized_frame = cv2.resize(frame, (400, 300))  # Resize to (400x300)
        cv2.imwrite('captured_photo_resized.jpg', resized_frame)  # Save resized image
        print("Photo saved as 'captured_photo_resized.jpg'")
        break
    elif key == ord('e'):  # Press 'q' to quit without saving
        break

cap.release()
cv2.destroyAllWindows()

