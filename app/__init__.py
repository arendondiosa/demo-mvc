from flask import Flask

import demo_mvc.app.views

def create_app():
    app = Flask(__name__)

    app.add_url_rule('/', view_func=demo_mvc.app.views.index) 
    app.add_url_rule('/users', view_func=demo_mvc.app.views.users)  

    return app

app = Flask(__name__)
