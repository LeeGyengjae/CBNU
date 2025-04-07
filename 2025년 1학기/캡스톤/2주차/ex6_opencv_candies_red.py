import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread("Candies.png")

# 이미지 채널 분리
b, g, r = cv2.split(image)

# Red 성분이 50 이상인 영역 마스크 생성
red_mask = cv2.inRange(r, 200, 255)

# 원본 이미지에서 Red 성분이 50 이상인 색만 추출
red_highlighted = cv2.bitwise_and(image, image, mask=red_mask)

# 결과 출력
cv2.imshow("Original Image", image)
cv2.imshow("Red Highlighted", red_highlighted)

# 종료 키
cv2.waitKey(0)
cv2.destroyAllWindows()