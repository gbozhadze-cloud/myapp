from db import db

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    course = db.Column(db.String(80), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

