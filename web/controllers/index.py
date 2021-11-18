from flask import Blueprint, render_template
from app.models.Apple import Apple, db

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def landing():
    apples = db.session.query(Apple).all()
    return render_template('index.html', apples=apples)
