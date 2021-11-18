#!/usr/bin/env python
# encoding: utf-8

# DO WPROWADZANIA ZMIAN W KONTENERZE:
# docker-compose -d --build
# docker-compose up

from os import path, system
from flask import Flask
from .externals import db
#from flask_migrate import Migrate 

 # 'app', a nie 'web' (jak folder) ponieważ w dockerze umieściliśmy projekt pod folderem 'app'
app = Flask(__name__, template_folder='views/page', static_folder='views/static')
app.config.from_object("app.config.Config")   
db.init_app(app)


from .controllers.index import index
from .controllers.add import add
from .controllers.apple import apple
app.register_blueprint(index, url_prefix="/")
app.register_blueprint(add, url_prefix="/add")
app.register_blueprint(apple, url_prefix="/apple")
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
app.run(host='0.0.0.0', port=5000, debug=True)