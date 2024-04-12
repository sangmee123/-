# import uvicorn
import requests
import urllib.parse
import urllib.request
from urllib.parse import urlencode

from fastapi import FastAPI, HTTPException
import httpx
from fastapi import Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter


app = FastAPI()
ROUTER = APIRouter()

NAVER_CLIENT_ID = "ApiPimNUJywHK4ZJe0hE"
NAVER_CLIENT_SECRET = "4gZgRWP66P"
NAVER_CALLBACK_URL = "http://localhost:8080/login/naver"
NAVER_INGA_URL = "https://nid.naver.com/oauth2.0/authorize?"
NAVER_TOKEN_URL = "https://nid.naver.com/oauth2.0/token"
NAVER_FINAL_TOKEN = "https://openapi.naver.com/v1/nid/me"
origins = [
    "http://localhost:8080",  # mohaet local
    "http://localhost:3000",
    "http://localhost:5050",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class Images(BaseModel):
#     code: str
#     state: str
# class DataOut(BaseModel):
#     access_token: str
#     refresh_token: str
#     token_type: str
#     expires_in: str
#     error: str
#     error_description: str
    

@ROUTER.get('/url')
def getUrl():
    data = {
        'response_type': "code",
        'client_id': NAVER_CLIENT_ID,
        'redirect_uri': NAVER_CALLBACK_URL,
        'state': 'test'
    }
    total_data = urllib.parse.urlencode(data)
    url = NAVER_INGA_URL + total_data
    # req = urllib.request.Request(url)
    # response = urllib.request.urlopen(req)
    return url


@ROUTER.get('/token')
def Token(code: str = None, state: str = None, request: Request = None):
    params = {
        'grant_type': 'authorization_code',
        'client_id': NAVER_CLIENT_ID,
        'client_secret': NAVER_CLIENT_SECRET,
        'code': code,
        'state': state
    }
    headers = {
        'Content-Type': 'application/json'
    }
    query_string =  urllib.parse.urlencode(params)
    url = f"{NAVER_TOKEN_URL}?{query_string}"
    print(url)

    response = requests.request("POST", url, headers=headers)
    response: dict = response.json()

    print(response)
    access_token = response.get("access_token", None)
    headers = {
        "Authorization" : f"Bearer {access_token}"
    }

    profile_res = requests.request("POST", NAVER_FINAL_TOKEN, headers=headers)
    profile_res = profile_res.json()
    print(profile_res)

    return profile_res

app.include_router(ROUTER)
# if __name__ == "__main__":
#     uvicorn.run("router_example:app", host='0.0.0.0', port=8000, reload=True)