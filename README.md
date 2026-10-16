# Computer Vision & Robotics — Research Portfolio

**Yinzheng Cheng · Durham University MSc (Computer Vision and Robotics)**

A curated collection of **one MSc dissertation research project** and **three independent coursework projects**. Each project has its own source code, dependencies, documentation and experiment notes.

个人计算机视觉与机器人科研/课程项目集。毕业设计与课程项目分开存放，便于阅读、复现和简历引用。

## 01 · MSc Dissertation / 硕士毕业设计

### [Perception-Aware Multi-UAV Leader–Follower Coordination](dissertation/multi-uav-coordination/)

Decentralized leader reassignment using perception, communication and geometric suitability, combined with adaptive follower formation recovery. Baseline comparisons, ablations and scenario-level evaluations in a **simplified 2D simulation**.

- **Main code:** [Integrated leader–follower validation](dissertation/multi-uav-coordination/integrated_multi_uav_leader_follower_validation.ipynb)
- **Results:** [Experiment tables and plots](dissertation/multi-uav-coordination/integrated_uav_results/)
- **Reproducibility:** [Run order and limitations](dissertation/multi-uav-coordination/REPRODUCIBILITY.md)

![Leader strategy comparison](dissertation/multi-uav-coordination/integrated_uav_results/figures/fig1_compact_leader_validation.png)

## 02 · Coursework Projects / 课程项目

| Project / 项目 | Methods | Source code |
| --- | --- | --- |
| [Biomedical Cell Instance Segmentation](coursework/biomedical-cell-instance-segmentation/) 医学细胞实例分割 | Mask R-CNN, ResNet-50-FPN, instance segmentation | [Notebook](coursework/biomedical-cell-instance-segmentation/notebooks/cell_instance_segmentation.ipynb) |
| [Monocular Visual Odometry](coursework/monocular-visual-odometry/) 单目视觉里程计 | ORB, SIFT, essential matrix, RANSAC, pose recovery | [Notebook](coursework/monocular-visual-odometry/notebooks/monocular_visual_odometry.ipynb) |
| [Robot Localization and Control](coursework/robot-localization-and-control/) 机器人定位与运动控制 | Dead reckoning, covariance propagation, drive-to-goal control | [Python source](coursework/robot-localization-and-control/dead_reckoning.py) |

See the [coursework overview](coursework/README.md) for input-data requirements and limitations.

## Repository layout

```text
.
├── dissertation/
│   └── multi-uav-coordination/     # Dissertation code, results, plots & docs
├── coursework/
│   ├── biomedical-cell-instance-segmentation/
│   ├── monocular-visual-odometry/
│   └── robot-localization-and-control/
├── .gitignore
└── README.md
```

## Reproduction & responsible use

- Read each project's README for setup and execution instructions; notebooks may require datasets or runtime environments **not included** here.
- Published output tables are from coursework and simulation experiments, **not clinical systems, field-tested drone software, or production deployments**.
- University datasets, course handouts, videos, large model checkpoints, and submitted assessment PDFs are not redistributed.
- **No open-source license** has been assigned. Contact the author for reuse/redistribution permissions.

**Author:** Yinzheng Cheng
