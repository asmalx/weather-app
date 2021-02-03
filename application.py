import os
import requests
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
weather_api_key = '1655e8bf094e16adf3b1762669827c5d'
url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + weather_api_key

city_list  = []

def get_weather(city_list):
    weather_list = []
    for i in range(0, len(city_list)):
        response = requests.get(url.format(city_list[i])).json() 
        if  response['cod'] != 200:
            city_list.pop(i)
            continue
        curr_weather = {
            'city': response['name'],
            'temperature': response['main']['temp'], 
            'wind': response['wind']['speed'],
            'icon': response['weather'][0]['icon'],
            'info': response['weather'][0]['description'],
            'city_no_space':response['name'].replace(' ', '_'),
        }  
        city_list[i] = curr_weather['city']
        weather_list += [curr_weather] 
    return weather_list

@app.route('/') 
@app.route('/index')
def index():
    return render_template("index.html", weather_cities=get_weather(city_list))

@app.route('/submit', methods=["POST"])
def submit():
    global city_list
    ct = request.form['city']
    if len(ct) > 1:
        city_list.append(ct)
    if len(city_list) > 3:
        city_list = city_list[-3:]
    return render_template("index.html", weather_cities=get_weather(city_list))

@app.route('/widget', methods=["POST"])
def widget():
    if request.form.get("close"):
        city_to_close = request.form['close'].replace('_', ' ')
        if city_to_close in city_list:
            city_list.remove(city_to_close)
        return render_template("index.html", weather_cities=get_weather(city_list))

    elif request.form.get("details"):
        return render_template("city.html", city=request.form['details'])






