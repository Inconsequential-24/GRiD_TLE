import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def load_clustered_data(file_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/data/processed/clustered_data.csv'):
    return pd.read_csv(file_path)

def train_model(data, model_save_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/models/trained_model.pkl'):
    X = data[['Height_in', 'Weight', 'Bust/Chest', 'Waist', 'Hips']]
    y = data['Cluster']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model trained with accuracy: {accuracy:.2f}")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    
    # Save the trained model
    joblib.dump(model, model_save_path)
    print(f"Trained model saved to {model_save_path}")

if __name__ == "__main__":
    df = load_clustered_data()
    train_model(df)