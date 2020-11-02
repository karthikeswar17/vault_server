from typing import List
from pydantic import BaseModel

class AccountBase(BaseModel):
    name: str
    username: str
    password: str
    url: str

class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    accounts: List[Account] = []
    class Config:
        orm_mode = True