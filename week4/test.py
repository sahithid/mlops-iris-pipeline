import joblib  
import unittest
import os
import pandas as pd
import subprocess
from sklearn.metrics import accuracy_score


class TestModel(unittest.TestCase):
    
    def setUp(self):
        self.version= "v2"
        print("Pulling input data from DVC")
        subprocess.run(['dvc', 'pull', 'week4/data.dvc', '-v'], check=True)

        data_path = f'week4/data/{self.version}_data.csv'
        self.test_data = pd.read_csv(data_path)
        self.X_test = self.test_data[['sepal_length','sepal_width','petal_length','petal_width']]
        self.y_test = self.test_data['species']
        
        print("Pulling model from DVC")
        model_path = f'week4/artifacts/model_v1/w4_model.joblib'
        subprocess.run(['dvc', 'pull', model_path, '-v'], check=True)
        
        print("Loading model from DVC")
        self.model = joblib.load(model_path)
        
    
    #Data Validation Tests
    
    def test_missing_values(self):
        self.assertFalse(self.test_data.isnull().any().any(), "Data contains missing values")
        
    def test_feature_columns(self):
        self.assertEqual(self.test_data['sepal_length'].dtype, 'float64', "sepal_length should be float64")
        self.assertEqual(self.test_data['sepal_width'].dtype, 'float64', "sepal_width should be float64")
        self.assertEqual(self.test_data['petal_length'].dtype, 'float64', "petal_length should be float64")
        self.assertEqual(self.test_data['petal_width'].dtype, 'float64', "petal_width should be float64")
        self.assertEqual(self.test_data['species'].dtype, 'object', "species should be categorical")
        #could be object or category 
        
        
    def test_duplicate_values(self):
        self.assertEqual(self.test_data.duplicated().sum(), 0, "Dataset contains duplicate rows")
    
    #Evaluation Test
    def test_model_accuuracy(self):
        print("Running Prediction") 
        prediction=self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, prediction)
        self.assertGreaterEqual(accuracy, 0.5, "Model Accuracy must be >= 0.5")
        

if __name__ == '__main__':
    unittest.main()
        
        