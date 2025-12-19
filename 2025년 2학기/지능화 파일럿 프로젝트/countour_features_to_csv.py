# contour_features_to_csv.py
import cv2
import numpy as np
import csv

mask = cv2.imread("candidate_mask.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("road.jpg")
if mask is None or img is None:
    raise FileNotFoundError("candidate_mask.png and road.jpg required")

cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rows = []
vis = img.copy()

for i, c in enumerate(cnts):
    area = cv2.contourArea(c)
    if area < 300:  # 너무 작은 것 제외
        continue
    peri = cv2.arcLength(c, True)
    circularity = 0 if peri == 0 else (4 * np.pi * area) / (peri * peri)
    x, y, w, h = cv2.boundingRect(c)

    rows.append([i, area, peri, circularity, x, y, w, h])
    cv2.rectangle(vis, (x, y), (x+w, y+h), (255, 0, 0), 2)

with open("contour_features.csv", "w", newline="", encoding="utf-8") as f:
    wr = csv.writer(f)
    wr.writerow(["id", "area", "perimeter", "circularity", "x", "y", "w", "h"])
    wr.writerows(rows)

cv2.imwrite("contours_vis.png", vis)
print("Saved: contour_features.csv, contours_vis.png")
