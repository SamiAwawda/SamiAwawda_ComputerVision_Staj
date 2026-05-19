# OpenCV Training Tasks Summary (1-15)

هذا الملف يحتوي على ملخص للـ 15 مهمة (Tasks) التي أنجزتها في مجال OpenCV. تم قراءة وتحليل كل ملف لفهم التقنيات المستخدمة.

| المهمة | الملف | الوصف (Description) | التقنيات المستخدمة |
| :--- | :--- | :--- | :--- |
| 1 | `task1.py` | قراءة صورة وعرضها مع خيارات الحفظ أو الخروج. | `imread`, `imshow`, `imwrite`, `waitKey` |
| 2 | `task2.py` | تحويل الصورة من BGR إلى Grayscale (رمادي). | `cvtColor`, `COLOR_BGR2GRAY` |
| 3 | `task3.py` | تغيير حجم الصورة واقتطاع جزء منها (ROI). | `resize`, ROI Slicing |
| 4 | `task4.py` | رسم مستطيل ملون ومملوء على الصورة. | `rectangle` |
| 5 | `task5.py` | تمويه جزء معين من الصورة (Gaussian Blur) مع شرح الفائدة العملية. | `GaussianBlur`, ROI Processing |
| 6 | `task6.py` | تطبيق العتبة (Thresholding) لفصل الكائنات عن الخلفية. | `threshold`, `THRESH_BINARY` |
| 7 | `task7.py` | تقسيم العملات باستخدام خوارزمية Watershed. | `distanceTransform`, `connectedComponents`, `watershed` |
| 8 | `task8.py` | كشف الحواف (Canny) والزوايا (Harris Corner Detection). | `Canny`, `cornerHarris`, `dilate` |
| 9 | `task9.py` | مقارنة خصائص الصورة الأصلية والرمادية (الأبعاد والقيم). | `shape`, Pixel accessing |
| 10 | `task10.py` | العمليات المورفولوجية (Dilation, Erosion, Opening). | `dilate`, `erode`, `morphologyEx` |
| 11 | `task11.py` | قلب الصورة (Flipping) أفقياً ورأسياً. | `flip` |
| 12 | `task12.py` | التقاط الفيديو من الكاميرا وتغيير أبعاده في الوقت الفعلي. | `VideoCapture`, `read`, `resize` |
| 13 | `task13.py` | تتبع الأجسام السوداء (Black Object Tracking) باستخدام HSV والكنتور. | `inRange`, `findContours`, `boundingRect` |
| 14 | `task14.py` | استخدام أشرطة التحكم (Trackbars) لتعديل قيم HSV في الفيديو. | `createTrackbar`, `getTrackbarPos`, `split`, `merge` |
| 15 | `task15.py` | تتبع الأجسام البيضاء (White Object Tracking) في ملف فيديو. | `inRange`, `findContours`, `max(contours)` |
| 16 | `task16.py` | بحث عن بنية الشبكات العصبية الالتفافية (CNN Architecture). | `cv2.dnn`, Deep Learning Concepts |
| 17 | `task17.py` | تطبيق للكشف عن الوجوه باستخدام نموذج YOLOv3. | `cv2.dnn.readNet`, YOLO, Object Detection |

---
**الوضع الحالي:** تم إتمام 16 مهمة، والمهمة 17 قيد التنفيذ (تحليل وتخطيط).
