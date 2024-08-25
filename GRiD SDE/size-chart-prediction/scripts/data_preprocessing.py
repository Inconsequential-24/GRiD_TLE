import os
import pandas as pd
import numpy as np

def load_data(file_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/data/raw/body_measurements_dataset.csv'):
    """
    Load the raw data from the CSV file.
    """
    data = pd.read_csv(file_path)
    print(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
    return data

def preprocess_data(data):
    """
    Preprocess the raw data.
    - Fill missing 'Cup Size' with 'None'
    - Convert categorical columns to numerical
    - Convert height from feet and inches to inches
    - Handle missing values in numerical columns
    """
    # Fill missing 'Cup Size' values with 'None'
    data['Cup Size'] = data['Cup Size'].fillna('None')

    # Convert height from feet and inches to inches
    def convert_height(height_str):
        if pd.isna(height_str):
            return np.nan
        try:
            feet, inches = height_str.split("'")
            feet = int(feet.strip())
            inches = int(inches.strip().replace('"', ''))
            return feet * 12 + inches
        except ValueError:
            return np.nan

    data['Height_in'] = data['Height'].apply(convert_height)

    # Convert categorical to numerical
    data['Gender'] = data['Gender'].apply(lambda x: 1 if x == 'Female' else 0)
    cup_size_columns = ['None', 'A', 'B', 'C', 'D', 'DD', 'E', 'F']
    for size in cup_size_columns:
        data[f'Cup Size_{size}'] = data['Cup Size'].apply(lambda x: 1 if x == size else 0)

    # Handle missing values for numerical columns
    for col in ['Height_in', 'Weight', 'Bust/Chest', 'Waist', 'Hips']:
        mode_value = data[col].mode()[0] if not data[col].mode().empty else np.nan
        data[col] = data[col].fillna(mode_value)
    
    print("Data preprocessing completed.")
    
    return data

def save_preprocessed_data(data, file_path='/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/data/processed/processed_data.csv'):
    """
    Save the preprocessed data to a CSV file.
    - Create the directory if it doesn't exist
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the processed data
    data.to_csv(file_path, index=False)
    print(f"Data saved successfully at {file_path}")

if __name__ == "__main__":
    # Load the raw data
    df = load_data()

    # Preprocess the data
    df_preprocessed = preprocess_data(df)

    # Save the preprocessed data
    save_preprocessed_data(df_preprocessed)