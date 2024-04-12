from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field
from enum import Enum

app = FastAPI()

# @app.get('/')
# def root():
#     return "Hello World"   # 문자열 반환

@app.get('/json')
def printJson():
    return {"Number": 12345}  # (key, value) 객체 반환

@app.get("/home/{name}")
def read_name(name:str):
    return {'name': name}

@app.get("/home_err/{name}")
def read_name_err(name:int):
    return {'name': name}

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, "message": "Deep Learning FTW!"}
    if model_name.value == 'lenet':
        return {'model_name': model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# get 방식
fake_item_db = [{'item_name': "Foo"}, {'item_name': 'Bar'}, {"item_name": "Baz"}]

@app.get('/items/{item_id}')
def read_item(item_id: str, skip: int=0, limit: int=10):
    return fake_item_db[skip: skip + limit]

# Post 방식
@app.get("/")
def home():
    return {"Hello": "GET"}

class DataInput(BaseModel):
    name : str

@app.post("/")
# def home_post(msg: str):
#     return {"Hello": "POST", "msg": msg}
def home_post(data_request: DataInput):
    return {'Hello': "POST", "msg": data_request.name}

