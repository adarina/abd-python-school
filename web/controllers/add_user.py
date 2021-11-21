from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.User import User, db

add_user = Blueprint('add_user', __name__)

@add_user.route('/', methods=['GET', 'POST'])
def add_user(success=False):
    if request.method == 'POST':
        userName = request.form.get("userName")
        userSurname = request.form.get("userSurname")
        userPassword = request.form.get("userPassword")
        db.session.add(User(userName, userSurname, userPassword))
        db.session.commit()
        return make_response(redirect(url_for('add_user.add_user', success=True)))
    else:
        return render_template('add_user.html', success=success)