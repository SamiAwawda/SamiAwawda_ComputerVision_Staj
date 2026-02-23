import cv2

img = cv2.imread('images/car.jpg')

start_point=(150, 200)
end_point=(250, 310)
color=(0, 255, 0)
thickness=-1

cv2.rectangle(img, start_point, end_point, color, thickness)


cv2.imshow('filled Rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()