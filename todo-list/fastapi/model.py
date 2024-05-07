from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    auth = Column(String(16))
    name = Column(String(16))
    email = Column(String(64))
    password = Column(String(64))
    mobile = Column(String(16))
    created_at = Column(DateTime, nullable=False, default=func.now())

class TodoList(Base):
    __tablename__ = "list"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255), nullable=True)
    end_yn = Column(Boolean, default=False, nullable=False)
    member = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
