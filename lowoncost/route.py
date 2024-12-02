from lowoncost import app
from flask import render_template, request, redirect, flash, session, url_for
import requests
from lowoncost.midleware import auth

local = "http://127.0.0.1:5000/api"
prod = "https://lowoncost.vercel.app/api"
url = local



@app.route("/")
def home():
    return "hi there"

@app.route("/login", methods = ["GET", "POST"])
@auth
def login():
    if request.method == "POST":
        data = request.form
        
        saved = requests.post(f"{url}/login", json = data)
        res =saved.json()
        msg =res["msg"]
        if msg== True :
            session["username"] = data["username"]
            username = session["username"]
            return redirect(f"/home/{username}")
        else:
            #return render_template("signup.html", e = msg)
            flash(msg)
    return render_template("login.html")

@app.route("/signup", methods = ["GET", "POST"])
@auth
def sign():
    if request.method == "POST":
        data = request.form
        #saved = requests.post("http://127.0.0.1:5000/api/signup", json = data)
        saved = requests.post(f"{url}/signup", json = data)
        res =saved.json()
        msg =res["msg"]
        if msg == True:
            return redirect("/login")
        else:
            #return render_template("signup.html", e = msg)
            flash(msg)
    return render_template("signup.html")


@app.route("/home/<username>", methods = ["GET", "POST"])
def dash(username):
    # username = session["username"]
    return render_template("dash.html")


@app.route("/home/addnewdeal", methods = ["GET", "POST"])
def addnewdeal():
    # username = session["username"]
    return render_template("adddeals.html")


@app.route("/home/editprofile", methods = ["GET", "POST"])
def editprofile():
    # username = session["username"]
    return render_template("editprofile.html")

