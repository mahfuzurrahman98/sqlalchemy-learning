from datetime import datetime

from dbconnection import Base, engine
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    address = relationship("Address", uselist=False, back_populates="user")
    created_at = Column(DateTime(), default=datetime.now())

    # def __repr__(self):
    #     return f"User(id={self.id}, name={self.name}, email={self.email}, city={self.addresses.city}, country={self.addresses.country})"
