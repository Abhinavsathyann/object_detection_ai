import requests

urls = {
    "yolov3.weights": "https://pjreddie.com/media/files/yolov3.weights",
    "yolov3-tiny.weights": "https://pjreddie.com/media/files/yolov3-tiny.weights"
}

for file_name, url in urls.items():
    print(f"Downloading {file_name}...")
    resp = requests.get(url, stream=True)
    with open(f"models/{file_name}", "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"{file_name} downloaded ✅")
