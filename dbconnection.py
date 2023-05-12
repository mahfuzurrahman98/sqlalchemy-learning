from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connection_string = 'mysql+mysqlconnector://root:pass9859@localhost/alchemy'

engine = create_engine(connection_string, echo=False)

Session = sessionmaker(bind=engine)
db = Session()

Base = declarative_base()
