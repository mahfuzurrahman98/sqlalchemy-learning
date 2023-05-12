from datetime import datetime

from dbconnection import Base, engine
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    addresses = relationship("Address", back_populates="user")
    created_at = Column(DateTime(), default=datetime.now())
