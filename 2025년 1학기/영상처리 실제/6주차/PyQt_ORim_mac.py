import cv2 as cv
import numpy as np
import sys
from PyQt5.QtWidgets import *

class Orim(QMainWindow):  # ✅ QMianWindow -> QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle('오림')
        self.setGeometry(200, 200, 700, 200)

        fileButton = QPushButton('파일', self)
        paintButton = QPushButton('페인팅', self)
        cutButton = QPushButton('오림', self)
        incButton = QPushButton('+', self)
        decButton = QPushButton('-', self)
        saveButton = QPushButton('저장', self)
        quitButton = QPushButton('나가기', self)

        fileButton.setGeometry(10, 10, 100, 30)
        paintButton.setGeometry(110, 10, 100, 30)
        cutButton.setGeometry(210, 10, 100, 30)
        incButton.setGeometry(310, 10, 50, 30)
        decButton.setGeometry(360, 10, 50, 30)
        saveButton.setGeometry(410, 10, 100, 30)
        quitButton.setGeometry(510, 10, 100, 30)

        fileButton.clicked.connect(self.fileOpenFunction)
        paintButton.clicked.connect(self.paintFunction)
        cutButton.clicked.connect(self.cutFunction)
        incButton.clicked.connect(self.incFunction)
        decButton.clicked.connect(self.decFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

        self.BrushSiz = 5
        self.LColor, self.RColor = (255, 0, 0), (0, 0, 255)
        self.img = None
        self.img_show = None
        self.mask = None
        self.grabImg = None

    def fileOpenFunction(self):
        fname, _ = QFileDialog.getOpenFileName(self, '파일 열기', './')
        if not fname:
            return
        self.img = cv.imread(fname)
        if self.img is None:
            QMessageBox.critical(self, '에러', '이미지를 불러올 수 없습니다.')
            return

        self.img_show = np.copy(self.img)
        cv.imshow('Painting', self.img_show)

        self.mask = np.zeros((self.img.shape[0], self.img.shape[1]), np.uint8)
        self.mask[:, :] = cv.GC_PR_BGD

    def paintFunction(self):
        if self.img_show is None:
            QMessageBox.information(self, '정보', '먼저 이미지를 불러오세요.')
            return
        cv.setMouseCallback('Painting', self.painting)

    def painting(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            cv.circle(self.img_show, (x, y), self.BrushSiz, self.LColor, -1)
            cv.circle(self.mask, (x, y), self.BrushSiz, cv.GC_FGD, -1)
        elif event == cv.EVENT_RBUTTONDOWN:
            cv.circle(self.img_show, (x, y), self.BrushSiz, self.RColor, -1)
            cv.circle(self.mask, (x, y), self.BrushSiz, cv.GC_BGD, -1)
        elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
            cv.circle(self.img_show, (x, y), self.BrushSiz, self.LColor, -1)
            cv.circle(self.mask, (x, y), self.BrushSiz, cv.GC_FGD, -1)
        elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
            cv.circle(self.img_show, (x, y), self.BrushSiz, self.RColor, -1)
            cv.circle(self.mask, (x, y), self.BrushSiz, cv.GC_BGD, -1)

        cv.imshow('Painting', self.img_show)

    def cutFunction(self):
        if self.img is None or self.mask is None:
            QMessageBox.information(self, '정보', '먼저 이미지와 마스크를 준비하세요.')
            return
        background = np.zeros((1, 65), np.float64)
        foreground = np.zeros((1, 65), np.float64)
        cv.grabCut(self.img, self.mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)
        mask2 = np.where((self.mask == 2) | (self.mask == 0), 0, 1).astype('uint8')
        self.grabImg = self.img * mask2[:, :, np.newaxis]
        cv.imshow('Scissoring', self.grabImg)

    def incFunction(self):
        self.BrushSiz = min(20, self.BrushSiz + 1)

    def decFunction(self):
        self.BrushSiz = max(1, self.BrushSiz - 1)

    def saveFunction(self):
        if self.grabImg is None:
            QMessageBox.information(self, '정보', '오림 결과가 없습니다.')
            return
        fname, _ = QFileDialog.getSaveFileName(self, '파일 저장', './cut_result.png', "Images (*.png *.jpg)")
        if fname:
            cv.imwrite(fname, self.grabImg)

    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Orim()
    win.show()
    app.exec_()
