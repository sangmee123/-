from pydantic import BaseModel
import datetime

class TodoList(BaseModel):
    id: int = None
    content: str = None
    created_at: datetime.datetime = None  
    updated_at: datetime.datetime = None