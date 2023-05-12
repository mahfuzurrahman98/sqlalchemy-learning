from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLAlchemy engine to connect to MySQL database
engine = create_engine(
    'mysql+mysqlconnector://root:pass9859@localhost/alchemy',
    echo=True
)

# Create declarative base class
Base = declarative_base()

# Define "users" table schema


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())


# Create table "users"
# Base.metadata.create_all(engine)

# Create session to interact with database
Session = sessionmaker(bind=engine)
session = Session()

# Insert user into "users" table
user = User(name='Mahfuz2', email='mahfuz2.dev.98@gmail.com')
session.add(user)
session.commit()

# Close session
session.close()
