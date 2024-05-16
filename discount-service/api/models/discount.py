from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = 'car'

    pno = Column(Integer, primary_key=True, autoincrement=True)
    cno = Column(String(20), nullable=False)
    pname = Column(String(30), nullable=False)
    ent = Column(String(30), nullable=False)
    ent_time = Column(DateTime, default=datetime.now)
    checks = Column(String(10),nullable=False)
    exit_time = Column(DateTime)
    ptime = Column(String(40))
    disc = Column(String(30))
