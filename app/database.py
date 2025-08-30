from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import config   # config obyektini chaqiramiz

# 1) URL ni yasash
url = URL.create(
    drivername="postgresql+psycopg2",
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME,
)

# 2) Engine – DB bilan aloqani qiladi
engine = create_engine(url)

# 3) Base – barcha model klasslari uchun asos
Base = declarative_base()

# 4) Session – DB ga ulanishni boshqaradi
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
