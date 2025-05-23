from ultralytics import YOLO

# 모델 불러오기 (yolov8n)
model = YOLO("yolov8n.pt")  # 자동 다운로드

# 학습
model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="yolov8_custom"
)
