from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Coupon(Base):
    __tablename__ = 'coupon'

    dno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    cno = Column(String(20))
    disc = Column(String(30))
    disc_time = Column(String(20))
    usec = Column(String(3), default='n')
