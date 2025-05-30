from lowoncost import app
from lowoncost.db import get_deals, home_deals
from flask import render_template, request, flash, session, send_from_directory, Response
from flask_caching import Cache
import requests


def session_user():
    if "username" in session:
        return True
    else:
        return False
    
#old working code with index.html
# @app.route("/")
# def home():
#     loggedin = session_user()
#     if loggedin:
#         username = session['username']
#     else:
#         username = None
    
#     items = get_deals(cat = "all")
#     return render_template("index.html", loggedin = loggedin, userprofile = False, username= username, items = items)
#old code ends heere 


app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFOULT_TIMEOUT"] = 600 * 6
cache =Cache(app)

#new code for home page with 3 items from each category
@app.route("/")
@cache.cached()
def home():
    loggedin = session_user()
    if loggedin:
        username = session['username']
    else:
        username = None
    items = home_deals()
    
    #return return render_template("index.html", loggedin = loggedin, userprofile = False, username= username, items = items)("index.html", loggedin = loggedin, userprofile = False, username= username, items = items)
    return render_template("home.html", datas= items, loggedin = loggedin, userprofile = False, username= username)


@app.route("/<cat>")
def home_category(cat):
    loggedin = session_user()
    if loggedin:
        username = session['username']
    else:
        username = None
    items = get_deals(cat)
    return render_template("index.html", loggedin = loggedin, userprofile = False, username= username, items = items, cat = cat)

@app.route("/homepage/<pagenum>/<cat>")
def home_paginate(pagenum, cat):
    pagenum = int(pagenum)
    items = get_deals(cat, page=pagenum )
    if items == []:
        return "0"
    else:
        return render_template("page.html", navshow = {'userprofile' : False, "items": items})


@app.route('/manifest.xml')
def manifest():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
    <manifest>
        <name>LowonCost</name>
        <short_name>LowonCost</short_name>
        <description>Find the lowest prices on the product you love with Lowoncost.</description>
        <version>1.0</version>
        <start_url>/</start_url>
        <display>standalone</display>
        <theme_color>#ffffff</theme_color>
        <background_color>#000000</background_color>
    </manifest>
    """
    return Response(xml_content, mimetype='application/xml')

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

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.root_path, 'sitemap.xml')

# Custom error pages
@app.route('/error_404')
def error_404():
    return render_template("error.html") , 404

# redirects to error page when user visits any unwanted Urls
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404