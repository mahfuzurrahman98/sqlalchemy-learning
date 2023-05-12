from Controller import Controller
from dbconnection import Base, engine

Base.metadata.create_all(engine)


# resp = Controller.create(
#     'Josh Little',
#     'josh@gmail.com',
#     'Dublin',
#     'Ireland'
# )

# resp = Controller.create(
#     'Mahfuz',
#     'mahfuz@gmail.com',
#     'Sylhet',
#     'Bangladesh'
# )

# resp = Controller.create(
#     'Virat',
#     'kohli@gmail.com',
#     'Delhi',
#     'India'
# )

# resp = Controller.create(
#     'Joe Root',
#     'joeroot@gmail.com',
#     'London',
#     'England'
# )

# print(resp)

# users = Controller.get_all()
# print(users)

# user = Controller.retrive(id=1)
# print(user)

resp = Controller.delete(id=1)
print(resp)

# resp = Controller.update(
#     id=1,
#     data={
#         'name': 'Kumar Sangakara',
#         'email': 'kumarsanga@gmail.com',
#         'city': 'Kandy',
#         'country': 'Sri Lanka'
#     }
# )
# print(resp)
