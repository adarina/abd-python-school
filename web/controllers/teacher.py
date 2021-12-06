from datetime import datetime, date
import random
import string
from flask import request, Blueprint, render_template, redirect, session
from flask.helpers import make_response, url_for
from sqlalchemy import func
from app.models.models import Grade, Class, Frequency, Lesson, Teacher, User, Pupil, Teacher, ListOfGrades, db
from flask import Flask, render_template, redirect, request, session

from app.mytimer import Timer
from app.common import NAMES, SURNAMES

teacher = Blueprint('teacher', __name__)

@teacher.route('', methods=['GET'])
def landing():
    teacher_id = db.session.query(Teacher.id).filter(Teacher.login == session["name"]).first()[0]
    gradings = db.session.query(Pupil, Grade)\
        .filter(Grade.teacher_id == teacher_id)\
        .filter(Grade.evaluated == Pupil.id).order_by(Grade.date).limit(3).all()
    pupils = db.session.query(Pupil).all()
    classes = db.session.query(Class).order_by(Class.name).all()
    lectures = db.session.query(Lesson, Class, func.count(1).filter(Frequency.frequency > 0))\
        .select_from(Lesson).join(Class, Frequency).filter(Lesson.teacher_id == teacher_id)\
        .group_by(Lesson, Class).order_by(Lesson.dateOfExecution.desc()).limit(3).all()
    return render_template('teacher.html', gradings=gradings, pupils=pupils, classes=classes, lectures=lectures)


# TESTS
@teacher.route('', methods=['POST'])
def add_grade(success=False):
    with Timer('Generate users') as t:
            for i in range(10):
                user_id = (db.session.query(func.max(User.id)).scalar() or 0) + 1
                class_name = db.session.query(Class.name).order_by(func.random()).first()[0]
                start_date = datetime.strptime('1/1/2005', '%m/%d/%Y').date()
                end_date = datetime.strptime('1/1/2015', '%m/%d/%Y').date()
                random_date = random.random() * (end_date - start_date) + start_date
                db.session.add(Pupil(
                    user_id,
                    login=random.choice(string.ascii_uppercase),
                    name=random.choice(NAMES),
                    surname=random.choice(SURNAMES),
                    password=random.choice(string.ascii_uppercase),
                    birthDate=random_date,
                    class_name=class_name
                ))
                a_class = db.session.query(Class).filter(Class.name == class_name).first()
                a_class.pupilCount += 1
                db.session.add(a_class)
                db.session.commit()
                
                listOfGrades = ListOfGrades('Chemistry', 0, user_id)
                db.session.add(listOfGrades)
                db.session.commit()

                listOfGrades = ListOfGrades('Maths', 0, user_id)
                db.session.add(listOfGrades)
                db.session.commit()

                listOfGrades = ListOfGrades('English', 0, user_id)
                db.session.add(listOfGrades)
                db.session.commit()


            for i in range(5):
                user_id = (db.session.query(func.max(User.id)).scalar() or 0) + 1
                db.session.add(Teacher(
                    user_id,
                    login=random.choice(string.ascii_uppercase),
                    name=random.choice(NAMES),
                    surname=random.choice(SURNAMES),
                    password=random.choice(string.ascii_uppercase),
                    room=random.randrange(1, 20)
                ))
            db.session.commit()

    with Timer('Generate grades') as t:
        pupils = db.session.query(Pupil.id, Pupil.birthDate).all()
        teachers_ids = db.session.query(Teacher.id).all()
        today = datetime.now().date()
        date = datetime.strptime('1/1/2010', '%m/%d/%Y').date()
        past = today - date
        for ids, bds in pupils:
            age = today - bds
            if (age > past):
                gradelist_id = db.session.query(ListOfGrades.id).filter(User.id == ids).filter(ListOfGrades.name == 'ENGLISH').first()[0]
                db.session.add(Grade(
                    date=today, 
                    evaluated=ids, 
                    description=random.choice(string.ascii_uppercase), 
                    subject='ENGLISH', 
                    grade=random.randrange(1, 5), 
                    weight=random.randrange(1, 3), 
                    teacher_id = random.choice(teachers_ids)[0],
                    listofgrades_id = gradelist_id
                    ))
            else:
                gradelist_id = db.session.query(ListOfGrades.id).filter(User.id == ids).filter(ListOfGrades.name == 'CHEMISTRY').first()[0]
                db.session.add(Grade(
                    date=today, 
                    evaluated=ids, 
                    description=random.choice(string.ascii_uppercase), 
                    subject='CHEMISTRY', 
                    grade=random.randrange(1, 5), 
                    weight=random.randrange(1, 3), 
                    teacher_id = random.choice(teachers_ids)[0],
                    listofgrades_id = gradelist_id
                    ))
            db.session.commit()
    return make_response(redirect(url_for('grading.landing', success=True)))