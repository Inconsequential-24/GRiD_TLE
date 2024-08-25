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
