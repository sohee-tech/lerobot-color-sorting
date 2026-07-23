# ACT Policy Training

## Overview

The robot was trained using the ACT (Action Chunking Transformer) policy provided by the LeRobot framework.

The objective was to learn a color sorting task from human demonstrations collected through teleoperation.

---

## Dataset

Two datasets were collected.

### Main Dataset

- Task: Sort the red cube to the left and the green cube to the right
- Demonstrations: 100 episodes

### Additional Dataset

To improve the success rate for green cube manipulation, an additional dataset was collected.

- Task: Pick the green cube and place it in the right bin
- Demonstrations: 40 episodes

Total demonstrations:

- **140 episodes**

---

## Training Configuration

| Parameter | Value |
|-----------|-------|
| Policy | ACT |
| Device | CUDA |
| Batch Size | 64 |
| Training Steps | 10,000 |
| Framework | LeRobot |

---

## Training Command

```bash
lerobot-train \
  --dataset.repo_id=my_workspace/sort_red_green_cubes_v9 \
  --policy.type=act \
  --policy.device=cuda \
  --output_dir=outputs/sort_policy_today \
  --batch_size=64 \
  --steps=10000
```

---

## Outcome

The trained ACT policy was successfully deployed on the SO-101 robotic arm and evaluated on real-world color sorting tasks.

Additional demonstrations for the green cube improved the policy's performance.
