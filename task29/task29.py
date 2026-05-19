import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class SpectralSimulationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multispektral Kamera Simülasyonu")
        self.setGeometry(100, 100, 1000, 700)
        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        self.btn_select = QPushButton("Görsel Seç")
        self.btn_select.setStyleSheet("padding: 10px; font-size: 25px; background-color: #28a745; color: white; font-weight: bold;")
        self.btn_select.clicked.connect(self.load_image)
        main_layout.addWidget(self.btn_select)

        # 1. Satır: Orijinal ve NDVI
        row1_layout = QHBoxLayout()
        self.lbl_original = self.create_label("Orijinal (RGB)")
        self.lbl_ndvi = self.create_label("Sahte NDVI (Bitki İndeksi)")
        row1_layout.addWidget(self.lbl_original)
        row1_layout.addWidget(self.lbl_ndvi)
        main_layout.addLayout(row1_layout)

        # 2. Satır: Bantlar (Red, Green, Blue)
        row2_layout = QHBoxLayout()
        self.lbl_red = self.create_label("Band 1 (Kırmızı)")
        self.lbl_green = self.create_label("Band 2 (Yeşil)")
        self.lbl_blue = self.create_label("Band 3 (Mavi)")
        
        row2_layout.addWidget(self.lbl_red)
        row2_layout.addWidget(self.lbl_green)
        row2_layout.addWidget(self.lbl_blue)
        main_layout.addLayout(row2_layout)

    def create_label(self, text):
        lbl = QLabel(text)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("border: 1px solid gray; background-color: #f0f0f0; font-weight: bold; font-size: 25px;")
        return lbl

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Görsel Seç", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        # Resmi Oku
        img = cv2.imread(file_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 1. Orijinal Görüntü
        self.display_image(self.lbl_original, img_rgb, "Orijinal (RGB)")

        # Görüntüyü Kanallara (Bantlara) Ayır
        b, g, r = cv2.split(img)

        # 2. Bant 1, 2, 3 (Multispektral kameralar her dalga boyunu ayrı kaydeder)
        self.display_image(self.lbl_red, r, "Band 1 (Red)", is_gray=True)
        self.display_image(self.lbl_green, g, "Band 2 (Green)", is_gray=True)
        self.display_image(self.lbl_blue, b, "Band 3 (Blue)", is_gray=True)

        # 3. Sahte NDVI (Normalized Difference Vegetation Index) Hesaplama
        # Gerçek multispektral kameralarda NIR (Kızılötesi) bandı olur. 
        # Formül: (NIR - Red) / (NIR + Red)
        # Burada simülasyon için NIR yerine Green kullanıyoruz: (Green - Red) / (Green + Red)
        g_float = g.astype(np.float32)
        r_float = r.astype(np.float32)
        
        # Sıfıra bölünmeyi engellemek için küçük bir değer ekliyoruz
        ndvi = (g_float - r_float) / (g_float + r_float + 1e-5)
        
        # NDVI değerlerini 0-255 arasına normalize edip renklendiriyoruz
        ndvi_normalized = cv2.normalize(ndvi, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        ndvi_colored = cv2.applyColorMap(ndvi_normalized, cv2.COLORMAP_SUMMER)
        
        self.display_image(self.lbl_ndvi, cv2.cvtColor(ndvi_colored, cv2.COLOR_BGR2RGB), "Sahte NDVI İndeksi")

    def display_image(self, label, img_data, title, is_gray=False):
        h, w = img_data.shape[:2]
        if is_gray:
            bytes_per_line = w
            q_img = QImage(img_data.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        else:
            bytes_per_line = 3 * w
            q_img = QImage(img_data.data, w, h, bytes_per_line, QImage.Format_RGB888)
            
        pixmap = QPixmap.fromImage(q_img)
        label.setPixmap(pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio))
        label.setText("") 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpectralSimulationApp()
    window.show()
    sys.exit(app.exec_())

"""
=============================================================================
AÇIKLAMA: Multispektral ve Hiperspektral Kameralar
=============================================================================
1. Multispektral Kameralar:
   - İnsan gözü sadece 3 renk (Kırmızı, Yeşil, Mavi) görür.
   - Multispektral kameralar genellikle 3 ila 15 arasında geniş bant yakalar.
   - Örnek: RGB + Near Infrared (NIR - Yakın Kızılötesi) + Red Edge.
   - Kullanım Alanı: Tarımda bitki sağlığını (NDVI indeksi) ölçmek için kullanılır.

2. Hiperspektral Kameralar:
   - 100 ile 200 arasında çok dar ve sürekli spektral bant yakalar.
   - Her bir piksel için tam bir elektromanyetik spektrum çıkarır (Işığın parmak izi).
   - Kullanım Alanı: Mineralleri tespit etmek, kimyasal sızıntıları bulmak veya 
     gözle aynı renkte görünen iki farklı materyali birbirinden ayırmak için kullanılır.

Bu Python kodunda:
Gözümüzün gördüğü tek bir fotoğrafın aslında farklı "bantlardan" oluştuğunu 
(Red, Green, Blue) gösteriyoruz ve Multispektral kameraların bitkileri 
nasıl analiz ettiğini anlatan sahte bir NDVI indeksi (Renk Haritası) üretiyoruz.
=============================================================================
"""
