import cv2

camera = cv2.VideoCapture('task15/flag.mp4')

while True:
    ret, video = camera.read()

    if not ret:
        print("Error: Cannot read frame")
        break

    hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    # White color range
    lower_white = (0, 0, 200)
    upper_white = (180, 50, 255)

    mask = cv2.inRange(hsv, lower_white, upper_white)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frame = video.copy()

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest_contour) > 500:
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('White Object Tracking', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()