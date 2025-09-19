from sqlalchemy import Column, Integer, String
from app.database import Base
from uuid6 import uuid7

def generate_uuid7():
    return str(uuid7())

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=generate_uuid7)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)