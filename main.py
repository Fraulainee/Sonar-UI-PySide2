import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui_splash_art import Ui_SplashScreen  
from ui_sonar_gui import Ui_MainWindow  

counter = 0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()

            self.main = MainWindow()
            self.main.show()

            self.close()
        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.show()  
    sys.exit(app.exec_())
