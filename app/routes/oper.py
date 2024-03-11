# app/routes/oper.py

from app.models.model import db, User, Faculty
from flask import current_app

def add_user(username, password, course):
    new_user = User(username=username, password=password, course=course)
    db.session.add(new_user)
    db.session.commit()

def check_user_exists(username):
    with current_app.app_context():
        return User.query.filter_by(username=username).first() is not None

def check_user_with_id(id, username, password):
    return User.query.filter_by(id=id, username=username, password=password).first() is not None

def get_user_course(username):
    user = User.query.filter_by(username=username).first()
    return user.course if user else None

def add_faculty(email, password, course):
    new_faculty = Faculty(email=email, password=password, course=course)
    db.session.add(new_faculty)
    db.session.commit()

def check_faculty_exists(email):
    return Faculty.query.filter_by(email=email).first() is not None

def authenticate_faculty(email, password):
    return Faculty.query.filter_by(email=email, password=password).first()

def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return {
            'id': user.id,
            'username': user.username,
            'course': user.course,
            'password':user.password
        }
    return None
