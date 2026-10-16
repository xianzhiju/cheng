# Differential-Drive Robot Localization and Drive-to-Goal Control

Durham University COMP52815 Robotics coursework, using the course PuzzleBot framework.

## What is implemented

- `dead_reckoning.py`: differential-drive kinematics, incremental pose integration, angle wrapping, covariance propagation with Jacobians (`H @ Sigma @ H.T + G @ Q @ G.T`).
- `driveToGoal.py`: rotate-to-heading / drive-to-goal proportional controller with actuator limits, slowing near the goal, and stop tolerance.

The code was written against course-provided `lib.puzz_msgs` and `my_examples.dead_reckoning`. Those modules are **not bundled** in this repository, so the Python files are not standalone runnable without the PuzzleBot/course framework.

## Setup

1. Obtain access to the relevant robotics teaching simulator/runtime through authorized means.
2. Place `dead_reckoning.py` and `driveToGoal.py` inside the expected `my_examples/` directory of the course environment.
3. Install `numpy` (using the environment version supported by the runtime).
4. Run the experiment through the course simulator and observe pose/covariance and goal trajectories.

**Note:** target `(2, 1)` is an example used in the coursework; adjust to a valid scene before running. Wheel radius, baseline and controller gains should be validated for the simulated robot.

Large course demonstration video and submitted report are omitted. The code is a course simulation exercise, not physical-robot deployment evidence.