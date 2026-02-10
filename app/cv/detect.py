from ultralytics import YOLO

model = None


def get_model():
    global model
    if model is None:
        model = YOLO("yolov8n.pt")
    return model


def analyze_frame(image_path: str):
    yolo_model = get_model()
    results = yolo_model(image_path)

    people_count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = yolo_model.names[cls]

            if label == "person":
                people_count += 1

    if people_count > 25:
        crowd = "HIGH"
    elif people_count > 10:
        crowd = "MEDIUM"
    else:
        crowd = "LOW"

    return {
        "people_count": people_count,
        "crowd_density": crowd
    }
