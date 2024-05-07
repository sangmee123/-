from pydantic import BaseModel
from typing import Union
import datetime

class Member(BaseModel):
    id: int = None
    auth: str = None
    name: str = None
    email: str = None
    password: str = None
    mobile: str = None
    created_at: datetime.datetime = None  

class TodoList(BaseModel):
    id: int = None
    content: str = None
    end_yn: bool = False
    member: Union[int, Member, None]
    created_at: datetime.datetime = None  
    updated_at: datetime.datetime = None
    deleted_at: datetime.datetime = None