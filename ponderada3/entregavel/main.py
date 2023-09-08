# -*- coding: utf-8 -*-

import pandas as pd
import pickle
from fastapi import FastAPI
import uvicorn
import json

# Create the app
app = FastAPI()

# Load trained Pipeline
pickled_model = pickle.load(open('model.pkl', 'rb'))


# Define predict function
@app.post("/predict")
def predict(age: int, sex: int, 
            cp: int, trtbps: int, 
            chol: int, fbs: int, 
            restecg: int, thalachh: int, 
            exng: int, oldpeak: float, 
            slp: int, caa: int, thall: int):
    data = {'age': age, 'sex': sex, 
            'cp': cp, 'trtbps': trtbps, 
            'chol': chol, 'fbs': fbs, 
            'restecg': restecg, 'thalachh': thalachh, 
            'exng': exng, 'oldpeak': oldpeak,
            'slp': slp, 'caa': caa, 'thall': thall
            }
    data_df = pd.DataFrame([data])
    predictions = pickled_model.predict(data_df)
    return json.dumps(predictions[0], default=str)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
