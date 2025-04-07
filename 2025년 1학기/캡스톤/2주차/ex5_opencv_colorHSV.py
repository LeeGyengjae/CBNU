import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('Lenna.png')

# BGR 이미지를 HSV로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV 성분 분리하기
h, s, v = cv2.split(hsv_image)

# 각각의 성분을 출력
print("Hue Component:")
print(h)
print("\nSaturation Component:")
print(s)
print("\nValue Component:")
print(v)

# 결과를 시각적으로 확인하기 위해 각 성분을 이미지로 보여줌
cv2.imshow('Hue', h)
cv2.imshow('Saturation', s)
cv2.imshow('Value', v)

cv2.waitKey(0)
cv2.destroyAllWindows()