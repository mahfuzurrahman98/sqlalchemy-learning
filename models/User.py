from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create declarative base class
Base = declarative_base()


# Define 'users' table schema
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    address = relationship("Address", back_populates="user")
    created_at = Column(DateTime(), default=datetime.now())
