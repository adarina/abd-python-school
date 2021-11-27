from flask import request, Blueprint, render_template, redirect, sessions
from flask.helpers import make_response, url_for
from flask_sqlalchemy import _SessionSignalEvents
from app.models.models import Teacher, User, Pupil, db
from flask import Flask, render_template, redirect, request, session
# from flask_session import Session

teacher = Blueprint('teacher', __name__)

# @login.route('/', methods=['GET'])
# def landingl():
#     users = db.session.query(User).all()
#     return render_template('login.html', users=users)

@teacher.route('/', methods=['GET'])
def landing():
    teachers = db.session.query(Teacher).all()
    return render_template('teacher.html', teachers=teachers)

@teacher.route('/', methods=['GET', 'POST'])
def log_out(success=False):
    session["name"] = None
    return render_template('login.html', success=success)      