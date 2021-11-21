from flask_sqlalchemy import SQLAlchemy
from app import db
from models.User import user

class Teacher(db.Model):
    __tablename__ = "teacher"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    room = db.Column(db.Integer, nullable=False)
    
    def __init__(self, user_id, room):
        self.user_id = user_id
        self.room = room