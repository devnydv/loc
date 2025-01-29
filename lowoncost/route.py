from lowoncost import app
from lowoncost.db import get_deals
from flask import render_template, request, redirect, flash, session, url_for
import requests
import json

def session_user():
    if "username" in session:
        
        return True
    else:
        return False
    

@app.route("/")
def home():
    loggedin = session_user()
    username = session['username']
    items = get_deals()
    return render_template("index.html", loggedin = loggedin, userprofile = False, username= username, items = items)





@app.route("/<cat>")
def home_category(cat):
    loggedin = session_user()
    if loggedin:
        username = session['username']
    else:
        username = None
    return render_template("index.html", loggedin = loggedin, userprofile = False, username= username)


# Custom error pages
@app.route('/error_404')
def error_404():
    return render_template("error.html") , 404