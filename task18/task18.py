import cv2
import numpy as np

net = cv2.dnn.readNet(
    "task18/yolov4.weights",
    "task18/yolov4.cfg"
)

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# In COCO dataset, "person" is class index 0
PERSON_CLASS_ID = 0

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    ret, video = camera.read()

    if not ret:
        print("Error: Cannot read frame")
        break

    frame = video.copy()
    height, width = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (608, 608), swapRB=True, crop=False)

    net.setInput(blob)
    detections = net.forward(output_layers)

    boxes = []
    confidences = []

    for output in detections:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if class_id == PERSON_CLASS_ID and confidence > 0.5:
                cx = int(detection[0] * width)
                cy = int(detection[1] * height)
                w  = int(detection[2] * width)
                h  = int(detection[3] * height)
                x  = cx - w // 2
                y  = cy - h // 2

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))

    indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            conf = confidences[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Person: {conf:.2f}", (x, y - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("YOLOv4 - Person Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()


"""
GÖREV ANALİZİ: Confidence (Güven) Değerinin Sonuçlar Üzerindeki Etkisi

Kod içerisinde "confidence > 0.5" ve "score_threshold=0.5" değerlerini değiştirerek yaptığım incelemeler sonucunda şu etkileri gözlemledim:

1. Düşük Confidence Değeri (Örn: 0.1 - 0.2):
   Eşik değerini düşürdüğümüzde, model çok emin olmadığı şekilleri bile "insan" olarak işaretlemeye başlar. Bu durum "Yanlış Pozitif" (False Positive) oranını artırır. Yani arka plandaki cansız nesneler, gölgeler veya eşyalar hatalı bir şekilde insan olarak algılanır.

2. Yüksek Confidence Değeri (Örn: 0.8 - 0.9):
   Eşik değerini yükselttiğimizde, model sadece çok net gördüğü ve %100'e yakın emin olduğu insanları tespit eder. Yanlış algılamalar tamamen ortadan kalkar ancak bu kez de "Yanlış Negatif" (False Negative) sorunu başlar. Yani uzaktaki, karanlıkta kalan veya kameraya sadece profilden görünen gerçek insanlar tespit edilemez olur.

Sonuç: 
0.4 ile 0.5 arasındaki bir değer, hem gereksiz nesneleri elemek hem de gerçek insanları kaçırmamak için en optimum/dengeli seviyedir.
"""