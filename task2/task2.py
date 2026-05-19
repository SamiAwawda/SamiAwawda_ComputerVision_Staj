import cv2

img = cv2.imread('images/car.jpg')

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow('car', gray)
k = cv2.waitKey(0)  

if  k == ord('q'):
    print("Exiting without saving.")

cv2.destroyAllWindows()
