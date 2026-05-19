import cv2
import numpy as np

def nothing(x):
    pass

video = cv2.VideoCapture('task14/video1.mp4')

if not video.isOpened():
    print("Error: Cannot open video file")
    exit()

cv2.namedWindow('Trackbars')

cv2.createTrackbar('H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('V', 'Trackbars', 0, 255, nothing)

while True:
    ret, frame = video.read()

    if not ret:
        print("Video finished")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    h_value = cv2.getTrackbarPos('H', 'Trackbars')
    s_value = cv2.getTrackbarPos('S', 'Trackbars')
    v_value = cv2.getTrackbarPos('V', 'Trackbars')

    h = cv2.add(h, h_value)
    s = cv2.add(s, s_value)
    v = cv2.add(v, v_value)

    hsv_modified = cv2.merge([h, s, v])
    result = cv2.cvtColor(hsv_modified, cv2.COLOR_HSV2BGR)

    cv2.imshow('Original Video', frame)
    cv2.imshow('HSV Modified Video', result)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


"""
GÖREVİ: HSV Nedir ve Neden Kullanılır?

HSV (Hue, Saturation, Value), insan gözünün renkleri algılama biçimine en yakın olan renk uzayıdır. BGR (Mavi, Yeşil, Kırmızı) formatından farklı olarak, renk bilgisini ve ışık (parlaklık) bilgisini birbirinden ayırır.

1. H (Hue - Renk Tonu): Rengin kendisini ifade eder (Kırmızı, sarı, mavi vb.). OpenCV'de 0 ile 179 arasında değer alır.
2. S (Saturation - Doygunluk): Rengin canlılığını ifade eder. 0 (soluk/beyaz-gri) ile 255 (tam canlı renk) arasında değişir.
3. V (Value - Parlaklık): Rengin ne kadar aydınlık veya karanlık olduğunu belirtir. 0 (tamamen siyah) ile 255 (tam aydınlık) arasında değişir.

Neden Kullanılır?
Görüntü işlemede (özellikle nesne takibi ve renk tespiti uygulamalarında) BGR yerine HSV tercih edilir. Çünkü ortamdaki ışık değişimleri (gölgeler, parlamalar) BGR değerlerini tamamen değiştirirken, HSV'de sadece 'V' (parlaklık) değeri değişir, rengin özü ('H') sabit kalır. Bu da algoritmaların daha kararlı çalışmasını sağlar.
"""