import pandas as pd
from sklearn.metrics import classification_report
import joblib
import os

def load_clustered_data(file_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/data/processed/clustered_data.csv'):
    return pd.read_csv(file_path)

def load_model(model_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/models/trained_model.pkl'):
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        raise FileNotFoundError(f"No model found at {model_path}")

def evaluate_model(data, model):
    X = data[['Height_in', 'Weight', 'Bust/Chest', 'Waist', 'Hips']]
    y_true = data['Cluster']
    
    y_pred = model.predict(X)
    
    report = classification_report(y_true, y_pred)
    print("Model Evaluation Report:\n")
    print(report)

if __name__ == "__main__":
    df = load_clustered_data()
    model = load_model()
    evaluate_model(df, model)