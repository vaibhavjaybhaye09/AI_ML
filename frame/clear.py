import cv2
import os

# ============== SETTINGS ==============
INPUT_DIR = "raw_4"     # folder with all images
OUTPUT_DIR = "dataset_images"  # folder for clear images

LAPLACIAN_THRESHOLD = 200      # reduce if too strict
EDGE_DENSITY_THRESHOLD = 0.015
# =====================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

def is_blurry(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    edges = cv2.Canny(gray, 50, 150)
    edge_density = edges.mean() / 255.0

    return lap_var < LAPLACIAN_THRESHOLD or edge_density < EDGE_DENSITY_THRESHOLD

saved = 0
skipped = 0

for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img_path = os.path.join(INPUT_DIR, filename)
    img = cv2.imread(img_path)

    if img is None:
        continue

    if is_blurry(img):
        skipped += 1
    else:
        out_name = f"img_{saved:06d}.jpg"
        cv2.imwrite(os.path.join(OUTPUT_DIR, out_name), img)
        saved += 1

print("Image filtering completed")
print("Saved (clear)     :", saved)
print("Skipped (blurry)  :", skipped)
