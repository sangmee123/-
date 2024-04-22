from fastapi import FastAPI, Depends
from database import EngineConn
from model import TodoList as TodoListModel
from schema import TodoList as TodoListSchema
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.sql import func

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

@app.get("/")
def root(): 
    return { "message": "Hello 123" }

@app.get("/home")
def home(): 
    return { "message": "home" }


# 모든 항목을 불러오는 엔드포인트
@app.get("/lists")
def read_todos():
    lists = session.query(TodoListModel).all()
    return lists

# 새로운 항목을 추가하는 엔드포인트
@app.post("/add_todo")
def create_todo(todo: TodoListSchema):
    new_todo = TodoListModel(content = todo.content, deleted_at = None)
    session.add(new_todo)
    session.commit()
    return new_todo

# 기존 항목을 수정하는 엔드포인트
@app.put("/edit_todo/{id}")
def update_todo(id: int, todo: TodoListSchema):
    edited_todo = session.query(TodoListModel).filter(TodoListModel.id == id).one_or_none()  
    if edited_todo is None:
        return {"error": "Todo not found"}
    
    edited_todo.content = todo.content
    edited_todo.updated_at = func.now()  
    session.add(edited_todo)
    session.commit()
    return edited_todo

# 해당 항목을 체크하는 엔드포인트
@app.post("/edit_check/{id}")
def update_check(id: int, todo:TodoListSchema):
    edited_check = session.query(TodoListModel).filter(TodoListModel.id == id).one_or_none()
    if edited_check is None:
        return {"error": "Todo not found"}
    edited_check.end_yn = todo.end_yn
    session.add(edited_check)
    session.commit()
    return edited_check

# 해당 항목을 삭제하는 엔드포인트
@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    deleted_todo = session.query(TodoListModel).filter(TodoListModel.id == id).one_or_none()
    if deleted_todo is None:
        return {"error": "Todo not found"}
    session.delete(deleted_todo)
    session.commit()
    return {"message": "Todo deleted"}