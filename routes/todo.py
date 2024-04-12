from fastapi import Depends, APIRouter
from models import TodoList
from schema import TodoIn
from datetime import datetime
from sqlalchemy.orm import Session
from dependency import get_db, get_current_user

router = APIRouter()


@router.get("/read_todo/{todo_date}")
def read_todo(todo_date: datetime, db: Session = Depends(get_db)):
    todos = db.query(TodoList).filter(TodoList.date == todo_date).all()
    return todos


@router.post("/add_todo")
def create_todo(
    todo: TodoIn,
    db: Session = Depends(get_db),
    user: TodoList = Depends(get_current_user),
):
    new_todo = TodoList(
        text=todo.text, date=todo.date, done=todo.done, color=todo.color
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)  # 새로운 할 일을 DB로부터 새로고침하여 업데이트된 값 가져옴
    return new_todo


@router.put("/edit_todo/{id}")
def update_todo(
    id: int,
    todo: TodoIn,
    db: Session = Depends(get_db),
    user: TodoList = Depends(get_current_user),
):
    db_todo = db.query(TodoList).filter(TodoList.id == id).one_or_none()
    if db_todo is None:
        return {"error": "Todo not found"}
    db_todo.text = todo.text
    db_todo.date = todo.date
    db_todo.done = todo.done
    db_todo.color = todo.color
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.delete("/delete_todo/{id}")
def delete_todo(
    id: int, db: Session = Depends(get_db), user: TodoList = Depends(get_current_user)
):
    db_todo = db.query(TodoList).filter(TodoList.id == id).one_or_none()
    if db_todo is None:
        return {"error": "Todo not found"}
    db.delete(db_todo)
    db.commit()
    return {"message": "할 일이 삭제되었습니다"}
