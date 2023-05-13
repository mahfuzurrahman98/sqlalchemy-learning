from Controller import Controller
from dbconnection import Base, engine

Base.metadata.create_all(engine)


# CRUD operations

# creating users
# resp = Controller.create(
#     name='Josh Little',
#     email='josh@gmail.com',
#     city='Dublin',
#     country='Ireland'
# )

# resp = Controller.create(
#     name='Mahfuz',
#     email='mahfuz@gmail.com',
#     city='Sylhet',
#     country='Bangladesh'
# )

# resp = Controller.create(
#     name='Kohli',
#     email='kohli@gmail.com',
#     city='Delhi',
#     country='India'
# )

# resp = Controller.create(
#     name='Joe Root',
#     email='joeroot@gmail.com',
#     city='London',
#     country='England'
# )


# get all users
# resp = Controller.get_all()


# get a single user
# resp = Controller.retrive(id=1)


# delete a single user
# resp = Controller.delete(id=1)


# update a signle user
# resp = Controller.update(
#     id=12,
#     data={
#         'name': 'Kumar Sangakara',
#         'email': 'kumarsanga@gmail.com',
#         'city': 'Kandy',
#         'country': 'Sri Lanka'
#     }
# )


# print(resp)
