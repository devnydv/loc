from flask import render_template, request, flash
from api import api
from api.valid import SignupForm
from api.db import newuser, checkusername



# routes related to authentication


@api.route("/api/signup", methods = ["GET", "POST"] )
def apisignup():
    if request.method == "GET":
        return {"msg":"this is signup"}
    if request.method == "POST":
        data = request.get_json()
        chkuser = checkusername(data["username"])
        print(chkuser)
        form = SignupForm(data= data)
        if form.validate() and chkuser["case"]:
            newuser(data)
            return {"msg": True}
        elif not chkuser["case"]:
            return {"msg": "Username already taken"}
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    #flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
                    #print(error)
                    return {"msg": error}



@api.route("/api/login", methods = ["GET", "POST"] )
def apilogin():
    if request.method == "GET":
        
        return {"msg":"this is login route"}
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
    


