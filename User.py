import random


class User:
    __user_list = []

    def __init__(self, name, email, address, type, password) -> None:
        self.__current_user = len(self.__user_list)+1,
        self.__user_list.append({
            'id': self.__current_user,
            'name': name,
            'email': email,
            'address': address,
            'type': type,
            'account_number': str((1000 + max(1, random.randint(1, 100))) + len(self.__user_list)+1),
            'password': password
        })

    @staticmethod
    def get_user(id=None):
        if id is not None:
            if next((user for user in User.__user_list if user['id'] == id), None):
                return next((user for user in User.__user_list if user['id'] == id), None)
            return f'User Not Found For the Id {id}'
        return User.__user_list

    @staticmethod
    def delete_user(account_number):
        user = None
        for index, user in enumerate(User.__user_list):
            if user['account_number'] == account_number:
                user = index
                break
        if user is not None:
            User.__user_list.pop(user)
            return f'User deleted'

    def current_user(self):
        return self.__current_user

