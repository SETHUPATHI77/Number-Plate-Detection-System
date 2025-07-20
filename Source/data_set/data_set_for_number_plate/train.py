from ultralytics import YOLO

model = YOLO("yolov8m.pt")
model.train(data="data.yaml", epochs=1000, imgsz=640,batch = 6,patience=100)
metrics = model.val()
