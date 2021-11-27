from flask import Blueprint, render_template

classes = Blueprint('classes', __name__)

@classes.route('/', methods=['GET'])
def landing():
    return render_template('teacher/classes.html')