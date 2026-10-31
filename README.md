# Movement Detection & Pose Extractor 🏃‍♂️✨

A computer vision script that uses YOLOv8 Pose Estimation to track, extract, and isolate human movement. 

This project processes an input video and simultaneously generates two outputs: the original video with the skeletal tracking overlaid, and a clean, isolated version showing *only* the moving keypoints on a pure black background to highlight the kinematics of the subject.

## 🚀 Features

* **Real-Time Pose Estimation:** Utilizes the `yolov8n-pose.pt` model to detect the 17 standard **COCO keypoints** (shoulders, elbows, knees, etc.) on the human body.
* **Movement Isolation:** Strips away all background noise by rendering the tracked skeleton on a zero-pixel (black) frame, highlighting only the pure movement and physics of the subject.
* **Efficient Dual Processing:** Reads the input video frame-by-frame once, but simultaneously writes to two separate `.mp4` video files to save processing time.

## 📽️ Output Demo

*(Insert a 3-5 second GIF here showing the black background tracking video next to the original video)*

## 🛠️ Prerequisites

Before running the script, ensure you have Python installed along with the required computer vision libraries. 

Install the dependencies using pip:
bash
pip install ultralytics opencv-python
