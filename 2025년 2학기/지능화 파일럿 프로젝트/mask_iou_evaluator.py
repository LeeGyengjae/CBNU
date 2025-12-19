# mask_iou_evaluator.py
import cv2
import numpy as np

pred = cv2.imread("pred_mask.png", cv2.IMREAD_GRAYSCALE)
gt = cv2.imread("gt_mask.png", cv2.IMREAD_GRAYSCALE)
if pred is None or gt is None:
    raise FileNotFoundError("pred_mask.png and gt_mask.png required")

# 이진화(0/255)
_, pred_b = cv2.threshold(pred, 127, 1, cv2.THRESH_BINARY)
_, gt_b = cv2.threshold(gt, 127, 1, cv2.THRESH_BINARY)

intersection = int(np.sum((pred_b == 1) & (gt_b == 1)))
union = int(np.sum((pred_b == 1) | (gt_b == 1)))

iou = intersection / union if union > 0 else 0.0
precision = intersection / max(int(np.sum(pred_b == 1)), 1)
recall = intersection / max(int(np.sum(gt_b == 1)), 1)

print(f"Intersection={intersection}, Union={union}")
print(f"IoU={iou:.4f}, Precision={precision:.4f}, Recall={recall:.4f}")
