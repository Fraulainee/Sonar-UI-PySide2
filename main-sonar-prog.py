import sys, folium, io, os
import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QGraphicsDropShadowEffect  

# os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('/home/lab/Documents/sonar-gui/sonar_gui.ui', self)

        self.frame_4.setHidden(True)
        
        self.setup_map(37.7749, -122.4194)

        


    def setup_map(self, latitude, longitude):
        map = folium.Map(location=[latitude, longitude], zoom_start=18, tiles="OpenStreetMap")

        folium.Marker([latitude, longitude], popup=f"Lat: {latitude}, Lon: {longitude}").add_to(map)

        data = io.BytesIO()
        map.save(data, close_file=False)

        # Store WebView as an instance variable
        self.webview = QWebEngineView()
        self.webview.setHtml(data.getvalue().decode())

        mapwidget = self.findChild(QWidget, "mapwidget")
        if mapwidget:
            if mapwidget.layout() is None:
                layout = QVBoxLayout(mapwidget)
                mapwidget.setLayout(layout)
            mapwidget.layout().addWidget(self.webview)
            self.webview.show()
        else:
            print("Error: 'mapwidget' not found.")


        
class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()  
        uic.loadUi('/home/lab/Documents/sonar-gui/splash_art.ui', self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

    def progress(self):
        global counter
        self.progressBar.setValue(counter)
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

