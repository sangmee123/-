from fastapi import Depends, HTTPException, status, Response, Request, APIRouter
from user_crud import get_user, create_user, verify_password
from schema import NewUserForm, Token
from datetime import timedelta
from config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from dependency import get_db, create_access_token, Session

router = APIRouter()


@router.post("/signup")
async def signup(new_user: NewUserForm, db: Session = Depends(get_db)):
    # 회원 존재 여부 확인
    user = get_user(new_user.email, db)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User already exists"
        )

    # 회원 가입
    create_user(new_user, db)

    return HTTPException(status_code=status.HTTP_200_OK, detail="Signup successful")


@router.post("/login")
async def login(response: Response, login_form: dict, db: Session = Depends(get_db)):
    # 회원 존재 여부 확인
    user = get_user(login_form["username"], db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user or password"
        )

    # 로그인
    res = verify_password(login_form["password"], user.hashed_pw)

    if not res:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user or password"
        )

    # 토큰 생성
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    # 쿠키에 저장
    response.set_cookie(
        key="access_token",
        value=access_token,
        expires=access_token_expires,
        httponly=True,
    )

    return Token(access_token=access_token, token_type="bearer")


@router.get("/logout")
async def logout(response: Response, request: Request):
    response.delete_cookie(key="access_token")
    return HTTPException(status_code=status.HTTP_200_OK, detail="Logout successful")
