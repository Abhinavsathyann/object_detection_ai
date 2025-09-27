from ui.gui import ObjectDetectionApp
from ttkthemes import ThemedTk

if __name__ == "__main__":
    root = ThemedTk(theme="breeze")
    app = ObjectDetectionApp(root)
    root.mainloop()
