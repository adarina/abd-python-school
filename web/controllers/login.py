from flask import Blueprint, render_template
from app.models.User import User, db

login = Blueprint('login', __name__)

@login.route('/', methods=['GET'])
def landing():
    users = db.session.query(User).all()
    return render_template('login.html', users=users)