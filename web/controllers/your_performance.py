from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, ListOfGrades, db
from flask import Flask, render_template, redirect, request, session

your_performance = Blueprint('your_performance', __name__)

@your_performance.route('/', methods=['GET'])
def landing():
    pupil_id = db.session.query(User.id).filter(User.login == session["name"]).first()
    listofgrades = db.session.query(ListOfGrades).filter(ListOfGrades.pupil_id == pupil_id[0]).all()
    return render_template('pupil/your_performance.html', listofgrades = listofgrades)