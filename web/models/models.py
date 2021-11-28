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
    class_id = db.Column(db.ForeignKey('class.id'))
    _class = db.relationship('Class')
    lesson_id = db.Column(db.ForeignKey('lesson.id'), nullable=True)
    lesson = db.relationship('Lesson')
    
    def __init__(self, user_id, birthDate, class_id, lesson_id):
        self.user_id = user_id
        self.birthDate = birthDate
        self.class_id = class_id
        self.lesson_id = lesson_id

class Grade(db.Model):
    __tablename__ = "grade"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    evaluated = db.Column(db.ForeignKey('pupil.user_id'))
    pupil = db.relationship('Pupil')
    description = db.Column(db.String(128), nullable=False)
    subject = db.Column(db.ForeignKey('listofgrades.id'))
    grade = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.ForeignKey('teacher.user_id'))
    teacher = db.relationship('Teacher')
    listofgrades = db.relationship('ListOfGrades')

    def __init__(self, date, evaluated, description, subject, grade, weight, teacher_id):
        self.date = date
        self.evaluated = evaluated
        self.description = description
        self.subject = subject
        self.grade = grade
        self.weight = weight
        self.teacher_id = teacher_id

class Lesson(db.Model):
    __tablename__ = "lesson"

    id = db.Column(db.Integer, primary_key=True)
    dateOfExecution = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(128), nullable=False)
    teacher_id = db.Column(db.ForeignKey('teacher.user_id'))
    teacher = db.relationship('Teacher')
    class_id = db.Column(db.ForeignKey('class.id'))
    _class = db.relationship('Class')

    def __init__(self, dateOfExecution, topic, teacher_id, class_id):
        self.dateOfExecution = dateOfExecution
        self.topic = topic
        self.teacher_id = teacher_id
        self.class_id = class_id

class Class(db.Model):
    __tablename__ = "class"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    pupilCount = db.Column(db.Integer, nullable=False)

    def __init__(self, name, pupilCount):
        self.name = name
        self.pupilCount = pupilCount

class ListOfGrades(db.Model):
    __tablename__ = "listofgrades"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    average = db.Column(db.Numeric(asdecimal=False), nullable=False)
    pupil_id = db.Column(db.ForeignKey('pupil.user_id'))
    pupil = db.relationship('Pupil')

    def __init__(self, name, average, pupil_id):
        self.name = name
        self.average = average
        self.pupil_id = pupil_id

class Frequency(db.Model):
    __tablename__ = "frequency"

    id = db.Column(db.Integer, primary_key=True)
    id_lesson = db.Column(db.ForeignKey('lesson_id'))
    lesson = db.relationship('Lesson')
    id_pupil = db.Column(db.ForeignKey('pupil.user_id'))
    pupil = db.relationship('Pupil')

    def __init__(self, lesson_id, pupil_id):
        self.lesson_id = lesson_id
        self.pupil_id = pupil_id


    