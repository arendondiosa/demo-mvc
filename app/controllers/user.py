from demo_mvc.app.models.user import UserModel

class UserController():
    @classmethod
    def get_users(self):
        user_model = UserModel()

        users = user_model.select()

        return users
