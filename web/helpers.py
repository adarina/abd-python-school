import datetime
import random
from app.models.models import Grade, Class, Frequency, Lesson, Teacher, User, Pupil, Teacher, ListOfGrades, db

def random_date_sql():
    """
    This function will return a random datetime between two datetime
    objects.
    """
    start = datetime.date(year=2005, month=1, day=1)
    end = datetime.date(year=2015, month=12, day=31)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

def truncate():
    tables = ['frequency', 'listofgrades', 'class', 'lesson', 'grade', 'pupil', 'teacher']

    for table in tables:
        db.session.execute("TRUNCATE %s CASCADE" % table)
    db.session.commit()

    db.session.add(Class("1A"))
    db.session.add(Class("1B"))
    db.session.add(Class("2A"))
    db.session.add(Class("2B"))
    db.session.add(Class("3A"))
    db.session.add(Class("3B"))

    db.session.commit()