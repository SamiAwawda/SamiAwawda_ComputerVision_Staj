import cv2  # Import OpenCV library

# Read the image from the folder
img = cv2.imread('images/car.jpg')

# Check if the image is loaded
if img is None:
    print("Error: Image not found")
else:
    cv2.imshow('Staj', img) # Display the image in a window
    print("Press 's' to save, 'q' to quit.")

k = cv2.waitKey(0)  # Wait for a key press

if k == ord('s'):
        cv2.imwrite('images/car_New_image.jpg', img) # Save a new copy
        print("Image saved.")
elif k == ord('q'):
        print("Exiting without saving.")

