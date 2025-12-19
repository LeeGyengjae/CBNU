# dataset_sanity_check.py
import os
from pathlib import Path

images_dir = Path("images")   # 예: images/*.jpg
labels_dir = Path("labels")   # 예: labels/*.txt (YOLO 포맷이든 뭐든 상관없이 '존재'만 체크)

img_exts = {".jpg", ".jpeg", ".png", ".bmp"}

images = {p.stem: p for p in images_dir.iterdir() if p.suffix.lower() in img_exts}
labels = {p.stem: p for p in labels_dir.iterdir() if p.suffix.lower() == ".txt"}

missing_label = sorted(set(images.keys()) - set(labels.keys()))
missing_image = sorted(set(labels.keys()) - set(images.keys()))

print(f"Images: {len(images)}")
print(f"Labels: {len(labels)}")
print(f"Missing labels: {len(missing_label)}")
print(f"Missing images: {len(missing_image)}")

if missing_label:
    print("\n[Examples missing label]")
    for k in missing_label[:10]:
        print(" -", images[k])

if missing_image:
    print("\n[Examples missing image]")
    for k in missing_image[:10]:
        print(" -", labels[k])
