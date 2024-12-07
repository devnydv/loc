from lowoncost import app
from flask import render_template, request, redirect, flash, session, url_for
import requests
from lowoncost.midleware import auth

local = "http://127.0.0.1:5000/api"
prod = "https://lowoncost.vercel.app/api"
url = local


def session_user():
    if "username" in session:
        return True
    else:
        return False


@app.route("/")
def home():
    
    loggedin = session_user()
    return render_template("index.html", loggedin = loggedin)




@app.route("/profile/<username>", methods = ["GET", "POST"])
def dash(username):
    loggedin = session_user()
    # username = session["username"]
    return render_template("dash.html", loggedin = loggedin)


@app.route("/profile/addnewdeal", methods = ["GET", "POST"])
def addnewdeal():
    # username = session["username"]
    return render_template("adddeals.html")


@app.route("/profile/editprofile", methods = ["GET", "POST"])
def editprofile():
    # username = session["username"]
    return render_template("editprofile.html")

