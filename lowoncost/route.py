from lowoncost import app
from flask import render_template

@app.route("/")
def home():
    return "hi there"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def sign():
    return render_template("signup.html")