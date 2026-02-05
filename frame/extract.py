import cv2
import os

# ============== SETTINGS ==============
VIDEO_PATH = r"C:\Users\cg636\Documents\New folder\AI_ML\frame\input.mp4"
OUTPUT_DIR = "raw_4"
# ======================================

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError("Cannot open video file")

frame_id = 0
saved_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # take 2 frame, skip 2 frame
    if frame_id  % 4 == 0:
        filename = f"frame_{saved_id:06d}.jpg"
        cv2.imwrite(os.path.join(OUTPUT_DIR, filename), frame)
        saved_id += 1

    frame_id += 1

cap.release()

print("Extraction completed")
print("Total frames read :", frame_id)
print("Frames saved      :", saved_id)
