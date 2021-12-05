from flask import request, Blueprint, render_template, redirect, session
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, Lesson, Frequency, db

attendance = Blueprint('attendance', __name__)

@attendance.route('', methods=['GET'])
def landing():

    pupil_id = db.session.query(User.id).filter(User.login == session["name"]).first()
    attendance = db.session.query(Frequency, Lesson).join(Lesson).filter(Frequency.id_pupil == pupil_id[0]).all()
    return render_template('pupil/attendance.html', attendance=attendance)