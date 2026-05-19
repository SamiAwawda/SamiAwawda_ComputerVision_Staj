import cv2
import numpy as np

img = cv2.imread('images/smarties.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresholded_img = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(thresholded_img, kernel, iterations=1)
erosion = cv2.erode(thresholded_img, kernel, iterations=1)
opening = cv2.morphologyEx(thresholded_img, cv2.MORPH_OPEN, kernel, iterations=1)


cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresholded_img)
cv2.imshow('Dilated Image', dilation)
cv2.imshow('Eroded Image', erosion)
cv2.imshow('Opened Image', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
