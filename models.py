from sqlalchemy import Column, Integer, VARCHAR, DateTime, String, Date, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TodoList(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    text = Column(String, index=True)  # 할 일 내용
    date = Column(Date)  # 날짜
    done = Column(Boolean)  # 완료 여부
    color = Column(String)  # 글자색

class User(Base):
    __tablename__ = "UsersInfo"
    user_no = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(VARCHAR(10), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    hashed_pw = Column(VARCHAR(100), nullable=False)
    role = Column(VARCHAR(20), nullable=False, default='MEMBER')
    status = Column(VARCHAR(1), nullable=False, default='1')
    regdate = Column(DateTime, nullable=False, default=datetime.now)
