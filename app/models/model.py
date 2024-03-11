# app/models/model.py
from app.extensions.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    course = db.Column(db.String(64)) 

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password= generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password= db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(64))  

    def __repr__(self):
        return f'<email {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
