# AI-Powered Size Chart Generator for Apparel Sellers

## Project Overview

This project aims to build an AI-powered size chart generator for apparel sellers, particularly designed to integrate with e-commerce platforms like Flipkart. The system uses Agglomerative Clustering to group customers based on their body measurements and provides personalized size recommendations, helping to improve customer satisfaction and reduce size-related returns.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Setup and Installation](#setup-and-installation)
4. [Running the Project](#running-the-project)
5. [Pipeline Overview](#pipeline-overview)
6. [Challenges with Dataset](#challenges-with-dataset)
7. [Testing](#testing)
8. [License](#license)

## Project Structure

```bash
size-chart-prediction/
│
├── data/
│   ├── processed/
│   │   ├── processed_data.csv
│   │   └── clustered_data.csv
│   └── raw/
│       └── raw_data.csv
│
├── models/
│   └── trained_model.pkl
│
├── scripts/
│   ├── clustering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
│
├── tests/
│   ├── test_data_preprocessing.py
│   ├── test_clustering.py
│   ├── test_model.py
│   └── test_predict.py
│
├── README.md
└── requirements.txt

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Installation Steps

1. Clone the Repository
   ```bash
   git clone <repository-url>
   cd size-chart-prediction```

2.	Install Dependencies
    Install the necessary Python packages using pip:
    ```bash
    pip install -r requirements.txt
## Running the Project

### Step 1: Data Preparation

Ensure that the `processed_data.csv` file is present in the `data/processed/` directory. This file should contain cleaned and preprocessed data ready for clustering.

### Step 2: Perform Clustering

Run the clustering script to group the data based on body measurements:
```bash
python3 scripts/clustering.py

This will generate clustered_data.csv in the data/processed/ directory.

###Step 3: Train the Model

Train the Random Forest model on the clustered data:
```bash
python3 scripts/train_model.py

### Step 4: Evaluate the Model

Evaluate the model’s performance by running:

```bash
python3 scripts/evaluate_model.py

This script will output metrics such as accuracy, precision, recall, and f1-score.

### Step 5: Make Predictions

To predict the size cluster for a new set of user measurements:
```bash
python3 scripts/predict.py

Follow the prompts to input the measurements and receive a size recommendation.



