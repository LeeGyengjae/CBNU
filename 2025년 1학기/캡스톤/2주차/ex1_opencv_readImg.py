import cv2

# 이미지 파일 읽기
image = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

# 이미지가 제대로 로드되었는지 확인
if image is None:
    print("Error: Could not load image. Please check the file path.")
else:
    # 이미지 출력하기
    cv2.imshow("Lenna", image)

    # 사용자가 키를 누를 때까지 이미지 창 열어두기
    cv2.waitKey(0)

    # 모든 창 닫기
    cv2.destroyAllWindows()