from . import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    pwd = db.Column(db.String(), nullable=False)
    db.relationship("Note", backref="user", lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    note_head = db.Column(db.String())
    note_desc = db.Column(db.String())
    note_user = db.Column(db.Integer(), db.ForeignKey("user.id"))