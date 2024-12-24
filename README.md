# Hand Gesture Volume Control

This project allows users to control the system volume using hand gestures. It utilizes a webcam to detect the distance between the thumb and index finger and adjusts the audio volume in real-time. The system leverages `MediaPipe`, `OpenCV`, and `Pycaw` for gesture detection and audio control.

## Features
- Real-time hand tracking with MediaPipe.
- Smooth volume adjustments using distance between fingers.
- Intuitive and contactless volume control.

## Libraries Used
- `opencv-python`: For video capture and frame processing.
- `mediapipe`: For hand landmark detection.
- `pycaw`: For controlling system audio.
- `numpy`: For efficient numerical operations.

## How It Works
1. Captures video input from the webcam.
2. Detects hand landmarks using MediaPipe.
3. Calculates the distance between the thumb and index finger.
4. Maps the distance to the system volume range.
5. Smoothly adjusts the volume using Pycaw.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo/hand-gesture-volume-control.git
    cd hand-gesture-volume-control
    ```
2. Install required libraries:
    ```bash
    python volume_control.py
    ```

## Usage
1. Run the script:
    ```bash
    python Volume_Control.py
    ```
2. Adjust the system volume by changing the distance between your thumb and index finger in front of the webcam.
3. Press q to exit the application.

## Acknowledgments
- MediaPipe
- OpenCV
- Pycaw


## License
This project is licensed under the MIT License. See the LICENSE file for details.