
from flask import request, Blueprint, render_template, redirect
from flask.helpers import make_response, url_for
from app.models.Teacher import Teacher, User, Pupil, db

log = Blueprint('log', __name__)

@log.route('/', methods=['GET', 'POST'])
def log_in(success=False):
    if request.method == 'POST':
        userName = request.form.get("userName")
        userPassword = request.form.get("userPassword")
        user_name = db.session.query(User.name).filter(User.name == userName).first()
        user_password = db.session.query(User.password).filter(User.name == userName).first()
        user_id = db.session.query(User.id).filter(User.name == userName).first()
       
        if (user_name != None and user_password != None):
            if (user_name[0] == userName and user_password[0] == userPassword):
              
                pupil_id = db.session.query(Pupil.user_id).filter(Pupil.user_id == user_id[0]).first()
                teacher_id = db.session.query(Teacher.user_id).filter(Teacher.user_id == user_id[0]).first()
                
                
                
                if (teacher_id != None):
                    if(user_id[0] == teacher_id[0]):
                        return render_template('teacher.html', success=success)
                if (pupil_id != None):
                    if(user_id[0] == pupil_id[0]):
                        return render_template('pupil.html', success=success)
                else: 
                    return render_template('log.html', success=success)
            return render_template('log.html', success=success)  
        else:
            return render_template('log.html', success=success)     
    else:     
        return render_template('log.html', success=success)      
                
    