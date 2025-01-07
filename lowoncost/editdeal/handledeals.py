from lowoncost import app
from flask import render_template, request, redirect, flash, session, url_for
import requests
from lowoncost.midleware import auth
import json

from lowoncost.url import apiurl

url = apiurl()


@app.route("/profile/addnewdeal", methods = ["GET", "POST"])
def addnewdeal():
    if request.method == "GET":
        if "username" in session:
            username = session["username"]
            return render_template("adddeal.html", name= username)
        else:
            return redirect(url_for('login'))
    if request.method == "POST":
        data = request.form
        if "username" in session:
            username = session["username"]
            saved = requests.post(f"{url}/newdeal/{username}", json = data)
            res =saved.json()
            
            return redirect(url_for('dash', username=username))
        else:
            return redirect(url_for('login'))