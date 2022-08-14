from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String(255), unique=True, index=True)
    phone = Column(String(255))
    address = Column(String(255))
    hashed_password = Column(String(255))
    disabled = Column(Boolean, default=False)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    modified_time = Column(DateTime(timezone=True), onupdate=func.now())
    
    #hashed_password = Column(String)
    #is_active = Column(Boolean, default=True)

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    price = Column(String(255))
    stored_amount = Column(String(255))
    status = Column(String(255))
    img = Column(String(255))
    category = Column(String(255))
    info = Column(String(255))
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    modified_time = Column(DateTime(timezone=True), onupdate=func.now())
