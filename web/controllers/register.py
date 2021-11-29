from sqlalchemy import func
from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Lesson, Teacher, User, Pupil, Grade, Class, ListOfGrades, db
import random

register = Blueprint('register', __name__)


@register.route('', methods=['GET', 'POST'])
def add_user(success=False):
    if request.method == 'POST':
        userLogin = request.form.get("userLogin")
        userName = request.form.get("userName")
        userSurname = request.form.get("userSurname")
        userPassword = request.form.get("userPassword")

        teacherRoom = request.form.get("teacherRoom")
        pupilBirthDate = request.form.get("pupilBirthDate")

        user_id = (db.session.query(func.max(User.id)).scalar() or 0) + 1
        
        if (teacherRoom != None):
            db.session.add(Teacher(user_id, userLogin, userName, userSurname, userPassword, teacherRoom))
            db.session.commit()
            
        elif (pupilBirthDate != None):
            class_name = db.session.query(Class.name).order_by(func.random()).first()[0]
            
            db.session.add(Pupil(user_id, userLogin, userName, userSurname, userPassword, pupilBirthDate, class_name))
            a_class = db.session.query(Class).filter(Class.name == class_name).first()
            a_class.pupilCount += 1
            db.session.add(a_class)
            db.session.commit()

            listOfGrades = ListOfGrades('Chemistry', 0, user_id)
            db.session.add(listOfGrades)
            db.session.commit()

            listOfGrades = ListOfGrades('Maths', 0, user_id)
            db.session.add(listOfGrades)
            db.session.commit()

            listOfGrades = ListOfGrades('English', 0, user_id)
            db.session.add(listOfGrades)
            db.session.commit()

        return make_response(redirect(url_for('register.add_user', success=True)))
    else:
        return render_template('register.html', success=success)