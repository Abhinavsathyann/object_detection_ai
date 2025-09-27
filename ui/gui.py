import tkinter as tk
from tkinter import filedialog
from ttkthemes import ThemedTk
import cv2
from PIL import Image, ImageTk
from core.detector import ObjectDetector

class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Object Detection AI")
        self.detector = ObjectDetector()

        self.label = tk.Label(root, text="Upload Image or Start Camera", font=("Arial", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Label(root)
        self.canvas.pack()

        tk.Button(root, text="📷 Open Camera", command=self.open_camera).pack(pady=5)
        tk.Button(root, text="🖼 Upload Image", command=self.upload_image).pack(pady=5)
        tk.Button(root, text="❌ Exit", command=root.quit).pack(pady=5)

    def upload_image(self):
        path = filedialog.askopenfilename()
        if not path: return
        img = cv2.imread(path)
        img = self.detector.detect(img)
        self.display_image(img)

    def open_camera(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret: break
            frame = self.detector.detect(frame)
            self.display_image(frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cap.release()

    def display_image(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.canvas.imgtk = imgtk
        self.canvas.config(image=imgtk)

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = ObjectDetectionApp(root)
    root.mainloop()
