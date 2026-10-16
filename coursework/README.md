# Computer Vision and Robotics Coursework Portfolio

Selected source-code projects from Durham University's Scientific Computing and Data Analysis (Computer Vision and Robotics) MSc coursework. These are **coursework / simulated experiments**, not peer-reviewed publications or production deployments.

| Project | Focus | Source |
| --- | --- | --- |
| [Biomedical Cell Instance Segmentation](./biomedical-cell-instance-segmentation/) | Mask R-CNN, image segmentation, evaluation | Jupyter notebook |
| [Monocular Visual Odometry](./monocular-visual-odometry/) | ORB, SIFT, CLAHE, essential matrix, RANSAC | Jupyter notebook |
| [Robot Localization and Goal Control](./robot-localization-and-control/) | Dead reckoning, covariance propagation, differential drive | Python modules |

## Academic-use and reproducibility notes

- The university-supplied datasets, course handouts, submitted reports, and large learned checkpoints are not published here. Supply data you are authorized to use before running the corresponding notebooks.
- Large recorded videos were excluded from this GitHub version to keep the repository lean; refer to each project README for expected paths.
- Notebook execution outputs and local filesystem paths were stripped to remove machine-specific or potentially sensitive traces.
- The robotics control scripts require the course's `puzz_msgs` / PuzzleBot runtime; the runtime is **not** redistributed.
- Please see each project for limitations. No claim of external test-set generalization, physical drone deployment, or peer-reviewed publication is made.

Author: Yinzheng Cheng.