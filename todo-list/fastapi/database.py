from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = {
    'name': 'mysql+pymysql',
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'yukiguni1025!',
    'dbname': 'todoListDB',
    'charset': 'utf8'
}

DB_URL = f"{db['name']}://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['dbname']}"

class EngineConn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn
