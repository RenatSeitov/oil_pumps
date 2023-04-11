from database.db import Base
from sqlalchemy import Column, Integer


class Pumps(Base):
    __tablename__ = 'Oil_Pumps'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    pressure = Column(Integer)
    temperature = Column(Integer)
    speed = Column(Integer)
