import cv2

# 비디오 파일 읽기
cap = cv2.VideoCapture('test_video.mp4')

# 비디오 파일이 열렸는지 확인
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# 비디오 프레임을 읽고 출력
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 모든 창 닫기
cap.release()
cv2.destroyAllWindows()