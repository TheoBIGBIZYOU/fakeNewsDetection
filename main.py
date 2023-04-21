from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"VOIR": "/docs"}

@app.get("/news/?t={title}&c={content}")
def read_item(title: Union[str, None] = None, content: Union[str, None] = None):
    return {"title": title,"content": content}


@app.get("/news/{title}")
def read_item(title: Union[str, None] = None):
    return {"title": title}

@app.get("/news/{content}")
def read_item(content: Union[str, None] = None):
    return {"content": content}