from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    def __init__(self, name, surname, password = None):
        self.name = name
        self.surname = surname
        self.password = password