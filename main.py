""" Weather Web app using FastAPI."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """ it is a test api."""
    return {"Hello": "World"}
