import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "best.pt")

if not os.path.exists(model_path):
    print(f"Model su yolda bulunamadi: {model_path}")
    exit()

print(".pt formatindaki model yukleniyor ve ONNX formatina donusturuluyor...")
print("Bu islem biraz zaman alabilir, lutfen bekleyin...")

# YOLOv5 dosyalarını indiriyoruz (eski model oldugu icin)
yolov5_dir = os.path.join(current_dir, "yolov5")
export_script = os.path.join(yolov5_dir, "export.py")

if not os.path.exists(yolov5_dir):
    print("YOLOv5 deposu indiriliyor...")
    subprocess.run(f"git clone https://github.com/ultralytics/yolov5 \"{yolov5_dir}\"", shell=True)
    
    # Windows'ta egitilmis modeli Linux'ta egitilmis gibi acmak icin kod ekliyoruz (PosixPath hatasi cozumu)
    if os.path.exists(export_script):
        with open(export_script, 'r', encoding='utf-8') as f:
            content = f.read()
        if "pathlib.PosixPath = pathlib.WindowsPath" not in content:
            content = content.replace("from pathlib import Path", "from pathlib import Path\nimport pathlib\npathlib.PosixPath = pathlib.WindowsPath\n")
            with open(export_script, 'w', encoding='utf-8') as f:
                f.write(content)

# İndirilen export.py dosyasını çalıştırıyoruz
command = f"python \"{export_script}\" --weights \"{model_path}\" --include onnx"

try:
    print("Donusturme basladi...")
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print("Donusturme basarili 'best.onnx' dosyasi olusturuldu.")
except subprocess.CalledProcessError as e:
    print("Donusturme sirasinda hata olustu:")
    print(e.stderr)

print("Artik model daha hafif ve PyTorch olmadan herhangi bir ortamda calistirilabilir!")

"""
=============================================================================
AÇIKLAMALAR VE FARKLAR (.pt vs .onnx)
=============================================================================

NOT: Bu kodda YOLOv5 deposunu (repository) internetten indirmemizin sebebi, 
PyTorch'un (.pt) modeli ONNX'e dönüştürebilmesi için modelin orijinal mimari 
kodlarına (models/yolo.py) ihtiyaç duymasıdır. Eğer model YOLOv8 ile eğitilmiş 
olsaydı, ultralytics kütüphanesi zaten yüklü olduğu için ekstra dosya 
indirmeden sadece 3 satır kodla dönüştürme yapılabilirdi.

--- .pt ve .onnx Formatlarının Farkları ---

1. .pt (PyTorch Formatı):
   - PyTorch kütüphanesine özeldir. Sadece PyTorch olan ortamlarda çalışır.
   - Modeli eğitmeye veya eğitime kaldığı yerden devam etmeye uygundur.
   - Çalıştırmak için PyTorch kütüphanesinin ve modelin orijinal mimari 
     kodlarının (örneğin YOLOv5 klasörü) ortamda bulunması şarttır.
   - Boyutu daha büyüktür ve çalışması nispeten daha ağırdır.

2. .onnx (Open Neural Network Exchange):
   - Evrensel ve açık kaynaklı bir sinir ağı formatıdır (Belgelerdeki PDF gibi).
   - Eğitimi bitmiş modelleri hızlıca kullanmak (Inference) için tasarlanmıştır.
   - PyTorch'a bağımlı değildir! C++, Java, JavaScript (Web tarayıcısı), Mobil 
     (iOS/Android) ve OpenCV gibi platformlarda kendi başına çalıştırılabilir.
   - Mimari kod dosyalarına ihtiyaç duymaz, çünkü mimariyi kendi içinde barındırır. 
     Üretim (Production) aşamasında çok daha optimize ve hızlı çalışır.
=============================================================================
"""
