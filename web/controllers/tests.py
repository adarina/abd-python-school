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
from app.helpers import random_date_sql, truncate

tests = Blueprint('tests', __name__)


@tests.route('', methods=['GET'])
def landing():
    return render_template('tests.html')


@tests.route('', methods=['POST'])
def select(success=False):
    if request.form['action'] == 'First_orm':
        
        truncate()

        with Timer('Generate first orm') as t:
            for i in range(100):
                user_id = (db.session.query(
                    func.max(User.id)).scalar() or 0) + 1
                class_name = db.session.query(
                    Class.name).order_by(func.random()).first()[0]
                
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
                
                a_class = db.session.query(Class).filter(
                    Class.name == class_name).first()
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

            for i in range(10):
                user_id = (db.session.query(
                    func.max(User.id)).scalar() or 0) + 1
                db.session.add(Teacher(
                    user_id,
                    login=random.choice(string.ascii_uppercase),
                    name=random.choice(NAMES),
                    surname=random.choice(SURNAMES),
                    password=random.choice(string.ascii_uppercase),
                    room=random.randrange(1, 20)
                ))
            db.session.commit()
            
            pupils = db.session.query(Pupil.id, Pupil.birthDate).all()
            teachers_ids = db.session.query(Teacher.id).all()
            today = datetime.now().date()
            date = datetime.strptime('1/1/2010', '%m/%d/%Y').date()
            past = today - date
            for ids, bds in pupils:
                age = today - bds
                if (age > past):
                    gradelist_id = db.session.query(ListOfGrades.id).filter(
                        User.id == ids).filter(ListOfGrades.name == 'ENGLISH').first()[0]
                    db.session.add(Grade(
                        date=today,
                        evaluated=ids,
                        description=random.choice(string.ascii_uppercase),
                        subject='ENGLISH',
                        grade=random.randrange(1, 5),
                        weight=random.randrange(1, 3),
                        teacher_id=random.choice(teachers_ids)[0],
                        listofgrades_id=gradelist_id
                    ))
                else:
                    gradelist_id = db.session.query(ListOfGrades.id).filter(
                        User.id == ids).filter(ListOfGrades.name == 'CHEMISTRY').first()[0]
                    db.session.add(Grade(
                        date=today,
                        evaluated=ids,
                        description=random.choice(string.ascii_uppercase),
                        subject='CHEMISTRY',
                        grade=random.randrange(1, 5),
                        weight=random.randrange(1, 3),
                        teacher_id=random.choice(teachers_ids)[0],
                        listofgrades_id=gradelist_id
                    ))
                db.session.commit()

    
    elif request.form['action'] == 'First_sql':
    
        truncate()
        
        with Timer('Generate first sql') as t:

            pupils_values = []
            for i in range(100):
                get_class = db.session.execute(
                    "SELECT name FROM class ORDER BY RANDOM() LIMIT 1").first()

                pupils_values.append(
                    "('%s', '%s', '%s', '%s', '%s', '%s')" % (
                        random.choice(string.ascii_uppercase),
                        random.choice(string.ascii_uppercase),
                        random.choice(SURNAMES),
                        random.choice(string.ascii_uppercase),
                        random_date_sql(),
                        get_class[0]
                    )
                )
                insert_sql = """
                    INSERT INTO "pupil" (login, name, surname, password, "birthDate", class_name)
                    VALUES 
                    """
                values_sql = ",".join(pupils_values)

                result = db.session.execute(
                    insert_sql + values_sql + "RETURNING id",
                )
                [user_id] = result.fetchone()
                print("inserted!!!!!!!!!!!!!!!!")
                pupils_values.clear()
                
                lists_values = []
                lists_values.append(
                    "('%s', '%i', '%s')" % (
                        'Chemistry',
                        0,
                        user_id
                    )
                )

                lists_values.append(
                    "('%s', '%i', '%s')" % (
                        'English',
                        0,
                        user_id
                    )
                )

                lists_values.append(
                    "('%s', '%i', '%s')" % (
                        'Maths',
                        0,
                        user_id
                    )
                )
                insert_sql = """
                    INSERT INTO "listofgrades" (name, average, pupil_id)
                    VALUES 
                    """
                values_sql = ",".join(lists_values)
                db.session.execute(
                    insert_sql + values_sql,
                )
                db.session.commit()
                lists_values.clear()
               

            teachers_values = []
            for i in range(10):
                teachers_values.append(
                    "('%s', '%s', '%s', '%s', '%i')" % (
                        random.choice(string.ascii_uppercase),
                        random.choice(string.ascii_uppercase),
                        random.choice(SURNAMES),
                        random.choice(string.ascii_uppercase),
                        random.randrange(1, 20),
                    )
                )
            insert_sql = """
                INSERT INTO "teacher" (login, name, surname, password, room)
                VALUES 
                """
            values_sql = ",".join(teachers_values)
            db.session.execute(
                insert_sql + values_sql
            )
            db.session.commit()

            pupils = db.session.execute("""SELECT id, "birthDate" FROM pupil""").fetchall()
            teachers_ids = db.session.execute("SELECT id FROM teacher").fetchall()

            today = datetime.now().date()
            date = datetime.strptime('1/1/2010', '%m/%d/%Y').date()
            past = today - date
            grades_values = []
            for ids, bds in pupils:
                age = today - bds
                if (age > past):
                    gradelist_id = db.session.execute("SELECT id FROM listofgrades WHERE name='English' AND pupil_id = :ids", {'ids': ids}).first()
                    grades_values.append(
                        "('%s', '%s', '%s', '%s', '%i', '%i', '%s', '%i')" % (
                            today,
                            ids,
                            random.choice(string.ascii_uppercase),
                            'ENGLISH',
                            random.randrange(1, 5),
                            random.randrange(1, 3),
                            random.choice(teachers_ids)[0],
                            gradelist_id[0],
                        )
                    )
                
                else:
                    gradelist_id = db.session.execute("SELECT id FROM listofgrades WHERE name='Chemistry' AND pupil_id = :ids", {'ids': ids}).first()
                    grades_values.append(
                        "('%s', '%s', '%s', '%s', '%i', '%i', '%s', '%i')" % (
                            today,
                            ids,
                            random.choice(string.ascii_uppercase),
                            'CHEMISTRY',
                            random.randrange(1, 5),
                            random.randrange(1, 3),
                            random.choice(teachers_ids)[0],
                            gradelist_id[0],
                        )
                    )
                insert_sql = """
                INSERT INTO "grade" (date, evaluated, description, subject, grade, weight, teacher_id, listofgrades_id)
                VALUES
                """
                values_sql = ",".join(grades_values)
                db.session.execute(
                    insert_sql + values_sql
                )
                db.session.commit()
                grades_values.clear()

    elif request.form['action'] == 'Second_orm':
        with Timer('Generate second orm') as t:
            average = db.session.query(Class.name, func.avg(Grade.grade)).select_from(Lesson).join(Frequency, Pupil, ListOfGrades, Grade).outerjoin(Class, Class.name == Pupil.class_name).filter(Lesson.dateOfExecution == '2021-12-07', Lesson.topic == 'CHEMISTRY', Grade.date == '2021-12-07', Grade.subject == 'CHEMISTRY' ).group_by(Class.name).order_by(Class.name.asc()).all()
            print(average)

    elif request.form['action'] == 'Second_sql':
        with Timer('Generate second sql') as t:
            average = db.session.execute("""SELECT class.name, avg(grade.grade)
                                FROM lesson 
                                JOIN frequency ON lesson.id = frequency.lesson_id 
                                JOIN pupil ON pupil.id = frequency.pupil_id 
                                JOIN listofgrades ON pupil.id = listofgrades.pupil_id 
                                JOIN grade ON listofgrades.id = grade.listofgrades_id 
                                JOIN class ON class.name = pupil.class_name
                                WHERE lesson."dateOfExecution" = '2021-12-07' AND lesson.topic = 'CHEMISTRY' AND grade.date = '2021-12-07' AND grade.subject = 'CHEMISTRY'
                                GROUP BY class.name ORDER BY class.name ASC""").fetchall()
            print(average)
 

    return make_response(redirect(url_for('tests.landing', success=True)))