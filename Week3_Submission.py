import cv2
import numpy as np
import os

# =============================================
# CHECK OVERLAY IMAGE
# =============================================
if not os.path.exists("overlay.png"):
    raise FileNotFoundError("overlay.png not found in current folder")

overlay = cv2.imread("overlay.png", cv2.IMREAD_UNCHANGED)
overlay = cv2.resize(overlay, (80, 80))

# =============================================
# LOAD FACE DETECTOR (OpenCV Haar Cascade)
# =============================================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Default position → nose
position_mode = 2

# =============================================
# WEBCAM
# =============================================
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Could not access webcam")

print("Controls:")
print("1 → Forehead")
print("2 → Nose (default)")
print("3 → Mouth")
print("q → Quit")

# =============================================
# OVERLAY FUNCTION
# =============================================
def overlay_image(bg, fg, x, y):
    h, w = fg.shape[:2]

    if x < 0 or y < 0 or x + w > bg.shape[1] or y + h > bg.shape[0]:
        return bg

    if fg.shape[2] == 4:
        alpha = fg[:, :, 3] / 255.0
        for c in range(3):
            bg[y:y+h, x:x+w, c] = (
                alpha * fg[:, :, c] +
                (1 - alpha) * bg[y:y+h, x:x+w, c]
            )
    else:
        bg[y:y+h, x:x+w] = fg[:, :, :3]

    return bg

# =============================================
# MAIN LOOP
# =============================================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Approximate landmark positions
        forehead = (x + w // 2, y + int(0.15 * h))
        nose = (x + w // 2, y + int(0.5 * h))
        mouth = (x + w // 2, y + int(0.75 * h))

        if position_mode == 1:
            px, py = forehead
        elif position_mode == 2:
            px, py = nose
        elif position_mode == 3:
            px, py = mouth

        px -= overlay.shape[1] // 2
        py -= overlay.shape[0] // 2

        frame = overlay_image(frame, overlay, px, py)

    cv2.imshow("Week 3 - Real-time Webcam Filter", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        position_mode = 1
    elif key == ord('2'):
        position_mode = 2
    elif key == ord('3'):
        position_mode = 3
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
