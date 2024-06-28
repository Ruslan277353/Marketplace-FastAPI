from database.models import Product
from database import get_db
from datetime import datetime

def get_all_product():
    db = next(get_db())
    product = db.query(Product).all()
    return product
def get_exact_product(name: str):
    db = next(get_db())
    exact_product = db.query(Product).filter_by(name=name).first()
    if exact_product:
        return exact_product
    return 'Нет такого продукта'

def add_product(name, description, price, quantity):
    db = next(get_db())
    checker = get_exact_product(name)
    if checker:
        new_product = Product(name=name, description=description, price=price, quantity=quantity, reg_date=datetime.now())
        db.add(new_product)
        db.commit()
        return 'Продукт добавлен'
    else:
        checker

def change_data_product(id, change_info, new_info):
    db = next(get_db())
    product = db.query(Product).filter_by(id=id).first()
    if product:
        try:
            if change_info == 'name':
                product.name = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'description':
                product.description = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'price':
                product.price = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'quantity':
                product.quantity = new_info
                db.commit()
                return 'Успешно изменено'
        except:
            return 'Нет такого значения для изменения'
    return False


def delete_product(id):
    db = next(get_db())
    product = db.query(Product).filter_by(id=id).first()
    if product:
        db.delete(product)
        db.commit()
        return f'{product} успешно удален'
    return False

