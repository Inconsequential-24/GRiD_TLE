import unittest
import pandas as pd
from scripts.predict import predict_size

class TestPrediction(unittest.TestCase):
    def test_predict_size(self):
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
        self.assertEqual(len(predicted_size), 1)

if __name__ == '__main__':
    unittest.main()