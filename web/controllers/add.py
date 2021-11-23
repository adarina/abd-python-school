from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.Teacher import Teacher, User, Pupil, Grade, db

add = Blueprint('add', __name__)


@add.route('/', methods=['GET', 'POST'])
def add_user(success=False):
    if request.method == 'POST':
        userLogin = request.form.get("userLogin")
        userName = request.form.get("userName")
        userSurname = request.form.get("userSurname")
        userPassword = request.form.get("userPassword")

        teacherRoom = request.form.get("teacherRoom")
        pupilBirthDate = request.form.get("pupilBirthDate")

        user = User(userLogin, userName, userSurname, userPassword)
        db.session.add(user)
        
        if (teacherRoom != None):
            db.session.commit()
            db.session.add(Teacher(user.id, teacherRoom))
            db.session.commit()
            db.session.add(Grade(1, "lol", "lol2", 2,3,user.id))
            db.session.commit()
        elif (pupilBirthDate != None):
            db.session.commit()
            p = Pupil(user.id, pupilBirthDate)
            db.session.add(Pupil(user.id, pupilBirthDate))
            db.session.commit()
            grade = Grade(1, "lol", "lol2", 2,3,9)
            db.session.add(grade)
            db.session.commit()

        return make_response(redirect(url_for('add.add_user', success=True)))
    else:
        return render_template('add.html', success=success)


#  id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.Integer, nullable=False)
#     evaluated = db.Column(db.Pupil, nullable=False)
#     description = db.Column(db.String(128), nullable=False)
#     subject = db.Column(db.String(128), nullable=False)
#     grade = db.Column(db.Integer, nullable=False)
#     weight = db.Column(db.Integer, nullable=False)
#     teacher_id = db.Column(db.ForeignKey('teacher.user_id'))
#     user = db.relationship('Teacher')