import joblib  
import unittest
import os
import pandas as pd
import subprocess
from sklearn.metrics import accuracy_score
import mlflow 
from mlflow import MlflowClient


class TestModel(unittest.TestCase):
    
    def setUp(self):
        self.version= "v2"
        print("Pulling input data from DVC")
        subprocess.run(['dvc', 'pull', 'week5/data.dvc', '-v'], check=True)

        data_path = 'week5/data/iris.csv'
        self.test_data = pd.read_csv(data_path)
        self.X_test = self.test_data[['sepal_length','sepal_width','petal_length','petal_width']]
        self.y_test = self.test_data['species']
        
        print("Pulling model from mlflow")
        #model_path = f'week4/artifacts/model_v1/w4_model.joblib'
        #subprocess.run(['dvc', 'pull', model_path, '-v'], check=True)
        
        print("Loading model from mlflow")
        mlflow.set_tracking_uri("http://127.0.0.1:8100")
        client = MlflowClient(mlflow.get_tracking_uri())
        model_name = "Iris_DecisionTree_Classifier"
        #latest_model = client.get_latest_versions(model_name, stages=["None"])
        #print(latest_model[-1])
        
        #get best model 
        #all_runs = client.search_runs([e_id], order_by = ["metrics.accuracy DESC"], max_results = 1)
        #best_model = all_runs[0]
        
        versions = client.search_model_versions(f"name='{model_name}'")
        #print(versions)
        
        best_version = 1 
        max_accuracy = -1.0
        
        for ver in versions: 
            run_id = ver.run_id 
            metrics = client.get_run(run_id).data.metrics
            accuracy = metrics.get("accuracy", -1.0)
            if accuracy > max_accuracy: 
                best_version = ver.version 
                max_accuracy = accuracy
            
        
        self.model = mlflow.sklearn.load_model(f'models:/{model_name}/{best_version}')
        print(f'Using Model: {model_name} | Version: {best_version}')
        
    
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
        
        
    # def test_duplicate_values(self):
    #     self.assertEqual(self.test_data.duplicated().sum(), 0, "Dataset contains duplicate rows")
    
    #Evaluation Test
    def test_model_accuuracy(self):
        print("Running Prediction") 
        print(self.model)
        prediction=self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, prediction)
        self.assertGreaterEqual(accuracy, 0.5, "Model Accuracy must be >= 0.5")
        

if __name__ == '__main__':
    unittest.main()
        
        