# 🤖 LeRobot Color Sorting with Imitation Learning

An imitation learning project using the **LeRobot SO-101 robotic arm** for autonomous color sorting.

This project demonstrates the complete workflow of robot calibration, teleoperation-based data collection, vision-based color detection, ACT policy training, and real-world evaluation.

---

## 📌 Project Overview

The goal of this project is to train a robotic arm to autonomously sort colored cubes using imitation learning.

Human demonstrations were collected through teleoperation with the SO-101 leader/follower robot system. The collected dataset was then used to train an **ACT (Action Chunking Transformer)** policy, enabling the robot to perform the sorting task autonomously.

---

## 🎯 Task

The robot performs the following task:

- Pick up the **red cube** and place it into the **left bin**
- Pick up the **green cube** and place it into the **right bin**

---

## ✨ My Contributions

During this project, I personally completed the following tasks:

- Assembled and configured the LeRobot SO-101 leader/follower robotic arms
- Performed motor setup and robot calibration
- Configured USB cameras for front and wrist views
- Collected demonstration datasets using teleoperation
- Recorded approximately **140 demonstration episodes**
- Modified and tested OpenCV-based color detection
- Changed the color detection pipeline from **Red/Blue** to **Red/Green**
- Trained an ACT policy using the collected dataset
- Evaluated the trained policy on the real robot
- Improved green cube performance by collecting additional demonstration data

---

## 🛠 Hardware

- LeRobot SO-101 Leader Robot
- LeRobot SO-101 Follower Robot
- USB Front Camera
- USB Wrist Camera
- NVIDIA GPU (CUDA)

---

## 💻 Software

- Python 3.10
- LeRobot
- OpenCV
- PyTorch
- NumPy
- CUDA

---

## 📂 Project Structure

```text
lerobot-color-sorting/
│
├── color_test.py          # OpenCV color detection
├── README.md
└── .gitignore
```

---

## 🎨 Color Detection

A custom OpenCV script was used to detect colored cubes before data collection.

Main features:

- HSV color space conversion
- Red and green color masking
- Contour detection
- Bounding box visualization
- Real-time camera display

The original implementation was modified to replace blue cube detection with green cube detection.

---

## 🤖 Robot Calibration

The robot system was calibrated before every experiment.

Main steps:

- Motor setup
- Leader calibration
- Follower calibration
- Camera configuration

---

## 📦 Dataset Collection

Demonstration data was collected through teleoperation.

Dataset summary:

| Dataset | Episodes |
|---------|----------:|
| Red & Green Sorting | 100 |
| Green-only Boost | 40 |
| **Total** | **140** |

Each demonstration includes:

- Front camera image
- Wrist camera image
- Robot joint states
- Robot actions

---

## 🧠 Policy Training

The collected demonstrations were used to train an **ACT (Action Chunking Transformer)** policy.

Training configuration:

- Policy: ACT
- Framework: LeRobot
- Device: CUDA
- Batch Size: 64
- Training Steps: 10,000

---

## 🚀 Evaluation

The trained policy was evaluated on the real robot.

Evaluation procedure:

1. Load trained ACT policy
2. Observe camera images
3. Predict robot actions
4. Execute autonomous manipulation
5. Record evaluation results

---

## 📈 Results

- Successfully collected over **140** demonstrations
- Trained an ACT policy for robotic manipulation
- Performed autonomous color sorting on a real robot
- Improved green cube performance through additional demonstrations

---

## 📖 Skills Demonstrated

This project helped develop practical experience in:

- Robot manipulation
- Robot calibration
- Teleoperation
- Imitation Learning
- Computer Vision
- OpenCV
- Deep Learning
- ACT Policy
- Dataset Collection
- Real Robot Experiments

---

## 🔮 Future Work

Potential improvements include:

- Object detection using deep learning models
- Multi-object sorting
- Automatic failure recovery
- Additional camera viewpoints
- Generalization to unseen objects

---

## 🙏 Acknowledgements

This project is built upon the **LeRobot** framework.

My primary contributions include:

- Robot setup and calibration
- Dataset collection
- OpenCV-based color detection
- ACT policy training
- Experimental evaluation on the real robot
