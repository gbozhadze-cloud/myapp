from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about ():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/namravli/<int:a>/<int:b>', methods=['GET', 'POST'])
def namravli (a, b):
    return f"პირველი რიცხვი: {a}, მეორე რიცხვი: {b}, ნამრავლი უდრის {a*b}"

@app.route('/myjson', methods=['GET', 'POST'])
def myjson ():
    return {
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com",
  "isActive": "True"
}

@app.route('/misalmeba/<string:name>', methods=['GET', 'POST'])
def misalmeba (name):
    return f"გამარჯობა მომხმარებელო: {name}"

@app.errorhandler(404)
def page_not_found(e):
    return "თქვენ მოხვდით არარსებულ გვერდზე, გთხოვთ დაბრუნდეთ მთავარ გვერდზე", 404


if __name__ == '__main__':
    app.run(debug=True)
