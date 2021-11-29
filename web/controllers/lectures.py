from flask import request, Blueprint, render_template, redirect, session
from flask.helpers import make_response, url_for
from app.models.models import User, Grade, Lesson, Class, Pupil, db

lectures = Blueprint('lectures', __name__)

@lectures.route('/', methods=['GET'])
def landing():
    teacher_id = db.session.query(User.id).filter(User.login == session["name"]).first()
    lectures = db.session.query(Lesson, Class).join(Class).filter(Lesson.teacher_id == teacher_id[0]).all()

    pupils = db.session.query(Lesson, Class, Pupil).filter(Lesson.teacher_id == teacher_id[0]).filter(Class.name == '2B').all()

    print(pupils)
    return render_template('teacher/lectures.html', lectures=lectures, pupils=pupils)

@lectures.route('/', methods=['GET', 'POST'])
def add_lecture(success=False):
    if request.method == 'POST':
        lectureDate = request.form.get("lectureDate")
        lectureTopic = request.form.get("lectureTopic")
        lectureClass = request.form.get("lectureClass")
    
        teacher_id = db.session.query(User.id).filter(User.login == session["name"]).first()
        class_id = db.session.query(Class.id).filter(Class.name == '2B').first()

        lecture = Lesson(lectureDate, lectureTopic, teacher_id[0], class_id[0])
        db.session.add(lecture)
        db.session.commit()

        return make_response(redirect(url_for('lectures.add_attendance', success=True)))
    else:
        return render_template('lectures.html', success=success)

@lectures.route('/', methods=['GET', 'POST'])
def add_attendance(success=False):
    if request.method == 'POST':
        checkbox = request.form.get("checkbox")
        print(checkbox)
        print("lol")
    
        # teacher_id = db.session.query(User.id).filter(User.login == session["name"]).first()
        # class_id = db.session.query(Class.id).filter(Class.name == '2B').first()

        # lecture = Lesson(lectureDate, lectureTopic, teacher_id[0], class_id[0])
        # db.session.add(lecture)
        # db.session.commit()

        return make_response(redirect(url_for('lectures.add_attendance', success=True)))
    else:
        return render_template('lectures.html', success=success)