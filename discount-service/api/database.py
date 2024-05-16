import sqlalchemy

from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

#db_url = 'sqlite:///car.db'
db_url = os.getenv("DATABASE_URL")

engine = sqlalchemy.create_engine(db_url, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# 서버시작시 테이블 생성
def db_startup():
    from api.models import discount
    discount.Base.metadata.create_all(engine)
