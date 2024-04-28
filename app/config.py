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

def users_collection():
    return db["users"]

def orders_collection():
    return db["orders"]

def shipping_collection():
    return db["shipping"]

def order_items_collection():
    return db["order_items"]

# products_collection = 
# orders_collection = db["orders"]
# shipping_collection = db["shipping"]
# users_collection = db["users"]



