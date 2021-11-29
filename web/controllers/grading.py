from flask import request, Blueprint, render_template, redirect, session
from flask.helpers import make_response, url_for
from app.models.models import User, Grade, ListOfGrades, Pupil, db
from sqlalchemy.sql import func

grading = Blueprint('grading', __name__)


@grading.route('/', methods=['GET'])
def landing():
    teacher_id = db.session.query(User.id).filter(User.login == session["name"]).first()
    gradings = db.session.query(Pupil, Grade, ListOfGrades)\
        .filter(Grade.teacher_id == teacher_id[0])\
        .filter(Grade.evaluated == Pupil.id)\
        .filter(ListOfGrades.name == Grade.subject).all()

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

        pupil_id = db.session.query(User.id).filter(
            User.login == gradePupil).first()
        gradelist_id = db.session.query(ListOfGrades.id).filter(
            ListOfGrades.name == gradeSubject).first()
        teacher_id = db.session.query(User.id).filter(
            User.login == session["name"]).first()

        grade = Grade(gradeDate, pupil_id[0], gradeDescription,
                      gradelist_id[0], gradeGrade, gradeWeight, teacher_id[0])
        db.session.add(grade)
        db.session.commit()

        average = db.session.query(func.avg(Grade.grade * Grade.weight)
                                   .label('average'))\
            .filter(Grade.subject == gradelist_id[0])\
            .filter(Grade.evaluated == pupil_id[0]).scalar()
        db.session.query(ListOfGrades)\
            .filter(ListOfGrades.name == gradeSubject)\
            .filter(ListOfGrades.pupil_id == pupil_id[0])\
            .update({ListOfGrades.average: average})

        db.session.commit()
        return make_response(redirect(url_for('grading.add_grade', success=True)))
    else:
        return render_template('grading.html', success=success)
