from flask import Blueprint, render_template, session
from app.models.models import Lesson, Frequency, Pupil, db
from datetime import datetime, timedelta
from collections import defaultdict

attendance = Blueprint('attendance', __name__)

@attendance.route('', methods=['GET'])
def landing():
    today = datetime.today().date()
    date_start = today - timedelta(days=today.weekday())
    date_end = date_start + timedelta(days=4)

    pupil_id = db.session.query(Pupil.id).filter(Pupil.login == session["name"]).first()[0]
    attendance = db.session.query(Lesson.dateOfExecution, Lesson.topic, Frequency.frequency)\
        .select_from(Lesson).join(Frequency).filter(Frequency.pupil_id == pupil_id, Lesson.dateOfExecution.between(date_start, date_end))\
        .order_by(Lesson.dateOfExecution.desc()).all()
        
    attendance_grouped = defaultdict(list)
    for date, *values in attendance:
        attendance_grouped[date].append(values)
        
    return render_template('pupil/attendance.html', attendance=attendance_grouped, date_start=date_start, date_end=date_end)