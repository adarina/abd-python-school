from sqlalchemy import func
from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, Grade, Class, ListOfGrades, db

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
        # db.session.add(user)
        
        if (teacherRoom != None):
            db.session.commit()
            db.session.add(Teacher(user_id, userLogin, userName, userSurname, userPassword, teacherRoom))
            db.session.commit()
            
        elif (pupilBirthDate != None):
            db.session.commit()
            _class = Class('2B', 0)
            db.session.add(_class)
            db.session.commit()
            class_id = db.session.query(Class.id).filter(Class.name == '2B').first()
            

            
            db.session.add(Pupil(user_id, userLogin, userName, userSurname, userPassword, pupilBirthDate, class_id[0], None))
            db.session.commit()
            a_class = db.session.query(Class).filter(Class.name == '2B').first()
            a_class.pupilCount += 1
            db.session.commit()

            listOfGrades = ListOfGrades('Chemistry',0 , user_id)
            db.session.add(listOfGrades)
            db.session.commit()

            listOfGrades = ListOfGrades('Biology',0 , user_id)
            db.session.add(listOfGrades)
            db.session.commit()

            listOfGrades = ListOfGrades('English',0 , user_id)
            db.session.add(listOfGrades)
            db.session.commit()

        return make_response(redirect(url_for('register.add_user', success=True)))
    else:
        return render_template('register.html', success=success)