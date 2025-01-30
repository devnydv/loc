from lowoncost import app
from lowoncost.db import get_deals
from flask import render_template, request, redirect, flash, session, url_for

import requests


def session_user():
    if "username" in session:
        
        return True
    else:
        return False
    

@app.route("/")
def home():
    loggedin = session_user()
    if loggedin:
        username = session['username']
    else:
        username = None
    
    items = get_deals(cat = "all")
    return render_template("index.html", loggedin = loggedin, userprofile = False, username= username, items = items)





@app.route("/<cat>")
def home_category(cat):
    loggedin = session_user()
    if loggedin:
        username = session['username']
    else:
        username = None
    items = get_deals(cat)
    return render_template("index.html", loggedin = loggedin, userprofile = False, username= username, items = items)

@app.route("/homepage/<pagenum>/<cat>")
def home_paginate(pagenum, cat):
    pagenum = int(pagenum)
    items = get_deals(cat, page=pagenum )
    if items == []:
        return "0"
    else:
        return render_template("page.html", navshow = {'userprofile' : True, "items": items})



# Custom error pages
@app.route('/error_404')
def error_404():
    return render_template("error.html") , 404