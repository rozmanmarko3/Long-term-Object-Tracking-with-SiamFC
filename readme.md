# Long-term Object Tracking with SiamFC

This project implements a long-term object tracking system using SiamFC (Siamese Fully-Convolutional) neural network with custom enhancements for handling occlusions and target reappearance.

## Project Structure

- **Core Files:**
  - [`run_tracker.py`](run_tracker.py) - Main tracker runner script
  - [`siamfc_lt/`](siamfc_lt/) - Long-term SiamFC tracker implementation
  - [`performance_evaluation.py`](performance_evaluation.py) - Evaluation metrics calculation

- **Experiments:**
  - [`naloga3.py`](naloga3.py) - Threshold parameter tuning
  - [`naloga4.py`](naloga4.py) - Redetection parameter optimization  
  - [`naloga5.py`](naloga5.py) - Basic tracker evaluation
  - [`naloga6.py`](naloga6.py) - Enhanced tracker with 2D Gaussian sampling

- **Results:**
  - [`results3.csv`](results3.csv), [`results4.csv`](results4.csv) - Performance metrics
  - [`tracking_results/`](tracking_results/) - Visual tracking outputs
  - [`report/`](report/) - Project documentation

## Usage

Run the tracker on a dataset:
```bash
python run_tracker.py --dataset dataset/ --net siamfc_net.pth --results_dir results/ [--visualize]
```

Evaluate performance:
```bash
python performance_evaluation.py --dataset dataset/ --results_dir results/
```

## Key Features

- Long-term tracking with occlusion handling
- 2D Gaussian sampling for target reappearance detection
- Configurable detection thresholds and search parameters
- Comprehensive performance evaluation (Precision, Recall, F-score)

## Dataset

The tracker is tested on sequences including car9, cat1, dog, and skiing from the [`dataset/`](dataset/) directory.