import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('candies.png')

# BGR에서 HSV로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV에서 붉은색의 범위 정의
# 붉은색은 HSV에서 두 영역에 걸쳐 있음: [0~10]과 [170~180]
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([180, 255, 255])

# 두 범위에 해당하는 마스크 생성
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# 두 마스크 합치기
red_mask = cv2.bitwise_or(mask1, mask2)

# 원본 이미지와 마스크를 통해 붉은색만 추출
red_only = cv2.bitwise_and(image, image, mask=red_mask)

# 결과 보여주기
cv2.imshow('Original Image', image)
cv2.imshow('Red Mask', red_mask)
cv2.imshow('Red Only', red_only)

# 키 입력 대기 및 종료
cv2.waitKey(0)
cv2.destroyAllWindows()