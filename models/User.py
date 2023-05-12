from datetime import datetime

from dbconnection import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    address = relationship('Address', uselist=False,
                           back_populates='user', cascade='delete')
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(
        TIMESTAMP,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )

    # def __repr__(self):
    #     return f'User(id={self.id}, name={self.name}, email={self.email}, city={self.address.city}, country={self.address.country})'
