from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, validator
from pydantic import Field
from pydantic import BaseSettings

class Movie(BaseModel):
    mid: int
    genre: str
    rate: Union[int, float] 
    tag: Optional[str] = None
    date: Optional[datetime] = None
    some_variable_list: List[int] = []

class User(BaseModel):
    '''
    gt : 설정된 값보다 큰
    ge : 설정된 값보다 크거나 같은
    lt : 설정된 값보다 작은
    le : 설정된 값보다 작거나 같은
    '''
    uid : int
    name: str = Field(min_length=2, max_length=7)
    age: int = Field(gt=1, le=130)

tmp_movie_data = {
    'mid': '1',
    'genre': 'action',
    'rate': '1.5',
    'tag': None,
    'date': '2024-03-15 14:59:00'
}

tmp_user_data = {
    'uid' : '100',
    'name' : 'soojin',
    'age': '12'
}

tmp_movie = Movie(**tmp_movie_data)
tmp_user_data = User(**tmp_user_data)
print(tmp_movie.json())
print(tmp_user_data.json())


# class DBConfig(BaseSettings):
#     host: str = Field(default='127.0.0.1', env='db_host')
#     port: int = Field(default=3306, env='db_port')

#     class Config:
#         env_file = '.env_ex'

#     @validator("host", pre=True)
#     def check_host(cls, host_input):
#         if host_input == 'localhost':
#             return "127.0.0.1"
#         return host_input
    
#     @validator("port")
#     def check_port(cls, port_input):
#         if port_input not in [3306, 8080]:
#             raise ValueError("port error")
#         return port_input
    
# class ProjectConfig(BaseModel):
#     project_name : str = 'subeen'
#     db_info : DBConfig = DBConfig()


# data = {
#     'project_name': '이수빈의 프로젝트',
#     'db_info': {
#         'host': 'localhost',
#         'port': 3306
#     }
# }
# print(DBConfig().dict())

# my_pjt = ProjectConfig(**data)
# print(my_pjt.dict())
# print(my_pjt.db_info)


