import cv2
import numpy as np

# 이미지 읽기 (grayscale로 읽음)
image = cv2.imread('mountain.jpg', cv2.IMREAD_GRAYSCALE)

# 평균값 필터 적용
# 커널 크기 (5x5)로 설정
kernel_size = (5, 5)
avg_filtered = cv2.blur(image, kernel_size)

# 샤프닝 필터 생성 및 적용
# 3x3 샤프닝 커널 정의
sharpening_kernel = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, sharpening_kernel)

# 라플라시안 필터 적용
laplacian_filtered = cv2.Laplacian(image, cv2.CV_64F)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Average Filter', avg_filtered)
cv2.imshow('Sharpening Filter', sharpened)
cv2.imshow('Laplacian Filter', np.uint8(np.absolute(laplacian_filtered)))

# 키 입력 대기 및 종료
cv2.waitKey(0)
cv2.destroyAllWindows()