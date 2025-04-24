import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
import sys

class VideoSpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('비디오 특수 효과')
        self.setGeometry(200, 200, 400, 100)
        
        videoButton = QPushButton('비디오 시작', self)
        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(['엠보싱', '카툰', '연필 스케치(명암)', '연필 스케치(컬러)', '유화'])
        quitButton = QPushButton('나가기', self)
        
        videoButton.setGeometry(10, 10, 140, 30)
        self.pickCombo.setGeometry(150, 10, 110, 30)
        quitButton.setGeometry(280, 10, 100, 30)
        
        videoButton.clicked.connect(self.videoSpecialEffectFunction)
        quitButton.clicked.connect(self.quitFunction)

        self.cap = None  # 나가기 전에 확인용
        
    def videoSpecialEffectFunction(self):
        self.cap = cv.VideoCapture(0)  # ✅ mac에서는 CAP_DSHOW 제거
        if not self.cap.isOpened():
            QMessageBox.critical(self, '오류', '카메라 연결 실패')
            return
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            pick_effect = self.pickCombo.currentIndex()
            special_img = frame.copy()
            
            try:
                if pick_effect == 0:  # 엠보싱
                    femboss = np.array([[-1.0, 0.0, 0.0],
                                        [0.0, 0.0, 0.0],
                                        [0.0, 0.0, 1.0]])
                    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                    gray16 = np.int16(gray)
                    special_img = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))
                elif pick_effect == 1:  # 카툰
                    special_img = cv.stylization(frame, sigma_s=60, sigma_r=0.45)
                elif pick_effect == 2:  # 연필 스케치 (명암)
                    gray_sketch, _ = cv.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
                    special_img = gray_sketch
                elif pick_effect == 3:  # 연필 스케치 (컬러)
                    _, color_sketch = cv.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
                    special_img = color_sketch
                elif pick_effect == 4:  # 유화
                    special_img = cv.xphoto.oilPainting(frame, 10, 1, cv.COLOR_BGR2Lab)
            except Exception as e:
                print(f"필터 적용 오류: {e}")
                special_img = frame

            cv.imshow('Special effect', special_img)
            key = cv.waitKey(1)
            if key == ord('q'):
                break

        self.cap.release()
        cv.destroyAllWindows()

    def quitFunction(self):
        if self.cap:
            self.cap.release()
        cv.destroyAllWindows()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = VideoSpecialEffect()
    win.show()
    app.exec_()
