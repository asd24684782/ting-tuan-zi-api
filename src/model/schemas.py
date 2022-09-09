from typing import List, Union

from pydantic import BaseModel

class UserBase(BaseModel):
	email: str
	username: str
	address: str
	phone: str

class UserCreate(UserBase):
	password: str

class User(UserBase):
    id: int
    disabled: bool

    class Config:
        orm_mode = True


class Product(BaseModel):
	name: str
	price: str
	stored_amount: str
	status: str
	img: str
	category: str
	info: str

	class Config:
		orm_mode = True


class CartModel(BaseModel):
	product_id : int
	username : str
	amount : int