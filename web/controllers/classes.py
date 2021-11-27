from flask import Blueprint, render_template

classes = Blueprint('classes', __name__)

@classes.route('/', methods=['GET'])
def landing():
    # TO DO
    return render_template('teacher/classes.html')