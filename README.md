# AI-Powered Size Chart Generator for Apparel Sellers

## Project Overview

This project aims to create an AI-powered size chart generator tailored for apparel sellers, with a focus on integration with e-commerce platforms like Flipkart. The goal is to improve the accuracy of size recommendations, which can lead to higher customer satisfaction and reduced return rates. The solution leverages Agglomerative Clustering to categorize customers based on their body measurements and subsequently uses a Random Forest classifier to provide personalized size suggestions.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
   - [Data Directory](#data-directory)
   - [Processed Directory](#processed-directory)
   - [Raw Directory](#raw-directory)
   - [Models Directory](#models-directory)
   - [Scripts Directory](#scripts-directory)
   - [Tests Directory](#tests-directory)
   - [README File](#readme-file)
   - [Requirements File](#requirements-file)
3. [Setup and Installation](#setup-and-installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [Running the Project](#running-the-project)
   - [Step 1: Data Preparation](#step-1-data-preparation)
   - [Step 2: Perform Clustering](#step-2-perform-clustering)
   - [Step 3: Train the Model](#step-3-train-the-model)
   - [Step 4: Evaluate the Model](#step-4-evaluate-the-model)
   - [Step 5: Make Predictions](#step-5-make-predictions)
5. [Pipeline Overview](#pipeline-overview)
6. [Challenges with Dataset](#challenges-with-dataset)
   - [Missing Values](#missing-values)
   - [Data Imbalance](#data-imbalance)
7. [Testing](#testing)
8. [License](#license)

## Project Structure

The project is organized into several directories:

- **[data/](#data-directory)**: Contains raw and processed data files.
  - **[processed/](#processed-directory)**: Includes the processed dataset for clustering and model training.
  - **[raw/](#raw-directory)**: Holds the original raw dataset.
- **[models/](#models-directory)**: Stores the trained Random Forest model.
- **[scripts/](#scripts-directory)**: Includes various scripts for clustering, training, evaluating, and making predictions based on the model.
- **[tests/](#tests-directory)**: Contains unit tests for data preprocessing, clustering, model training, and prediction scripts.
- **[README.md](#readme-file)**: The project documentation.
- **[requirements.txt](#requirements-file)**: Lists the Python dependencies needed for the project.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Installation Steps

1. **Clone the Repository**: Clone the project repository to your local machine and navigate into the project directory.
   ```bash
   git clone <repository-url>
   cd size-chart-prediction
   ```

3. **Install Dependencies**: Install the necessary Python packages using pip.

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

## Detailed Section Links

### Data Directory

The `data/` directory contains all the data files used in the project.

### Processed Directory

The `processed/` directory within `data/` includes the cleaned and preprocessed dataset that is used for clustering and model training.

### Raw Directory

The `raw/` directory within `data/` holds the original raw dataset before any processing.

### Models Directory

The `models/` directory stores the trained Random Forest model that has been generated after training.

### Scripts Directory

The `scripts/` directory includes various Python scripts for different stages of the project:
- Clustering the data
- Training the machine learning model
- Evaluating the model's performance
- Making predictions based on input features

### Tests Directory

The `tests/` directory contains unit tests that verify the accuracy and reliability of each component of the project, including:
- Data preprocessing
- Clustering process
- Model training
- Prediction scripts

### README File

The `README.md` file provides documentation for the project, including setup instructions, project structure, and usage guidelines.

### Requirements File

The `requirements.txt` file lists all the Python dependencies required to run the project, ensuring that all necessary packages are installed.
