# Monocular Visual Odometry — ORB / SIFT + RANSAC

Durham University MSc robotics / computer vision coursework.

## Overview

Implements a classical **monocular visual odometry** pipeline with ORB matching on the provided teaching image sequence and SIFT + CLAHE on a more challenging self-recorded PuzzleBot video. Estimates relative camera movement through the essential matrix with RANSAC and `cv2.recoverPose`, then accumulates poses.

## Experiments

1. Feature matching quality: ORB versus SIFT on visually challenging inputs.
2. Relative pose estimation and visual trajectory comparison.
3. Gaussian noise robustness analysis (feature matches and RANSAC inliers).

**Limitations:** monocular trajectories have unknown absolute scale; texture scarcity and motion blur degrade tracking; calibration correctness matters. Results are coursework experiments, not a deployed SLAM system.

## Running

1. Install `python -m pip install -r requirements.txt`.
2. Open [`notebooks/monocular_visual_odometry.ipynb`](notebooks/monocular_visual_odometry.ipynb).
3. Use this directory as your notebook **working directory** (or adjust `PROJECT_ROOT` in its setup cell).
4. Supply your authorized input files in the following layout:
   ```text
   video/dataset_frames/*.png
   video/turn_plus.mp4
   calibration_result.npz
   ```
5. Run the notebook from top to bottom.

The university-provided teaching dataset and camera-calibration binary are **not uploaded** here. The self-recorded PuzzleBot video is also excluded from the GitHub upload to keep repository contents limited to source code. Without these inputs, full notebook execution is not possible.

The notebook's output cells were cleared for publication; the original submission included plots and comparisons. Results were not rerun during repository preparation.