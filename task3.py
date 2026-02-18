import cv2

img = cv2.imread('images/car0.jpg')
 
new_img = cv2.resize(img, (640 , 500))
cv2.imshow('size img', new_img)

roi = new_img[250:400, 120:160] 
cv2.imshow('Selected Area (ROI)', roi)

k = cv2.waitKey(0)  

if k == ord('s'):
        
    cv2.imwrite('images/resized_image.jpg', new_img)   
    cv2.imwrite('images/selected_area_roi.jpg', roi)        
    print("Image saved.")

elif k == ord('q'):
    print("Exiting without saving.")