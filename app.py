from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    return render_template('results.html')