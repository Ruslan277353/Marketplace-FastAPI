from database.models import Order, Cart, Product
from database import get_db
from datetime import datetime

def create_order(user_id, total=None):
    db = next(get_db())
    item_in_cart = db.query(Cart).filter_by(user_id=user_id).all()
    if not item_in_cart:
        return False
    if total is None:
        total = 0
        for item in item_in_cart:
            product = db.query(Product).filter_by(id=item.product_id).first()
            if not product:
                return False
            total += product.price * item.quantity
    if user_id:
        new = Order(user_id=user_id, total=total, reg_date=datetime.now())
        db.add(new)
        db.commit()
        return f'Общая сумма заказа: {new.total}\nКлиент: {new.user_id}'
    return False