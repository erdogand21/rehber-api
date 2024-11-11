from .database import Base
from sqlalchemy import Column,String,Integer


class Rehber(Base):
    __tablename__ = "rehber"
    
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    Surname = Column(String, nullable=True)
    Number = Column(String, nullable=False)
    Adress = Column(String, nullable=True)
