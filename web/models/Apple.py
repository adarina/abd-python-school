from flask_sqlalchemy import SQLAlchemy
from app import db

class Apple(db.Model):
    __tablename__ = "apple"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    image_link = db.Column(db.String(512), nullable=False)
    origin_country = db.Column(db.String(128), nullable=True)
    
    def __init__(self, name, image_link, origin_country = None):
        self.name = name
        self.image_link = image_link
        self.origin_country = origin_country