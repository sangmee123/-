from jose import jwt
from datetime import datetime, timedelta
import os
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

# .env 파일로부터 환경 변수 로드
from dotenv import load_dotenv
load_dotenv()

# 환경 변수로부터 SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES 가져오기
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호 해시화
def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

# 비밀번호 검증
def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


# 토큰 생성
def create_access_token(data: dict, expiration_time: timedelta = None):
    to_encode = data.copy() # 입력된 데이터 복사
    
    # 만료 시간 설정
    if expiration_time:
        expire = datetime.utcnow() + expiration_time
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # 토큰에 만료 시간 추가
    to_encode.update({"exp": expire})
    
    # JWT 생성
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# OAuth2를 사용하여 토큰을 추출하기 위한 인스턴스 생성
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# 토큰 검증 함수
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

