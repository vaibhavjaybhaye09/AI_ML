import cv2
import os

# Path to video file
video_path = "input.mp4"

# Folder to save frames
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

# Read video
cap = cv2.VideoCapture(video_path)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save frame
    frame_filename = os.path.join(output_dir, f"frame_{frame_count:05d}.jpg")
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

cap.release()
print(f"Done! {frame_count} frames saved in '{output_dir}' folder.")
