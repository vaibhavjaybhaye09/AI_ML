import cv2
import os

# ================= SETTINGS =================
VIDEO_PATH = r"C:\Users\cg636\Documents\New folder\AI_ML\frame\input.mp4"
OUTPUT_DIR = "raw_dataset"

LAPLACIAN_THRESHOLD = 200
EDGE_DENSITY_THRESHOLD = 0.015
# ============================================

# ---------- Create output folder ----------
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------- Blur detection ----------
def is_blurry(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    edges = cv2.Canny(gray, 50, 150)
    edge_density = edges.mean() / 255.0

    return lap_var < LAPLACIAN_THRESHOLD or edge_density < EDGE_DENSITY_THRESHOLD

# ---------- Main ----------
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError("Cannot open video file")

frame_id = 0
saved = 0
skipped_blur = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if is_blurry(frame):
        skipped_blur += 1
    else:
        filename = f"frame_{saved:06d}.jpg"
        cv2.imwrite(os.path.join(OUTPUT_DIR, filename), frame)
        saved += 1

    frame_id += 1

cap.release()

print("Raw dataset extraction completed")
print("Total frames read :", frame_id)
print("Saved (clean)     :", saved)
print("Skipped (blurry)  :", skipped_blur)
