from api.database.db import collection, db
import bcrypt
from bson.objectid import ObjectId


def addnewdeal(post_data):
    print(post_data)
    # Insert the new deal into the deals collection
    deals_collection = db.deals
    result = deals_collection.insert_one(post_data)
    #return { "deal_id": str(result.inserted_id)}

    # Update the user's deals array
    users_collection = db.users
    user_id = post_data.get("username")
    if user_id:
        users_collection.update_one(
            {"username": user_id},
            {"$push": {"total_deals": result.inserted_id}}
        )
    return {"deal_id": str(result.inserted_id)}

def editdeal(deal_id, post_data):
    # Update the deal in the deals collection
    deals_collection = db.deals
    result = deals_collection.update_one(
        {"_id": deal_id},
        {"$set": post_data}
    )
    return {"modified_count": result.modified_count}


def deletedeal(deal_id):
    # Delete the deal from the deals collection
    
    deals_collection = db.deals
    object_id = ObjectId(deal_id)
    result = deals_collection.delete_one(
        {"_id": object_id}
    )
    #return {"deleted_count": result.deleted_count}
    return {"msg": "deleted"}