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
        self.initUI()
        self.load_model()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        btn_layout = QHBoxLayout()

        self.btn_image = QPushButton("Resim Seç ")
        self.btn_image.clicked.connect(self.select_image)
        self.btn_image.setStyleSheet("padding: 10px; font-size: 25px; background-color: #28a745; color: white;")
        self.btn_image.setEnabled(False) 

        self.btn_3d = QPushButton("3D Model Oluştur")
        self.btn_3d.clicked.connect(self.generate_3d)
        self.btn_3d.setStyleSheet("padding: 10px; font-size: 25px; background-color: #007bff; color: white;")
        self.btn_3d.setEnabled(False)

        btn_layout.addWidget(self.btn_image)
        btn_layout.addWidget(self.btn_3d)
        main_layout.addLayout(btn_layout)

        self.info_label = QLabel("Model yükleniyor, lütfen bekleyin...")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("color: blue; font-weight: bold; margin: 10px; font-size: 25px;")
        main_layout.addWidget(self.info_label)

        img_display_layout = QHBoxLayout()

        self.lbl_original = QLabel("Orijinal Resim")
        self.lbl_original.setAlignment(Qt.AlignCenter)
        self.lbl_original.setStyleSheet("border: 2px solid gray; background-color: #f0f0f0; font-size: 25px;")
        img_display_layout.addWidget(self.lbl_original)

        self.lbl_processed = QLabel("Derinlik Haritası")
        self.lbl_processed.setAlignment(Qt.AlignCenter)
        self.lbl_processed.setStyleSheet("border: 2px solid #007bff; background-color: #f0f0f0; font-size: 25px;")
        img_display_layout.addWidget(self.lbl_processed)

        main_layout.addLayout(img_display_layout)

    def load_model(self):
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
            self.info_label.setText("İşleniyor...")
            QApplication.processEvents() 
            
            self.display_image(file_path, self.lbl_original)
            self.process_image()

    def process_image(self):
        if not hasattr(self, 'model') or not self.image_path:
            return

        img = cv2.imread(self.image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.rgb_img = img.copy()

        input_batch = self.transform(img).to('cpu')

        with torch.no_grad():
            prediction = self.model(input_batch)

            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=img.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()

        output = prediction.cpu().numpy()
        self.raw_depth = output.copy() 

        output = cv2.normalize(output, None, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        output_colored = cv2.applyColorMap(output, cv2.COLORMAP_INFERNO)

        self.display_image_from_array(output_colored, self.lbl_processed)
        self.info_label.setText("İşlem Başarıyla Tamamlandı")
        self.btn_3d.setEnabled(True) 

    def display_image(self, path, label):
        pixmap = QPixmap(path)
        scaled_pixmap = pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

    def display_image_from_array(self, img_array, label):
        
        rgb_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

    def generate_3d(self):
        if not hasattr(self, 'raw_depth') or not hasattr(self, 'rgb_img'):
            return
            
        import open3d as o3d
        
        self.info_label.setText("3D Model oluşturuluyor...")
        QApplication.processEvents()

        color_img = self.rgb_img
        depth_img = self.raw_depth

       
        depth_img = depth_img - depth_img.min() + 1.0 
        
        
        o3d_color = o3d.geometry.Image(color_img)
        o3d_depth = o3d.geometry.Image(depth_img.astype(np.float32))

        
        rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
            o3d_color, o3d_depth, depth_scale=20.0, depth_trunc=1000.0, convert_rgb_to_intensity=False)

        
        h, w, _ = color_img.shape
        fx = fy = max(w, h)
        cx = w / 2
        cy = h / 2
        intrinsic = o3d.camera.PinholeCameraIntrinsic(w, h, fx, fy, cx, cy)

        
        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsic)
        
       
        pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

        self.info_label.setText("3D Model hazır! ")
        
        
        o3d.visualization.draw_geometries([pcd], window_name="3D Depth Viewer", width=800, height=600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DepthEstimationApp()
    window.show()
    sys.exit(app.exec_())
