# WiDS_AR
AR Face Tracking & Overlay System
🚀 Project Overview
This repository contains the development work for an Augmented Reality (AR) system that tracks human faces and applies digital overlays in real-time. This project was developed as part of the Summer of Science (SoS) program.

📁 Repository Structure
Week1_Submission.ipynb: Contains the GrabCut background removal and image composition logic.

Week2_Submission.ipynb: Contains the real-time video processing pipeline, using MediaPipe for face landmarking and dynamic asset scaling.

assets/: (Recommended) Store your overlay.png and face_landmarker.task here.

⚙️ How It Works
Tracking: We use MediaPipe to extract a 478-point 3D face mesh.

Logic: The system calculates the distance between the eyes to determine the required size of the glasses.

Stability: An Exponential Moving Average (EMA) filter is applied to the coordinates to eliminate jitter.

Rendering: Transparent PNGs are alpha-blended onto each video frame.

🛠️ Requirements
Python 3.10+

OpenCV (opencv-python)

MediaPipe

NumPy
