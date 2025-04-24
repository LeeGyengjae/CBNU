import os
from PyQt5.QtWidgets import *
import sys

class BeepSound(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('삑 소리 내기 (macOS)')
        self.setGeometry(200, 200, 500, 100)
        
        shortBeepButton = QPushButton('짧게 삑', self)
        longBeepButton = QPushButton('길게 삑',self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다!', self)
        
        shortBeepButton.setGeometry(10, 10, 100, 30)
        longBeepButton.setGeometry(110, 10, 100, 30)
        quitButton.setGeometry(210, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 70)
        
        shortBeepButton.clicked.connect(self.shortBeepFunction)
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFunction)
        
    def shortBeepFunction(self):
        self.label.setText('짧게 삑 (say)')
        QApplication.processEvents()
        os.system('say "short beep"')
        
    def longBeepFunction(self):
        self.label.setText('길게 삑 (say)')
        QApplication.processEvents()
        os.system('say "long beep"')
        
    def quitFunction(self):
        self.close()

app = QApplication(sys.argv)
win = BeepSound()
win.show()
app.exec_()
