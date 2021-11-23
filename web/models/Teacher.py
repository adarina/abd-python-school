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

class Grade(db.Model):
    __tablename__ = "grade"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    # evaluated = db.Column(db.Pupil.name, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    subject = db.Column(db.String(128), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.ForeignKey('user.id'))
    user = db.relationship('User')

    def __init__(self, date, description, subject, grade, weight, user_id):
        self.date = date
        # self.evaluated =evaluated
        self.description = description
        self.subject = subject
        self.grade = grade
        self.weight = weight
        self.user_id = user_id,