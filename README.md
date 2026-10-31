# YOLOv8 Movement Detection 
## Objective
This script processes an input video to track and extract human movement using YOLOv8 pose estimation. This updated version is optimized for **accuracy testing, facial focus, and clean visual output**. 

Key updates in this version include:
- **Clean Visualization:** Bounding boxes and text labels are removed, and the skeletal keypoints are rendered in pure white.
- **Interval Processing:** Processes frames at specific time intervals (e.g., every 2-3 seconds) to speed up accuracy checks.
- **High Accuracy:** Utilizes the extra-large `yolov8x-pose.pt` model for maximum precision.
- **Face Tracking:** Isolates and logs the exact coordinates for the 5 primary facial keypoints.

It generates two video outputs: 
1. The original video with the pure white tracked keypoints overlaid.
2. An isolated version showing only the pure white moving keypoints on a solid black background.

## Installation
Install the required dependencies using pip:
```bash
pip install ultralytics opencv-python
