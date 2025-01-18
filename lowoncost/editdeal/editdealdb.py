from lowoncost.db import db, collection
from bson.objectid import ObjectId

def addnewdeal(data):
    
    
    # Insert the new deal into the deals collection
    deals_collection = db.deals
    result = deals_collection.insert_one(data)
    #return { "deal_id": str(result.inserted_id)}

    # Update the user's deals array
    users_collection = db.users
    user_id = data.get("username")
    if user_id:
        users_collection.update_one(
            {"username": user_id},
            {"$push": {"total_deals": result.inserted_id}}
        )
    return {"deal_id": str(result.inserted_id)}

def editdealdata(deal_id, post_data):
    # Update the deal in the deals collection
    
    deals_collection = db.deals
    deal_id = ObjectId(deal_id)
    print(deal_id)
    result = deals_collection.find_one_and_update(
        {"_id": deal_id},
        {"$set": post_data}
    )
    #return {"modified_count": result.modified_count}
    return {"msg": "updated"}


def deletedeal(deal_id, username):
    # Delete the deal from the deals collection
    deals_collection = db.deals
    object_id = ObjectId(deal_id)
    result = deals_collection.delete_one(
        {"_id": object_id}
    )

    collection = db["users"]
    filter_query = {"username": username}  # Identify the document
    update_query = {"$pull": {"total_deals": object_id}}  # Remove "banana" from the items array

# Update the document
    userresult = collection.update_one(filter_query, update_query)
    return {"deleted_count": result.deleted_count}
    

def getaitem(id):
    deals_collection = db.deals
    id = ObjectId(id)
    data = deals_collection.find_one({"_id":id})
    

    return data