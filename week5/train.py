import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
import joblib
import time
import mlflow
from mlflow import MlflowClient
from mlflow.models import infer_signature

#set up mlflow ----------------------------------

mlflow.set_tracking_uri("http://127.0.0.1:8100")

# BUCKET_NAME= "mlops-course-gentle-presence-472611-u8-v4-unique-week1"

# os.environ["MLFLOW_ARTIFACT_URI"] = f'gs://{BUCKET_NAME}/mlflow_model'

client = MlflowClient(mlflow.get_tracking_uri())
all_experiments = client.search_experiments() 
print(all_experiments)
mlflow.set_experiment("IRIS Classifier - Mlflow Integration")

#get inpu data --------------------------------
data_version = "v1"
if len(sys.argv) > 1:
    data_version = sys.argv[1]

#data = pd.read_csv(f"week4/data/{data_version}_data.csv")
data = pd.read_csv("week5/data/iris.csv")

#print(f"Running on data {data_version}")


#train function --------------------------------
def train(version, data):
    train, test = train_test_split(data, test_size = 0.4, stratify = data['species'], random_state = 42)
    X_train = train[['sepal_length','sepal_width','petal_length','petal_width']]
    y_train = train.species
    X_test = test[['sepal_length','sepal_width','petal_length','petal_width']]
    y_test = test.species
    
    params = { 
        "max_depth": 3, 
        "random_state":1
    }
    
    mod_dt = DecisionTreeClassifier(**params)
    mod_dt.fit(X_train,y_train)
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    prediction=mod_dt.predict(X_test)
    accuracy_score = metrics.accuracy_score(prediction,y_test)
    print('The accuracy of the Decision Tree is',"{:.3f}".format(accuracy_score))
    
    #dump model to artifacts folder 
    joblib.dump(mod_dt, "week5/artifacts/w5_model.joblib")
    print("Model saved to artifacts")
    
    # out_path = f"week4/outputs/{version}/predictions.csv"
    # pd.DataFrame({f"predicted_{version}": prediction}).to_csv(out_path, index=False)
    # print("Predictions saved to outputs")
    with mlflow.start_run():
        print("Artifact URI:", mlflow.get_artifact_uri())
        mlflow.log_params(params)
        mlflow.log_metric("accuracy", accuracy_score) 
        mlflow.set_tag("Training Info", "DecisionTreeClassifier model")
        signature = infer_signature(X_train, mod_dt.predict(X_train))
        model_info = mlflow.sklearn.log_model(
            sk_model = mod_dt, 
            name = "mlflow_model", 
            signature = signature, 
            input_example = X_train, 
            registered_model_name = "Iris_DecisionTree_Classifier",
        )
        

train(data_version,data)

