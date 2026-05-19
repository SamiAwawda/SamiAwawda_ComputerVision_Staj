import cv2
import numpy as np

img = cv2.imread('images/coins.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



ret, thresholded_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
Clean_img = cv2.morphologyEx(thresholded_img, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))

kernel = np.ones((3,3), np.uint8)
sure_bg = cv2.dilate(Clean_img, kernel, iterations=3)

distanceCalc = cv2.distanceTransform(Clean_img, cv2.DIST_L2, 5)

ret, sure_fg = cv2.threshold(distanceCalc, 0.7 * distanceCalc.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

unknown_region = cv2.subtract(sure_bg, sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)

markers = markers + 1
markers[unknown_region == 255] = 0

markers = cv2.watershed(img, markers)

img[markers == -1] = [0, 0, 255]

cv2.imshow('Watershed Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()