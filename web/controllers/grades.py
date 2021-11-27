from flask import Blueprint, render_template, session
from app.models.models import Grade, User, ListOfGrades, db

grades = Blueprint('grades', __name__)

@grades.route('/', methods=['GET'])
def landing():
    pupil_id = db.session.query(User.id).filter(User.login == session["name"]).first()
    grades = db.session.query(Grade, ListOfGrades).join(ListOfGrades).filter(Grade.evaluated == pupil_id[0]).all()
    
    return render_template('pupil/grades.html', grades=grades)