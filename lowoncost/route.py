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
    data = {"username": username }
    saved = requests.post(f"{url}/user", json = data)
    res =saved.json()
    if "userdata" in res:
        print(res["userdata"])
        if "username" in session:
            session_name = session["username"]
            if session_name == username:
                return render_template("dash.html", loggedin = loggedin, edit= True, userdata = res["userdata"] )
            else:
                return render_template("dash.html", loggedin = True, otherprofile =True, edit= False)
        else:
            return render_template("dash.html", loggedin = False, edit= False)
    else:
        return redirect(url_for('error_404'))

@app.route("/profile/addnewdeal", methods = ["GET", "POST"])
def addnewdeal():
    if request.method == "GET":
        if "username" in session:
            username = session["username"]
            return render_template("adddeals.html", name= username)
        else:
            return redirect(url_for('error_404'))
    if request.method == "POST":
        if "username" in session:
            return "yes"
    

    


@app.route("/profile/editprofile", methods = ["GET", "POST"])
def editprofile():
    if "username" in session:
        username = session["username"]
        return render_template("editprofile.html", name= username)
    else:
        return redirect(url_for('error_404'))

@app.route("/logout", methods = ["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for('home'))









# Custom error pages
@app.route('/error_404')
def error_404():
    return render_template("error.html") , 404
    