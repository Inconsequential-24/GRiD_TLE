import sys
import os
import unittest

# Add the 'scripts' directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from clustering import load_processed_data, perform_agglomerative_clustering # type: ignore

class TestClustering(unittest.TestCase):
    def test_load_processed_data(self):
        # Your test code here
        pass

    def test_perform_agglomerative_clustering(self):
        # Your test code here
        pass

if __name__ == '__main__':
    unittest.main()