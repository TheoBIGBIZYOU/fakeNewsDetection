from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import sklearn
import pickle
import pandas as pd

app = FastAPI()

with open('./files/fakeNewsDetection_model.sav', 'rb') as model_file:
    model = pickle.load(model_file)


with open('./files/tfidf_dump.pickle', 'rb') as tfidf_file:
    tfidf = pickle.load(tfidf_file)


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
    title: str
#     content: str


@app.post('/predict')
def predict(data: InputData):
    print(data)
    print(data.title)

    title = tfidf.transform([data.title]).toarray()
    y_pred = model.predict(title)
    return {'prediction': str(y_pred[0])}
