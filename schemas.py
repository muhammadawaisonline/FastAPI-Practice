from pydantic import BaseModel
from typing import List
class ArticleBase(BaseModel):
    title:str
    content:str
    published:bool
    class config():
        orm_mode = True


class User(BaseModel):
    id:int
    username:str
    class config():
        orm_model: True

class UserBase(BaseModel):
    username:str
    email:str
    password:str


class UserDisplay(BaseModel):
    username:str
    email:str
    items:List[ArticleBase] = []
    class Config():
        orm_mode = True
        # from_attributes = True

class ArticleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user:User
    class Config():
        orm_mode = True