from ultralytics import YOLO

# Loading a pre-trained model
model = YOLO('yolov8n.pt')

# Using the model
results = model.train(data='coco8.yaml', epochs=3)  # train the model
results = model.val()  # evaluate model performance on the validation set
results = model.export(format='onnx')  # export the model to ONNX format