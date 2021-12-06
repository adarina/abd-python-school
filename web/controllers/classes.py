from collections import defaultdict
from flask import Blueprint, render_template
from sqlalchemy.orm import joinedload
from app.models.models import Pupil, Class, db

classes = Blueprint('classes', __name__)

@classes.route('', methods=['GET'])
def landing():
    classes = db.session.query(Class, Pupil).select_from(Class).join(Pupil).filter(Class.pupilCount > 0)\
        .order_by(Class.name).options(joinedload(Class.pupils)).all()
    pupils_per_class = defaultdict(list)
    for class_, pupil in classes:
        pupils_per_class[class_.name].append(pupil)
        
    return render_template('teacher/classes.html', classes=pupils_per_class)