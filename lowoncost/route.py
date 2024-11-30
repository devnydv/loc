from lowoncost import app
from flask import render_template, request, redirect, flash
import requests

@app.route("/")
def home():
    return "hi there"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods = ["GET", "POST"])
def sign():
    if request.method == "POST":
        data = request.form
        #saved = requests.post("http://127.0.0.1:5000/api/signup", json = data)
        saved = requests.post("https://lowoncost.vercel.app/api/signup", json = data)
        res =saved.json()
        msg =res["msg"]
        if msg == True:
            return redirect("/login")
        else:
            #return render_template("signup.html", e = msg)
            flash(msg)
    return render_template("signup.html")