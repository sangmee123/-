from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
import requests, uuid, time, json
from pydantic import BaseModel

# FastAPI 앱 생성
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImgUrl(BaseModel):
    imgUrl: str = None

def load_api(img_url =None):
    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo',
                'url': img_url
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = json.dumps(request_json).encode('UTF-8')
    headers = {
    'X-OCR-SECRET': ,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", , headers=headers, data = payload)

    json_response = response.json()
    return json_response


@app.get("/get_data")
def get_data(request: Request):
    params = request.query_params
    imgUrl = params.get("imgUrl")
    json_response = load_api(imgUrl)
    return json_response


