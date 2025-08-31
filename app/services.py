# services.py
from .database import SessionLocal
from .models import User

def save_user(user_data, telegram_id):
    """User ma'lumotlarini bazaga saqlash funksiyasi"""
    with SessionLocal() as session:
        user = User(
            telegram_id=telegram_id,
            name=user_data["name"],
            contact=user_data["contact"],
            date=user_data["date"],
            guests=user_data["guests"]
        )
        session.add(user)
        session.commit()
       