import cv2
import os
import time

SAVE_DIR = "task20/dataset/images"
MAX_IMAGES = 300
LABEL = "hand"  

os.makedirs(SAVE_DIR, exist_ok=True)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Cannot open camera")
    exit()

count = 0
auto_capture = False
last_capture_time = 0
AUTO_DELAY = 0.5  

print("SPACE: capture one image | A: toggle auto capture | Q: quit")

while True:
    ret, video = camera.read()

    if not ret:
        print("Error: Cannot read frame")
        break

    frame = video.copy()

    if auto_capture and time.time() - last_capture_time >= AUTO_DELAY:
        filename = os.path.join(SAVE_DIR, f"{LABEL}_{count:04d}.jpg")
        cv2.imwrite(filename, frame)
        count += 1
        last_capture_time = time.time()

    status = "AUTO ON" if auto_capture else "AUTO OFF"
    cv2.putText(frame, f"Captured: {count}/{MAX_IMAGES}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(frame, status, (10, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255) if auto_capture else (100, 100, 100), 2)
    cv2.putText(frame, "SPACE: capture | A: auto | Q: quit", (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.imshow("Image Capture", frame)

    if count >= MAX_IMAGES:
        print(f"Done! {MAX_IMAGES} images saved in: {SAVE_DIR}")
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord(' '):
        filename = os.path.join(SAVE_DIR, f"{LABEL}_{count:04d}.jpg")
        cv2.imwrite(filename, frame)
        count += 1
        print(f"Saved: {filename}")
    elif key == ord('a'):
        auto_capture = not auto_capture
        print(f"Auto capture: {'ON' if auto_capture else 'OFF'}")

camera.release()
cv2.destroyAllWindows()
print(f"Total images captured: {count}")
