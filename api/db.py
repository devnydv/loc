from pymongo.mongo_client import MongoClient
import bcrypt


url= "mongodb+srv://bittumail:12356789@cluster0.fqrswkj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(url)
db = client.lowoncost
collection = db.users


# insert data to db when new user signp
def newuser(data):
    data.popitem()
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
    password = logdata["password"]
    user = list(collection.find({"username": uname}))
    if user == []:
        return {"msg":"User name not found", "case":False}
    else: 
        if bcrypt.checkpw(password.encode("utf-16"), user[0]['password']):
            return {"msg":"You are logged in", "case":True}
        else:
            return {"msg":"Password did not match", "case":False}
    