from flask import Blueprint, render_template
from app.models.models import Class, db

classes = Blueprint('classes', __name__)

@classes.route('/', methods=['GET'])
def landing():
    classes = db.session.query(Class).filter(Class.pupilCount > 0).all()
    return render_template('teacher/classes.html', classes=classes)