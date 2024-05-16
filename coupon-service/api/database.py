import sqlalchemy
from api.models.coupon import Base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

#db_url = 'sqlite:///coupon.db'
db_url = os.getenv("DATABASE_URL")

engine = sqlalchemy.create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    Base.metadata.create_all(engine)


# 데이터베이스 세션 의존생 생성
def get_db():
    with SessionLocal() as db:
        yield db
