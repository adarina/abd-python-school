from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.Apple import Apple, db

add = Blueprint('add', __name__)

@add.route('/', methods=['GET', 'POST'])
def add_apple(success=False):
    if request.method == 'POST':
        appleName = request.form.get("appleName")
        origin = request.form.get("origin")
        imageLink = request.form.get("imageLink")
        db.session.add(Apple(appleName, imageLink, origin))
        db.session.commit()
        return make_response(redirect(url_for('add.add_apple', success=True)))
    else:
        return render_template('add.html', success=success)
