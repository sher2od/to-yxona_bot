from datetime import datetime
from sqlalchemy import Column,Integer,BigInteger,String,DateTime
from app.database import Base

# Foydalanuvchi jadvali
class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    telegram_id = Column(BigInteger,unique=True,nullable=False)
    name = Column(String(64),nullable=False)
    contact = Column(String(15),nullable=False)
    created_at = Column(DateTime,default=datetime.now)

# Buyurtma jadvali
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,nullable=False)
    date = Column(DateTime,nullable=False) #To'y sanas
    guests_count = Column(DateTime,nullable=False) # MEhmonlar soni
    creadet_at = Column(DateTime,default=datetime.now)