# pothole_candidate_mask.py
import cv2
import numpy as np

img = cv2.imread("road.jpg")
if img is None:
    raise FileNotFoundError("road.jpg not found")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# 밝기(V) 기반 적응 이진화 (어두운 영역을 후보로)
mask = cv2.adaptiveThreshold(
    v, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
    blockSize=31, C=5
)

# 작은 노이즈 제거 + 구멍 메우기
k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, k, iterations=1)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k, iterations=2)

overlay = img.copy()
overlay[mask > 0] = (0, 0, 255)  # 후보를 빨간색으로 표시
out = cv2.addWeighted(img, 0.7, overlay, 0.3, 0)

cv2.imwrite("candidate_mask.png", mask)
cv2.imwrite("candidate_overlay.png", out)
print("Saved: candidate_mask.png, candidate_overlay.png")
