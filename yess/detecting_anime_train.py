from ultralytics import YOLO

def train_model():
    model = YOLO('yolov8n.pt') 

    # Run the training
    model.train(
        data='data.yaml', 
        epochs=100, 
        imgsz=1080, 
        device=0,
        workers=4 
    )

if __name__ == '__main__':
    train_model()