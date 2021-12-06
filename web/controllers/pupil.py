from collections import defaultdict
from flask import request, Blueprint, render_template, redirect, sessions
from datetime import datetime, timedelta
from app.models.models import Lesson, Grade, Frequency, Pupil, db
from flask import Flask, render_template, redirect, request, session
import itertools 

pupil = Blueprint('pupil', __name__)


@pupil.route('', methods=['GET'])
def landing():
    today = datetime.today().date()
    date_start = today - timedelta(days=today.weekday())
    date_end = date_start + timedelta(days=4)

    pupil_id = db.session.query(Pupil.id).filter(Pupil.login == session["name"]).first()[0]
    
    grades = db.session.query(Grade).filter(Grade.evaluated == pupil_id).order_by(Grade.date.desc()).limit(3).all()
    attendance = db.session.query(Lesson.dateOfExecution, Lesson.topic, Frequency.frequency)\
        .select_from(Lesson).join(Frequency).filter(Frequency.pupil_id == pupil_id, Lesson.dateOfExecution.between(date_start, date_end))\
        .order_by(Lesson.dateOfExecution.desc()).all()
        
    attendance_grouped = defaultdict(list)
    for date, *values in attendance:
        if (len(attendance_grouped.keys()) > 3) & (date not in attendance_grouped.keys()):
            continue
        attendance_grouped[date].append(values)
        
    return render_template('pupil.html', attendance=attendance_grouped, date_start=date_start, date_end=date_end, grades=grades)

@pupil.route('', methods=['GET', 'POST'])
def log_out(success=False):
    session["name"] = None
    return render_template('login.html', success=success)      