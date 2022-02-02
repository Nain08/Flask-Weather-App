import requests
from flask import Flask, redirect, render_template, request

app=Flask(__name__) # to initialise my app

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/results',methods=['GET','POST'])
def results():
    if request.method=="POST":
        city=request.form["city"]
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1"
        r=requests.get(url.format(city)).json()
        weather={
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        print(weather)
        return render_template('weather.html',weather=weather)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)