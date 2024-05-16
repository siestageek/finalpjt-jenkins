from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#
#
#     mno = Column(Integer, primary_key=True, autoincrement=True, index=True)
#     userid = Column(String(18), nullable=False)
#     passwd = Column(String(128), nullable=False)
#     name = Column(String(15), nullable=False)
#     email = Column(String(100), nullable=False)
#     # regdate = Column(DateTime, default=datetime.now(), nullable=False)
#     regdate = Column(String(20), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
# from app.models.base import Base


class Member(Base):
    __tablename__ = 'members'

    mno = Column(Integer, primary_key=True, autoincrement=True)
    mid = Column(String(18), nullable=False, unique=True)
    mpwd = Column(String(128), nullable=False)
    mname = Column(String(20), nullable=False)
    pname = Column(String(40), nullable=False)
    #regdate = Column(String(20), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    regdate = Column(String(20))

