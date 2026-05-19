import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from ultralytics import YOLO

import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt

class CameraTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLOv8 Object Tracking with ID")
        self.setGeometry(100, 100, 800, 600)

        # YOLOv8 modelini yukle
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, "yolov8n.pt")
        self.model = YOLO(model_path)

        self.capture = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Kamera goruntu alani
        self.video_label = QLabel("Kamera Kapalı")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setStyleSheet("background-color: black; color: white; font-size: 25px; border: 2px solid gray;")
        self.video_label.setMinimumSize(640, 480)
        main_layout.addWidget(self.video_label)

        # Butonlar
        btn_layout = QHBoxLayout()

        self.btn_start = QPushButton("Kamerayı Başlat")
        self.btn_start.setStyleSheet("padding: 10px; font-size: 25px; background-color: #28a745; color: white; font-weight: bold;")
        self.btn_start.clicked.connect(self.start_camera)

        self.btn_stop = QPushButton("Kamerayı Durdur")
        self.btn_stop.setStyleSheet("padding: 10px; font-size: 25px; background-color: #dc3545; color: white; font-weight: bold;")
        self.btn_stop.clicked.connect(self.stop_camera)
        self.btn_stop.setEnabled(False)

        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        main_layout.addLayout(btn_layout)

    def start_camera(self):
        if not self.capture:
            self.capture = cv2.VideoCapture(0)
            
        if not self.capture.isOpened():
            self.video_label.setText("Hata: Kamera açılamadı")
            return

        self.timer.start(30) 
        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)

    def stop_camera(self):
        self.timer.stop()
        if self.capture:
            self.capture.release()
            self.capture = None
        
        self.video_label.clear()
        self.video_label.setText("Kamera Kapalı")
        self.btn_start.setEnabled(True)
        self.btn_stop.setEnabled(False)

    def update_frame(self):
        ret, frame = self.capture.read()
        if not ret:
            return

        results = self.model.track(frame, persist=True, verbose=False)

        annotated_frame = results[0].plot()

        rgb_image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        
        self.video_label.setPixmap(pixmap.scaled(self.video_label.width(), self.video_label.height(), Qt.KeepAspectRatio))

    def closeEvent(self, event):
        self.stop_camera()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraTrackerApp()
    window.show()
    sys.exit(app.exec_())
