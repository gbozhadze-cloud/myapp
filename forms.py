from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateTimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddStudent(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    course = StringField('Course Name', validators=[DataRequired()])
    value = IntegerField('Value', validators=[DataRequired()])
    date = DateTimeField('Date', validators=[DataRequired()])
    sumbit = SubmitField('Submit')

class StudentListForm(FlaskForm):
    pass
