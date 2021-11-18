from flask import redirect, request, Blueprint, render_template
from flask.helpers import make_response, url_for
from app.models.Apple import Apple, db

apple = Blueprint('apple', __name__)

@apple.route('/<int:id>', methods=['GET'])
def landing(id, success=False):
    apple = db.session.query(Apple).get(id)
    return render_template('apple.html', apple=apple)

@apple.route('/<int:id>', methods=['PUT', 'DELETE'])
def update(id):
    apple = db.session.query(Apple).get(id)
    if apple:
        if request.method == 'PUT':
            appleName = request.form.get("appleName")
            origin = request.form.get("origin")
            imageLink = request.form.get("imageLink")
            apple.name = appleName 
            apple.image_link = imageLink 
            apple.origin_country = origin
            db.session.add(apple)
            db.session.commit()
            return make_response(redirect(url_for('apple.landing', id=id, success=True)))
        else:
            db.session.delete(apple)
            db.session.commit()
            return make_response(redirect(url_for('index.landing'), code=200))
            
