from datetime import datetime
from flask import Flask, render_template
from . import app
import pandas as pd
from os import environ
from sqlalchemy import create_engine

def recup_data(url):
    print('recup', url)
    df = pd.read_csv(url)
    print(df.head())
    print(df.shape)

URL='https://data.seattle.gov/api/views/2bpz-gwpy/rows.csv?accessType=DOWNLOAD' # 2016
URL='https://data.seattle.gov/api/views/qxjw-iwsh/rows.csv?accessType=DOWNLOAD' # 2017
recup_data(URL)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
