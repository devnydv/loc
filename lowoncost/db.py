from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
from bson import json_util
import json
envpath = find_dotenv()

load_dotenv(envpath)
url = os.getenv('db')
client = MongoClient(url, socketTimeoutMS= 60000, connectTimeoutMS=60000)
db = client.lowoncost
collection = db.users

# db conn for home route

def get_deals(cat, page=1, page_size=12):
    skip =   (12 * page) - 12
    collection = db.deals
    if cat == "all":
        #deals = list(collection.find({"status": "varified"}).skip(skip).limit(page_size))
        deals = list(collection.find().sort('_id', -1).skip(skip).limit(page_size))
    else: 
        #deals = list(collection.find({"status": "varified", "category": cat}).skip(skip).limit(page_size))
        deals = list(collection.find({"category": cat}).sort('_id', -1).skip(skip).limit(page_size))
    deals = json.loads(json_util.dumps(deals))
    return deals
