from lowoncost.db import db, collection
import json
from bson import json_util

def get_user_data(uname):
    user = list(collection.find({"username": uname}, {"password": 0}))

    if user == []:
        return []
    else: 
        data = json.loads(json_util.dumps(user))
        
        pipeline = [
        {
        "$match": { "username": uname }  # Match the specific user
        },
        {
        "$lookup": {
            "from": "deals",         # Items collection name
            "localField": "total_deals",  # Field in users collection
            "foreignField": "_id",      # Field in items collection
            "as": "item_details"        # Output array field
        }
        }
        ]

        result = db.users.aggregate(pipeline)
        deals = json.loads(json_util.dumps(result))
        return json.dumps({"data": deals})
    
def edit_user_data(uname, post_data):
    user = collection.find({"username": uname}, {"password": 0})
    if user == []:
        result = collection.update_one(
            {"username": uname},
            {"$set": post_data}
        )
    
        return True
    else:
        return {"msg": "Username already exists."}