@"
# Object Detection AI (Python)

![Object Detection](assets/preview.png)

## Overview
This is an **advanced real-time object detection application** built using **Python**, **OpenCV**, and **YOLOv3-tiny / YOLOv3**.  
It features a **user-friendly GUI**, **animations for detected objects**, and **robust error handling** for smooth webcam-based detection.

The application supports:  
- YOLOv3-tiny for **lightweight, fast detection**  
- YOLOv3 for **high-accuracy detection**  
- Non-Maximum Suppression (NMS) to remove duplicate boxes  
- Dynamic confidence threshold and customizable class colors  

---

## Features

- Real-time object detection with webcam feed  
- Friendly GUI interface using **Tkinter + TTKThemes**  
- Handles empty frames and missing detections gracefully  
- Optimized for **CPU and GPU acceleration**  
- Supports multiple object classes (COCO dataset)  
- Adjustable confidence and NMS thresholds for performance tuning  

---

## Project Structure
object_detection_ai/
│
├─ core/
│ └─ detector.py # YOLO detection logic with OpenCV DNN
│
├─ ui/
│ └─ gui.py # Tkinter GUI code
│
├─ models/
│ ├─ yolov3-tiny.weights
│ ├─ yolov3-tiny.cfg
│ └─ coco.names
│
├─ config.py # Configuration file (paths, thresholds)
├─ main.py # Entry point to run the app
└─ README.md # This documentation


---


### 1. Clone the repository

```bash
git clone <https://github.com/Abhinavsathyann/object_detection_ai>
cd object_detection_ai
'''



