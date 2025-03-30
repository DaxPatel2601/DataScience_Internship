# 8) Create a program that opens camera , captures a video for 15 seconds and stores
# # it.
import cv2
import time

# Open the camera (0 = default, 1 = front camera)
cap = cv2.VideoCapture(0)  # Change to 1 if needed

# Get the default frame width and height
frame_width = int(cap.get(3))  # Width
frame_height = int(cap.get(4))  # Height

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI format
out = cv2.VideoWriter('captured_video.avi', fourcc, 20.0, (frame_width, frame_height))

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

start_time = time.time()  # Start time

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    out.write(frame)  # Write the frame to the video file
    cv2.imshow('Recording - Press Q to Stop', frame)  # Display recording

    # Stop recording after 15 seconds
    if time.time() - start_time > 15:
        print("Recording finished: 15 seconds reached.")
        break

    # Stop recording if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Recording stopped by user.")
        break

cap.release()
out.release()
cv2.destroyAllWindows()
