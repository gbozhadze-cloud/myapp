from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

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
