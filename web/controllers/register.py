from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, Grade, Class, db

register = Blueprint('register', __name__)


@register.route('/', methods=['GET', 'POST'])
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
            # db.session.add(Grade(1, "lol", "lol2", 2,3,user.id))
            # db.session.commit()
        elif (pupilBirthDate != None):
            db.session.commit()
            _class = Class('2B', 0)
            db.session.add(_class)
            db.session.commit()
            class_id = db.session.query(Class.id).filter(Class.name == '2B').first()
            # pupil_count = db.session.query(Class.pupilCount).filter(Class.name == '2B').first()

            print(class_id[0])
            print(user.id)
            db.session.add(Pupil(user.id, pupilBirthDate, class_id[0]))
            db.session.commit()
            a_class = db.session.query(Class).filter(Class.name == '2B').first()
            a_class.pupilCount += 1

            # db.session.update(Class).where(Class.id == class_id).values(pupilCount = pupil_count + 1)
            db.session.commit()
            

            # grade = Grade(1, "lol", "lol2", 2,3,9)
            # db.session.add(grade)
            # db.session.commit()

        return make_response(redirect(url_for('register.add_user', success=True)))
    else:
        return render_template('register.html', success=success)


#  id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.Integer, nullable=False)
#     evaluated = db.Column(db.Pupil, nullable=False)
#     description = db.Column(db.String(128), nullable=False)
#     subject = db.Column(db.String(128), nullable=False)
#     grade = db.Column(db.Integer, nullable=False)
#     weight = db.Column(db.Integer, nullable=False)
#     teacher_id = db.Column(db.ForeignKey('teacher.user_id'))
#     user = db.relationship('Teacher')