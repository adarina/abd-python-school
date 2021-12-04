from flask import request, Blueprint, render_template, redirect, sessions
from flask.helpers import make_response, url_for
from flask_sqlalchemy import _SessionSignalEvents
from app.models.models import Teacher, User, Pupil, db
from flask import Flask, render_template, redirect, request, session

pupil = Blueprint('pupil', __name__)


@pupil.route('', methods=['GET'])
def landing():
    return render_template('pupil.html')

@pupil.route('', methods=['GET', 'POST'])
def log_out(success=False):
    session["name"] = None
    return render_template('login.html', success=success)      