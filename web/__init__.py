#!/usr/bin/env python
# encoding: utf-8

# DO WPROWADZANIA ZMIAN W KONTENERZE:
# docker-compose -d --build
# docker-compose up

from os import path, system
from flask import Flask
from sqlalchemy.sql.expression import exists

from .externals import db
#from flask_migrate import Migrate 

 # 'app', a nie 'web' (jak folder) ponieważ w dockerze umieściliśmy projekt pod folderem 'app'
app = Flask(__name__, template_folder='views/page', static_folder='views/static')
app.config.from_object("app.config.Config")   
db.init_app(app)


# from .controllers.index import index
from .controllers.login import login
from .controllers.register import register
from .controllers.teacher import teacher
from .controllers.pupil import pupil
from .controllers.attendance import attendance
from .controllers.grades import grades
from .controllers.your_performance import your_performance
from .controllers.classes import classes
from .controllers.grading import grading
from .controllers.lectures import lectures

# from .controllers.apple import apple
# app.register_blueprint(index, url_prefix="/")
app.register_blueprint(login, url_prefix="/")
app.register_blueprint(register, url_prefix="/register")
app.register_blueprint(teacher, url_prefix="/teacher")
app.register_blueprint(pupil, url_prefix="/pupil")
app.register_blueprint(attendance, url_prefix="/attendance")
app.register_blueprint(grades, url_prefix="/grades")
app.register_blueprint(your_performance, url_prefix="/your_performance")
app.register_blueprint(classes, url_prefix="/classes")
app.register_blueprint(grading, url_prefix="/grading")
app.register_blueprint(lectures, url_prefix="/lectures")
# app.register_blueprint(apple, url_prefix="/apple")
#migrate = Migrate(app, db)

'''
Aby stworzyć bazę danych:
   / docker-compose exec web flask shell

A w konsoli:

    from app import db

    db.drop_all()
    db.create_all()
    db.session.commit()
''' 
               
            
'''
Aby stworzyć swojego użytkownika:
    db.session.add(User(email='abc@example.com'))
    db.session.commit()
'''

@app.before_first_request
def create_tables():
    db.create_all()
    from .models.models import Class
    app.app_context().push()
    any_class = db.session.query(Class).first()
    if not any_class:
        db.session.add(Class("1A"))
        db.session.add(Class("1B"))
        db.session.add(Class("2A"))
        db.session.add(Class("2B"))
        db.session.add(Class("3A"))
        db.session.add(Class("3B"))
    db.session.commit()

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

    # Recreate database each time for demo

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    