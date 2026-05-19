import sys
import os
import cv2
import numpy as np
import torch
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                             QFileDialog, QVBoxLayout, QHBoxLayout, QWidget)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class DepthEstimationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Depth Estimation V2 (MiDaS) Viewer")
        self.setGeometry(100, 100, 1200, 700)

        self.image_path = ""
        
        self.initUI()
        self.load_model()

    def initUI(self):
        # Main Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Buttons Layout
        btn_layout = QHBoxLayout()

        self.btn_image = QPushButton("Resim Seç")
        self.btn_image.clicked.connect(self.select_image)
        self.btn_image.setStyleSheet("padding: 10px; font-size: 25px; background-color: #28a745; color: white;")
        self.btn_image.setEnabled(False) # Disable until model loads

        btn_layout.addWidget(self.btn_image)
        main_layout.addLayout(btn_layout)

        # Info Label
        self.info_label = QLabel("Model yükleniyor, lütfen bekleyin...")
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
        self.lbl_processed = QLabel("Derinlik Haritası (Depth Map)")
        self.lbl_processed.setAlignment(Qt.AlignCenter)
        self.lbl_processed.setStyleSheet("border: 2px solid #007bff; background-color: #f0f0f0; font-size: 25px;")
        img_display_layout.addWidget(self.lbl_processed)

        main_layout.addLayout(img_display_layout)

    def load_model(self):
        # Using MiDaS v2.1 Small model for fast CPU inference
        try:
            self.model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small", trust_repo=True)
            self.model.eval()
            
            midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms", trust_repo=True)
            self.transform = midas_transforms.small_transform
            
            self.info_label.setText("Lütfen bir resim seçin.")
            self.info_label.setStyleSheet("color: green; font-weight: bold; font-size: 25px;")
            self.btn_image.setEnabled(True)
        except Exception as e:
            self.info_label.setText(f"Model yüklenirken hata oluştu: {e}")
            self.info_label.setStyleSheet("color: red; font-weight: bold; font-size: 25px;")

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.info_label.setText("İşleniyor...)")
            QApplication.processEvents() # Force UI update
            
            self.display_image(file_path, self.lbl_original)
            self.process_image()

    def process_image(self):
        if not hasattr(self, 'model') or not self.image_path:
            return

        # Read image
        img = cv2.imread(self.image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Apply transforms
        input_batch = self.transform(img).to('cpu')

        # Run model
        with torch.no_grad():
            prediction = self.model(input_batch)

            # Resize the prediction to match original image resolution
            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=img.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()

        # Convert to numpy array
        output = prediction.cpu().numpy()

        # Normalize the output to 0-255 for visualization
        output = cv2.normalize(output, None, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        # Apply a colormap (INFERNO gives a nice heat-map look for depth)
        output_colored = cv2.applyColorMap(output, cv2.COLORMAP_INFERNO)

        # Display processed image
        self.display_image_from_array(output_colored, self.lbl_processed)
        self.info_label.setText("İşlem Başarıyla Tamamlandı ")

    def display_image(self, path, label):
        pixmap = QPixmap(path)
        scaled_pixmap = pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

    def display_image_from_array(self, img_array, label):
        # Convert BGR to RGB (OpenCV uses BGR, QImage uses RGB)
        rgb_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DepthEstimationApp()
    window.show()
    sys.exit(app.exec_())
