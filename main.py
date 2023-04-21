from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

with open('./files/fakeNewsDetection_model.sav', 'rb') as model_file:
    model = pickle.load(model_file)


@app.get("/")
def read_root():
    return {"VOIR": "/docs"}

@app.get("/news/?t={title}&c={content}")
def read_item(title: Union[str, None] = None, content: Union[str, None] = None):
    return {"title": title,"content": content}


@app.get("/news/{title}")
def read_item(title: Union[str, None] = None):
    return {"title": title}

@app.get("/news/?c={content}")
def read_item(content: Union[str, None] = None):
    return {"content": content}

class InputData(BaseModel):
    titre: string
#     content: string

@app.post('/predict')
def predict(data: InputData):
    form_data = data.dict()
    X_new = pd.DataFrame([form_data])
    y_pred = model.predict(X_new)
    return {'prediction': y_pred[0]}
