from app.bot import run_bot
from app.database import Base, engine
from app.models import User   # jadval klassini import qilish kerak

if __name__ == "__main__":
    # Jadval(lar)ni yaratish (agar mavjud bo‘lmasa)
    Base.metadata.create_all(bind=engine)

    run_bot()
