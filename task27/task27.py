import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import easyocr

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class OCRApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optik Karakter Tanıma (OCR)")
        self.setGeometry(100, 100, 900, 600)

        self.reader = easyocr.Reader(['tr', 'en'], gpu=False)

        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        self.btn_select = QPushButton("Görsel Seç")
        self.btn_select.setStyleSheet("padding: 10px; font-size: 25px; background-color: #007bff; color: white;")
        self.btn_select.clicked.connect(self.select_image)
        main_layout.addWidget(self.btn_select)

        display_layout = QHBoxLayout()

        self.image_label = QLabel("Seçilen görsel burada gösterilecektir")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 2px dashed gray; background-color: #f8f9fa;  font-size: 25px")
        display_layout.addWidget(self.image_label)

        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_display.setPlaceholderText("Okunan metin bu alanda gösterilecektir")
        self.text_display.setStyleSheet("font-size: 25px; padding: 10px; border: 2px solid #28a745; ")
        display_layout.addWidget(self.text_display)

        main_layout.addLayout(display_layout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Görsel Seç", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)

            self.extract_text(file_path)

    def extract_text(self, image_path):
        self.text_display.setText("Görsel işleniyor, lütfen bekleyin")
        QApplication.processEvents()

        try:
            result = self.reader.readtext(image_path, detail=0)
            extracted_text = "\n".join(result)
            
            if extracted_text.strip():
                self.text_display.setText(extracted_text)
            else:
                self.text_display.setText("Görselde herhangi bir metin tespit edilemedi")
        except Exception as e:
            self.text_display.setText(f"Hata oluştu: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCRApp()
    window.show()
    sys.exit(app.exec_())
