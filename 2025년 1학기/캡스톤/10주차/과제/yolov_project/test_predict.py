import os
import random
import shutil
from ultralytics import YOLO
from pathlib import Path

# 설정
VAL_IMAGE_DIR = Path('dataset/valid/images')   # ← 실제 validation 이미지 경로
VAL_LABEL_DIR = Path('dataset/valid/labels')   # ← 실제 validation 라벨 경로
SAMPLE_IMAGE_DIR = Path('sample_eval/images')  # ← 샘플 이미지 복사 위치
SAMPLE_LABEL_DIR = Path('sample_eval/labels')  # ← 샘플 라벨 복사 위치
MODEL_PATH = 'runs/detect/yolov8_custom/weights/best.pt'
NUM_SAMPLES = 5

# 1. 테스트 샘플 준비
def prepare_sample_dataset(num_samples=5):
    SAMPLE_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    SAMPLE_LABEL_DIR.mkdir(parents=True, exist_ok=True)

    all_images = [f for f in VAL_IMAGE_DIR.iterdir() if f.suffix in ['.jpg', '.png']]
    selected = random.sample(all_images, min(num_samples, len(all_images)))

    for img_path in selected:
        shutil.copy(img_path, SAMPLE_IMAGE_DIR / img_path.name)
        label_path = VAL_LABEL_DIR / img_path.with_suffix('.txt').name
        if label_path.exists():
            shutil.copy(label_path, SAMPLE_LABEL_DIR / label_path.name)

    print(f"샘플 {len(selected)}장 추출 완료.")
    return selected

# 2. 평가용 data.yaml 임시 생성
def write_temp_data_yaml():
    yaml_path = Path('sample_eval/data.yaml')
    with open(yaml_path, 'w') as f:
        f.write(
            f"path: sample_eval\n"
            f"train: images  # dummy path for requirement\n"
            f"val: images\n"
            f"nc: 9\n"
            f"names: ['Capacitor', 'Diode', 'EMC filter', 'IC', 'Inductor', 'Mosfet', 'Register', 'Soldering', 'led']\n"
        )
    return yaml_path

# 3. 모델 평가 수행
def evaluate_model(model_path, data_yaml_path):
    model = YOLO(model_path)
    metrics = model.val(data=str(data_yaml_path))

    # 주요 지표 출력
    print("평가 결과:")
    print(f"mAP@0.5       : {metrics.box.map50:.4f}")
    print(f"mAP@0.5:0.95  : {metrics.box.map:.4f}")
    print(f"Precision     : {metrics.box.mp:.4f}")
    print(f"Recall        : {metrics.box.mr:.4f}")

if __name__ == "__main__":
    prepare_sample_dataset(NUM_SAMPLES)
    data_yaml = write_temp_data_yaml()
    evaluate_model(MODEL_PATH, data_yaml)
