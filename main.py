from fastapi import FastAPI

from api.cart_api.cart import cart_router
from api.category_api.category import category_router
from api.order_api.order import order_router
from api.photo_api.photos import photo_router
from api.products_api.products import product_router
from api.users_api.users import user_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(photo_router)
app.include_router(category_router)