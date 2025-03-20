from lowoncost import app
from flask import render_template, request, redirect, session, url_for


@app.route("/flashdeals", methods = ["GET", "POST"])
def flash():
    return "flashdeals"