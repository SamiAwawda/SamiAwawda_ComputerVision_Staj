import cv2


img = cv2.imread('images/yaprak.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresholded_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Leaf', img)
cv2.imshow('Threshold Leaf', thresholded_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""   GÖREVİ: Thresholding Nedir ve Nerelerde Kullanılır? 

1. Thresholding (Eşikleme) Nedir?
Thresholding, görüntü işlemede kullanılan en temel "bölütleme" (segmentasyon) tekniğidir. Temel amacı, ilgilenilen nesneyi (ön plan) arka plandan ayırmaktır. Genellikle gri tonlamalı (grayscale) bir görüntü üzerinde uygulanır.
Belirli bir "eşik değeri" (threshold) belirlenir; pikselin renk değeri bu eşiğin altındaysa siyah (0), üstündeyse beyaz (255) veya tam tersi olacak şekilde değiştirilir. Sonuç olarak, sadece siyah ve beyazdan oluşan "ikili" (binary) bir görüntü elde edilir.

2. Hangi Alanlarda Kullanılır?
Görüntüdeki nesneleri belirginleştirmek için birçok farklı sektörde kullanılır:

- Belge Tarama ve OCR (Optik Karakter Tanıma): Tarayıcı uygulamalarında (örneğin CamScanner), kağıdın arka planını bembeyaz, yazıları ise simsiyah yaparak metnin bilgisayar tarafından okunmasını (OCR) sağlar.
- Tıbbi Görüntüleme: Röntgen, MR veya tomografi görüntülerinde tümörleri, kemikleri veya kan damarlarını diğer dokulardan ayırmak için kullanılır.
- Endüstriyel Kalite Kontrol: Fabrika üretim hatlarında, ürünlerin üzerindeki çizik, leke veya üretim hatalarını tespit etmek amacıyla kameralı sistemlerde kullanılır.
"""