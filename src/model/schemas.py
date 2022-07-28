from typing import List, Union

from pydantic import BaseModel

class UserBase(BaseModel):
	email: str
	address: str
	phone: str
	username: str

class UserCreate(UserBase):
	password: str

class User(UserBase):
    id: int
    disabled: bool

    class Config:
        orm_mode = True
