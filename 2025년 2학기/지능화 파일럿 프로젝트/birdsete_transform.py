# birdseye_transform.py
import cv2
import numpy as np

img = cv2.imread("road.jpg")
if img is None:
    raise FileNotFoundError("road.jpg not found")

h, w = img.shape[:2]

# 원본 4점(대략 도로 사다리꼴) - 필요 시 수정
src = np.float32([
    [int(w*0.15), int(h*0.60)],
    [int(w*0.85), int(h*0.60)],
    [int(w*0.98), int(h*0.98)],
    [int(w*0.02), int(h*0.98)],
])

# 목표 4점(직사각형)
dst_w, dst_h = 800, 600
dst = np.float32([
    [0, 0],
    [dst_w-1, 0],
    [dst_w-1, dst_h-1],
    [0, dst_h-1],
])

M = cv2.getPerspectiveTransform(src, dst)
bev = cv2.warpPerspective(img, M, (dst_w, dst_h))

vis = img.copy()
for i in range(4):
    p1 = tuple(src[i].astype(int))
    p2 = tuple(src[(i+1) % 4].astype(int))
    cv2.line(vis, p1, p2, (0, 255, 255), 2)

cv2.imwrite("road_quad.png", vis)
cv2.imwrite("bev.png", bev)
print("Saved: road_quad.png, bev.png")
