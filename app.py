import pickle
from flask import Flask, request, app, render_template, url_for
import requests
import numpy as np
import pandas as pd
import os


app = Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "main":
    app.run(debug=True)