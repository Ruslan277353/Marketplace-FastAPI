from fastapi import APIRouter, UploadFile, File
from database.photoservice import *
from typing import List

photo_router = APIRouter(prefix='/photos', tags=['Photo'])

@photo_router.post('/add_photo')
async def add_photos(product_id: int, photo_path: List[UploadFile] = File(...)):
    if not photo_path:
        return {'status': 0, 'message': 'Нет фото'}
    saved_files = []
    for i, photo_path in enumerate(photo_path):
        file_location = f'database/photos/photo_{product_id}_{i}.jpg'
        with open(file_location, 'wb') as photo:
            photo_to_save = await photo_path.read()
            photo.write(photo_to_save)
            add_photo_db(product_id, file_location)
            saved_files.append(file_location)
    return {'status': 1, 'message': 'Фото добавлено'}