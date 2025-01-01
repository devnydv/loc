from flask import render_template, request, flash, session
from api import api
from api.valid import SignupForm, LoginForm
from api.db import newuser, checkusername, login




# routes related to authentication


@api.route("/api/signup", methods = ["GET", "POST"] )
def apisignup():
    if request.method == "GET":
        return {"msg":"this is signup"}
    if request.method == "POST":
        data = request.get_json()
        username = data["username"]
        chkuser = checkusername(username.lower())
        
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
                    
                    return {"msg": error}



@api.route("/api/login", methods = ["GET", "POST"] )
def apilogin():
    if request.method == "GET":
        return {"msg":"this is login route"}
    if request.method == "POST":
        data = request.get_json()
        lowername = data["username"]
        data["username"] = lowername.lower()
        
        form = LoginForm(data= data)
        if form.validate():
            check = login(data)
            
            if check["case"]:
                
                return {"user":check["user"]["username"] ,"msg":True}
            else:
                return {"msg":check["msg"] }
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    #flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
                    return {"msg": error}
       
        


    


@api.route("/api/forgot", methods = ["GET", "POST"] )
def apiforgot():
    if request.method == "GET":
        return {"msg":"this is log in route"}
    if request.method == "POST":
        form = request.form
        return form
    


