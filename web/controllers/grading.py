from flask import request, Blueprint, render_template, redirect, session, jsonify
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Grade, ListOfGrades, Pupil, db
from sqlalchemy.sql import func, label

grading = Blueprint('grading', __name__)


@grading.route('', methods=['GET'])
def landing():
    success = request.args.get('success')
    teacher_id = db.session.query(User.id).filter(User.login == session["name"]).first()
    gradings = db.session.query(Pupil, Grade)\
        .filter(Grade.teacher_id == teacher_id[0])\
        .filter(Grade.evaluated == Pupil.id).order_by(Grade.date).limit(6).all()
    pupils = db.session.query(Pupil).all()

    return render_template('teacher/grading.html', gradings=gradings, pupils=pupils, success=success)


@grading.route('', methods=['POST'])
def add_grade(success=False):
    gradeDate = request.form.get("gradeDate")
    gradeDescription = request.form.get("gradeDescription")
    gradePupil = request.form.get("gradePupil")
    gradeSubject = request.form.get("gradeSubject").upper()
    gradeGrade = request.form.get("gradeGrade")
    gradeWeight = request.form.get("gradeWeight")

    pupil_id = db.session.query(Pupil.id).filter(Pupil.id == gradePupil).first()[0]
    gradelist_id = db.session.query(ListOfGrades.id).filter(ListOfGrades.name == gradeSubject).first()[0]
    teacher_id = db.session.query(Teacher.id).filter(Teacher.login == session["name"]).first()[0]

    grade = Grade(gradeDate, pupil_id, gradeDescription, gradeSubject, gradeGrade, gradeWeight, teacher_id, gradelist_id)
    db.session.add(grade)
    db.session.commit()

    average = db.session.query(label('average', 1.0 * func.sum(Grade.grade * Grade.weight) / func.sum(Grade.weight)))\
        .filter(Grade.subject == gradeSubject)\
        .filter(Grade.evaluated == pupil_id).scalar()
    db.session.query(ListOfGrades)\
        .filter(ListOfGrades.name == gradeSubject)\
        .filter(ListOfGrades.pupil_id == pupil_id)\
        .update({ListOfGrades.average: average})

    db.session.commit()
    return make_response(jsonify({'message': 'Created'}), 200)
    
@grading.route('/update', methods=['POST'])
def update():
    gradeId = request.form.get("gradeId")
    gradeDate = request.form.get("gradeDate")
    gradeDescription = request.form.get("gradeDescription")
    gradeSubject = request.form.get("gradeSubject").upper()
    gradeGrade = request.form.get("gradeGrade")
    gradeWeight = request.form.get("gradeWeight")
    
    grade = db.session.query(Grade).filter(Grade.id == gradeId).first()

    grade.date = gradeDate
    grade.description = gradeDescription
    grade.subject = gradeSubject
    grade.grade = gradeGrade
    grade.weight = gradeWeight
    db.session.commit()

    average = db.session.query(label('average', 1.0 * func.sum(Grade.grade * Grade.weight) / func.sum(Grade.weight)))\
        .filter(Grade.subject == gradeSubject)\
        .filter(Grade.listofgrades_id == grade.listofgrades_id).scalar()
    db.session.query(ListOfGrades)\
        .filter(ListOfGrades.name == gradeSubject)\
        .filter(ListOfGrades.pupil_id == grade.listofgrades_id)\
        .update({ListOfGrades.average: average})

    db.session.commit()
        
    return make_response(jsonify({'message': 'Updated'}), 200)

@grading.route('/delete/<gradeId>', methods=['DELETE'])
def delete(gradeId):
    grade = db.session.query(Grade).filter(Grade.id == gradeId).first()
    gradeSubject = grade.subject
    gradeLog = grade.listofgrades_id
    
    db.session.delete(grade)
    db.session.commit()

    average = db.session.query(label('average', 1.0 * func.sum(Grade.grade * Grade.weight) / func.sum(Grade.weight)))\
        .filter(Grade.subject == gradeSubject)\
        .filter(Grade.listofgrades_id == gradeLog).scalar() or 0
    db.session.query(ListOfGrades)\
        .filter(ListOfGrades.name == gradeSubject)\
        .filter(ListOfGrades.pupil_id == gradeLog)\
        .update({ListOfGrades.average: average})

    db.session.commit()
        
    return make_response(jsonify({'message': 'Deleted'}), 200)
