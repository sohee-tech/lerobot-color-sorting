# Policy Evaluation

## Overview

After training the ACT policy, the model was evaluated on the real LeRobot SO-101 robotic arm.

The objective was to verify whether the robot could autonomously perform the learned color sorting task using the trained policy.

---

## Evaluation Task

The robot was required to:

- Pick up the **red cube** and place it into the **left bin**
- Pick up the **green cube** and place it into the **right bin**

The robot executed the task autonomously without human intervention.

---

## Evaluation Setup

- Robot: LeRobot SO-101 Follower
- Cameras:
  - Front Camera
  - Wrist Camera
- Policy: ACT
- Framework: LeRobot

---

## Evaluation Procedure

1. Load the trained ACT policy.
2. Capture images from the front and wrist cameras.
3. Predict robot actions using the trained model.
4. Execute the predicted actions.
5. Observe and record the sorting results.

---

## Evaluation Command

```bash
lerobot-record \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM0 \
  --robot.id=my_follower_arm \
  --robot.cameras="{front: {type: opencv, index_or_path: '/dev/video0', width: 640, height: 480, fps: 30, fourcc: YUYV}, wrist: {type: opencv, index_or_path: '/dev/video2', width: 640, height: 480, fps: 30, fourcc: YUYV}}" \
  --policy.path="outputs/sort_policy_today/checkpoints/last/pretrained_model" \
  --dataset.repo_id="my_workspace/eval_$(date +%H%M%S)" \
  --dataset.single_task="Sort the red cube to the left and the green cube to the right" \
  --dataset.num_episodes=1 \
  --dataset.episode_time_s=45 \
  --dataset.reset_time_s=8 \
  --dataset.push_to_hub=false
```

---

## Result

The trained ACT policy was successfully deployed to the real robotic system for autonomous color sorting experiments.

The evaluation confirmed that the robot could perform the learned manipulation task based on camera observations and the trained imitation learning policy.

---

## Future Improvements

- Increase the number of training demonstrations.
- Improve robustness under different lighting conditions.
- Extend the task to additional object categories.
- Improve generalization to unseen object positions.
