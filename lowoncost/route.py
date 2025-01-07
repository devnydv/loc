from lowoncost import app
from flask import render_template, request, redirect, flash, session, url_for
import requests
from lowoncost.midleware import auth
import json
from lowoncost.url import apiurl

url = apiurl()


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
    #data = {"username": username }
    saved = requests.post(f"{url}/user/{username}")
    res =saved.json()
    
    #res = res['data']
    if "userdata" in res:
        userdata = res["userdata"]
        
        userdata = json.loads(userdata)
        deals = userdata
        userdata = userdata['data']
        
        if "username" in session:
            session_name = session["username"]
            session['data'] = userdata
            if session_name == username:
                return render_template("dash.html", loggedin = loggedin, edit= True, userdata = userdata, deals= deals )
            else:
                return render_template("dash.html", loggedin = True, userdata = userdata, otherprofile =True, edit= False)
        else:
            return render_template("dash.html", loggedin = False, userdata = userdata, edit= False)
    else:
        return redirect(url_for('error_404'))


@app.route("/profile/editprofile", methods = ["GET", "POST"])
def editprofile():
    if "username" in session:
        username = session["username"]
        return render_template("editprofile.html", name= username)
    else:
        return redirect(url_for('error_404'))








# Custom error pages
@app.route('/error_404')
def error_404():
    return render_template("error.html") , 404
    