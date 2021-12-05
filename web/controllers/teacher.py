from flask import request, Blueprint, render_template, redirect, session
from flask.helpers import make_response, url_for
from sqlalchemy import func
from app.models.models import Grade, Class, Frequency, Lesson, Teacher, User, Pupil, db
from flask import Flask, render_template, redirect, request, session

teacher = Blueprint('teacher', __name__)

@teacher.route('', methods=['GET'])
def landing():
    teacher_id = db.session.query(Teacher.id).filter(Teacher.login == session["name"]).first()[0]
    gradings = db.session.query(Pupil, Grade)\
        .filter(Grade.teacher_id == teacher_id)\
        .filter(Grade.evaluated == Pupil.id).order_by(Grade.date).limit(3).all()
    pupils = db.session.query(Pupil).all()
    classes = db.session.query(Class).order_by(Class.name).all()
    lectures = db.session.query(Lesson, Class, func.count(1).filter(Frequency.frequency > 0))\
        .select_from(Lesson).join(Class, Frequency).filter(Lesson.teacher_id == teacher_id)\
        .group_by(Lesson, Class).order_by(Lesson.dateOfExecution.desc()).limit(3).all()
    return render_template('teacher.html', gradings=gradings, pupils=pupils, classes=classes, lectures=lectures)
