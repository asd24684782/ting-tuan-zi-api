from sqlalchemy.orm import Session

from . import models, schemas

# user
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(email=user.email, 
                        username=user.username,
                        address=user.address,
                        phone=user.phone,
                        hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# product
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.Product):

    db_product = models.Product(
                        name            = product.name, 
                        price           = product.price,
                        stored_amount   = product.stored_amount,
                        status          = product.status,
                        img             = product.img,
                        category        = product.category,
                        info            = product.info)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

