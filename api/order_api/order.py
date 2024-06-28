from fastapi import APIRouter
from pydantic import BaseModel
from database.orderservice import *
from database import get_db

order_router = APIRouter(prefix='/order', tags=['Order'])


@order_router.get('/all-orders')
async def get_all_orders():
    all_orders = get_all_orders_db()
    return all_orders


@order_router.get('api/get-order')
async def get_order(id: int):
    order = get_order_db(id=id)
    return order


@order_router.post('api/create-order')
async def create_order(user_id: int, cart_id: int):
    order_create = create_order_db(user_id=user_id, cart_id=cart_id)
    return order_create


@order_router.delete('api/delete-order')
async def delete_order(id: int):
    order_delete = delete_order_db(id=id)
    return order_delete