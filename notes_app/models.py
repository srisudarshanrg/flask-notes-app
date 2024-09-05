from notes_app import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=15), unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    notes = db.relationship("Notes", backref="user", lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    note_head = db.Column(db.String(), nullable=False)
    note_desc = db.Column(db.String())
    note_user = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Note: {self.note_head} is for user whose id is {self.note_user}"