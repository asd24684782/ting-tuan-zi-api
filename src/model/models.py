from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "user"

    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True)
    username        = Column(String(255), unique=True, index=True)
    phone           = Column(String(255))
    address         = Column(String(255))
    hashed_password = Column(String(255))
    disabled        = Column(Boolean, default=False)
    created_time    = Column(DateTime(timezone=True), server_default=func.now())
    modified_time   = Column(DateTime(timezone=True), onupdate=func.now())
    
    user_UserCart  = relationship("usercart", backref="user")
    user_UserOrder = relationship("userorder", backref="user")
    #hashed_password = Column(String)
    #is_active = Column(Boolean, default=True)

class Product(Base):
    __tablename__ = "product"
    
    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String(255))
    price           = Column(Integer)
    stored_amount   = Column(Integer)
    status          = Column(Integer)
    img             = Column(String(255))
    category        = Column(String(255))
    info            = Column(String(255))
    created_time    = Column(DateTime(timezone=True), server_default=func.now())
    modified_time   = Column(DateTime(timezone=True), onupdate=func.now())

    product_UserCart  = relationship("usercart", backref="product")
    product_UserOrder = relationship("userorder", backref="product")

class UserCart(Base):
    __tablename__ = "usercart"
    
    id              = Column(Integer, primary_key=True, index=True)
    product_id      = Column(Integer, ForeignKey("product.id"))
    user_id         = Column(Integer, ForeignKey("user.id"))
    amount          = Column(Integer)
    status          = Column(Integer)
    created_time    = Column(DateTime(timezone=True), server_default=func.now())
    modified_time   = Column(DateTime(timezone=True), onupdate=func.now())




class UserOrder(Base):
    __tablename__ = "userorder"
    
    id              = Column(Integer, primary_key=True, index=True)
    product_id      = Column(Integer, ForeignKey("Product.id"))
    user_id         = Column(Integer, ForeignKey("User.id"))
    amount          = Column(Integer)
    status          = Column(Integer)
    orderno         = Column(Integer)
    created_time    = Column(DateTime(timezone=True), server_default=func.now())
    modified_time   = Column(DateTime(timezone=True), onupdate=func.now())
