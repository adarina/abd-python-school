from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.Teacher import Teacher, User, Pupil, db

grade = Blueprint('grade', __name__)

@grade.route('/', methods=['GET'])
def landing():
    # grades = db.session.query(User).all()
    # teachers = db.session.query(Teacher).all()
    # return render_template('grade.html', teachers=teachers)
    return render_template('pupil/grade.html')