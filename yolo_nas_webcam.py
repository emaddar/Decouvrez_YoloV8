
from super_gradients.training import models

model = models.get('yolo_nas_s', pretrained_weights='coco')


model.predict_webcam()