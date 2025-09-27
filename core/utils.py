import cv2

def load_classes(path):
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]

def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h, classes, COLORS):
    label = f"{classes[class_id]}: {confidence:.2f}"
    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), COLORS[class_id], 2)
    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[class_id], 2)
