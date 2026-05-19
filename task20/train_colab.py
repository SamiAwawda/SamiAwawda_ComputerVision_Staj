# ── CELL 1: Install & Download Dataset ──────────────────
!pip install roboflow -q

from roboflow import Roboflow
rf = Roboflow(api_key="S4hiBADT0xnqZSmDRuAJ")
project = rf.workspace("school-orhpf").project("hand-detection-aeqa1")
version = project.version(2)
dataset = version.download("yolov5")

# ── CELL 2: Clone YOLOv5 & Install Requirements ─────────
!git clone https://github.com/ultralytics/yolov5
import os
os.chdir("yolov5")
!pip install -r requirements.txt -q


# ── CELL 3: Train ────────────────────────────────────────
!python train.py \
    --img 640 \
    --batch 16 \
    --epochs 50 \
    --data /kaggle/working/Hand-Detection-2/data.yaml \
    --weights yolov5s.pt \
    --name hand_model


# ── CELL 4: Download best.pt ─────────────────────────────
from IPython.display import FileLink
FileLink('runs/train/hand_model/weights/best.pt')
