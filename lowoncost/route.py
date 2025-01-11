from lowoncost import app
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
    return render_template("index.html", loggedin = loggedin, userprofile = False)


# Custom error pages
@app.route('/error_404')
def error_404():
    return render_template("error.html") , 404