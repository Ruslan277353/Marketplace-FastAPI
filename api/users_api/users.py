from fastapi import APIRouter
from pydantic import BaseModel
from database.userservice import *
from database import get_db
from database.models import User

class UserValidator(BaseModel):
    username: str
    email: str
    password: str

user_router = APIRouter(prefix='/users', tags=['Users'])

@user_router.post('/api/registation')
async def user_registration(validator: UserValidator):
    db = next(get_db())
    user_data = dict(validator)
    user_username = user_data.get('username')
    checker = db.query(User).filter_by(username=user_username).first()
    if not checker:
        try:
            reg_user = register_user_db(**user_data)
            return {'status': 1, 'message': reg_user}
        except Exception as a:
            return {'status': 0, 'mwssage': a}
    else:
        return {'status': 0, 'message': 'Данный пользователь уже зарегестрирован'}

@user_router.post('/api/login')
async def login_user_api(username, password):
    user = login_user(username=username, password=password)
    return user

@user_router.get('/api/user')
async def get_user(username: str):
    exact_user = get_profile_db(username)
    return exact_user

@user_router.put('/api/change_data')
async def change_data(id, change_info, new_info):
    data = change_user_data_db(id=id, change_info=change_info, new_info=new_info)
    return f'Данные пользователя изменены\n{data}'

@user_router.delete('/api/delete')
async def delete_user(user_id: int):
    data = delete_user(user_id)
    return data
