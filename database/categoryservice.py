from database.models import Category
from database import get_db
from datetime import datetime

def add_category(category_name):
    db = next(get_db())
    category = Category(category_name=category_name, reg_date=datetime.now())
    db.add(category)
    db.commit()
    return category

def get_all_categories():
    db = next(get_db())
    categories = db.query(Category).all()
    return categories

def get_exact_category(id):
    db = next(get_db())
    exact_category = db.query(Category).filter_by(id=id).first()
    if exact_category:
        return exact_category
    return False

def get_categories(category_name):
    db = next(get_db())
    categories = db.query(Category).filter_by(category_name=category_name).all()
    if categories:
        return categories
    return False

def delete_category(id):
    db = next(get_db())
    exact_category =db.query(Category).filter_by(id=id).first()
    if exact_category:
        db.delete(exact_category)
        db.commit()
        return 'Успешно удалено'
    return False