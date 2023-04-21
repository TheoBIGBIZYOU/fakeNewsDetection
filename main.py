from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import sklearn
import pickle
import pandas as pd

app = FastAPI()

# Ici on récupère le model de notre IA ainsi que TFIDF ( besoin pour vectoriser )
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
    titre: str
#     content: string


# Prediction ou on récupère les data du formulaire,
# on transforme le titre en vecteur car il ne comprend pas le string
# et on fait notre prédiction qui renvoi 0 ou 1
@app.post('/predict')
def predict(data: InputData):
    print(data)
    print(data.titre)

    titre = tfidf.transform([data.titre]).toarray()
    y_pred = model.predict(titre)
    return {'prediction': str(y_pred[0])}
