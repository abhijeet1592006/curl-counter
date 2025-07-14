# Curl Counter

This is a basic real-time **bicep curl counter** built using **OpenCV** and **MediaPipe Pose**. The project detects specific arm landmarks to compute the angle of your right arm during a curl motion, allowing it to track your workout and count the repetitions.

Created with ❤️ by **Abhijeet Singh**.

---

# 🧠 Features

- Real-time pose tracking using webcam.
- Detects right-arm movement (shoulder, elbow, wrist).
- Computes the angle between upper arm and lower arm.
- Counts complete curls based on movement thresholds.
- Visual angle arc and strength bar indicator.
- Simple UI with live rep count display.

---

# 🔧 Requirements

Make sure you have the following installed:

```bash
python>=3.7
opencv-python
mediapipe
```

# You can install dependencies using:

```bash
pip install opencv-python mediapipe
```

# 🚀 How It Works

- Uses MediaPipe Pose to detect human pose landmarks in each frame.

- Tracks three main points:

- Right Shoulder (landmark #12)

- Right Elbow (landmark #14)

- Right Wrist (landmark #16)

- Calculates angles using math.atan2 and basic trigonometry.

- If the angle goes below a threshold (e.g., arm curled up), and then above another (e.g., arm extended), it counts as one repetition.

# Displays:

- Current angle

- Repetition count

- Strength bar (based on current arm angle)

# 📄 Code Overview
**Main Libraries:**
cv2 – For video stream handling and drawing.

mediapipe – For pose detection.

math – For angle calculation.

**Key Variables:**
- up, down – State trackers to validate a full rep.

- count – Total number of curl reps.

- draw() – Helper function to draw joints on the frame.

- cv2.ellipse() – To visualize the curl angle arc.

# 🖼️ UI Elements


🟢 Green Circles: Landmark points.

⚪ White Lines: Bones between joints.

🔴 Text: Current curl count and angle.

🟡 Strength Bar: Displays dynamic arm angle level.


# 🏁 Usage
**Run the script:**

```bash
python curl_counter.py
```

**To quit the program, press the Q key.**

## 📌 Notes
The script currently tracks the right arm only.

Camera index 0 is used by default. Change it to 1 or the correct device index if needed:

```python

cap = cv2.VideoCapture(0)
```


# 🙏 Acknowledgements
**MediaPipe by Google for pose estimation.**

- OpenCV for image processing.

# 📫 Contact
**Abhijeet Singh**

📧 Email: abhijeet8800434205@gmail.com


# 📜 License
**This project is open-source and available under the MIT License.**
