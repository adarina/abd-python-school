from flask import request, Blueprint, render_template, redirect, sessions
from flask.helpers import url_for
from app.models.models import Teacher, User, Pupil, db
from flask import Flask, render_template, redirect, request, session

login = Blueprint('login', __name__)


@login.route('', methods=['GET'])
def landing():
    return render_template('login.html')


@login.route('', methods=['POST'])
def log_in(success=False):
    if request.method == 'POST':
        userLogin = request.form.get("userLogin")
        userPassword = request.form.get("userPassword")
        user_login = db.session.query(User.login).filter(User.login == userLogin).first()
        user_password = db.session.query(User.password).filter(User.login == userLogin).first()
        user_id = db.session.query(User.id).filter(User.login == userLogin).first()

        if (user_login != None and user_password != None):
            if (user_login[0] == userLogin and user_password[0] == userPassword):

                pupil_id = db.session.query(Pupil.id).filter(Pupil.id == user_id[0]).first()
                teacher_id = db.session.query(Teacher.id).filter(Teacher.id == user_id[0]).first()

                if (teacher_id != None):
                    if(user_id[0] == teacher_id[0]):
                        session["name"] = request.form.get("userLogin")
                        return redirect(url_for('teacher.landing'))

                if (pupil_id != None):
                    if(user_id[0] == pupil_id[0]):
                        session["name"] = request.form.get("userLogin")
                        return redirect(url_for('pupil.landing'))

        return render_template('login.html', success=success)
    else:
        return render_template('login.html', success=success)

@login.route('', methods=['GET', 'POST'])
def log_out():
    session["name"] = None
    print("here")
    return redirect(url_for('/login'))    
