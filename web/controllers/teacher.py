from flask import request, Blueprint, render_template, redirect, sessions
from flask.helpers import make_response, url_for
from app.models.models import Teacher, User, Pupil, db
from flask import Flask, render_template, redirect, request, session
# from flask_session import Session

teacher = Blueprint('teacher', __name__)

@teacher.route('', methods=['GET'])
def landing():
    return render_template('teacher.html')
