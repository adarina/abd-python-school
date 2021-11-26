from flask import request, Blueprint, render_template, redirect, sessions
from flask.helpers import make_response, url_for
from flask_sqlalchemy import _SessionSignalEvents
from app.models.models import Teacher, User, Pupil, db
from flask import Flask, render_template, redirect, request, session
# from flask_session import Session

login = Blueprint('login', __name__)

# @login.route('/', methods=['GET'])
# def landingl():
#     users = db.session.query(User).all()
#     return render_template('login.html', users=users)


@login.route('/', methods=['GET'])
def landing():
    teachers = db.session.query(Teacher).all()
    return render_template('login.html', teachers=teachers)

@login.route('/', methods=['GET', 'POST'])
def log_in(success=False):
    if request.method == 'POST':
        userLogin = request.form.get("userLogin")
        userPassword = request.form.get("userPassword")
        user_login = db.session.query(User.login).filter(User.login == userLogin).first()
        user_password = db.session.query(User.password).filter(User.login == userLogin).first()
        user_id = db.session.query(User.id).filter(User.login == userLogin).first()
       
        if (user_login != None and user_password != None):
            if (user_login[0] == userLogin and user_password[0] == userPassword):
              
                pupil_id = db.session.query(Pupil.user_id).filter(Pupil.user_id == user_id[0]).first()
                teacher_id = db.session.query(Teacher.user_id).filter(Teacher.user_id == user_id[0]).first()
                
                
                
                if (teacher_id != None):
                    if(user_id[0] == teacher_id[0]):
                        session["name"] = request.form.get("userLogin")
                        print(session["name"])
                        return render_template('teacher.html', success=success)
                if (pupil_id != None):
                    if(user_id[0] == pupil_id[0]):
                        session["name"] = request.form.get("userLogin")
                        print(session["name"])
                        return render_template('pupil.html', success=success)
                else: 
                    return render_template('login.html', success=success)
            return render_template('login.html', success=success)  
        else:
            return render_template('login.html', success=success)     
    else:     
        return render_template('login.html', success=success)      