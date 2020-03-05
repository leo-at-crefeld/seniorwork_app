from datetime import datetime
from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    color = db.Column(db.String(64), index=True)
    mod_time = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '<Person {}>'.format(self.username)
