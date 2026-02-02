from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from forms import *
from models import *
from db import *




app = Flask(__name__)
app.config['SECRET_KEY'] = 'MYSUPERSECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = StudentListForm
    studentlist = Students.query.all
    return render_template('index.html')
#
# @app.route('/add', methods=['GET', 'POST'])
# def add ():
#     form = AddStudent
#
#     if form.validate_on_submit():
#         studentsdetails = Students(name=form.name.data, email=form.email.data, course=form.course.data,
#                                    value=form.value.data, date=form.date.data)
#         db.session.add(studentsdetails)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('add.html', form=form)






    return render_template('add.html')













@app.route('/about', methods=['GET', 'POST'])
def about ():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    today_weekday = datetime.today().weekday()
    return render_template('contact.html', weekday=today_weekday)



if __name__ == '__main__':
    app.run(debug=True)
#
# @app.route('/namravli/<int:a>/<int:b>', methods=['GET', 'POST'])
# def namravli (a, b):
#     return f"პირველი რიცხვი: {a}, მეორე რიცხვი: {b}, ნამრავლი უდრის {a*b}"
#
# @app.route('/myjson', methods=['GET', 'POST'])
# def myjson ():
#     return {
#   "name": "John Doe",
#   "age": 30,
#   "email": "john.doe@example.com",
#   "isActive": "True"
# }
#
# @app.route('/misalmeba/<string:name>', methods=['GET', 'POST'])
# def misalmeba (name):
#     return f"გამარჯობა მომხმარებელო: {name}"
#
