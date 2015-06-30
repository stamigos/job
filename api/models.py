__author__ = 'amigos'
from datetime import datetime
from passlib.apps import custom_app_context as pwd_context
from api import db, app


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    registered_on = db.Column('registered_on', db.DateTime)
    info = db.Column('info', db.String(50))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def __repr__(self):
        return '<User %r>' % self.email