from google.oauth2.service_account import Credentials
from fastapi import HTTPException, status, Request, APIRouter
from user_crud import get_user, create_user
from schema import NewUserForm
from datetime import timedelta
from config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    GOOGLE_AUTH_ENDPOINT,
    GOOGLE_REDIRECT_URI,
    GOOGLE_TOKEN_ENDPOINT,
    GOOGLE_USER_INFO_ENDPOINT,
)
from dependency import create_access_token, Session
import requests
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode

import gspread

router = APIRouter()


@router.get("/oauth_login/google")
async def google_oauth_login(request: Request):
    params = {
        "response_type": "code",
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "scope": "openid email profile",
        "access_type": "offline",
    }
    google_auth_url = f"{GOOGLE_AUTH_ENDPOINT}?{urlencode(params)}"
    return RedirectResponse(url=google_auth_url)


@router.get("/google/callback")  # 구글 로그인 콜백
async def google_auth_callback(request: Request):
    code = request.query_params.get("code")
    if code is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="권한 코드 없음"
        )
    # 구글로부터 받은 코드로 액세스 토큰을 요청
    token_params = {
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": GOOGLE_REDIRECT_URI,
    }
    token_response = requests.post(GOOGLE_TOKEN_ENDPOINT, data=token_params)
    token_data = token_response.json()
    if "access_token" not in token_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="토큰 발급 실패"
        )

    # 구글에서 받은 액세스 토큰으로 사용자 정보를 요청
    headers = {"Authorization": f"Bearer {token_data['access_token']}"}
    user_info_response = requests.get(GOOGLE_USER_INFO_ENDPOINT, headers=headers)
    user_info_data = user_info_response.json()
    print("user_info_data", user_info_data)
    user_email = user_info_data["email"]
    user_name = user_info_data["name"]
    user_mobile = "010-1111-1111"

    db = Session()  # 세션 생성
    try:
        # 사용자가 이미 회원인지 확인
        user = get_user(user_email, db)
        if not user:
            # 사용자가 회원이 아니라면 회원가입 진행
            new_user_form = NewUserForm(
                email=user_email, name=user_name, phone=user_mobile, password="a1234567"
            )
            create_user(new_user_form, db)
            user = get_user(user_email, db)  # 회원가입 후에는 다시 해당 사용자를 가져옴

        # 로그인 처리를 위해 토큰 생성
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )

        response = RedirectResponse(url="http://localhost:8080/#/googlesheet")
        response.set_cookie(
            key="access_token",
            value=access_token,
            expires=access_token_expires,
            httponly=True,
        )

        return response
    finally:
        db.close()


# 구글 서비스 계정의 JSON키 파일을 직접 로드 하는 것이 아닌, Credentials를 통해 서비스 계정 파일을 로드 함
# 따라서 OAuth를 통해서 액세스 한다는 점에서, 서비스 계정 파일에 스프레드시트의 접근권한을 설정하지 않고도 액세스 가능하다는 차이가 있음
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = Credentials.from_service_account_file("./google-sheet-key.json", scopes=scope)
client = gspread.authorize(creds)


@router.get("/get_spreadsheet_data/{spreadsheet_id}/{range}")
async def get_spreadsheet_data(spreadsheet_id: str, range: str):
    sheet = client.open_by_key(spreadsheet_id)
    worksheet = sheet.worksheet(range)
    values = worksheet.get_all_values()
    return values


# @router.get("/data")
# async def get_spreadsheet_data(request: Request):
#     gc = gspread.service_account(JSON_FILE_PATH)
#     doc = gc.open_by_url(SPREADSHEET_URL)
#     worksheet = doc.worksheet(WORKSHEET_NAME)

#     all_values = worksheet.get_all_values()
#     return all_values
