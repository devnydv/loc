from lowoncost import app
from flask import render_template, request, redirect, flash, session, url_for
import requests
from lowoncost.midleware import auth

local = "http://127.0.0.1:5000/api"
prod = "https://lowoncost.vercel.app/api"
url = local



@app.route("/")
def home():
    return render_template("index.html")




@app.route("/profile/<username>", methods = ["GET", "POST"])
def dash(username):
    # username = session["username"]
    return render_template("dash.html")


@app.route("/profile/addnewdeal", methods = ["GET", "POST"])
def addnewdeal():
    # username = session["username"]
    return render_template("adddeals.html")


@app.route("/profile/editprofile", methods = ["GET", "POST"])
def editprofile():
    # username = session["username"]
    return render_template("editprofile.html")

