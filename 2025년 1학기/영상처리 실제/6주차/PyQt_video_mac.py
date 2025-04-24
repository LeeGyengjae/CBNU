from PyQt5.QtWidgets import *
import sys
import cv2 as cv

class Video(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('비디오에서 프레임 수집')
        self.setGeometry(200, 200, 500, 100)

        videoButton = QPushButton('비디오 켜기', self)
        captureButton = QPushButton('프레임 잡기', self)
        saveButton = QPushButton('프레임 저장', self)
        quitButton = QPushButton('나가기', self)

        videoButton.setGeometry(10, 10, 100, 30)
        captureButton.setGeometry(110, 10, 110, 30)
        saveButton.setGeometry(210, 10, 100, 30)
        quitButton.setGeometry(310, 10, 100, 30)

        videoButton.clicked.connect(self.videoFunction)
        captureButton.clicked.connect(self.captureFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

        self.cap = None
        self.frame = None
        self.captureFrame = None

    def videoFunction(self):
        self.cap = cv.VideoCapture(0)  # mac에서는 CAP_AVFOUNDATION 사용 가능
        if not self.cap.isOpened():
            QMessageBox.warning(self, '오류', '카메라를 열 수 없습니다.')
            return

        while True:
            ret, self.frame = self.cap.read()
            if not ret:
                break
            cv.imshow('video display', self.frame)
            key = cv.waitKey(1)
            if key == ord('q'):
                break

    def captureFunction(self):
        if self.frame is not None:
            self.captureFrame = self.frame.copy()
            cv.imshow('Capture Frame', self.captureFrame)
        else:
            QMessageBox.information(self, '정보', '먼저 비디오를 실행해주세요.')

    def saveFunction(self):
        if self.captureFrame is not None:
            fname, _ = QFileDialog.getSaveFileName(self, '파일 저장', './frame.png', "Images (*.png *.jpg)")
            if fname:
                cv.imwrite(fname, self.captureFrame)
        else:
            QMessageBox.information(self, '정보', '먼저 프레임을 캡처하세요.')

    def quitFunction(self):
        if self.cap:
            self.cap.release()
        cv.destroyAllWindows()
        self.close()

app = QApplication(sys.argv)
win = Video()
win.show()
app.exec_()
