from database.models import Cart, Product
from database import get_db
from datetime import datetime


def get_all_carts_db():
    db = next(get_db())
    all_carts = db.query(Cart).all()
    return all_carts


def get_cart_db(id):
    db = next(get_db())
    cart = db.query(Cart).filter_by(id=id).first()
    if cart:
        return cart
    return False


def add_product_to_cart_db(user_id, product_id, amount, price):
    db = next(get_db())

    if user_id and product_id:
        add_product = Cart(user_id=user_id, product_id=product_id,
                           amount=amount, price=price)
        db.add(add_product)
        db.commit()
        return 'Товар успешно добавлен в корзину'
    return 'Такой корзины не существует'


def delete_cart_db(id):
    db = next(get_db())
    cart = db.query(Cart).filter_by(id=id).first()

    if cart:
        db.delete(cart)
        db.commit()
        return 'Корзина успешна удалена'
    return 'Такой корзины не существует'