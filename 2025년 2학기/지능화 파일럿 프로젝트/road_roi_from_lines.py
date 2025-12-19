# road_roi_from_lines.py
import cv2
import numpy as np

img = cv2.imread("road.jpg")
if img is None:
    raise FileNotFoundError("road.jpg not found")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 80, 160)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=80,
                        minLineLength=80, maxLineGap=10)

h, w = gray.shape
y_candidates = []

if lines is not None:
    for x1, y1, x2, y2 in lines.reshape(-1, 4):
        # 거의 수평인 선만 사용
        if abs(y2 - y1) < 10:
            y_candidates.append((y1 + y2) // 2)

# 수평선 후보의 중앙값을 “대략적인 수평선”으로 사용
horizon = int(np.median(y_candidates)) if y_candidates else h // 3
roi_y = min(max(horizon, 0), h-1)

roi = img[roi_y:, :]
vis = img.copy()
cv2.line(vis, (0, roi_y), (w-1, roi_y), (0, 255, 0), 2)

cv2.imwrite("roi.png", roi)
cv2.imwrite("roi_line.png", vis)
print(f"Estimated horizon y={roi_y}. Saved: roi.png, roi_line.png")
