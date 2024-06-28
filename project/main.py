from fastapi import FastAPI, HTTPException, Path, Query, Body
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Примеры данных для демонстрации
fake_items_db = [
    {"item_id": 1, "name": "Item 1", "description": "Description 1", "price": 99.9},
    {"item_id": 2, "name": "Item 2", "description": "Description 2", "price": 149.5},
    {"item_id": 3, "name": "Item 3", "description": "Description 3", "price": 199.0},
]

fake_users_db = [
    {"username": "user1", "full_name": "User One"},
    {"username": "user2", "full_name": "User Two"},
]

fake_orders_db = [
    {"order_id": 1, "items": [1, 2], "total_amount": 249.4, "username": "user1"},
    {"order_id": 2, "items": [3], "total_amount": 199.0, "username": "user2"},
]

fake_cart_db = {}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


class Order(BaseModel):
    order_id: int
    items: List[int]
    total_amount: float
    username: str


# GET методы
@app.get("/")
def read_root():
    return {"message": "Welcome to the online store API"}


@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int = Path(..., description="The ID of the item to retrieve")):
    for item in fake_items_db:
        if item["item_id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10):
    return fake_users_db[skip: skip + limit]


@app.get("/users/{username}", response_model=User)
def read_user(username: str = Path(..., description="The username of the user to retrieve")):
    for user in fake_users_db:
        if user["username"] == username:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/orders/", response_model=List[Order])
def read_orders(skip: int = 0, limit: int = 10):
    return fake_orders_db[skip: skip + limit]


@app.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int = Path(..., description="The ID of the order to retrieve")):
    for order in fake_orders_db:
        if order["order_id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


@app.get("/cart/", response_model=dict)
def read_cart():
    return fake_cart_db


@app.get("/orders/history/{username}", response_model=List[Order])
def read_user_order_history(username: str = Path(..., description="The username of the user to retrieve orders for")):
    user_orders = [order for order in fake_orders_db if order["username"] == username]
    if not user_orders:
        raise HTTPException(status_code=404, detail=f"No orders found for username {username}")
    return user_orders


@app.get("/items/search", response_model=List[Item])
def search_items(query: str = Query(..., description="Query string for searching items")):
    results = []
    for item in fake_items_db:
        if query.lower() in item["name"].lower() or (item["description"] and query.lower() in item["description"].lower()):
            results.append(item)
    return results


# POST методы
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    new_item_id = len(fake_items_db) + 1
    new_item = {"item_id": new_item_id, "name": item.name, "description": item.description, "price": item.price}
    fake_items_db.append(new_item)
    return new_item


@app.post("/users/", response_model=User)
def create_user(user: User):
    fake_users_db.append(user.dict())
    return user


@app.post("/orders/create", response_model=Order)
def create_order(order_items: List[int] = Body(...), username: str = Body(...)):
    total_amount = sum(fake_items_db[item_id - 1]["price"] for item_id in order_items)
    new_order_id = len(fake_orders_db) + 1
    new_order = {"order_id": new_order_id, "items": order_items, "total_amount": total_amount, "username": username}
    fake_orders_db.append(new_order)
    return new_order


@app.post("/cart/add_item", response_model=dict)
def add_item_to_cart(item_id: int, quantity: int = 1):
    if item_id not in fake_cart_db:
        fake_cart_db[item_id] = 0
    fake_cart_db[item_id] += quantity
    return {"message": f"Added {quantity} item(s) to cart for item_id {item_id}"}


# PUT методы
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for i, existing_item in enumerate(fake_items_db):
        if existing_item["item_id"] == item_id:
            fake_items_db[i] = {"item_id": item_id, "name": item.name, "description": item.description, "price": item.price}
            return fake_items_db[i]
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/users/{username}", response_model=User)
def update_user(username: str, user: User):
    for i, existing_user in enumerate(fake_users_db):
        if existing_user["username"] == username:
            fake_users_db[i] = user.dict()
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/cart/update_item/{item_id}", response_model=dict)
def update_cart_item(item_id: int, quantity: int):
    if item_id in fake_cart_db:
        fake_cart_db[item_id] = quantity
        return {"message": f"Updated quantity of item_id {item_id} in cart to {quantity}"}
    raise HTTPException(status_code=404, detail=f"Item_id {item_id} not found in cart")


# DELETE методы
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for i, item in enumerate(fake_items_db):
        if item["item_id"] == item_id:
            deleted_item = fake_items_db.pop(i)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/users/{username}", response_model=User)
def delete_user(username: str):
    for i, user in enumerate(fake_users_db):
        if user["username"] == username:
            deleted_user = fake_users_db.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/orders/cancel/{order_id}", response_model=Order)
def cancel_order(order_id: int):
    for i, order in enumerate(fake_orders_db):
        if order["order_id"] == order_id:
            deleted_order = fake_orders_db.pop(i)
            return deleted_order
    raise HTTPException(status_code=404, detail="Order not found")


# Дополнительные методы

@app.get("/users/count", response_model=dict)
def count_users():
    return {"total_users": len(fake_users_db)}

@app.get("/items/count", response_model=dict)
def count_items():
    return {"total_items": len(fake_items_db)}

@app.get("/orders/count", response_model=dict)
def count_orders():
    return {"total_orders": len(fake_orders_db)}

@app.get("/cart/total", response_model=dict)
def cart_total():
    total_quantity = sum(quantity for quantity in fake_cart_db.values())
    return {"total_items_in_cart": total_quantity}

@app.get("/orders/average_amount", response_model=dict)
def average_order_amount():
    if len(fake_orders_db) > 0:
        total_amount = sum(order["total_amount"] for order in fake_orders_db)
        average_amount = total_amount / len(fake_orders_db)
        return {"average_order_amount": average_amount}
    else:
        return {"average_order_amount": 0.0}
