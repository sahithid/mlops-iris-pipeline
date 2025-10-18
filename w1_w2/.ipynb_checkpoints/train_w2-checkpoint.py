import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
#import pickle
import joblib
import time

data_version = "v1"
if len(sys.argv) > 1:
    data_version = sys.argv[1]

data = pd.read_csv(f"data/{data_version}_data.csv")
#data_v2 = pd.read_csv("data/v2_data.csv")
print(f"Running on data {data_version}")

def train(version, data):
    train, test = train_test_split(data, test_size = 0.4, stratify = data['species'], random_state = 42)
    X_train = train[['sepal_length','sepal_width','petal_length','petal_width']]
    y_train = train.species
    X_test = test[['sepal_length','sepal_width','petal_length','petal_width']]
    y_test = test.species
    mod_dt = DecisionTreeClassifier(max_depth = 3, random_state = 1)
    mod_dt.fit(X_train,y_train)
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    prediction=mod_dt.predict(X_test)
    print('The accuracy of the Decision Tree is',"{:.3f}".format(metrics.accuracy_score(prediction,y_test)))
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    OUTPUT_FOLDER = f"artifacts/model_{version}"
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    joblib.dump(mod_dt, f"{OUTPUT_FOLDER}/model_{timestamp}.joblib")
    print("Model saved to artifacts")
    
    out_path = f"outputs/{version}/predictions_{timestamp}.csv"
    pd.DataFrame({f"predicted_{version}": prediction}).to_csv(out_path, index=False)
    print("Predictions saved to outputs")
    

train(data_version,data)