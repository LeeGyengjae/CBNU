import cv2

# 이미지 흑백으로 읽기
image = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

# 이미지 출력
cv2.imshow('Lenna', image)
cv2.waitKey(0)
cv2.destroyAllWindows()