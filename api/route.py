from flask import render_template, request, session
from api import api
from api.database.db import get_user_data



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
    

    


