from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os
import sqlalchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'


if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from comuna import routes


from comuna import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
if not engine.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados criada")
else:
    print("Base de dados já existente")

from comuna import routes


