from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///notes_app.db"
app.config['SECRET_KEY'] = "3bd7e299f5c85baff143fb40"

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from notes_app import routes
