from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="views")
    app.config.from_object("app.config.Config")    # 'app', a nie 'web' (jak folder) ponieważ w dockerze umieściliśmy projekt pod folderem 'app'
    db.init_app(app)
    return app