from pymongo import MongoClient
import os


MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL, connect=False)
# CLIENT = AsyncIOMotorClient(MONGO_URL)
# DB_NAME = "dev_superkick"
# DB = CLIENT.get_database(DB_NAME)
db = client['dev_superkick']



# def product_collection():
#     return DB.get_collection("products")

def products_collection():
    return db["products"]


# products_collection = 
# orders_collection = db["orders"]
# shipping_collection = db["shipping"]
# users_collection = db["users"]



