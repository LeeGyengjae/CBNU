from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np
import sys
import os

class Panorama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파노라마 영상")
        self.setGeometry(200, 200, 700, 200)
        
        collectButton = QPushButton("영상 수집", self)
        self.showButton = QPushButton("영상 보기", self)
        self.stitchButton = QPushButton("봉합", self)
        self.saveButton = QPushButton('저장', self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다.', self)
        
        collectButton.setGeometry(10, 25, 100, 30)
        self.showButton.setGeometry(110, 25, 100, 30)
        self.stitchButton.setGeometry(210, 25, 100, 30)
        self.saveButton.setGeometry(310, 25, 100, 30)
        quitButton.setGeometry(450, 25, 100, 30)
        self.label.setGeometry(10, 70, 600, 170)
        
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        
        collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)
        self.stitchButton.clicked.connect(self.stitchFunction)
        self.saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)
        
    def collectFunction(self):
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.label.setText('c를 여러 번 눌러 수집하고 끝나면 q를 눌러 비디오를 끕니다.')

        self.cap = cv.VideoCapture(0)  # mac에서는 CAP_DSHOW 없이도 동작
        if not self.cap.isOpened():
            sys.exit('카메라 연결 실패')
        
        self.imgs = []
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            cv.imshow('video display', frame)

            key = cv.waitKey(1)
            if key == ord('c'):
                self.imgs.append(frame)
            elif key == ord('q'):
                self.cap.release()
                cv.destroyWindow('video display')
                break

        if len(self.imgs) >= 2:
            self.showButton.setEnabled(True)
            self.stitchButton.setEnabled(True)
            self.saveButton.setEnabled(True)

    def showFunction(self):
        self.label.setText(f'수집된 영상은 {len(self.imgs)}장입니다.')
        stack = cv.resize(self.imgs[0], dsize=(0, 0), fx=0.25, fy=0.25)
        for i in range(1, len(self.imgs)):
            resized = cv.resize(self.imgs[i], dsize=(0, 0), fx=0.25, fy=0.25)
            stack = np.hstack((stack, resized))
        cv.imshow('Image collection', stack)

    def stitchFunction(self):
        stitcher = cv.Stitcher_create()
        status, self.img_stitched = stitcher.stitch(self.imgs)
        if status == cv.Stitcher_OK:
            cv.imshow('Image stitched panorama', self.img_stitched)
        else:
            self.label.setText('파노라마 제작에 실패했습니다. 다시 시도하세요.')
            os.system('say "파노라마 제작 실패. 다시 시도하세요."')  # mac 음성 알림

    def saveFunction(self):
        fname, _ = QFileDialog.getSaveFileName(self, '파일 저장', './', "Images (*.png *.jpg)")
        if fname:
            cv.imwrite(fname, self.img_stitched)

    def quitFunction(self):
        if hasattr(self, 'cap'):
            self.cap.release()
        cv.destroyAllWindows()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Panorama()
    win.show()
    app.exec_()
