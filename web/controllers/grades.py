from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, db

grades = Blueprint('grades', __name__)

@grades.route('/', methods=['GET'])
def landing():
    # grades = db.session.query(User).all()
    # teachers = db.session.query(Teacher).all()
    # return render_template('grade.html', teachers=teachers)
    return render_template('pupil/grades.html')