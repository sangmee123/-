from fastapi import FastAPI
from db import _database
import pymysql

# 데이터베이스 연결 정보
# db_config = _database

# 데이터베이스 연결
# conn = pymysql.connect(db_config)

# Cursor 생성(연결한 DB 호출)
# cur = conn.cursor()

# FastAPI 앱 생성
app = FastAPI()

@app.get("/")

def root(): 
    return { "message": "Hello World" }

@app.get("/home")
def home(): 
    return { "message": "home" }