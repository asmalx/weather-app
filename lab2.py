import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__) #referenced to This file
app.config['SECRET_KEY'] = 'you-will-never-guess'

path = 'E:\\lab2\\'
lbl1 = "Processing satelite data"
lbl2 = "Satelite data managing"
rows = ['VCI', 'TCI', 'VHI']

# route() decorator that is used to register a view function for a given URL rule. 
@app.route('/') 
@app.route('/index')
def index():
    return render_template("index.html", label=lbl2, submit=submit, regions='regions', rows=rows)


@app.route('/submit', methods=["POST"])
def submit():
    content_year = request.form['years']
    content_weeks = request.form['weeks']
    region = request.form["region"]
    data_row = request.form['row']

    return render_template("index.html", label=lbl2, submit=submit, regions=[1,23], rows=rows, comment='checked')
    return render_template("submit.html", return_back=return_back,  label=lbl1, years=years, weeks = weeks, region=region, row=data_row)


@app.route('/return_back', methods=["POST"])
def return_back():
    return render_template("index.html", label=lbl2, submit=submit, regions=lab1.regions, rows=rows)














#requarements:
# - Chosing VCI, TCI, VHI row (drop-down list)
# - choose the region (drop-down list)
# - weeks interlav
# - tables, graphs
# - add to repo 
# jinja2
#функция render_template вызывает шаблонизатор Jinja2,
#  который является частью фреймворка Flask. 
# Jinja2 заменяет блоки {{...}} на соответствующие им значения,
#  переданные как аргументы шаблона.
#Представления views — это обработчики, которые отвечают на 
# запросы веб-браузера
