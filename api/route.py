from flask import render_template, request, session
from api import api
from api.database.db import get_user_data, addnewdeal
from api.valid import adddeal

# other user routes

@api.route("/api")
def apihome():
    return {"msg":"this is home page for the api. Do not missuse this end point."}

@api.route("/api/user/<username>", methods = ["GET", "POST"])
def getuser(username):
    
    if request.method == "POST":
        #data = request.get_json()
        #username = data["username"]
        data = get_user_data(username)
        
        if data == []:
            return {"msg":"User Not Found", "case": False}
        else: 
            return {"userdata": data, "case":True}
    else:
        return {"msg":"not found"}
    

    

@api.route("/api/newdeal/<username>", methods = ["GET", "POST"])
def newdeal(username):
    if request.method == "POST":
        data = request.get_json()
        correntprice = int(data["currentPrice"])
        originalprice = int(data["originalPrice"])
        data["status"] = False
        data["username"] = username
        data["currentPrice"] = correntprice
        data["originalPrice"] = originalprice
        print(data)
        form = adddeal(data= data)
        if form.validate():
            res = addnewdeal(data)
            return {"msg": True, "res": res}
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    return {"msg": error}  
        return {"msg": "validating the form"}
    else:
        return {'msg': "created a new deal"}
        #return {"msg":"not found"}
