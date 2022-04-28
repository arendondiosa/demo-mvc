users_mock = [
    {"id": 1, "name": "John", "last_name": "Doe"},
    {"id": 2, "name": "Jane", "last_name": "Doe"},
]


class UserModel:
    @classmethod
    def select(self):
        return users_mock
