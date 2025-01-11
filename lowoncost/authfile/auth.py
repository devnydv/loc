from lowoncost import app
from flask import render_template, request, redirect, flash, session, url_for, flash
from lowoncost.midleware import auth
from lowoncost.authfile.validate import LoginForm, SignupForm
from lowoncost.authfile.authdb import newuser, checkusername, userlogin
import json

@app.route("/login", methods = ["GET", "POST"])
@auth
def login():
    form = LoginForm(request.form)
    
    if request.method == "POST":
        username = request.form.get("username").lower()
        data = request.form
        data = json.dumps(data)
        check = userlogin(data)
        if form.validate() and check["case"]:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            flash(check["msg"])
            
    return render_template("login.html", form = form)



@app.route("/signup", methods = ["GET", "POST"])
@auth
def sign():
    form = SignupForm(request.form)
    
    
    if request.method == "POST":
        username = request.form.get("username").lower()
        if form.validate() and checkusername(username)["case"]:
            data= request.form
            data = json.dumps(data)
            newuser(data)
            return redirect(url_for("login"))
        else:
            flash("Username is already taken")
    return render_template("signup.html", form = form)



@app.route("/logout", methods = ["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for('home'))