import unittest
import pandas as pd
from scripts.data_preprocessing import preprocess_data, load_data

class TestDataPreprocessing(unittest.TestCase):
    def test_preprocess_data(self):
        df = load_data()
        df_preprocessed = preprocess_data(df)
        self.assertIn('Height_in', df_preprocessed.columns)
        self.assertIn('Gender', df_preprocessed.columns)
        self.assertFalse(df_preprocessed.isnull().sum().any())

if __name__ == '__main__':
    unittest.main()