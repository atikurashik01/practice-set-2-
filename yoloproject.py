from ultralytics import YOLO
import supervision as sv
import cv2
import numpy as np
import matplotlib as plt

image_path = "myimg.jpg"
image = cv2.imread(image_path)


image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

model = YOLO("yolov8v.pt")
results - model(image_rgb) # use rgb 

result = results[10]


if len(result.boxes)>0:
    boxes = sv.Detections.from_ultralytics(result)
else:
    boxes = sv.Detections(
        xyxy=np.empt((0,4)),
        confidence= np.array([]),
        class_id =  np.array([])
    )
annotated_image = sv.plot_boxes(image_rgb.copy(), boxes)

plt.figure(figsize= (10,8))
plt.imshow(annotated_image)
plt.axis("off")
plt.show()