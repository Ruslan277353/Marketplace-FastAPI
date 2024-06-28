from database.models import User
from database import get_db
from datetime import datetime

def check_user_db(username, email):
    db = next(get_db())
    checker_name =db.query(User).filter_by(username=username).first()
    checker_email = db.query(User).filter_by(email=email).first()
    if checker_name:
        return 'Такой username уже существует'
    elif checker_email:
        return 'Такой email уже занят'
    else:
        return True

def register_user_db(username, email, password):
    db = next(get_db())
    checker = check_user_db(username, email)
    if checker:
        new_user = User(username=username, email=email, password=password, reg_date=datetime.now())
        db.add(new_user)
        db.commit()
        return f'Новый пользователь {new_user.username} добавлен'
    else:
        checker

def login_user(username, password):
    db = next(get_db())
    user = db.query(User).filter_by(username=username).first()
    if user:
        if user.password == password:
            return user
        else:
            return 'Неправельные данные'
    else:
        return 'Нет такого пользователя'

def get_profile_db(username):
    db = next(get_db())
    user_info = db.query(User).filter_by(username=username).first()
    if user_info:
        return user_info
    return False

def change_user_data_db(id, change_info, new_info):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        try:
            if change_info == 'username':
                user.username = new_info
                db.commit()
                return 'username изменен успешно'
            elif change_info == 'email':
                user = db.query(User).filter_by(email=new_info).first()
                if user:
                    return 'Этот email занят'
                else:
                    user.email = new_info
                    db.commit()
                    return 'email изменен успешно'
            elif change_info == 'password':
                user.password = new_info
                db.commit()
                return 'Пароль изменен успешно'
        except:
            return 'Нет такого знаения для изменений'
    return False

def delete_user(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        db.delete(user)
        db.commit()
        return f'{user.username} Успешно удален'
    return False