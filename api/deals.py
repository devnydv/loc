from flask import request
from api import api
from api.database.dealsdb import addnewdeal, editdeal, deletedeal
from api.validate.dealvalidate import adddeal



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

@api.route("/api/deletedeal/<id>", methods = ["GET", "POST"])
def removedeal(id):
    if request.method == "GET":
        result = deletedeal(id)
        return {"msg":"okk"}
    
    