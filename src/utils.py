import os 
import sys

import pandas as pd
import numpy as np

import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV as gridSearchCV

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj: 
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)
def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report={}
        tuned_models={}

        for name, model in models.items():
            para = param.get(name, {})
            gs = gridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_  # already refit on full training when refit=True
            y_test_pred = best_model.predict(X_test)

            r2_square = r2_score(y_test, y_test_pred)
            report[name] = r2_square
            tuned_models[name] = best_model

        return report, tuned_models
    except Exception as e:
        raise CustomException(e,sys)