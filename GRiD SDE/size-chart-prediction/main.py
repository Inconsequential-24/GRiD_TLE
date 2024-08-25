from scripts.data_preprocessing import load_data, preprocess_data, save_preprocessed_data
from scripts.clustering import perform_clustering, save_clustered_data, save_model
from scripts.train_model import train_model, save_model as save_trained_model
from scripts.evaluate_model import evaluate_model, load_model
from scripts.predict import predict_size
import pandas as pd

def run_pipeline():
    # Step 1: Data Preprocessing
    df = load_data()
    df_preprocessed = preprocess_data(df)
    save_preprocessed_data(df_preprocessed)
    
    # Step 2: Clustering
    df_clustered, kmeans_model = perform_clustering(df_preprocessed)
    save_clustered_data(df_clustered)
    save_model(kmeans_model, '../models/kmeans_model.pkl')
    
    # Step 3: Model Training
    model = train_model(df_clustered)
    save_trained_model(model, '../models/size_chart_model.pkl')
    
    # Step 4: Model Evaluation
    evaluate_model(model, df_clustered)
    
    # Step 5: Prediction (Example)
    new_data = pd.DataFrame({
        'Gender': [0],
        'Height_in': [66],
        'Weight': [70],
        'Bust/Chest': [38],
        'Cup Size_None': [1],
        'Waist': [32],
        'Hips': [36],
        'Cluster': [2]
    })
    predicted_size = predict_size(new_data)
    print(f'Predicted Size: {predicted_size}')

if __name__ == "__main__":
    run_pipeline()