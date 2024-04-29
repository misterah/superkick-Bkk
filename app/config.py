from pymongo import MongoClient
import os
import secrets
# Generate a random 32-byte key
SECRET_KEY = secrets.token_hex(32)

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL, connect=False)
db = client['dev_superkick']


def db_call():
    return db

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

def counter_collection():
    return db["order_counter"]


if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application. Please set SECRET_KEY in your .env file.")




