from notes_app import db
from notes_app import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    notes = db.relationship("Note", backref="user", lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    note_head = db.Column(db.String(), nullable=False)
    note_desc = db.Column(db.String())
    note_user = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Note: {self.note_head} is for user whose id is {self.note_user}"