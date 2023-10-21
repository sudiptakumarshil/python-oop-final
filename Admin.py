class Admin:
    __admin = []

    def __init__(self, name, email, password) -> None:
        self.__admin.append({
            'id': len(self.__admin)+1,
            'name': name,
            'email': email,
            'password': password
        })

    @staticmethod
    def get_admin(id=None):
        if id is not None:
            if next((admin for admin in Admin.__admin if admin['id'] == id), None):
                return next((admin for admin in Admin.__admin if admin['id'] == id), None)
            return f'Admin Not Found For the Id {id}'
        return Admin.__admin
