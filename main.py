from click import DateTime

from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLAlchemy engine to connect to MySQL database
engine = create_engine(
    'mysql+mysqlconnector://root:pass9859@localhost/alchemy')

# Create declarative base class
Base = declarative_base()

# Define "users" table schema
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    created_at = Column(DateTime(), default=text('CURRENT_TIMESTAMP'))


# Create table "users"
Base.metadata.create_all(engine)

# Create session to interact with database
Session = sessionmaker(bind=engine)
session = Session()

# Insert user into "users" table
user = User(name='Arif', email='arif.dev.98@gmail.com')
session.add(user)
session.commit()

# Close session
session.close()
