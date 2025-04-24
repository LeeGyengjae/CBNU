import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
import sys

class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('사진 특수 효과')
        self.setGeometry(200, 200, 800, 200)
        
        pictureButton = QPushButton('사진 읽기', self)
        embossButton = QPushButton('엠보싱', self)
        cartoonButton = QPushButton('카툰', self)
        sketchButton = QPushButton('연필 스케치', self)
        oilButton = QPushButton('유화', self)
        saveButton = QPushButton('저장하기', self)
        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(['엠보싱', '카툰', '연필 스케치(명암)', '연필 스케치(컬러)', '유화'])
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다!', self)
        
        pictureButton.setGeometry(10, 10, 100, 30)
        embossButton.setGeometry(110, 10, 100, 30)
        cartoonButton.setGeometry(210, 10, 100, 30)
        sketchButton.setGeometry(310, 10, 100, 30)
        oilButton.setGeometry(410, 10, 100, 30)
        saveButton.setGeometry(510, 10, 100, 30)
        self.pickCombo.setGeometry(510, 40, 110, 30)
        quitButton.setGeometry(620, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 170)
        
        pictureButton.clicked.connect(self.pictureOpenFunction)
        embossButton.clicked.connect(self.embossFunction)
        cartoonButton.clicked.connect(self.cartoonFunction)
        sketchButton.clicked.connect(self.sketchFunction)
        oilButton.clicked.connect(self.oilFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

        # 이미지 변수 초기화
        self.img = None
        self.emboss = self.cartoon = self.sketch_gray = self.sketch_color = self.oil = None
        
    def pictureOpenFunction(self):
        fname, _ = QFileDialog.getOpenFileName(self, '사진 읽기', './')
        if not fname:
            return
        self.img = cv.imread(fname)
        if self.img is None:
            QMessageBox.warning(self, '에러', '이미지를 불러올 수 없습니다.')
            return
        cv.imshow('Painting', self.img)
        
    def embossFunction(self):
        if self.img is None:
            return
        femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)
        self.emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))
        cv.imshow('Emboss', self.emboss)
        
    def cartoonFunction(self):
        if self.img is None:
            return
        self.cartoon = cv.stylization(self.img, sigma_s=60, sigma_r=0.45)
        cv.imshow('Cartoon', self.cartoon)
    
    def sketchFunction(self):
        if self.img is None:
            return
        self.sketch_gray, self.sketch_color = cv.pencilSketch(self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
        cv.imshow('Pencil sketch (gray)', self.sketch_gray)
        cv.imshow('Pencil sketch (color)', self.sketch_color)
        
    def oilFunction(self):
        if self.img is None:
            return
        try:
            self.oil = cv.xphoto.oilPainting(self.img, 10, 1, cv.COLOR_BGR2Lab)
            cv.imshow('Oil Painting', self.oil)
        except AttributeError:
            QMessageBox.warning(self, '에러', 'oilPainting 함수 사용 불가: opencv-contrib-python이 설치되어야 합니다.')

    def saveFunction(self):
        fname, _ = QFileDialog.getSaveFileName(self, '파일 저장', './', "Images (*.png *.jpg)")
        if not fname:
            return
        i = self.pickCombo.currentIndex()
        try:
            if i == 0 and self.emboss is not None:
                cv.imwrite(fname, self.emboss)
            elif i == 1 and self.cartoon is not None:
                cv.imwrite(fname, self.cartoon)
            elif i == 2 and self.sketch_gray is not None:
                cv.imwrite(fname, self.sketch_gray)
            elif i == 3 and self.sketch_color is not None:
                cv.imwrite(fname, self.sketch_color)
            elif i == 4 and self.oil is not None:
                cv.imwrite(fname, self.oil)
            else:
                QMessageBox.information(self, '저장 실패', '해당 효과를 먼저 적용해주세요.')
        except Exception as e:
            QMessageBox.warning(self, '오류', f'파일 저장 중 오류 발생: {e}')
        
    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SpecialEffect()
    win.show()
    app.exec_()
