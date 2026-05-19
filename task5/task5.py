import cv2

img = cv2.imread('images/car.jpg')

roi = img[70:310, 30:570]
gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

blurred_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

blurred_roi_bgr = cv2.cvtColor(blurred_roi, cv2.COLOR_GRAY2BGR)
img[70:310, 30:570] = blurred_roi_bgr

cv2.imshow('Blurred Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""  GÖREVİ (Gerçek Hayatta Kullanım Alanları)

Kare içine alınıp griye çevrilen ve bulanıklaştırılan (blur) bu işlemlerin gerçek hayatta iki temel kullanım alanı vardır:

1. Gizlilik ve Güvenlik (Günlük Hayat):
   Özellikle Google Street View, Yandex Haritalar gibi uygulamalarda araç plakalarının ve insan yüzlerinin sansürlenmesinde kullanılır. Ayrıca haber bültenlerinde veya videolarda kimliği gizlenmek istenen kişilerin yüzleri bu yöntemle bulanıklaştırılır.

2. Görüntü İşleme ve Yapay Zeka (Teknik Boyut):
   Yapay zeka modellerine (örneğin plaka tanıma, yüz tanıma veya OCR - optik karakter tanıma sistemleri) görüntü verilmeden önce bir 'ön işleme' (preprocessing) adımı olarak kullanılır. 
   - Griye çevirmek: Renk kanallarını 3'ten 1'e düşürerek veri boyutunu küçültür ve işlem hızını artırır.
   - Bulanıklaştırmak (Blur): Görüntüdeki parazitleri (noise) ve gereksiz detayları azaltarak, yapay zekanın sadece temel hatlara odaklanmasını ve daha doğru çalışmasını sağlar.

"""