from fastapi import FastAPI, Request, HTTPException
from database import EngineConn
from model import Member as MemberModel
from schema import Member as MemberSchema
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.sql import func
from datetime import date

# FastAPI 앱 생성
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 세션 연결
engine = EngineConn()
session = engine.sessionmaker()


# 회원가입 엔드포인트
@app.post("/add_member")
def create_member(member: MemberSchema):
    new_member = MemberModel(email = member.email, name = member.name, password = member.password, mobile = member.mobile)
    session.add(new_member)
    session.commit()
    return new_member

# 로그인 엔드포인트
@app.post("/login")
def login_member(email: str, password: str):
    # 이메일과 비밀번호로 사용자를 찾음
    member = session.query(MemberModel).filter(MemberModel.email == email)
    if not member or not member.check_password(password):
        # 사용자가 없거나 비밀번호가 일치하지 않으면 오류 반환
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # 로그인 성공
    return { "member_id": member.id, "name": member.name }