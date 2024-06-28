from fastapi import APIRouter
from database.categoryservice import *

category_router = APIRouter(prefix='/category', tags=['Category'])

@category_router.post('/api/add_category')
async def add_category_db(category_name: str):
    data = add_category(category_name=category_name)
    return data

@category_router.get('/api/all_categories')
async def get_all_categories_db():
    data = get_all_categories()
    return data

@category_router.get('/api/exact_category')
async def get_exact_category_db(id: int):
    data = get_exact_category(id=id)
    return data

@category_router.delete('/api/delete_category')
async def delete_category_db(id: int):
    data = delete_category(id=id)
    return data