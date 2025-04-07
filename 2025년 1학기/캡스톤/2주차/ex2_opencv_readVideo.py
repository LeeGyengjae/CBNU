import cv2

# 동영상 파일 경로
video_path = "test_video.mp4"

# 동영상 파일을 읽기 위한 VideoCapture 객체 생성
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("동영상을 열 수 없습니다.")
    exit()

# 동영상 출력
while True:
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:
        print("동영상 출력이 완료되었습니다.")
        break

    # 프레임 표시
    cv2.imshow("Video", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()