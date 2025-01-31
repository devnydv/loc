from lowoncost import app
from flask import render_template, request, redirect, flash, session, url_for, flash
from lowoncost.midleware import auth
from lowoncost.authfile.validate import LoginForm, SignupForm, is_valid_email
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
            return redirect(url_for("dash", name = username))
        else:
            flash(check["msg"])
            
    return render_template("login.html", form = form)



@app.route("/signup", methods = ["GET", "POST"])
@auth
def sign():
    form = SignupForm(request.form)
    
    
    if request.method == "POST":
        username = request.form.get("username").lower()
        uniquename = checkusername(username)["case"]
        email = request.form.get("email")
        emailcheck = is_valid_email(email)
        print(emailcheck)
        if form.validate() and uniquename and emailcheck:
            data= request.form
            data = json.dumps(data)
            newuser(data)
            return redirect(url_for("login"))
        elif uniquename == False:
            flash("Username already exists chose another name")
        elif emailcheck == False:
            flash("Please provide a valid email")
        else:
            flash("Opps...")
    return render_template("signup.html", form = form)



@app.route("/logout", methods = ["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for('home'))