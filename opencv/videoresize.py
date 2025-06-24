import cv2 as cv

# Open video file or webcam (use 0 for webcam)
cap = cv.VideoCapture('videos/abc.mp4')  # Replace with your actual file path

# Check if video opened successfully
if not cap.isOpened():
    print("❌ Error: Cannot open video file or webcam")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("✅ Video finished or frame not captured.")
        break

    # Resize the frame
    resized_frame = cv.resize(frame, (640, 480))  # (width, height)

    # Display resized frame
    cv.imshow('Resized Video', resized_frame)

    # Exit on 'q' key press
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
