from lowoncost import app
from lowoncost.db import get_deals
from flask import render_template, request, flash, session, send_from_directory

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
        return render_template("page.html", navshow = {'userprofile' : False, "items": items})




@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/privacy')
def privacy():
    return render_template("privacy.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/how-it-works')
def how():
    return render_template("how.html")

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')

# Custom error pages
@app.route('/error_404')
def error_404():
    return render_template("error.html") , 404

# redirects to error page when user visits any unwanted Urls
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404