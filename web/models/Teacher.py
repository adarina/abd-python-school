from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    def __init__(self, login, name, surname, password = None):
        self.name = name
        self.login = login
        self.surname = surname
        self.password = password

class Teacher(db.Model):
    __tablename__ = "teacher"
    
    user_id = db.Column(db.ForeignKey('user.id'), primary_key=True)
    room = db.Column(db.Integer, nullable=False)
    user = db.relationship('User')
    
    def __init__(self, user_id, room):
        self.user_id = user_id
        self.room = room

class Pupil(db.Model):
    __tablename__ = "pupil"
    
    user_id = db.Column(db.ForeignKey('user.id'), primary_key=True)
    birthDate = db.Column(db.Integer, nullable=False)
    user = db.relationship('User')
    
    def __init__(self, user_id, birthDate):
        self.user_id = user_id
        self.birthDate = birthDate