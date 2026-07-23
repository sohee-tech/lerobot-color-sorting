# 🤖 LeRobot Color Sorting with Imitation Learning

A robotics project that applies **imitation learning** to enable a LeRobot SO-101 robotic arm to autonomously sort colored cubes.

This project covers the complete workflow from robot setup and teleoperation-based data collection to ACT policy training and real-world evaluation.

---

## 📌 Project Overview

The objective of this project is to train a robotic arm to perform a simple color sorting task through imitation learning.

Human demonstrations were collected using the SO-101 leader/follower teleoperation system. The collected dataset was then used to train an **ACT (Action Chunking Transformer)** policy provided by the LeRobot framework.

---

## 🎯 Task

The robot learns to perform the following task:

- Pick up the **red cube** and place it into the **left bin**
- Pick up the **green cube** and place it into the **right bin**

---

## ✨ My Contributions

During this project, I:

- Assembled and configured the LeRobot SO-101 leader/follower robotic arms
- Performed robot calibration before experiments
- Configured front and wrist cameras for data collection
- Modified an OpenCV-based color detection program from **Red/Blue** to **Red/Green**
- Collected approximately **140 teleoperation demonstrations**
- Trained an ACT policy using the collected demonstrations
- Evaluated the trained policy on the real robot
- Collected additional demonstrations focused on green cube manipulation

---

## 🛠 Hardware

- LeRobot SO-101 Leader Robot
- LeRobot SO-101 Follower Robot
- USB Front Camera
- USB Wrist Camera
- NVIDIA GPU

---

## 💻 Software

- Python 3.10
- LeRobot
- OpenCV
- PyTorch
- NumPy
- CUDA

---

## 📂 Repository Structure

```text
lerobot-color-sorting/
│
├── README.md
├── color_test.py
├── docs/
│   ├── setup.md
│   ├── training.md
│   └── evaluation.md
│
├── images/
│
├── .gitignore
└── LICENSE
```

---

## 🎨 Color Detection

The project includes a Python program (`color_test.py`) for real-time color detection using OpenCV.

Main features:

- HSV color space conversion
- Red and green color masking
- Contour detection
- Bounding box visualization
- Real-time camera display

The original color detection pipeline was modified to detect **red and green cubes** instead of **red and blue cubes**.

---

## 📦 Dataset

Human demonstrations were collected through teleoperation.

| Dataset | Episodes |
|---------|----------:|
| Red & Green Sorting | 100 |
| Green-only Demonstrations | 40 |
| **Total** | **140** |

The collected data includes:

- Front camera images
- Wrist camera images
- Robot joint states
- Robot actions

---

## 🧠 Policy Training

The collected demonstrations were used to train an **ACT (Action Chunking Transformer)** policy using the LeRobot framework.

Training configuration:

| Parameter | Value |
|-----------|-------|
| Policy | ACT |
| Device | CUDA |
| Batch Size | 64 |
| Training Steps | 10,000 |

More details are available in **docs/training.md**.

---

## 🚀 Evaluation

The trained policy was evaluated on the real SO-101 robotic arm.

The evaluation process included:

1. Loading the trained ACT policy
2. Capturing images from the robot cameras
3. Predicting robot actions
4. Executing autonomous manipulation
5. Recording the evaluation results

More details are available in **docs/evaluation.md**.

---

## 📖 Skills Demonstrated

- Robot Assembly
- Robot Calibration
- Teleoperation
- Computer Vision
- OpenCV
- Imitation Learning
- ACT Policy Training
- Dataset Collection
- Real Robot Evaluation

---

## 🔮 Future Work

Possible future improvements include:

- Object detection using deep learning
- Multi-object manipulation
- Improved robustness under different lighting conditions
- Better generalization to unseen object positions

---

## 🙏 Acknowledgements

This project was developed using the **LeRobot** framework.

My contributions focused on robot setup, data collection, OpenCV-based color detection, policy training, and real-world evaluation.
