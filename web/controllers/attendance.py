from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, db

attendance = Blueprint('attendance', __name__)

@attendance.route('', methods=['GET'])
def landing():
    # TO DO
    return render_template('pupil/attendance.html')