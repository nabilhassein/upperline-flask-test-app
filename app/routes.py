from app import app
from flask import render_template, request
from app.models import model

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/birthstone', methods = ['GET', 'POST'])
def birthstone():
    if request.method == "GET":
        return "<h1> use the form on the <a href='/'> home page </a> </h1>"

    data = dict(request.form)
    print('birthstone data', data)

    birthstone = model.get_birthstone(data[u'date'][0])

    return render_template("birthstone.html", birthstone=birthstone)
