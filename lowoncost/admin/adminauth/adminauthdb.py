from lowoncost.db import db
collection = db.admin

def adminid(uname):
    admin = list(collection.find({"username": uname}))
    return admin