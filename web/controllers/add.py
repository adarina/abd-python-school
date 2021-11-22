from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.Teacher import Teacher, User, Pupil, db

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
        elif (pupilBirthDate != None):
            db.session.commit()
            db.session.add(Pupil(user.id, pupilBirthDate))
            db.session.commit()

        return make_response(redirect(url_for('add.add_user', success=True)))
    else:
        return render_template('add.html', success=success)


