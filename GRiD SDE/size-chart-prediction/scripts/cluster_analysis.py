import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
import re

def load_clustered_data(file_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/data/processed/clustered_data.csv'):
    """
    Load the clustered data from the CSV file.
    """
    data = pd.read_csv(file_path)
    print(f"Clustered data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
    return data

def convert_height_to_inches(height_str):
    """
    Convert height from feet and inches (e.g., "6'1\"") to total inches.
    """
    if isinstance(height_str, str):
        match = re.match(r"(\d+)'(\d+)\"", height_str)
        if match:
            feet = int(match.group(1))
            inches = int(match.group(2))
            return feet * 12 + inches
    return np.nan

def clean_data(data):
    """
    Clean data by filling NaN values with a random valid value from the column or a default value.
    Ensure all relevant columns are numeric.
    """
    # Convert height columns from string format to inches
    data['Height_in'] = data['Height'].apply(convert_height_to_inches)

    for col in data.columns:
        if data[col].isnull().any() or (data[col] == '').any():
            if data[col].dtype in [np.float64, np.int64]:
                # Check if there are any valid values to choose from
                valid_values = data[col].dropna().values
                if len(valid_values) > 0:
                    data[col] = data[col].apply(lambda x: random.choice(valid_values) if pd.isnull(x) or x == '' else x)
                else:
                    # If the column is entirely NaN or empty, set a default value (e.g., 0 or mean of other columns)
                    data[col] = data[col].fillna(0)
            else:
                # Attempt to convert to numeric if it's supposed to be
                data[col] = pd.to_numeric(data[col], errors='coerce')
                # Check if there are any valid values to choose from after conversion
                valid_values = data[col].dropna().values
                if len(valid_values) > 0:
                    data[col] = data[col].apply(lambda x: random.choice(valid_values) if pd.isnull(x) else x)
                else:
                    # For non-numeric, set a default value or fill with random valid value from the column
                    data[col] = data[col].fillna("Unknown")

    print(f"Data cleaned. Remaining rows after cleaning: {len(data)}")
    return data

def perform_statistical_analysis(data):
    """
    Perform statistical analysis on the clustered data.
    - Calculate the number of samples in each cluster
    - Calculate the mean values (centroids) for each cluster
    - Calculate the standard deviation for each cluster
    """
    cluster_groups = data.groupby('Cluster')

    # Only include numeric columns for aggregation
    numeric_cols = data.select_dtypes(include=[np.number]).columns

    # Number of samples in each cluster
    cluster_counts = cluster_groups.size()

    # Mean values for each cluster
    cluster_centroids = cluster_groups[numeric_cols].mean()

    # Standard deviation for each cluster
    cluster_std_dev = cluster_groups[numeric_cols].std()

    print("Cluster Counts:\n", cluster_counts)
    print("\nCluster Centroids:\n", cluster_centroids)
    print("\nCluster Standard Deviations:\n", cluster_std_dev)
    
    return cluster_counts, cluster_centroids, cluster_std_dev

def visualize_clusters(data):
    """
    Create visualizations for the clustered data.
    - Scatter plot for Height vs Weight with cluster labels
    - Pair plot for all features with cluster labels
    """
    # Scatter plot for Height vs Weight
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Height_in'], data['Weight'], c=data['Cluster'], cmap='viridis')
    plt.xlabel('Height (inches)')
    plt.ylabel('Weight')
    plt.title('Agglomerative Clustering: Height vs Weight')
    plt.colorbar(label='Cluster')
    plt.show()

    # Pair plot for all features
    sns.pairplot(data, hue='Cluster', vars=['Height_in', 'Weight', 'Bust/Chest', 'Waist', 'Hips'])
    plt.suptitle('Pair Plot of Features Colored by Cluster', y=1.02)
    plt.show()

if __name__ == "__main__":
    # Load the clustered data
    df_clustered = load_clustered_data()

    # Clean the data
    df_clustered = clean_data(df_clustered)

    # Perform statistical analysis
    cluster_counts, cluster_centroids, cluster_std_dev = perform_statistical_analysis(df_clustered)

    # Visualize the clusters
    visualize_clusters(df_clustered)