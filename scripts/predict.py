import joblib
import numpy as np

def load_model(model_path='models/trained_model.pkl'):
    model = joblib.load(model_path)
    if not hasattr(model, 'predict'):
        raise ValueError("The loaded object is not a valid scikit-learn model.")
    print("Model loaded successfully.")
    return model

def predict_size(model, features):
    # Ensure the features are in the correct format (list of lists for a single prediction)
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]

def simulate_user_interaction(model):
    print("Simulating User Interaction...")
    
    # Simulated user inputs their measurements
    features_list = [70, 150, 38, 32, 40]  # Example: [Height_in, Weight, Bust/Chest, Waist, Hips]
    print(f"User's measurements: {features_list}")
    
    # Model predicts the cluster for these measurements
    predicted_cluster = predict_size(model, features_list)
    print(f"Predicted Cluster: {predicted_cluster}")
    
    # Based on the cluster, we could provide a size recommendation (this is a basic example)
    size_recommendation = {
        0: "Size M",
        1: "Size S",
        2: "Size L",
        3: "Size XL",
        4: "Size XS"
    }
    
    print(f"Recommended Size: {size_recommendation.get(predicted_cluster, 'Unknown Size')}")

if __name__ == "__main__":
    model = load_model()
    simulate_user_interaction(model)