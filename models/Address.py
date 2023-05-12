from datetime import datetime

from dbconnection import Base, engine
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(), default=datetime.now())
    user = relationship("User", back_populates="addresses")
