from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.Teacher import Teacher, User, Pupil, Grade, db

grading = Blueprint('grading', __name__)

@grading.route('/', methods=['GET'])
def landing():
    gradings = db.session.query(Grade).all()
    # teachers = db.session.query(Teacher).all()
    # return render_template('grade.html', teachers=teachers)
    return render_template('teacher/grading.html', gradings=gradings)