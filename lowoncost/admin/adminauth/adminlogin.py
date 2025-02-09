from lowoncost import app
from flask import render_template, request, redirect, session, url_for, flash
from lowoncost.admin.adminauth.validate import LoginForm
from lowoncost.admin.adminauth.adminauthdb import adminid


@app.route("/admin/login", methods = ["GET", "POST"])
def adminlogin():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")
        admindata = adminid(username)
        if admindata[0]['username'] == username and admindata[0]['password'] == password:
            session["admin"] = username
            return redirect(url_for('admindash'))
        else:
            flash("Kuch na Kuch to Gadbad hai...")
    return render_template("adminlogin.html", form = form)