import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, video = camera.read()

    if not ret:
        print("Error: Cannot read frame")
        break

    cv2.imshow('Camera Video', video)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()


