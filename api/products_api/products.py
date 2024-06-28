from fastapi import APIRouter
from database.productservice import *

product_router = APIRouter(prefix='/product', tags=['Product'])

@product_router.get('/api/products')
async def all_products():
    data = get_all_product()
    return data

@product_router.get('/api/exact_product')
async def exact_product(name: str):
    data = get_exact_product(name)
    return data

@product_router.post('/api/add_product')
async def add_product_db(name: str, description: str, price: float, quantity: int):
    data = add_product(name=name, description=description, price=price, quantity=quantity)
    return data

@product_router.put('/api/change_product')
async def change_product(id: int, change_info, new_info):
    data = change_data_product(id=id, change_info=change_info, new_info=new_info)
    return data

@product_router.delete('/api/delete')
async def delete_product_db(product_id: int):
    data = delete_product(product_id)
    return data