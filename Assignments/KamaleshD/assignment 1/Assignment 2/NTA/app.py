from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/About us")
def about():
    return render_template('about.html')

@app.route("/SignIn")
def SignIn():
    return render_template('SignIn.html') 

@app.route("/SignUP")
def SignUP():
    return render_template('SignUP.html') 
    

