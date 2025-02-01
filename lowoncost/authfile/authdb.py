from lowoncost.db import collection
import bcrypt
import json
from bson.objectid import ObjectId


# insert data to db when new user signp
def newuser(data):
    data = json.loads(data)
    print(data)
    username = data["username"]
    data["username"] = username.lower()
    
    data["description"]="Sharing the best deals and offers on best prices."
    data["cart_items"] = []
    data["total_deals"] = [ObjectId("6782ace8c6ff466c0e3b44d1")]
    
    data.pop("confirm_password")
    password =data["password"]
    encodepass = bcrypt.hashpw(password.encode("utf-16"), bcrypt.gensalt())
    data["password"] = encodepass
    #print(userdata)
    collection.insert_one(data)


def checkusername(uname):
    user = list(collection.find({"username": uname}, {"_id":0,  'username':1}))
    if user == []:
        return {"massage":"username is Unique", "case":True}
    else: 
        return {"massage":"username is already taken", "case":False}
    
    
def userlogin(logdata):
    logdata = json.loads(logdata)
    uname = logdata["username"]
    uname = uname.lower()
    password = logdata["password"]
    user = list(collection.find({"username": uname}))
    
    if user == []:
        return {"msg":"User name not found", "case":False}
    else: 
        if bcrypt.checkpw(password.encode("utf-16"), user[0]['password']):
            
            return {"msg":"You are logged in", "case":True, "user": user[0]}
        else:
            return {"msg":"Password did not match", "case":False}