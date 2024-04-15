from pydantic import BaseModel
import datetime

class TodoList(BaseModel):
    id: int
    content: str
    created_at: datetime.datetime 
    updated_at: datetime.datetime 
    delete_at: datetime.datetime 