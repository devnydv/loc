from pymongo.mongo_client import MongoClient
import bcrypt
from bson import json_util
import json
from dotenv import load_dotenv, find_dotenv
import os

envpath = find_dotenv()
load_dotenv(envpath)
url = os.getenv('db')
client = MongoClient(url, socketTimeoutMS= 60000, connectTimeoutMS=60000)
db = client.lowoncost
collection = db.users



    


#get user data from db and his dealsS
def get_user_data(uname):
    user = list(collection.find({"username": uname}))

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
        return json.dumps({"data": deals, "deals": deals})
        

   