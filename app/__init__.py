from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap() 
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
     app = Flask(__name__)
     
     app.config_class.from_object(config_options[config_name])
     
     bootstrap.init_app(app)
     db.init_app(app)
     login_manager.init_app(app)
     
     return app