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
        


@app.route('/profile/editdeal/<id>')
def editnewdeal(id):
    data =session["data"]
    items = data[0]['item_details']
    for item in items:
        if item['_id']['$oid'] == id:
            mainitem = item
    
    return render_template("editdeal.html", item = mainitem, id= id)


@app.route('/profile/delete/<id>')
def deletedeal(id):
    print(id)
    saved = requests.get(f"{url}/deletedeal/{id}")
    res = saved.json()
    username = session["username"]
    return redirect(url_for('dash', username=username))


