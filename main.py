from Controller import Controller
from dbconnection import Base, engine

Base.metadata.create_all(engine)


# Controller.create(
#     'Josh Little',
#     'josh@gmail.com',
#     'Dublin',
#     'Ireland'
# )

# Controller.create(
#     'Mahfuz',
#     'mahfuz@gmail.com',
#     'Sylhet',
#     'Bangladesh'
# )

# Controller.create(
#     'Virat',
#     'kohli@gmail.com',
#     'Delhi',
#     'India'
# )

# Controller.create(
#     'Joe Root',
#     'joeroot@gmail.com',
#     'London',
#     'England'
# )

# users = Controller.get_all()
# print(users)

# user = Controller.retrive(id=1)
# print(user)

# resp = Controller.delete(id=1)
# print(resp)

resp = Controller.update(
    id=3,
    data={
        'name': 'Kumar Sangakara',
        'email': 'kumarsanga@gmail.com',
        'city': 'Kandy',
        'country': 'Sri Lanka'
    }
)
print(resp)
