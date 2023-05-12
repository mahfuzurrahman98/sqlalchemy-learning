from dbconnection import db
from models.Address import Address
from models.User import User


class Controller:
    def create(name, email, city, country):
        try:
            user = User(name=name, email=email)
            db.add(user)

            address = Address(city=city, country=country, user_id=user.id)
            address.user = user
            db.add(address)

            db.commit()
            return {
                'message': 'User created',
                'data': {
                    'user': {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'city': user.address.city,
                        'country': user.address.country
                    }
                }
            }
        except Exception as e:
            return {'message': str(e.__repr__())}

    def get_all():
        try:
            users = db.query(User).all()
            users_list = []
            for user in users:
                users_list.append({
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'city': user.address.city,
                    'country': user.address.country
                })

            return {
                'message': 'Users retrieved',
                'data': {
                    'users': users_list
                }
            }
        except Exception as e:
            return {'message': str(e.__repr__())}

    def retrive(id):
        try:
            user = db.query(User).get(id)
            if user:
                return {
                    'message': 'User retrieved',
                    'data': {
                        'user': {
                            'id': user.id,
                            'name': user.name,
                            'email': user.email,
                            'city': user.address.city,
                            'country': user.address.country
                        }
                    }
                }
            else:
                return {'message': 'User not found'}
        except Exception as e:
            return {'message': str(e.__repr__())}

    def delete(id):
        try:
            user = db.query(User).get(id)
            if user:
                db.delete(user)
                db.commit()
                return {'message': 'User deleted'}
            else:
                return {'message': 'User not found'}
        except Exception as e:
            return {'message': str(e.__repr__())}

    def update(id, data):
        try:
            user = db.query(User).get(id)
            if user:
                user.name = data['name']
                user.email = data['email']
                user.address.city = data['city']
                user.address.country = data['country']
                db.commit()
                return {
                    'message': 'User updated',
                    'data': {
                        'user': {
                            'id': user.id,
                            'name': user.name,
                            'email': user.email,
                            'city': user.address.city,
                            'country': user.address.country
                        }
                    }
                }
            else:
                return {'message': 'User not found'}
        except Exception as e:
            return {'message': str(e.__repr__())}

    def __del__(self):
        db.close()
