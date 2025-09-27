import cv2, numpy as np
from core import config, utils

class ObjectDetector:
    def __init__(self):
        self.classes = utils.load_classes(config.MODEL_NAMES)
        self.net = cv2.dnn.readNet(config.MODEL_WEIGHTS, config.MODEL_CFG)
        self.COLORS = np.random.uniform(0, 255, size=(len(self.classes), 3))

    def detect(self, frame):
        Height, Width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.get_output_layers())
        class_ids, confidences, boxes = [], [], []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > config.CONF_THRESHOLD:
                    center_x, center_y, w, h = (
                        int(detection[0]*Width),
                        int(detection[1]*Height),
                        int(detection[2]*Width),
                        int(detection[3]*Height)
                    )
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)
                    boxes.append([x,y,w,h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indices = cv2.dnn.NMSBoxes(boxes, confidences, config.CONF_THRESHOLD, config.NMS_THRESHOLD)
        for i in indices:
            i = i[0]
            box = boxes[i]
            x,y,w,h = box
            utils.draw_prediction(frame, class_ids[i], confidences[i], x, y, x+w, y+h, self.classes, self.COLORS)
        return frame

    def get_output_layers(self):
        layer_names = self.net.getLayerNames()
        return [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]
