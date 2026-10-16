# Reproducibility and research notes

## Suggested experiment order

1. **Model baseline:** `multi_uav_modeling_notebook.ipynb`
2. **Leader strategy prototyping:** `perception_aware_uav_experiment_analysis.ipynb`
3. **Scenario-level comparison:** `multi_scenario_validation_statistics.ipynb`
4. **Follower ablation:** `follower_formation_response_ablation.ipynb` then `follower_formation_response_ablation_v2.ipynb`
5. **Integrated evaluation:** `integrated_multi_uav_leader_follower_validation.ipynb`
6. **Visual exploration:** `uav_formation_visualization_notebook.ipynb` and `uav_formation_visualization_with_animation.ipynb`

## Data and output files

Experiment CSVs under `integrated_uav_results`, `multi_scenario_results`, `follower_response_results` and `follower_response_v2_results` are retained to make reported findings inspectable without executing all runs. Plots are also provided. No external labelled dataset is claimed.

The animation notebook can generate HTML animations, but the exported HTML files were not included in version control because of their size. To regenerate them, run the animation notebook from the repository root.

## Known boundaries

The mathematical leader-selection and follower-control experiments take place in simplified 2D simulations; they do not constitute a full perception pipeline, physical drone flight-control stack, or hardware evaluation. Results should be interpreted within this experimental setup.
