from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_host = 'host'
db_name = 'dbname'
db_user = 'user'
db_password = 'pass'

connection_string = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'

engine = create_engine(connection_string, echo=False)

Session = sessionmaker(bind=engine)
db = Session()

Base = declarative_base()
