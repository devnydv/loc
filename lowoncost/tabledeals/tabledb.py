from lowoncost.db import db

deals_collection = db.tabledata


def addtablerow(data):
    insert =  deals_collection.insert_one(data)
    return insert

def gettabledata():
    deals = list(deals_collection.find().sort('_id', -1).skip(0).limit(50))
    return deals