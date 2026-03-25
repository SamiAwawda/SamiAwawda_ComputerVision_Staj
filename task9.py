import cv2

img = cv2.imread('images/yaprak.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("Original Image Shape:", img.shape)
print("Grayscale Image Shape:", gray.shape)
print("Original Image Pixel [0,0]:", img[0,0])
print("Grayscale Image Pixel [0,0]:", gray[0,0])


# Orijinal görüntü 3 kanaldan (BGR) oluşur, bu yüzden boyutu (yükseklik, genişlik, 3) şeklindedir.
# Gri tonlamalı görüntü ise yalnızca tek kanaldan oluşur, bu yüzden boyutu (yükseklik, genişlik) şeklindedir.
# Orijinal görüntüde her piksel 3 değer içerirken, gri tonlamalı görüntüde her piksel yalnızca parlaklığı temsil eden tek bir değer içerir.
# Görüntünün gri tonlamaya dönüştürülmesi veri miktarını azaltır ve işlemleri daha hızlı ve kolay hale getirir.
# Bu nedenle gri görüntüler edge detection, thresholding ve segmentasyon gibi uygulamalarda sıkça kullanılır.