from flask import request, Blueprint, render_template, redirect, sessions
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, Class, db
from flask import Flask, render_template, redirect, request, session
from sqlalchemy import func
from datetime import datetime
# from flask_session import Session
import random
import string

from app.helpers import random_date
from app.mytimer import Timer
from app.common import NAMES, SURNAMES

teacher = Blueprint('teacher', __name__)

@teacher.route('/', methods=['GET'])
def landing():
    return render_template('teacher.html')

@teacher.route('/', methods=['GET', 'POST'])
def query(success=False):
    if request.method == 'POST':
        with Timer('Generate users') as t:
            for i in range(10000):
                user_id = (db.session.query(func.max(User.id)).scalar() or 0) + 1
                class_name = db.session.query(Class.name).order_by(func.random()).first()[0]
                db.session.add(Pupil(
                    user_id,
                    login=random.choice(string.ascii_uppercase),
                    name=random.choice(string.ascii_uppercase),
                    surname=random.choice(string.ascii_uppercase),
                    password=random.choice(string.ascii_uppercase),
                    birthDate=datetime.strptime('1/1/2008', '%m/%d/%Y'),
                    class_name=class_name
                ))
            db.session.commit()

        return render_template('teacher.html')
    return render_template('teacher.html')
