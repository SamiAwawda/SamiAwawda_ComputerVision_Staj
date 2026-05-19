import cv2  

img = cv2.imread('images/car.jpg')

if img is None:
    print("Error: Image not found")
else:
    print("Press 's' to save, 'q' to quit.")
    
    cv2.imshow('Car Image', img) 

k = cv2.waitKey(0)  

if k == ord('s'):
    cv2.imwrite('images/car_New_image.jpg', img) # Save a new copy
    print("Image saved.")
elif k == ord('q'):
    print("Exiting without saving.")

cv2.destroyAllWindows()