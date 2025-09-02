from app.bot import run_bot
from app.database import Base, engine
from app.models import User  

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    run_bot()
