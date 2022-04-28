from flask import render_template

from demo_mvc.app.controllers.user import UserController

def index():
    return render_template('user/index.html')

def users():
    user_controller = UserController()
    users = user_controller.get_users()

    return render_template('user/users.html', users=users)
