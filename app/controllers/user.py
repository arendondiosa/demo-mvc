from demo_mvc.app.models.user import UserModel


class UserController:
    @classmethod
    def get_users(self):
        user_model = UserModel()

        users = user_model.select()
        users = [
            {
                "id": user["id"],
                "name": "{0} {1}".format(user["name"], user["last_name"]),
            }
            for user in users
        ]

        return users
