from flask import Blueprint, render_template
from app.models.Teacher import User, Teacher, db

login = Blueprint('login', __name__)

# @login.route('/', methods=['GET'])
# def landingl():
#     users = db.session.query(User).all()
#     return render_template('login.html', users=users)

@login.route('/', methods=['GET'])
def landing():
    teachers = db.session.query(Teacher).all()
    return render_template('login.html', teachers=teachers)