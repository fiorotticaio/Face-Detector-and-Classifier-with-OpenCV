# Face Detector and Classifier with OpenCV

This project demonstrates how to use the face recognition library along with OpenCV to detect and classify faces in real-time using a webcam.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory:

    ```bash
    cd seu-repositorio
    ```

2. Run the main script:

    ```bash
    python main.py
    ```

3. The webcam will activate, and faces will be detected and classified in real-time.

4. Press 'q' to quit the application.

## Understanding the Code

### Structure

- `data/`: Directory containing sample images of faces for recognition.
- `main.py`: Main Python script for running the face detection and classification.
- `requirements.txt`: File containing the required Python libraries.

### Functionality

- The `main.py` script loads pre-trained models for face recognition.
- It captures video frames from the webcam and detects faces in real-time.
- Detected faces are compared against known faces to classify them.
- The recognized faces are displayed on the video stream with their names.

## Acknowledgments

Special thanks to the authors of the [face_recognition](https://github.com/ageitgey/face_recognition) library and the contributors to the [OpenCV](https://opencv.org/) project.