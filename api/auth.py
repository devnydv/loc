from flask import render_template, request
from api import api


# routes related to authentication
@api.route("/api/login", methods = ["GET", "POST"] )
def apilogin():
    if request.method == "GET":
        return {"msg":"this is log in route"}
    if request.method == "POST":
        form = request.form
        return form

@api.route("/api/signup", methods = ["GET", "POST"] )
def apisignup():
    if request.method == "GET":
        return {"msg":"this is log in route"}
    if request.method == "POST":
        form = request.form
        return form
    


@api.route("/api/forgot", methods = ["GET", "POST"] )
def apiforgot():
    if request.method == "GET":
        return {"msg":"this is log in route"}
    if request.method == "POST":
        form = request.form
        return form