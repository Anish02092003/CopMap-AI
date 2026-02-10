from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def analyze_frame(image_path: str):
    results = model(image_path)

    people_count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

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
