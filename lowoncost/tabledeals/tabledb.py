from lowoncost.db import db
from bson.objectid import ObjectId


deals_collection = db.tabledata


def addtablerow(data):
    insert =  deals_collection.insert_one(data)
    return insert

def gettabledata():
    deals = list(deals_collection.find().sort('_id', -1).skip(0).limit(50))
    return deals

def tableonedata(id):
    id = ObjectId(id)
    deals = deals_collection.find_one({"_id":id})
    
    return deals

def updatetable(data, id):
    id = ObjectId(id)
    deals_collection.update_one({"_id":id}, {"$set":data})
    return True