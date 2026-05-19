# Bilgisayarlı Görü ve Derin Öğrenme Staj Projeleri
### Computer Vision and Deep Learning Internship Portfolio

Bu depo (repository), stajım kapsamında hazırladığım **30 adet Bilgisayarlı Görü (Computer Vision) ve Derin Öğrenme (Deep Learning)** görevini ve projelerini içermektedir.

Bu projeler; temel görüntü işleme algoritmalarından başlayarak nesne tespiti (YOLOv5/v8), derinlik tahmini, 3D bulut nokta üretimi (Point Cloud), nesne takibi (Tracking), optik karakter tanıma (OCR) ve Vision Transformers (ViT) gibi modern derin öğrenme mimarilerine kadar geniş bir yelpazeyi kapsamaktadır.

---

## 🛠️ Kullanılan Teknolojiler (Technologies Used)
* **Programlama Dili:** Python 3.11
* **Görüntü İşleme:** OpenCV (Open Source Computer Vision Library)
* **Derin Öğrenme / Frameworkler:** PyTorch, Ultralytics (YOLOv8), Timm (ViT)
* **Karakter Tanıma:** EasyOCR
* **3D İşleme:** Open3D
* **Arayüz Geliştirme (GUI):** PyQt5
* **Sürüm Kontrolü:** Git & Git LFS (Large File Storage)

---

## 📋 Görev Listesi (Tasks Table)

Aşağıda depoda bulunan tüm görevlerin listesi, açıklamaları ve kullanılan yöntemler yer almaktadır:

| # | Görev / Proje (Task) | Açıklama (Description) | Kullanılan Kütüphaneler & Yöntemler |
| :---: | :--- | :--- | :--- |
| **1** | `task1` | Görsel okuma, ekranda gösterme ve kaydetme işlemleri. | `cv2.imread`, `cv2.imshow`, `cv2.imwrite` |
| **2** | `task2` | Görselleri BGR renk uzayından Grayscale (Gri ton) seviyesine dönüştürme. | `cv2.cvtColor`, `cv2.COLOR_BGR2GRAY` |
| **3** | `task3` | Görsel boyutlandırma (Resize) ve ilgi alanı (ROI) kırpma işlemleri. | `cv2.resize`, ROI Slicing |
| **4** | `task4` | Görsel üzerine geometrik şekiller (dikdörtgen, çizgi) ve metin çizme. | `cv2.rectangle`, `cv2.line`, `cv2.putText` |
| **5** | `task5` | Görüntü yumuşatma ve parazit azaltma (Gaussian Blur) uygulaması. | `cv2.GaussianBlur` |
| **6** | `task6` | Eşikleme (Binary Thresholding) ile nesne ve arka plan ayrımı. | `cv2.threshold`, `cv2.THRESH_BINARY` |
| **7** | `task7` | Madeni paraların tespiti ve havza (Watershed) segmentasyonu algoritması. | `cv2.watershed`, `cv2.connectedComponents` |
| **8** | `task8` | Canny algoritması ile kenar tespiti ve Harris Corner ile köşe tespiti. | `cv2.Canny`, `cv2.cornerHarris` |
| **9** | `task9` | Orijinal ve gri görsel dizilerinin (Array) boyut, piksel değer analizleri. | `numpy`, `shape`, `dtype` |
| **10** | `task10` | Aşındırma (Erosion), Yayma (Dilation) ve Açma (Opening) morfolojik işlemleri. | `cv2.morphologyEx`, `cv2.dilate`, `cv2.erode` |
| **11** | `task11` | Görseli dikey, yatay ve her iki eksende döndürme (Flipping) işlemleri. | `cv2.flip` |
| **12** | `task12` | Kameradan canlı video akışı alma ve kareleri gerçek zamanlı boyutlandırma. | `cv2.VideoCapture`, `cv2.resize` |
| **13** | `task13` | HSV renk uzayı maskelemesi ve kontur tespiti ile siyah nesne takibi. | `cv2.inRange`, `cv2.findContours` |
| **14** | `task14` | İnteraktif Trackbar'lar ile gerçek zamanlı HSV filtreleme arayüzü. | `cv2.createTrackbar`, `cv2.getTrackbarPos` |
| **15** | `task15` | Kayıtlı bir videoda kontur analizi ile beyaz renkli nesnelerin takibi. | `cv2.findContours`, `cv2.contourArea` |
| **16** | `task16` | Evrişimli Sinir Ağları (CNN) mimarilerinin teorik analizi ve DNN modülü. | `cv2.dnn` teorisi |
| **17** | `task17` | YOLOv3 mimarisi ve OpenCV DNN kullanarak nesne tespiti uygulaması. | `cv2.dnn.readNetFromDarknet`, YOLOv3 |
| **18** | `task18` | YOLOv4 ağırlık dosyaları ile nesne tespiti uygulaması. | `cv2.dnn.readNet`, YOLOv4 |
| **19** | `task19` | YOLOv5 mimarisi ile nesne tespiti ve performans incelemesi. | `torch.hub`, YOLOv5 |
| **20** | `task20` | Roboflow veri seti ile el tespiti (Hand Detection) için YOLOv5 eğitimi. | `yolov5`, Custom Training |
| **21** | `task21` | Özel eğitilmiş modelin performans metrikleri (F1, PR, Karmaşıklık Matrisi). | PR Curve, Confusion Matrix analizi |
| **22** | `task22` | YOLOv8 nesne segmentasyonu (Object Segmentation) modeli uygulaması. | `ultralytics`, YOLOv8-seg |
| **23** | `task23` | PyQt5 arayüzü üzerinden YOLOv8-seg modeli ile görsel segmentasyon uygulaması. | PyQt5, YOLOv8 Segmentasyon |
| **24** | `task24` | MiDaS derin öğrenme modeli ile PyQt5 üzerinden derinlik tahmini (Depth Estimation). | PyQt5, PyTorch, MiDaS |
| **25** | `task25` | Derinlik haritasından Open3D kütüphanesi ile 3D Nokta Bulutu (Point Cloud) üretimi. | Open3D, `o3d.geometry.PointCloud` |
| **26** | `task26` | YOLOv8 modeli ile gerçek zamanlı kamera akışında kimlikli nesne takibi (Tracking). | PyQt5, `model.track` (ByteTrack) |
| **27** | `task27` | EasyOCR kütüphanesi kullanarak görsellerden metin okuyan PyQt5 OCR uygulaması. | PyQt5, `easyocr` |
| **28** | `task28` | YOLOv5 PyTorch model ağırlıklarının (.pt) ONNX (.onnx) formatına dönüştürülmesi. | ONNX Export |
| **29** | `task29` | Multispektral kamera simülasyonu ve görsel üzerinden NDVI bitki indeksi hesabı. | PyQt5, Band splitting, NDVI |
| **30** | `task30` | Vision Transformers (ViT) mimarisi çalışma prensibi ve teknik raporu. | ViT_Rapor.md (Teknik Rapor) |

---

## 🚀 Projelerin Çalıştırılması (How to Run)

Herhangi bir görevi çalıştırmak için ilgili klasöre gidip Python betiğini çalıştırmanız yeterlidir.

Örnek (Görsel Segmentasyon Uygulaması):
```bash
python task23/task23.py
```

Örnek (Metin Okuyucu OCR Uygulaması):
```bash
python task27/task27.py
```

---
**Sami Awawda**  
*Bilgisayar Mühendisliği Stajyeri / Computer Engineering Intern*  
