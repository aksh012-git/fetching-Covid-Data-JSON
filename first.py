# -*- coding: utf-8 -*-
"""
Created on Mon june 31 13:13:47 2021

@author: Aksh
"""


from flask import Flask,render_template,url_for,request


app = Flask(__name__)


import requests


response = requests.get("https://api.covid19india.org/data.json")
coviddata = response.json()

#print(coviddata)
#print(len(coviddata))

w = []
z = []
for i in coviddata['cases_time_series']:
    for x in i:
        w.append(i[x])
    z.append(w)
    w = []


@app.route('/')
def index():
    return render_template('index.html',len = len(z),data = reversed(z))

if __name__ == '__main__':
    app.run(debug=True)
