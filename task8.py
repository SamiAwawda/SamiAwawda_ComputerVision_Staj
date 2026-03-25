import cv2
import numpy as np

img = cv2.imread('images/home.jpeg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (5,5), 0)


edges = cv2.Canny(gray, 100, 200)


gray_float = np.float32(gray)

corners = cv2.cornerHarris(gray_float, 2, 3, 0.04)

corners = cv2.dilate(corners, None)

img[corners > 0.1 * corners.max()] = [0, 0, 255]

cv2.imshow('Original', img)
cv2.imshow('Edges (Canny)', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()