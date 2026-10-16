# Biomedical Cell Instance Segmentation with Mask R-CNN

Durham University MSc, COMP52715 Deep Learning for Computer Vision and Robotics (biomedical image analysis coursework).

## Overview

Fine-tunes a COCO-pretrained **Mask R-CNN with ResNet-50-FPN** for instance-level cell detection and segmentation across microscopy images. Includes data validation, mask-to-box conversion, small-object anchors, train/validation split, final retraining, and dataset-level metrics.

- Data: 670 microscopy images; **600 official training / 70 official testing** (original course dataset not redistributed).
- Dev protocol: 540 training / 60 validation, trained for 10 epochs to select a duration; best validation epoch was 9. A fresh model was then retrained for 9 epochs on all 600 training images.
- Model: Mask R-CNN with ResNet-50-FPN and small-object anchors (8, 16, 32, 64, 128 px).

## Reported results (70-image course test partition)

| Metric | Value |
| --- | ---: |
| Mask AP50 | **0.9020** |
| Mask AP75 | **0.6204** |
| Mask mAP50–95 | **0.5699** |
| Instance precision / recall / F1 at IoU 0.50 | 0.8702 / 0.8870 / 0.8785 |
| Mean cell-count absolute error | 3.5571 |
| Union-mask Dice | 0.8998 |

**Important:** Mask AP uses the notebook's custom dataset-level 101-point interpolation implementation, **not** the unmodified COCO evaluator. All results are reported from the original coursework run and were not rerun during repository preparation.

## Files

- [`notebooks/cell_instance_segmentation.ipynb`](notebooks/cell_instance_segmentation.ipynb): complete model-development code with outputs cleared.
- `requirements.txt`: original submitted dependencies. Match PyTorch and TorchVision versions to your Python/CUDA installation.

## Running

1. Obtain the course microscopy dataset **through authorized means** and unpack as:
   ```text
   dataset/<ImageId>/images/<ImageId>.png
   dataset/<ImageId>/masks/*.png
   ```
2. Place the *official* `Data_Split.csv` next to the notebook (this course-provided split is not hosted here).
3. Install dependencies: `python -m pip install -r requirements.txt` (prefer a Python 3.11 GPU environment).
4. Run the notebook from this project folder. It expects `./dataset` and `./Data_Split.csv`; move the notebook to the project root or adjust its working directory accordingly.
5. Set `QUICK_DEBUG_MODE=False` for formal evaluation.

Model weights (about 88 MB), the original dataset, source microscopy images, and course submission PDFs are excluded. Training from scratch on authorized data is required unless you have the separate checkpoint.

## Limitations

- Dense or overlapping cells remain challenging at strict IoU thresholds.
- Images are from a course dataset; do not assume clinical suitability.
- The train/test split must be supplied to reproduce exact reported numbers.