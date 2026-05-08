import cv2
from ultralytics import YOLO

# Load your custom trained model
model = YOLO('train-3/weights/best.pt')

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Run YOLO inference on the frame
        results = model(frame)
        
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        
        cv2.imshow("Anime Figure Detector", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()