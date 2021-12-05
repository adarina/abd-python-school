from flask import jsonify, request, Blueprint, render_template, redirect, session
from sqlalchemy import func
from flask.helpers import make_response, url_for
from sqlalchemy import or_, literal
from app.models.models import Pupil, Teacher, Frequency, User, Grade, Lesson, Class, db

lectures = Blueprint('lectures', __name__)

@lectures.route('', methods=['GET'])
def landing():
    success = request.args.get('success')
    classes = db.session.query(Class).order_by(Class.name).all()
    teacher_id = db.session.query(Teacher.id).filter(Teacher.login == session["name"]).first()[0]
    lectures = db.session.query(Lesson, Class, func.count(1).filter(Frequency.frequency > 0))\
        .select_from(Lesson).join(Class, Frequency).filter(Lesson.teacher_id == teacher_id)\
        .group_by(Lesson, Class).order_by(Lesson.dateOfExecution).limit(3).all()
    return render_template('teacher/lectures.html', lectures=lectures, classes=classes, success=success)

@lectures.route('', methods=['POST'])
def add_lecture():
    lectureDate = request.form.get("lectureDate")
    lectureTopic = request.form.get("lectureTopic").upper()
    lectureClass = request.form.get("lectureClass").upper()
    lectureFrequency =[]
    for key in request.form.keys():
        if key[0].isdigit():
            freq = request.form.get(key)
            id = key.split('-')[0]
            lectureFrequency.append((id, freq))
    

    teacher_id = db.session.query(Teacher.id).filter(Teacher.login == session["name"]).first()[0]
    lecture = Lesson(lectureDate, lectureTopic, teacher_id, lectureClass)
    db.session.add(lecture)
    db.session.flush()
    db.session.refresh(lecture)
    
    for pupil, freq_type in lectureFrequency:
        freq = Frequency(lecture.id, pupil, freq_type)
        db.session.add(freq)

    db.session.commit()

    return make_response(redirect(url_for('lectures.landing', success=True)))
    
@lectures.route('/get-class-pupils', methods=['GET'])
def get_class_pupils():
    class_name = request.args.get('class')
    pupils = db.session.query(Pupil).filter(Pupil.class_name == class_name).all()
    return jsonify(pups = [ pupil.serialize() for pupil in pupils ]), 200