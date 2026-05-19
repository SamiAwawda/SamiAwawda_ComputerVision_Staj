import cv2

img = cv2.imread('images/car.jpg')

# Vertical flip 
img_flipped_vertical = cv2.flip(img, 0)

# Horizontal flip 
img_flipped_horizontal = cv2.flip(img, 1)

cv2.imshow('Original Image', img)
cv2.imshow('Vertical Flipped Image', img_flipped_vertical)
cv2.imshow('Horizontal Flipped Image', img_flipped_horizontal)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Bu çalışmada OpenCV’nin flip() metodu uygulanmıştır.
Bu metod, görüntüyü belirli bir eksene göre ters çevirmek için kullanılır.
flip(img, 0) kullanıldığında görüntü dikey olarak çevrilir; yani üst kısım alta, alt kısım üste gelir.
flip(img, 1) kullanıldığında ise görüntü yatay olarak çevrilir; yani sol taraf sağa, sağ taraf sola geçer.
Bu yöntem, görüntünün yönünü değiştirmek ve farklı görünümler elde etmek için kullanılır.
"""