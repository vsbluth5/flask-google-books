# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import getProperties
from datetime import datetime
import os


# -- Initialization section --
app = Flask(__name__)
app.config['BOOKS_KEY'] = os.getenv("BOOKS_KEY")


# -- Routes section --

@app.route('/')
@app.route('/index')
def index():
    props = getProperties("random", app.config["BOOKS_KEY"])
    print(props['allcovers'])
    return render_template('index.html', props=props, time=datetime.now())
 
    
@app.route('/result', methods=['GET', 'POST'])
def show_book():
    choice = dict(request.form)
    props = getProperties(choice['interest'], app.config["BOOKS_KEY"])
    return render_template('results.html', props=props, time=datetime.now())