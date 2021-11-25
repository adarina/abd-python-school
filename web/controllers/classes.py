from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, db

classes = Blueprint('classes', __name__)

@classes.route('/', methods=['GET'])
def landing():
    return render_template('teacher/classes.html')