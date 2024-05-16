from datetime import timedelta, datetime
from typing import Optional

import bcrypt, jwt
from sqlalchemy.orm import Session

from api.schemas import member as pym
from api.models import member as sqlm

# 비밀번호 해싱을 위한 솔트값 정의
SALT = bcrypt.gensalt()

# 토큰생성시 사용할 비밀키
SECRETKEY = 'git6a'


# 회원가입 처리
# def register(db: Session, user: pym.UserCreate ):
#     hashed_passwd = (bcrypt.hashpw(user.mpwd.encode('utf-8'), SALT))
#     print(hashed_passwd)
#
#     user = sqlm.Member(**user.model_dump())
#     user.passwd = hashed_passwd #암호화된패스워드
#     user.regdate = datetime.now().isoformat(' ', 'seconds')
#     # seconds 부분을 ''빈칸으로 바꾼다는 뜻
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return pym.User.from_orm(user)

def register(db: Session, user: pym.UserCreate):
    hashed_passwd = bcrypt.hashpw(user.mpwd.encode('utf-8'), SALT)
    print(hashed_passwd)

    # model_dump에서 반환된 딕셔너리에서 'mpwd' 키를 제거
    user_data = user.model_dump()
    user_data.pop('mpwd', None)  # 'mpwd' 키가 있으면 제거

    # Member 객체 생성 시 mpwd 필드에 해시된 비밀번호를 명시적으로 설정
    member = sqlm.Member(**user_data, mpwd=hashed_passwd)
    member.regdate = datetime.now().isoformat(' ', 'seconds')

    db.add(member)
    db.commit()
    db.refresh(member)
    return pym.User.from_orm(member)




# 엑세스 토큰 생성
# JWT : JSON Web Token
# 웹 어플리케이션에서 정보를 안전하게 전송하기 위해 사용되는 표준 방법
# JWT는 토큰 기반 인증시스템을 구현하는데 사용
# 주로 클라이언트/서버 간 정보 교환에 안전하게 사용할 수 있음
# HS256 : 토큰 생성시 사용할 해시 알고리즘 중 하나
def generate_access_token(mid: str, expires_delta: Optional[timedelta] = None):
    # 토큰 유효기간 설정 (기본 30분)
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=30)

    # 토큰 발급
    to_encode = {'sub': mid, 'exp': expire}
    encode_jwt = jwt.encode(to_encode, SECRETKEY, algorithm='HS256')

    return encode_jwt


def authenticate(db: Session, user: pym.UserLogin):
    dbuser = db.query(sqlm.Member).filter(sqlm.Member.mid == user.mid).first()

    if not dbuser: # 토큰이 안넘어가고 비어있는 채로 넘김
        return None
    if not bcrypt.checkpw(user.mpwd.encode('utf-8'), dbuser.mpwd) : # 비밀번호 일치하지않으면
        return None

    # 토큰 생성
    #token_data = {'mid': user.mid, 'mname': user.mname}
    #token_data = {'mid': user.mid, 'mname': dbuser.mname }
    #token = generate_access_token(token_data)
    token = generate_access_token(user.mid)

    # 토큰 넘겨줌
    return {'access_token': token, 'token_type': 'bearer'}