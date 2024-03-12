# app/__init__.py
from flask import Flask
from Best_It.extensions.db import db
from Best_It.configure import Config
from Best_It.extensions.login_manager import login_manager
from Best_It.routes import main, student, faculty, stu_course, uploads

def create_app():
    server = Flask(__name__)
    server.config.from_object(Config)
    login_manager.init_app(server)  # Initialize login manager
    db.init_app(server)
    with server.app_context():
        db.create_all()
    register_blueprints(server)
    return server

def register_blueprints(app):
    app.register_blueprint(main.main_bp)
    app.register_blueprint(student.student_bp)
    app.register_blueprint(faculty.faculty_bp)
    app.register_blueprint(stu_course.course_bp)
    app.register_blueprint(uploads.uploads_bp)