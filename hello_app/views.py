from datetime import datetime
from flask import Flask, render_template
#from . import app
import pandas as pd
from os import environ
from sqlalchemy import create_engine, text
import re

app = Flask(__name__)    # Create an instance of the class for our use

def recup_data(url):
    print('recup', url)
    df = pd.read_csv(url)

    cols = [re.sub(r"[()]", "_", c) for c in list(df.columns)]
    df.columns = cols

    print(df.head())
    print(df.shape)
    df.to_sql('SEATTLE', engine, if_exists='append', index=False)

db_uri = environ.get('BDD_URI')
engine = create_engine(db_uri, echo=True)
print('engine :', engine)
#df=pd.read_sql("""SELECT * FROM "SEATTLE" LIMIT 10""", con=engine)
#print(df)

URL='https://data.seattle.gov/api/views/2bpz-gwpy/rows.csv?accessType=DOWNLOAD' # 2016
#recup_data(URL)
URL='https://data.seattle.gov/api/views/qxjw-iwsh/rows.csv?accessType=DOWNLOAD' # 2017
#recup_data(URL)

@app.route("/")
def home():
    print('home...')
    n=0
    df=pd.read_sql("""SELECT count(*) AS N FROM "SEATTLE" """, con=engine)
    return render_template("home.html", n=df)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
