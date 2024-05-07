from fastapi import Depends, FastAPI, Request, HTTPException
from database import EngineConn
from model import TodoList as TodoListModel, Member as MemberModel
from schema import TodoList as TodoListSchema, Member as MemberSchema
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.sql import func
from datetime import date
import re
from jose import jwt
from token_utils import (
    get_hashed_password, 
    verify_password,
    verify_token,
    create_access_token, 
)

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


# 오늘 날짜의 모든 항목을 불러오는 엔드포인트
@app.get("/lists")
def read_todos(user_info: dict = Depends(verify_token)):
    today = date.today()  # 오늘 날짜
    today_lists = session.query(TodoListModel).filter(
        TodoListModel.member == user_info['user_id'],
        TodoListModel.deleted_at == None,  # deleted_at 값이 null인 것만 필터링
        func.DATE(TodoListModel.created_at) == today,  # 오늘 날짜만 팔터링
    ).all()
    return {"user": user_info, "lists": today_lists}

# 해당 날짜의 모든 항목을 불러오는 엔트포인트
@app.get("/selected_date")
def read_selected_date_todos(request: Request):
    params = request.query_params
    selected_date = params.get("selectedDate")
    member_id = params.get("member")

    selected_date_todo = session.query(TodoListModel).filter(
        TodoListModel.member == member_id,
        TodoListModel.deleted_at == None, # deleted_at 값이 null인 것만 필터링
        func.DATE(TodoListModel.created_at) == selected_date # 선택한 날짜만 필터링
    ).all()
    return selected_date_todo

# 새로운 항목을 추가하는 엔드포인트
@app.post("/add_todo")
def create_todo(todo: TodoListSchema = None):
    print(todo)
    new_todo = TodoListModel(member=todo.member, content=todo.content, deleted_at=None)
    session.add(new_todo)
    session.commit()
    return new_todo

# 기존 항목을 수정하는 엔드포인트
@app.put("/edit_todo/{id}")
def update_todo(id: int, todo: TodoListSchema):
    edited_todo = session.query(TodoListModel).filter(
        TodoListModel.id == id
    ).one_or_none()  
    
    if edited_todo is None:
        return {"error": "Todo not found"}
    
    if(todo.content != None):
        edited_todo.content = todo.content
        edited_todo.updated_at = func.now()  
    else:
        edited_todo.end_yn = todo.end_yn

    session.add(edited_todo)
    session.commit()
    return edited_todo

# 해당 항목을 삭제하는 엔드포인트
@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    deleted_todo = session.query(TodoListModel).filter(TodoListModel.id == id).one_or_none()
    if deleted_todo is None:
        return {"error": "Todo not found"}
    
    deleted_todo.deleted_at = func.now()  
    session.commit()
    return {"message": "Todo deleted"}


## 사용자 서비스 ##
# 회원가입 엔드포인트
@app.post("/add_member")
def create_member(member: MemberSchema):
    # 숫자가 아닌 문자 제거(하이픈 제거)
    mobile_number = re.sub(r'\D', '', member.mobile)  

    new_member = MemberModel(
        auth = 'todolist',
        email=member.email, 
        name=member.name, 
        password=get_hashed_password(member.password), 
        mobile=mobile_number
    )
    session.add(new_member)
    session.commit()
    return new_member

# 로그인 엔드포인트
@app.post("/login")
def login_member(member: MemberSchema):
    db_member = session.query(MemberModel).filter(MemberModel.email == member.email).one_or_none()
    hashed_password = db_member.password

    # 이메일과 비밀번호로 사용자를 찾음
    if not db_member or not verify_password(member.password, hashed_password):
        # 사용자가 없거나 비밀번호가 일치하지 않으면 오류 반환
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # 토큰 생성
    access_token = create_access_token({
        "user_id": db_member.id, 
        "user_name": db_member.name
    })
    
    # 로그인 성공 및 토큰 반환
    return {"access_token": access_token}


## Naver 소셜 로그인 
# 회원가입 엔드포인트
@app.post("/add_naver")
def create_naver_member(member: MemberSchema):
    # 이메일 중복 확인
    existing_member = session.query(MemberModel).filter(
        MemberModel.auth == 'naver',
        MemberModel.email == member.email
    ).all()
    
    if existing_member:
        return {"message": "기존 가입되어 있는 이메일로 로그인 하였습니다."}
    else:
        # 숫자가 아닌 문자 제거(하이픈 제거)
        mobile_number = re.sub(r'\D', '', member.mobile)  

        new_member = MemberModel(
            auth = 'naver',
            email = member.email, 
            name = member.name, 
            password = '', 
            mobile = mobile_number
        )
        session.add(new_member)
        session.commit()

        return new_member
    
# 로그인 엔드포인트
@app.post("/naver_login")
def login_member(member: MemberSchema):
    db_member = session.query(MemberModel).filter(
        MemberModel.auth == 'naver',
        MemberModel.email == member.email
    ).one_or_none()
    
    # 토큰 생성
    access_token = create_access_token({
        "user_id": db_member.id, 
        "user_name": db_member.name
    })

    # 로그인 성공 및 토큰 반환
    return {"token": access_token}