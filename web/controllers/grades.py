from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Teacher, Grade, User, Pupil, db
from flask import Flask, render_template, redirect, request, session

grades = Blueprint('grades', __name__)

@grades.route('/', methods=['GET'])
def landing():
    pupil_id = db.session.query(User.id).filter(User.login == session["name"]).first()
    grades = db.session.query(Grade).filter(Grade.evaluated == pupil_id[0]).all()
    return render_template('pupil/grades.html', grades=grades)