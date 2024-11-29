from ultralytics import YOLO

# Loading the model
model = YOLO("yolo11n.pt")

# Training the model
results = model.train(
    data="coco8.yaml",  # Dataset configuration file
    epochs=50,                 # Number of epochs
    imgsz=224,                 # Image size for training
    lr0=0.001,                 # Initial learning rate
    batch=16,                  # Batch size
    device=0,                  # GPU index, to train on the GPU
    project="runs/train",      # Path to save the training results
    name="yolo11_finetune",    # Name for the training run
    workers=4                  # Number of data loader workers
)

print("Training complete.")
