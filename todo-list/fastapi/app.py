from fastapi import FastAPI, Depends
from database import EngineConn
from model import TodoList as TodoListModel
from schema import TodoList as TodoListSchema
from starlette.middleware.cors import CORSMiddleware

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

@app.get("/api/home")
def home(): 
    return { "message": "home" }

# 모든 항목을 불러오는 엔드포인트
@app.get("/api/lists")
def get_lists():
    lists = session.query(TodoListModel).all()
    return lists


# 새로운 항목을 추가하는 엔드포인트
@app.post("/api/add_todo")
def create_todo(todo: TodoListSchema):
    new_todo = TodoListModel(content = todo.content)
    session.add(new_todo)
    session.commit()
    return new_todo

