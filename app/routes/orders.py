from fastapi import APIRouter, HTTPException
from models.products import Product, Transaction, ShippingAddress
from models.users import Customer
from models.orders import *
from config import (db,products_collection,
                    users_collection, 
                    orders_collection, 
                    counter_collection,
                    shipping_collection)
from bson import ObjectId, json_util
import json

router = APIRouter()


# Check if the counter collection exists and initialize it if necessary
if "order_counter" not in db.list_collection_names():
    counter_collection().insert_one({"_id": "order_id", "value": 0})


@router.get("/")
async def testorder():
    return {"hello":"6666"}



@router.post("/checkout")
def create_transaction(order_data: OrderData):

    # ดึง username
    username_order = users_collection().find_one({"username":order_data.username})

    # map order_data กับ ShippingAddress
    shipping_ad = ShippingAddress(username=username_order["username"],
                                    name=order_data.shipping_info.name,
                                    email=username_order["email"],
                                    postcode=order_data.shipping_info.postcode,
                                    tel=order_data.shipping_info.tel,
                                    address=order_data.shipping_info.address)
    
    # add to database
    add_shipping = shipping_collection().insert_one(shipping_ad.dict()).inserted_id

    total_price = 0

    all_products_order = [ ]

    # loop products_order in order_data 
    # for calculate price and make list for field in Transaction
    # and use Transaction model to add data in orders_collection
    for products_order in order_data.products_order:
        product = products_collection().find_one({"sneakers_id": products_order.sneakers_id})
        if product:
            total_price += product["sneakers_price"] * products_order.quantity
            all_products_order.append({
                "name": product["sneakers_name"],
                "brand": product["sneakers_brand"],
                "size": products_order.size,
                "quantity": products_order.quantity
            })
        else:
            raise HTTPException(status_code=404, detail=f"Product with ID {products_order.sneakers_id} not found")
        
    #count order come in amount
    counter_collection().find_one_and_update(
        {"_id": "order_id"},
        {"$inc": {"value": 1}}
    )
     
    # get the current value of the counter (the new order_id)
    order_id = counter_collection().find_one({"_id": "order_id"})["value"]
    order_id = str(order_id)

    shipping_complete = False

    # map กับ Transaction model
    transaction = Transaction(order_id=order_id,
                              products=all_products_order,
                              total_price=total_price,
                              detail=shipping_ad,
                              complete=shipping_complete)
    
    # add to database
    orders_collection().insert_one(transaction.dict()).inserted_id
    
    # Return a response
    return {"order": "Order created successfully", "order_detail": transaction}


@router.get("/all_orders")
def admin_get_orders():
    all_orders = orders_collection().find()
    return {"all_orders": json.loads(json_util.dumps(all_orders))}


@router.post("/add_order")
def admin_add_order(order_data : Transaction):
    
    counter_collection().find_one_and_update(
        {"_id": "order_id"},
        {"$inc": {"value": 1}}
    )
    order = orders_collection().insert_one(order_data.dict()).inserted_id
    return {"order": "Order created successfully", "order_id": str(order)}
