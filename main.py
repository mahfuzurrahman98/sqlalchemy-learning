from Controller import Controller
from dbconnection import Base, engine

Base.metadata.create_all(engine)


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


# resp = Controller.get_all()


# resp = Controller.retrive(id=1)


# resp = Controller.delete(id=1)


resp = Controller.update(
    id=12,
    data={
        'name': 'Kumar Sangakara',
        'email': 'kumarsanga@gmail.com',
        'city': 'Kandy',
        'country': 'Sri Lanka'
    }
)


print(resp)
