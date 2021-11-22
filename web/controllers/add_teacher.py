from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.Teacher import Teacher, db

add = Blueprint('add_teacher', __name__)

@add.route('/', methods=['GET', 'POST'])
def add_teacher(success=False):
    if request.method == 'POST':
        userName = request.form.get("userName")
        userSurname = request.form.get("userSurname")
        userPassword = request.form.get("userPassword")
        teacherRoom = request.form.get("teacherRoom")
        db.session.add(Teacher(userName, userSurname, userPassword, teacherRoom))
        db.session.commit()
        return make_response(redirect(url_for('add.add_teacher', success=True)))
    else:
        return render_template('add.html', success=success)