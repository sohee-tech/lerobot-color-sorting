# LeRobot Color Sorting with Imitation Learning

## Overview

This project implements a color-sorting task using the **LeRobot SO-101 robotic arm**.

The robot learns to sort colored cubes through **Imitation Learning (ACT Policy)** based on human demonstrations.

Task:

- 🔴 Red Cube → Left Bin
- 🟢 Green Cube → Right Bin

---

## Features

- Robot motor setup
- Robot calibration
- Leader-Follower teleoperation
- RGB camera integration
- Demonstration dataset collection
- OpenCV-based color detection
- ACT policy training
- Autonomous color sorting evaluation

---

## Hardware

- LeRobot SO-101 Leader Arm
- LeRobot SO-101 Follower Arm
- USB RGB Cameras (Front / Wrist)

---

## Software

- Python
- OpenCV
- PyTorch
- LeRobot

---

## Project Pipeline

Robot Setup

↓

Calibration

↓

Teleoperation

↓

Dataset Collection

↓

ACT Policy Training

↓

Autonomous Color Sorting

---

## Dataset

Training Dataset

- 100 demonstrations
- Task:
  Sort the red cube to the left and the green cube to the right.

Additional Dataset

- 40 demonstrations
- Green-only data for performance improvement

---

## Training

Policy

- ACT (Action Chunking Transformer)

Framework

- LeRobot

GPU

- CUDA

---

## Color Detection

A custom OpenCV script was used to detect red and green cubes.

Functions

- HSV color segmentation
- Contour extraction
- Bounding box visualization
- Object center estimation

---

## Results

Example result

(images/result.gif)

(Add your GIF here.)

---

## Repository Structure

```
README.md
color_test.py
commands.md
images/
```

---

## Acknowledgements

This project is built on the LeRobot framework developed by Meta.

Custom work includes

- robot setup
- dataset collection
- OpenCV color detection
- training configuration
- experimental evaluation
