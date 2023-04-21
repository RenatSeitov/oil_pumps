from database.db import Base
from sqlalchemy import Column, String, Integer


class Users(Base):
    __tablename__ = 'UsersProfile'

    user_id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(75), unique=True)
    fast_name = Column(String(100), unique=True)
    last_name = Column(String(100), unique=True)
    password = Column(String(200), unique=True)

