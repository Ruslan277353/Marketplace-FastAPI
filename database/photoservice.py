from database import get_db
from database.models import ProductPhoto
from datetime import datetime

def add_photo_db(product_id, photo_path):
    db = next(get_db())
    photo = ProductPhoto(product_id=product_id, photo_path=photo_path, reg_date=datetime.now())
    db.add(photo)
    db.commit()
    return f'Успешно добавлено фото для {product_id}'
