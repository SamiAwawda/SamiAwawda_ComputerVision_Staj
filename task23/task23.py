import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from ultralytics import YOLO

import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                             QFileDialog, QVBoxLayout, QHBoxLayout, QWidget)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class SegmentationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLOv8 Semantic Segmentation Viewer")
        self.setGeometry(100, 100, 1200, 700)

        self.model = None
        self.model_path = ""
        self.image_path = ""

        self.initUI()

    def initUI(self):
        # Main Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Buttons Layout
        btn_layout = QHBoxLayout()
        self.btn_model = QPushButton("Model Seç (.pt)")
        self.btn_model.clicked.connect(self.select_model)
        self.btn_model.setStyleSheet("padding: 10px; font-size: 25px;")

        self.btn_image = QPushButton("Resim Seç")
        self.btn_image.clicked.connect(self.select_image)
        self.btn_image.setStyleSheet("padding: 10px; font-size: 25px;")

        btn_layout.addWidget(self.btn_model)
        btn_layout.addWidget(self.btn_image)
        main_layout.addLayout(btn_layout)

        # Info Label
        self.info_label = QLabel("Lütfen önce bir model, sonra bir resim seçin.")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("color: blue; font-weight: bold; margin: 10px; font-size: 25px;")
        main_layout.addWidget(self.info_label)

        # Images Display Layout
        img_display_layout = QHBoxLayout()

        # Original Image
        self.lbl_original = QLabel("Orijinal Resim")
        self.lbl_original.setAlignment(Qt.AlignCenter)
        self.lbl_original.setStyleSheet("border: 2px solid gray; background-color: #f0f0f0; font-size: 25px;")
        img_display_layout.addWidget(self.lbl_original)

        # Processed Image
        self.lbl_processed = QLabel("İşlenmiş (Segmentasyon)")
        self.lbl_processed.setAlignment(Qt.AlignCenter)
        self.lbl_processed.setStyleSheet("border: 2px solid green; background-color: #f0f0f0; font-size: 25px;")
        img_display_layout.addWidget(self.lbl_processed)

        main_layout.addLayout(img_display_layout)

    def select_model(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Model Dosyası Seç", "", "PyTorch Model (*.pt)")
        if file_path:
            self.model_path = file_path
            self.model = YOLO(file_path)
            if self.image_path:
                self.process_image()

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.display_image(file_path, self.lbl_original)
            if self.model:
                self.process_image()

    def process_image(self):
        if not self.model or not self.image_path:
            return

        results = self.model(self.image_path)
        
        processed_img = results[0].plot(boxes=False)
        
        self.display_image_from_array(processed_img, self.lbl_processed)

    def display_image(self, path, label):
        pixmap = QPixmap(path)
        scaled_pixmap = pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

    def display_image_from_array(self, img_array, label):
        # Convert BGR to RGB
        rgb_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SegmentationApp()
    window.show()
    sys.exit(app.exec_())
