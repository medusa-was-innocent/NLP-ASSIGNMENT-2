import cv2
import os
!pip install ultralytics
from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")

cap = cv2.VideoCapture("dancing.mp4")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out_overlay = cv2.VideoWriter("dancing_with_points.mp4",
                              cv2.VideoWriter_fourcc(*"mp4v"),
                              fps,
                              (width, height))

out_black = cv2.VideoWriter("only_points_black_bg.mp4",
                            cv2.VideoWriter_fourcc(*"mp4v"),
                            fps,
                            (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.25, verbose=False)

    black_frame = frame * 0

    skeleton_colored = results[0].plot(img=black_frame, boxes=False, labels=False)

    gray_skeleton = cv2.cvtColor(skeleton_colored, cv2.COLOR_BGR2GRAY)
    _, white_mask = cv2.threshold(gray_skeleton, 1, 255, cv2.THRESH_BINARY)

    white_skeleton_black_bg = cv2.cvtColor(white_mask, cv2.COLOR_GRAY2BGR)
    out_black.write(white_skeleton_black_bg)

    annotated_frame = frame.copy()
    annotated_frame[white_mask == 255] = (255, 255, 255) 
    out_overlay.write(annotated_frame)

cap.release()
out_overlay.release()
out_black.release()
print("Completed processing both videos")
print("Your videos are saved here:", os.getcwd())
