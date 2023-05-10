from ultralytics import YOLO
url = 'http://10.228.175.90:8080/video'
model = YOLO('yolov8n.pt')
model.predict(source=url, show=True)