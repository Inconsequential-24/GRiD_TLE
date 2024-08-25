# Size Chart Prediction Project

## Overview
This project aims to predict accurate size charts for apparel sellers using machine learning. The model is trained on a dataset of body measurements and predicts appropriate clothing sizes.

## Directory Structure
- `data/`: Contains raw and processed datasets.
- `notebooks/`: Jupyter notebooks for EDA and model development.
- `scripts/`: Python scripts for data preprocessing, clustering, training, and predictions.
- `models/`: Saved models.
- `tests/`: Unit tests for scripts.
- `.vscode/`: VSCode configuration files.
- `requirements.txt`: List of dependencies.
- `README.md`: Project overview and documentation.

## Getting Started
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

# Size Chart Prediction - Clustering Analysis

## Overview
This project involves clustering analysis on a dataset of body measurements to identify distinct groups or clusters that could be used for creating personalized size charts. The primary goal is to leverage Agglomerative Clustering to segment the data into meaningful clusters.

## Methods Used
- **Data Preprocessing:** The dataset was cleaned by handling missing values, where random valid values or the mode were used to replace NaNs.
- **Clustering Algorithm:** Agglomerative Clustering with 5 clusters was chosen as the method to segment the data.
- **Statistical Analysis:** Post-clustering, statistical analysis was conducted to summarize each cluster's characteristics.
- **Visualization:** Pair plots and cluster distributions were visualized to interpret the clustering results.

## Key Statistics

### Cluster Counts
The dataset was divided into 5 clusters with the following distribution:

| Cluster | Count |
|---------|-------|
| 0       | 193   |
| 1       | 248   |
| 2       | 308   |
| 3       | 118   |
| 4       | 133   |

### Cluster Centroids
Each cluster's centroid was calculated to understand the typical characteristics of the data points within that cluster. Below is a summary of key features:

| Feature     | Cluster 0 | Cluster 1 | Cluster 2 | Cluster 3 | Cluster 4 |
|-------------|-----------|-----------|-----------|-----------|-----------|
| **Weight**  | 84.25     | 59.08     | 72.71     | 102.26    | 53.02     |
| **Bust/Chest** | 37.98   | 37.13     | 40.00     | 39.54     | 37.68     |
| **Waist**   | 31.29     | 28.73     | 37.95     | 34.87     | 37.57     |
| **Hips**    | 35.85     | 32.82     | 43.30     | 39.50     | 43.37     |

(Include more features as required)

### Cluster Standard Deviations
To understand the variability within each cluster, standard deviations were calculated for each feature:

| Feature     | Cluster 0 | Cluster 1 | Cluster 2 | Cluster 3 | Cluster 4 |
|-------------|-----------|-----------|-----------|-----------|-----------|
| **Weight**  | 6.07      | 6.89      | 6.21      | 6.51      | 6.21      |
| **Bust/Chest** | 6.22   | 5.91      | 6.73      | 6.55      | 5.24      |
| **Waist**   | 5.88      | 4.18      | 5.10      | 6.75      | 4.11      |
| **Hips**    | 6.55      | 4.83      | 4.64      | 6.74      | 3.91      |

(Include more features as required)


## Interpretation of Results
- **Cluster 0:** Represents a group with relatively higher weight and bust/chest measurements.
- **Cluster 1:** Represents individuals with lower weight and average bust/chest measurements.
- **Cluster 2:** Consists of individuals with balanced measurements across all features.
- **Cluster 3:** Represents individuals with the highest weight and relatively higher bust/chest measurements.
- **Cluster 4:** Represents a group with the lowest weight and higher waist and hips measurements.

These clusters can be used to create personalized size charts that cater to different body shapes and sizes.

## Next Steps
- **Refinement:** Consider experimenting with different numbers of clusters or clustering algorithms to see if better segmentation can be achieved.
- **Application:** Implement these findings into a production environment for creating personalized size charts or other related applications.

## Conclusion
The clustering analysis provided insights into distinct groups within the dataset, which can be valuable for personalizing size charts and improving customer satisfaction. Further refinement and validation could enhance the results.