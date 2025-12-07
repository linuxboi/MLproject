from flask import Flask,render_template, request
import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, predictPipeline


application = Flask(__name__)
app = application


##route for homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # default to empty string to avoid None categories at inference time
        data=CustomData(
            gender=request.form.get('gender',''),
            race_ethnicity=request.form.get('race_ethnicity',''),
            parental_level_of_education=request.form.get('parental_level_of_education',''),
            lunch=request.form.get('lunch',''),
            test_preparation_course=request.form.get('test_preparation_course',''),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        final_new_data = data.get_data_as_data_frame()
        predict_pipeline = predictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        return render_template('home.html', prediction=pred[0]) 
if __name__=="__main__":
    app.run(host='0.0.0.0')