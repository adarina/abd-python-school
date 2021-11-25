from flask import request, Blueprint, render_template, redirect, session
from flask.helpers import make_response, url_for
from app.models.models import User, Grade, db

grading = Blueprint('grading', __name__)

@grading.route('/', methods=['GET'])
def landing():
    gradings = db.session.query(Grade).all()
    return render_template('teacher/grading.html', gradings=gradings)

@grading.route('/', methods=['GET', 'POST'])
def add_grade(success=False):
    if request.method == 'POST':
        gradeDate = request.form.get("gradeDate")
        gradeDescription = request.form.get("gradeDescription")
        gradePupil = request.form.get("gradePupil")
        gradeSubject = request.form.get("gradeSubject")
        gradeGrade = request.form.get("gradeGrade")
        gradeWeight = request.form.get("gradeWeight")

        teacher_id = db.session.query(User.id).filter(User.login == session["name"]).first()

        grade = Grade(gradeDate, gradePupil, gradeDescription, gradeSubject, gradeGrade, gradeWeight, teacher_id[0])
        db.session.add(grade)
        db.session.commit()

        return make_response(redirect(url_for('grading.add_grade', success=True)))
    else:
        return render_template('grading.html', success=success)