# 9) Create a program that opens a camera, capture videos when user press C , stops
# recording video when user press S.

import cv2

# Open the camera (0 = default, 1 = front camera)
cap = cv2.VideoCapture(0)  # Change to 1 if needed

# Get the default frame width and height
frame_width = int(cap.get(3))  # Width
frame_height = int(cap.get(4))  # Height

# Define the codec and VideoWriter object (not initialized yet)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None  # Placeholder for VideoWriter

recording = False  # Flag to track recording state

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'C' to start recording, 'S' to stop, and 'Q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    cv2.imshow('Camera - Press C to Start, S to Stop, Q to Quit', frame)

    key = cv2.waitKey(1) & 0xFF  # Wait for key press

    if key == ord('c') and not recording:
        print("Recording started...")
        out = cv2.VideoWriter('user_recorded_video.avi', fourcc, 20.0, (frame_width, frame_height))
        recording = True

    if recording:
        out.write(frame)  # Save the frame if recording

    if key == ord('s') and recording:
        print("Recording stopped.")
        recording = False
        out.release()  # Stop writing to file

    if key == ord('q'):
        print("Exiting program.")
        break

cap.release()
if recording:
    out.release()  # Ensure video is saved if recording was active
cv2.destroyAllWindows()
