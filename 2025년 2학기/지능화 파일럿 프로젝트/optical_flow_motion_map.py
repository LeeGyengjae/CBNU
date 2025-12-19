# optical_flow_motion_map.py
import cv2
import numpy as np

cap = cv2.VideoCapture("drive.mp4")
if not cap.isOpened():
    raise FileNotFoundError("drive.mp4 not found")

ret, prev = cap.read()
if not ret:
    raise RuntimeError("Cannot read first frame")

prev_g = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
acc = np.zeros_like(prev_g, dtype=np.float32)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prev_g, g, None,
                                        0.5, 3, 15, 3, 5, 1.2, 0)
    mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    acc += mag.astype(np.float32)

    prev_g = g

# 정규화 후 시각화
acc_norm = cv2.normalize(acc, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
heat = cv2.applyColorMap(acc_norm, cv2.COLORMAP_JET)

cv2.imwrite("motion_map.png", acc_norm)
cv2.imwrite("motion_heat.png", heat)
print("Saved: motion_map.png, motion_heat.png")
