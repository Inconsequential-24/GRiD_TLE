# AI-Powered Size Chart Generator for Apparel Sellers

## Project Overview

This project aims to create an AI-powered size chart generator tailored for apparel sellers, with a focus on integration with e-commerce platforms like Flipkart. The goal is to improve the accuracy of size recommendations, which can lead to higher customer satisfaction and reduced return rates. The solution leverages Agglomerative Clustering to categorize customers based on their body measurements and subsequently uses a Random Forest classifier to provide personalized size suggestions.

## Project Structure

The project is organized into several directories:

- **data/**: Contains raw and processed data files.
  - **processed/**: Includes the processed dataset for clustering and model training.
  - **raw/**: Holds the original raw dataset.
- **models/**: Stores the trained Random Forest model.
- **scripts/**: Includes various scripts for clustering, training, evaluating, and making predictions based on the model.
- **tests/**: Contains unit tests for data preprocessing, clustering, model training, and prediction scripts.
- **README.md**: The project documentation.
- **requirements.txt**: Lists the Python dependencies needed for the project.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Installation Steps

1. **Clone the Repository**: Clone the project repository to your local machine and navigate into the project directory.

2. **Install Dependencies**: Install the necessary Python packages using pip.

## Running the Project

### Step 1: Data Preparation

Ensure that the `processed_data.csv` file is present in the `data/processed/` directory. This file should contain cleaned and preprocessed data ready for clustering.

### Step 2: Perform Clustering

Run the clustering script to group the data based on body measurements. This will generate the `clustered_data.csv` file in the `data/processed/` directory.

### Step 3: Train the Model

Train the Random Forest model on the clustered data. The trained model will be saved in the `models/` directory.

### Step 4: Evaluate the Model

Evaluate the model's performance by running the evaluation script. This script will output metrics such as accuracy, precision, recall, and f1-score.

### Step 5: Make Predictions

To predict the size cluster for a new set of user measurements, run the prediction script. Follow the prompts to input the measurements and receive a size recommendation.

## Pipeline Overview

The pipeline consists of the following stages:

1. **Data Preprocessing**: Load the processed data, perform Agglomerative Clustering on selected features, and save the clustered data.
2. **Cluster Analysis**: Perform statistical analysis on the clustered data and generate visualizations to explore feature distributions.
3. **Model Training**: Train a Random Forest classifier on the clustered data, evaluate its performance, and save the trained model.
4. **Model Evaluation**: Evaluate the trained model on a test set and generate a performance report.
5. **Prediction**: Use the trained model to predict the size cluster based on user measurements.
6. **Testing**: Validate each component of the project through unit tests.

## Challenges with Dataset

### Missing Values

The dataset contained missing values, particularly in the height feature. Initial attempts to drop rows with missing values led to a significant loss of data. To address this, missing values were imputed with the most frequent value or randomly selected from existing valid entries in the column.

### Data Imbalance

Some clusters had a disproportionately low number of data points, which could potentially affect the model's performance. Addressing this involved careful parameter tuning and possibly oversampling underrepresented clusters during model training.

## Testing

The project includes unit tests to ensure the reliability and accuracy of each component:

- **Data Preprocessing**: Tested through the data preprocessing unit test script.
- **Clustering Process**: Verified to ensure correct cluster assignment.
- **Model Training**: The training process and model accuracy are validated through unit tests.
- **Prediction**: The functionality of the prediction script is tested to ensure accurate predictions.

To execute the tests, use the provided testing framework.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
