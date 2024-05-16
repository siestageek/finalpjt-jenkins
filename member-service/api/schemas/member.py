from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import DateTime

class UserBase(BaseModel):
    mid: str
    mname: str
    pname: str

class UserLogin(BaseModel):
    mid: str
    mpwd: str

class UserCreate(UserBase):
    mpwd: str

class User(UserBase):
    mno: int
    #regdate: datetime
    regdate: str

    class Config:
        from_attributes=True


class Token(BaseModel):
    access_token: str
    token_type: str
