from lowoncost.db import db, collection
import json
from bson import json_util


def get_user_data(uname, page=1, page_size=12):
    # Fetch user data
    user = db.users.find_one({"username": uname}, {"password": 0})
    if user == []:
        return []
    
    skip =   (12 * page) - 12
    # Fetch paginated deals
    deals_cursor = db.deals.find(
        {"_id": {"$in": user.get("total_deals", [])}}
    ).sort('_id', -1).skip(skip).limit(page_size)
    
    deals = json.loads(json_util.dumps(deals_cursor))
    # deals = []
    # for item in deals_cursor:
    #     deals.append(item)
    data = []
    userdetails = {
        "username": user.get('username'),
        "description": user.get('description'),
        "total_deals": user.get('total_deals'),
        "item_details": deals
    }
    data.append(userdetails)
    
    return data


def get_cat_data(uname, cate, page=1, page_size=12):
    # Fetch user data
    user = db.users.find_one({"username": uname}, {"password": 0})
    if user == []:
        return []
    total_deals= len(user.get('total_deals'))
    skipval = (12 * page) - 12
    # Fetch paginated deals
    deals_cursor = db.deals.find(
        {"_id": {"$in": user.get("total_deals", [])}, "category": cate}
    ).sort('_id', -1).skip(skipval).limit(page_size)
    deals = deals = json.loads(json_util.dumps(deals_cursor))
    data = []
    userdetails = {
        "username": user.get('username'),
        "description": user.get('description'),
        "total_deals": user.get('total_deals'),
        "item_details": deals
    }
    data.append(userdetails)
    
    return data





def edit_user_data(uname, post_data):
    newname = post_data["username"]
    user = list(collection.find({"username":newname}, {"password": 0}))
    
    for i in user:
        print(i)
    
    if user == []:
        result = collection.find_one_and_update(
            {"username": uname},
            {"$set": post_data}
        )
        return True
    elif newname == uname:
        result = collection.find_one_and_update(
            {"username": uname},
            {"$set": post_data}
        )
        return True
    else:
        return {"msg": "Username already exists chose other name."}
    


def deleteuser(username):
    print(username)