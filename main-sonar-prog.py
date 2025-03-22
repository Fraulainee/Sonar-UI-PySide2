import sys, folium, io, os, time, tempfile
import resources_rc, get_gps
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QGraphicsDropShadowEffect  


counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('/home/lab/Documents/sonar-gui/sonar_gui.ui', self)

        self.webview = QWebEngineView()

        self.side_menu.setHidden(True)

        latitude, longitude = get_gps.read_gps_once()
        self.setup_map(latitude, longitude)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_map_with_gps)
        self.timer.start(10000)


    def update_map_with_gps(self):
        latitude, longitude = get_gps.read_gps_once()
        print(f"Latitude: {latitude}, Longitude: {longitude}")

        js = f"updateMarker({latitude}, {longitude});"
        self.webview.page().runJavaScript(js)

    def setup_map(self, latitude, longitude):
        self.latitude_label.setText(f"{latitude}")
        self.longitude_label.setText(f"{longitude}")

        map_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <title>Live Map</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="file:///home/lab/Documents/sonar-gui/assets/leaflet/leaflet.css"/>
            <script src="file:///home/lab/Documents/sonar-gui/assets/leaflet/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width: 100%; height: 100vh;"></div>
            <script>
                var map = L.map('map').setView([{latitude}, {longitude}], 18);
                L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                    attribution: 'Map data © OpenStreetMap contributors'
                }}).addTo(map);

                var marker = L.marker([{latitude}, {longitude}]).addTo(map);

                function updateMarker(lat, lon) {{
                    marker.setLatLng([lat, lon]);
                    map.panTo([lat, lon]);
                }}
            </script>
        </body>
        </html>
        """

        # Write HTML to a temporary file
        with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
            f.write(map_html)
            temp_file_path = f.name

        # Load it using setUrl instead of setHtml
        self.webview.load(QUrl.fromLocalFile(temp_file_path))

        mapwidget = self.findChild(QWidget, "mapwidget")
        if mapwidget:
            if mapwidget.layout() is None:
                layout = QVBoxLayout(mapwidget)
                mapwidget.setLayout(layout)
            mapwidget.layout().addWidget(self.webview)
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

