from dbconnection import Base, db, engine
from models.Address import Address
from models.User import User

Base.metadata.create_all(engine)

# make a user and add it to session
user = User(name='Jafrul', email='syedjafrul4@gmail.com')
db.add(user)

# make an address, associate it to the user and add it to session
address = Address(city='London', country='UK', user_id=user.id)
address.user = user
db.add(address)

# commit the session
db.commit()

# close session
db.close()
