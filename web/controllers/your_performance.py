from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, db

your_performance = Blueprint('your_performance', __name__)

@your_performance.route('/', methods=['GET'])
def landing():
    return render_template('pupil/your_performance.html')