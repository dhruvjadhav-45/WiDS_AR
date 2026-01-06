# Augmented Reality: Face Tracking and Overlay System

## 📌 Project Overview
This project is part of the **Winter in Data Science** program. It explores the intersection of Computer Vision and Augmented Reality, transitioning from static image manipulation to real-time facial feature tracking and digital asset overlay.

The goal is to create a seamless "virtual try-on" experience where digital assets (like glasses or masks) automatically scale, rotate, and follow the user's face in a video stream.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Libraries:** OpenCV, MediaPipe, NumPy, Pillow (PIL)
* **Models:** MediaPipe Face Landmarker (478-point 3D Mesh)

---

## 📂 Project Phases

### Week 1: Image Segmentation & Background Removal
Focused on the fundamentals of foreground extraction and alpha compositing.
* **Algorithm:** GrabCut (Iterative segmentation based on Gaussian Mixture Models).
* **Key Concept:** Creating a 4-channel (RGBA) image from a 3-channel (BGR) image to handle transparency.
* **Result:** Isolated foreground objects seamlessly blended onto new background environments.

### Week 2: Real-Time Face Tracking & AR Overlays
Focused on dynamic video processing and sub-pixel landmark detection.
* **Algorithm:** MediaPipe Face Landmarker API.
* **Key Logic:** * **Euclidean Distance:** Calculating eye-to-eye distance to dynamically scale assets.
    * **Alpha Blending:** Implementing weighted transparency to prevent "box" artifacts around overlays.
    * **Smoothing:** Applying an Exponential Moving Average (EMA) filter to eliminate coordinate jitter.

---

## 🚀 How It Works

1.  **Detection:** The system loads a video and processes each frame through the MediaPipe Face Mesh model.
2.  **Landmarking:** Specific indices (Outer eye corners) are targeted to act as anchors for the digital asset.
3.  **Dynamic Scaling:** The distance $d$ between landmarks $(x1, y1)$ and $(x2, y2)$ is calculated:
    $$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$
    The overlay is then resized based on $d$ to ensure it fits the face regardless of the user's distance from the camera.
4.  **Temporal Filtering:** To ensure a stable experience, the current position is smoothed using:
    $$Pos_{final} = (\alpha \cdot Pos_{prev}) + ((1 - \alpha) \cdot Pos_{curr})$$

---

## 📖 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Dhruv-Jadhav/AR-Face-Tracking.git](https://github.com/Dhruv-Jadhav/AR-Face-Tracking.git)
