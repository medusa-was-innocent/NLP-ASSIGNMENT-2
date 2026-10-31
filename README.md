# YOLOv8 Movement Detection

## Objective
This script processes an input video to track and extract human movement using YOLOv8 pose estimation. It generates two video outputs: 
1. The original video with the tracked skeletal keypoints overlaid.
2. An isolated version showing only the moving skeletal keypoints on a solid black background.

## Installation
Install the required dependencies using pip:
```bash
pip install ultralytics opencv-python
```

## Usage
1. Place your input video in the same directory and name it `movement.mp4` (or update the script to match your filename).
2. Run the Python script:
```bash
python pose_tracker.py
```

## Outputs
After the script finishes, two files will be generated in your directory:
* `movement_with_points.mp4`
* `only_points_black_bg.mp4`
