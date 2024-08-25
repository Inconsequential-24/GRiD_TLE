import unittest
import os
from scripts.train_model import train_model
from scripts.evaluate_model import evaluate_model

class TestModel(unittest.TestCase):
    
    def test_train_model(self):
        accuracy = train_model()
        self.assertGreaterEqual(accuracy, 0.9)
        self.assertTrue(os.path.exists('/Users/juhidwivedi/Desktop/GRiD SDE/size-chart-prediction/models/trained_model.pkl'))
    
    def test_evaluate_model(self):
        report = evaluate_model()
        self.assertIn('precision', report)
        self.assertIn('recall', report)
        self.assertIn('f1-score', report)

if __name__ == '__main__':
    unittest.main()