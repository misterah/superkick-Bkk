from fastapi import APIRouter, HTTPException
from models.products import Product, Order
from models.users import Customer
from config import products_collection, users_collection, orders_collection
from bson import ObjectId, json_util
import json

router = APIRouter()

@router.get("/")
async def testorder():
    return {"hello":"6666"}

# @router.post("/order/{customer_id}")
# def create_cart(order_data: Order):
#     customer = users_collection().find_one({"user_id": customer_id})
#     if customer:
#         order = orders_collection().insert_one(order_data.dict()).inserted_id
#     return {"sneakers": "Product created successfully", "product_id": str(product_id)}

# @router.post("/cart/{sneakers_id}/{sneakers_size}/{quantity}}")
@router.post("/checkout")
def add_to_cart():
    

    return


# @router.get("/products/{sneakers_id}")
# def get_product(sneakers_id: str):
#     product = products_collection().find_one({"sneakers_id": sneakers_id})
#     if product:
#         product["_id"] = str(product["_id"])  # Convert ObjectId to string
#         return product
#     else:
#         raise HTTPException(status_code=404, detail="Product not found")

# @router.put("/products/{sneakers_id}")
# def update_product(sneakers_id: str, product_data: dict):
#     result = products_collection().update_one({"sneakers_id": sneakers_id}, {"$set": product_data})
#     if result.modified_count == 1:
#         return {"message": "Product updated successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Product not found")
    
# @router.get("/brand/{brand}")
# def get_product_by_brand(brand: str):

#     product = products_collection().find({"sneakers_brand": brand})
#     return {"sneakers": json.loads(json_util.dumps(product))}


# @router.get("/categories/{categories}")
# def get_product_by_categories(categories: str):
#     product = products_collection().find({"sneakers_categories": categories})
#     return {"sneakers": json.loads(json_util.dumps(product))}



# class CartItem(BaseModel):
#     product_id: str
#     quantity: int

# class Cart(BaseModel):
#     user_id: str
#     items: List[CartItem] = []

# @router.post("/cart/add-item/")
# async def add_item_to_cart(user_id: str, item: CartItem):
#     # Add item to cart
#     # You can implement your logic to add item to the cart, for example, by appending it to the items list
#     cart = Cart(user_id=user_id, items=[item])
#     # Return the updated cart
#     return cart

# @router.get("/cart/{user_id}")
# async def view_cart(user_id: str):
#     # Retrieve the cart for the given user_id
#     # You can implement your logic to retrieve the cart from a database or other storage
#     # For this example, we'll return a dummy cart
#     dummy_cart = Cart(user_id=user_id, items=[CartItem(product_id="123", quantity=2)])
#     return dummy_cart

# @router.put("/cart/update-item/")
# async def update_cart_item(user_id: str, item: CartItem):
#     # Update quantity of an item in the cart
#     # You can implement your logic to update the quantity of the item in the cart
#     # For this example, we'll just return the updated item
#     return item

# @router.delete("/cart/remove-item/")
# async def remove_item_from_cart(user_id: str, product_id: str):
#     # Remove item from the cart
#     # You can implement your logic to remove the item from the cart
#     return {"message": f"Item with product_id {product_id} removed from cart"}