import random
import string

from web.data_generation.connection_orm import session
from web.models import User, Class
from helpers import random_date
from mytimer import Timer
from common import NAMES, SURNAMES




# with Timer('Generate users') as t:
#     for i in range():
#         db.session.add(User(
#             login=random.choice(string.ascii_uppercase),
#             name=random.choice(string.NAMES),
#             surname=random.choice(string.SURNAMES),
#             password=random.choice(string.ascii_uppercase),     
#         ))
#     session.commit()

# with Timer('Generate users') as t:
#     for i in range(1000):
#         session.add(User(
#             login=random.choice(string.ascii_uppercase),
#             name=random.choice(string.NAMES),
#             surname=random.choice(string.SURNAMES),
#             password=random.choice(string.ascii_uppercase),     
#         ))
#     session.commit()

# with Timer('Generate users') as t:
#     users = []
#     for i in range(10000):
#         users.append({
#             'name': random.choice(NAMES),
#             'surname': random.choice(SURNAMES),
#             'date_of_birth': random_date()
#         })
#     session.execute(User.__table__.insert(users))
#     session.commit()


# class Class(db.Model):
#     __tablename__ = "class"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), nullable=False)
#     pupilCount = db.Column(db.Integer, nullable=False)

#     def __init__(self, name, pupilCount):
#         self.name = name
#         self.pupilCount = pupilCount

# class User(db.Model):
#     __tablename__ = "user"
    
#     id = db.Column(db.Integer, primary_key=True)
#     login = db.Column(db.String(128), nullable=False)
#     name = db.Column(db.String(128), nullable=False)
#     surname = db.Column(db.String(128), nullable=False)
#     password = db.Column(db.String(128), nullable=False)
    
#     def __init__(self, login, name, surname, password = None):
#         self.name = name
#         self.login = login
#         self.surname = surname
#         self.password = password

# class Teacher(db.Model):
#     __tablename__ = "teacher"
    
#     user_id = db.Column(db.ForeignKey('user.id'), primary_key=True)
#     room = db.Column(db.Integer, nullable=False)
#     user = db.relationship('User')
    
#     def __init__(self, user_id, room):
#         self.user_id = user_id
#         self.room = room

# class Pupil(db.Model):
#     __tablename__ = "pupil"
    
#     user_id = db.Column(db.ForeignKey('user.id'), primary_key=True)
#     birthDate = db.Column(db.Integer, nullable=False)
#     user = db.relationship('User')
#     class_id = db.Column(db.ForeignKey('class.id'))
#     _class = db.relationship('Class')
#     lesson_id = db.Column(db.ForeignKey('lesson.id'), nullable=True)
#     lesson = db.relationship('Lesson')
    
#     def __init__(self, user_id, birthDate, class_id, lesson_id):
#         self.user_id = user_id
#         self.birthDate = birthDate
#         self.class_id = class_id
#         self.lesson_id = lesson_id

