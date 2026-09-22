# 🤖 LeRobot Color Sorting with Imitation Learning

A hands-on robotics project using **LeRobot SO-101 leader/follower arms** to build an imitation-learning pipeline for autonomous color sorting.

The project covers the full workflow from **robot assembly and motor setup** to **camera integration, teleoperation, dataset collection, ACT policy training, and real-robot evaluation**.

---

## 📌 Project Overview

The goal of this project was to build a complete manipulation pipeline in which a human demonstrates a task through leader/follower teleoperation and the follower robot later reproduces the task autonomously using an imitation-learning policy.

The task was designed as a simple color-sorting problem:

- Pick up the **red cube** and place it into the **left bin**
- Pick up the **green cube** and place it into the **right bin**

Rather than using only a simulation or a preconfigured robot, I worked through the physical setup and integration process directly, including robot assembly, motor configuration, calibration, camera setup, data collection, training, and real-world execution.

---

## 🔄 End-to-End Workflow

```text
Robot Assembly
      │
      v
Motor Setup & Calibration
      │
      v
Leader ↔ Follower Teleoperation
      │
      v
Front / Wrist Camera Integration
      │
      v
Demonstration Data Collection
      │
      v
ACT Policy Training
      │
      v
Autonomous Inference
      │
      v
Real-Robot Evaluation
```

This project gave me practical experience connecting **hardware, sensors, software, data, and learned control** into one working robotic system.

---

## ✨ My Contributions

I carried out the project setup and experiment workflow directly, including:

- Assembled the LeRobot SO-101 leader and follower robot arms
- Configured and identified individual motors
- Performed leader/follower calibration
- Set up and debugged teleoperation between the two arms
- Integrated front and wrist USB cameras
- Modified an OpenCV color-detection program from **Red/Blue** to **Red/Green**
- Collected approximately **140 teleoperation demonstrations**
- Trained an **ACT (Action Chunking Transformer)** policy
- Evaluated the trained policy on the physical follower robot
- Collected additional demonstrations focused on green-cube manipulation
- Diagnosed and resolved hardware/software integration issues during setup

---

## 🧩 Hardware–Software Integration

The system combines several components that must work together correctly:

```text
Leader Arm
   │
   │ joint / motor commands
   v
Follower Arm
   │
   ├───────────────┐
   │               │
   v               v
Front Camera    Wrist Camera
   │               │
   └───────┬───────┘
           v
 Demonstration Dataset
           │
           v
       ACT Policy
           │
           v
 Autonomous Robot Actions
```

This integration process was an important part of the project because failures were often caused not by one algorithm, but by mismatches between motors, device configuration, code, and camera interfaces.

---

## 🔧 Troubleshooting

### 1. Motors not recognized correctly

During initial setup, some motors were not detected correctly by the system.

Instead of treating the robot as one unit, I disassembled the setup and checked the motors individually. Each motor was reconnected and configured one at a time until the full arm could be recognized correctly.

```text
Motor recognition failure
        ↓
Separate the arm setup
        ↓
Check / configure motors individually
        ↓
Reconnect the full chain
        ↓
Robot recognized successfully
```

**What I learned:** When several devices share one communication chain, checking components individually can isolate hardware/configuration issues much faster than repeatedly changing the full system.

---

### 2. Leader and follower arms did not move together

After the hardware was recognized, the follower arm did not correctly track the leader arm during teleoperation.

I checked the teleoperation code and configuration and corrected the software-side issue so that leader input could be transmitted properly to the follower.

**What I learned:** A physically connected system can still fail because the software interface between devices is incorrect. I learned to separate hardware-recognition problems from control / code problems during debugging.

---

### 3. Dual-camera integration issue

Using a single USB camera worked normally, but adding a second camera caused the camera pipeline to become unstable.

I checked the device recognition and camera configuration in the code and reorganized the setup so that the front and wrist cameras could be treated as separate input devices.

Because USB camera identifiers can change depending on connection order and system state, this step required checking device assignment rather than assuming fixed camera indices.

**What I learned:** Multi-device systems require explicit device management. Camera integration is not only an image-processing problem; stable hardware identification and software configuration are also important.

---

## 🎨 Color Detection

The project includes an OpenCV-based color detection script for real-time visual inspection.

The original Red/Blue setup was modified to detect **red and green cubes**.

Main steps:

```text
Camera Frame
    ↓
BGR → HSV
    ↓
Red / Green Masks
    ↓
Contour Detection
    ↓
Bounding Box Visualization
```

The script was used to verify camera input and color separation during the manipulation setup.

---

## 📦 Dataset Collection

Human demonstrations were collected through leader/follower teleoperation.

| Dataset | Episodes |
|---------|----------:|
| Red & Green Sorting | 100 |
| Green-focused Demonstrations | 40 |
| **Total** | **140** |

The demonstration data includes:

- Front camera images
- Wrist camera images
- Robot joint states
- Robot actions

Collecting the demonstrations directly helped me understand how data quality, camera configuration, and manipulation consistency affect the later training stage.

---

## 🧠 ACT Policy Training

The collected demonstrations were used to train an **ACT (Action Chunking Transformer)** policy using the LeRobot framework.

| Parameter | Value |
|-----------|-------|
| Policy | ACT |
| Device | CUDA |
| Batch Size | 64 |
| Training Steps | 10,000 |

The overall learning pipeline was:

```text
Human Demonstrations
        ↓
LeRobot Dataset
        ↓
ACT Training
        ↓
Trained Policy
        ↓
Camera + Robot State
        ↓
Predicted Actions
        ↓
Follower Arm Execution
```

More details are available in **docs/training.md**.

---

## 🚀 Real-Robot Evaluation

The trained policy was evaluated on the physical SO-101 follower arm.

The evaluation process included:

1. Loading the trained ACT policy
2. Reading current camera observations
3. Reading robot state
4. Predicting the next robot actions
5. Executing the actions on the real arm
6. Observing task performance and collecting additional demonstrations where needed

More details are available in **docs/evaluation.md**.

---

## 🛠 Hardware

- LeRobot SO-101 Leader Robot
- LeRobot SO-101 Follower Robot
- USB Front Camera
- USB Wrist Camera
- NVIDIA GPU workstation

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
├── images/
├── .gitignore
└── LICENSE
```

---

## 📖 Skills Demonstrated

- Robot assembly and hardware setup
- Motor configuration and calibration
- Leader/follower teleoperation
- Hardware–software integration
- Multi-camera device integration
- OpenCV-based visual processing
- Demonstration-data collection
- Imitation learning
- ACT policy training
- Real-robot inference and evaluation
- Systematic troubleshooting

---

## 🔮 Future Work

Possible extensions include:

- More robust object perception under changing lighting
- Multi-object manipulation
- Generalization to unseen cube positions
- Larger and more diverse demonstration datasets
- Quantitative success-rate evaluation across repeated trials

---

## 🙏 Acknowledgements

This project was developed using the **LeRobot** framework and the SO-101 robot platform.

This repository documents my hands-on experience with the complete manipulation workflow, with particular emphasis on **robot setup, hardware–software integration, data collection, learning, and real-world troubleshooting**.
