# 3) Change the size of camera screen.

import cv2

# Open front camera (change index if needed)
cap = cv2.VideoCapture(0)  # Try 0, 1, or 2 depending on your system

# Set camera resolution (width x height)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    # Resize frame to a new width and height (e.g., 400x300)
    # resized_frame = cv2.resize(frame, (1200, 900))

    cv2.imshow('Resized Camera Screen', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
