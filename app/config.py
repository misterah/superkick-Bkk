from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging

LOGGER = logging.getLogger(__name__)
MONGO_URL = os.getenv("MONGO_URL")
CLIENT = AsyncIOMotorClient(MONGO_URL)
DB_NAME = "dev_superkick"
DB = CLIENT.get_database(DB_NAME)

def product_collection():
    return DB.get_collection("products")




