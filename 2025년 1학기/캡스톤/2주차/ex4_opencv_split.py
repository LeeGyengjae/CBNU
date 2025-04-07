import cv2

# 이미지 읽기
image = cv2.imread('Lenna.png')

# 이미지를 B, G, R 성분으로 분리
b, g, r = cv2.split(image)

# 각 성분 출력
print("Blue Channel:\n", b)
print("Green Channel:\n", g)
print("Red Channel:\n", r)

# 성분 시각화(옵션)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

# 키 입력 대기 후 종료
cv2.waitKey(0)
cv2.destroyAllWindows()