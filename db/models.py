from db.database import base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey 



class DbUser(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index= True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    