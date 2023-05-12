from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create declarative base class
Base = declarative_base()


# Define 'addresses' table schema
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    country = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime(), default=datetime.now())
    user = relationship("User", back_populates="addresses")
