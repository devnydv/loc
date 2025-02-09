from lowoncost import app
from flask import render_template, request, redirect, session, url_for

@app.route("/admin/dashboard", methods = ["GET", "POST"])
def admindash():
    return render_template("admindash.html")