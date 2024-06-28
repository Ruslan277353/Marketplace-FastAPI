from datetime import datetime, timedelta

from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True)
    category_name = Column(String, nullable=False, unique=True)
    reg_date = Column(DateTime)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer)
    category_name = Column(String, ForeignKey('categories.category_name'))
    reg_date = Column(DateTime)

    category_fk = relationship(Category, foreign_keys=[category_name], lazy='subquery')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total = Column(Float)
    reg_date = Column(DateTime)

    user = relationship(User, foreign_keys=[user_id], lazy='subquery')


class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    reg_date = Column(DateTime)

    user = relationship(User, foreign_keys=[user_id], lazy='subquery')
    product = relationship(Product, foreign_keys=[product_id], lazy='subquery')

class ProductPhoto(Base):
    __tablename__ = 'product_photos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    photo_path = Column(String, nullable=False)
    reg_date = Column(DateTime)

    product_fk = relationship(Product, foreign_keys=[product_id], lazy='subquery')
