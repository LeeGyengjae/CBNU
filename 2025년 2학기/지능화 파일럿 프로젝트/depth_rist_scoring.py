# depth_risk_scoring.py
import cv2
import numpy as np

depth = cv2.imread("depth.png", cv2.IMREAD_GRAYSCALE)  # MiDaS 등으로 만든 결과라고 가정
if depth is None:
    raise FileNotFoundError("depth.png not found")

h, w = depth.shape
roi = depth[int(h*0.55):, :]  # 하단만 사용(도로 영역 가정)

# '깊음'을 큰 값으로 가정할지/작은 값으로 가정할지 케이스가 있어, 양쪽 다 계산해봄
mean = float(np.mean(roi))
std = float(np.std(roi))

# 간이 위험도: 변동이 큰 구간을 위험으로 간주
risk_score = std

grade = "LOW"
if risk_score > 25:
    grade = "MEDIUM"
if risk_score > 45:
    grade = "HIGH"

print(f"ROI mean={mean:.2f}, std={std:.2f}")
print(f"Risk score={risk_score:.2f} => grade={grade}")

# 시각화
roi_vis = cv2.resize(roi, (w, int(h*0.45)))
cv2.imwrite("depth_roi.png", roi_vis)
