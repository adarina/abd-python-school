from sqlalchemy.sql.expression import null
from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import backref, configure_mappers
class User(AbstractConcreteBase, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    def __init__(self, id, login, name, surname, password = None):
        self.id = id
        self.name = name
        self.login = login
        self.surname = surname
        self.password = password

class Teacher(User):
    __tablename__ = "teacher"
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    room = db.Column(db.Integer, nullable=False)
    lessons = db.relationship('Lesson', backref='teacher')
    
    __mapper_args__ = {
        'polymorphic_identity': 'teacher',
        'concrete': True
    }
    
    def __init__(self, id, login, name, surname, password, room):
        self.id = id
        self.name = name
        self.login = login
        self.surname = surname
        self.password = password
        self.room = room

class Pupil(User):
    __tablename__ = "pupil"
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    birthDate = db.Column(db.Integer, nullable=False)
    class_name = db.Column(db.String(128), db.ForeignKey('class.name'))
    grade_lists = db.relationship('ListOfGrades', backref='pupil')
    frequency = db.relationship('Frequency', backref=backref('pupil', lazy='joined'))

    __mapper_args__ = {
        'polymorphic_identity': 'pupil',
        'concrete': True
    }
    
    def __init__(self, id, login, name, surname, password, birthDate, class_name):
        self.id = id
        self.name = name
        self.login = login
        self.surname = surname
        self.password = password
        self.birthDate = birthDate
        self.class_name = class_name

class Grade(db.Model):
    __tablename__ = "grade"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    evaluated = db.Column(db.ForeignKey('pupil.id'))
    description = db.Column(db.String(128), nullable=False)
    subject = db.Column(db.String(128), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.ForeignKey('teacher.id'))
    listofgrades_id = db.Column(db.ForeignKey('listofgrades.id'))

    def __init__(self, date, evaluated, description, subject, grade, weight, teacher_id, listofgrades_id):
        self.date = date
        self.evaluated = evaluated
        self.description = description
        self.subject = subject.upper()
        self.grade = grade
        self.weight = weight
        self.teacher_id = teacher_id
        self.listofgrades_id = listofgrades_id

class Lesson(db.Model):
    __tablename__ = "lesson"

    id = db.Column(db.Integer, primary_key=True)
    dateOfExecution = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(128), nullable=False)
    teacher_id = db.Column(db.ForeignKey('teacher.id'))
    frequency  = db.relationship('Frequency', backref=backref('lesson', lazy='joined'))

    def __init__(self, dateOfExecution, topic, teacher_id):
        self.dateOfExecution = dateOfExecution
        self.topic = topic
        self.teacher_id = teacher_id

class Class(db.Model):
    __tablename__ = "class"

    name = db.Column(db.String(128), primary_key=True)
    pupilCount = db.Column(db.Integer, nullable=False)
    pupils = db.relationship('Pupil', backref='class')

    def __init__(self, name, pupilCount = 0):
        self.name = name.upper()
        self.pupilCount = pupilCount

class ListOfGrades(db.Model):
    __tablename__ = "listofgrades"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    average = db.Column(db.Numeric(asdecimal=False), nullable=False)
    pupil_id = db.Column(db.ForeignKey('pupil.id'))
    grades = db.relationship('Grade', backref=backref('listofgrades', lazy='joined'))

    def __init__(self, name, average, pupil_id):
        self.name = name
        self.average = average
        self.pupil_id = pupil_id

class Frequency(db.Model):
    __tablename__ = "frequency"
    
    id_lesson = db.Column(db.ForeignKey('lesson.id'), primary_key=True)
    id_pupil = db.Column(db.ForeignKey('pupil.id'), primary_key=True)


    def __init__(self, lesson_id, pupil_id):
        self.lesson_id = lesson_id
        self.pupil_id = pupil_id

configure_mappers()

    