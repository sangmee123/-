from pydantic import BaseModel
import datetime

class TodoList(BaseModel):
    id: int = None
    content: str = None
    end_yn: bool = False
    created_at: datetime.datetime = None  
    updated_at: datetime.datetime = None
    deleted_at: datetime.datetime = None