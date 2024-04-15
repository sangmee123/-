from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class TodoList(Base):
    __tablename__ = "todoListDB"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255))
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    delete_at = Column(DateTime)

