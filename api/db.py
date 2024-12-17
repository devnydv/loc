from pymongo.mongo_client import MongoClient
import bcrypt
from bson import json_util
import json
from dotenv import load_dotenv, find_dotenv
import os
envpath = find_dotenv()
load_dotenv(envpath)

url = os.getenv('db')


client = MongoClient(url, socketTimeoutMS=30000, connectTimeoutMS=30000)
db = client.lowoncost
collection = db.users


# insert data to db when new user signp
def newuser(data):
    username = data["username"]
    data["username"] = username.lower()
    
    data["description"]="Sharing the best deals and offers on best prices."
    data["cart_items"] = []
    data["total_deals"] = []
    
    
    data.pop("confirm_password")
    password =data["password"]
    encodepass = bcrypt.hashpw(password.encode("utf-16"), bcrypt.gensalt())
    data["password"] = encodepass
    #print(userdata)
    collection.insert_one(data)
    


def checkusername(uname):
    user = list(collection.find({"username": uname}))
    if user == []:
        return {"massage":"username is Unique", "case":True}
    else: 
        return {"massage":"username is already taken", "case":False}
    

def login(logdata):
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

def get_user_data(uname):
    user = list(collection.find({"username": uname}))
    
    if user == []:
        return []
    else: 
        data = json.loads(json_util.dumps(user))
        return json.dumps(data)
    

