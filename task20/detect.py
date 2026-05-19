import cv2
import torch
import pathlib
import time
pathlib.PosixPath = pathlib.WindowsPath 

model = torch.hub.load('ultralytics/yolov5', 'custom', path='task20/best.pt', force_reload=False)
model.conf = 0.4
model.iou  = 0.45

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Cannot open camera")
    exit()

prev_time = time.time()

while True:
    ret, video = camera.read()

    if not ret:
        print("Error: Cannot read frame")
        break

    frame = video.copy()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(rgb, size=640)

    for *box, conf, cls in results.xyxy[0]:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"Hand: {conf:.2f}", (x1, y1 - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    fps_text = f"FPS: {fps:.1f}"
    text_size = cv2.getTextSize(fps_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
    fps_x = frame.shape[1] - text_size[0] - 10
    cv2.putText(frame, fps_text, (fps_x, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)

    cv2.imshow("YOLOv5 - Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
