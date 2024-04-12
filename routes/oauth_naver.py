from fastapi import HTTPException, status, Request, APIRouter
from user_crud import get_user, create_user
from schema import NewUserForm
from datetime import timedelta
from config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    NAVER_CLIENT_ID,
    NAVER_CLIENT_SECRET,
    NAVER_REDIRECT_URI,
    NAVER_AUTH_ENDPOINT,
    NAVER_TOKEN_ENDPOINT,
    NAVER_USER_INFO_ENDPOINT,
)
from dependency import create_access_token, Session
import requests
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode

router = APIRouter()


@router.get("/oauth_login/naver")
async def naver_oauth_login(request: Request):
    # 네이버 로그인 페이지로 리다이렉트
    params = {
        "response_type": "code",
        "client_id": NAVER_CLIENT_ID,
        "redirect_uri": NAVER_REDIRECT_URI,
        "state": "some_random_state",
    }
    naver_auth_url = f"{NAVER_AUTH_ENDPOINT}?{urlencode(params)}"
    return RedirectResponse(url=naver_auth_url)


@router.get("/naver/callback")  # 네이버 로그인 콜백
async def naver_auth_callback(request: Request):
    code = request.query_params.get("code")
    if code is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="권한 코드 없음"
        )

    # 네이버로부터 받은 코드로 액세스 토큰을 요청
    token_params = {
        "grant_type": "authorization_code",
        "client_id": NAVER_CLIENT_ID,
        "client_secret": NAVER_CLIENT_SECRET,
        "code": code,
    }
    token_response = requests.post(NAVER_TOKEN_ENDPOINT, data=token_params)
    token_data = token_response.json()
    if "access_token" not in token_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="토큰 발급 실패"
        )

    # 네이버에서 받은 액세스 토큰으로 사용자 정보를 요청
    headers = {"Authorization": f"Bearer {token_data['access_token']}"}
    user_info_response = requests.get(NAVER_USER_INFO_ENDPOINT, headers=headers)
    user_info_data = user_info_response.json()
    user_email = user_info_data["response"]["email"]
    user_name = user_info_data["response"]["name"]
    user_mobile = user_info_data["response"]["mobile"]

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

        response = RedirectResponse(url="http://localhost:8080/#/todolist")
        response.set_cookie(
            key="access_token",
            value=access_token,
            expires=access_token_expires,
            httponly=True,
        )

        return response
    finally:
        db.close()
