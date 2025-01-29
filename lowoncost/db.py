from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv, find_dotenv
import os

envpath = find_dotenv()

load_dotenv(envpath)
url = os.getenv('db')
client = MongoClient(url, socketTimeoutMS= 60000, connectTimeoutMS=60000)
db = client.lowoncost
collection = db.users

# db conn for home route

def get_deals():
    collection = db.deals
    deals = list(collection.find({"status": True}))
    return deals
