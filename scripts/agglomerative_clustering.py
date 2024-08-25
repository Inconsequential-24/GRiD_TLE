import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import os

def load_processed_data(file_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/data/processed/processed_data.csv'):
    """
    Load the processed data from the CSV file.
    """
    data = pd.read_csv(file_path)
    print(f"Processed data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
    return data

def perform_agglomerative_clustering(data, n_clusters=5):
    """
    Perform Agglomerative Clustering on the data.
    """
    agg_clustering = AgglomerativeClustering(n_clusters=n_clusters)
    data['Cluster'] = agg_clustering.fit_predict(data[['Height_in', 'Weight', 'Bust/Chest', 'Waist', 'Hips']])
    print("Agglomerative Clustering completed.")
    return data, agg_clustering

def save_clustered_data(data, file_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/data/processed/clustered_data.csv'):
    """
    Save the clustered data to a CSV file.
    - Create the directory if it doesn't exist
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the clustered data
    data.to_csv(file_path, index=False)
    print(f"Clustered data saved successfully at {file_path}")

if __name__ == "__main__":
    # Load the processed data
    df = load_processed_data()

    # Perform Agglomerative Clustering
    df_clustered, clustering_model = perform_agglomerative_clustering(df)

    # Save the clustered data
    save_clustered_data(df_clustered)

    # Optional: Visualize the clusters
    plt.scatter(df_clustered['Height_in'], df_clustered['Weight'], c=df_clustered['Cluster'])
    plt.xlabel('Height (inches)')
    plt.ylabel('Weight')
    plt.title('Agglomerative Clustering')
    plt.show()