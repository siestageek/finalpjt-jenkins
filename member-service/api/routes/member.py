from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session




from api.database import get_db

from api.services import auth
from api.schemas import member as pym
from api.models import member as sqlm


router = APIRouter()

@router.get("/")
async def index():
    return {"message": "not here"}

# 유저 정보 가져오기
# @router.get("/users", response_model=list[pym.User])
# async def query_user(db:Session = Depends(get_db)):
#     pass
#     return
    # oneuser = db.query(sqlm.User).all()
    # oneuser = db.query(sqlm.User.mid, sqlm.User.mname, sqlm.User.pname).all()

    # return [pym.User.from_orm(p) for p in oneuser]

# @member_router.get('/myinfo', response_class=HTMLResponse)
# def myinfo(req: Request):
#     if 'm' not in req.session:
#         return RedirectResponse(url='/login', status_code=status.HTTP_303_SEE_OTHER)
#
#     myinfo = MemberService.selectone_member(req.session['m'])
#     return templates.TemplateResponse('myinfo.html',{'request': req, 'my': myinfo})


# @staticmethod
# def selectone_member(userid):
#     with Session() as sess:
#         result = sess.query(Member).filter_by(userid=userid).scalar()
#         return result


# 회원가입 하기
@router.post("/users", response_model=pym.User)
async def create_user(user: pym.UserCreate, db:Session = Depends(get_db)):
    return auth.register(db, user)

# 로그인 하기
@router.post("/login", response_model=pym.Token)
async def login_user(user: pym.UserLogin, db:Session = Depends(get_db)):
    token = auth.authenticate(db, user)

    if not token:
        raise HTTPException(status_code=401, detail='로그인 실패!! - 아이디 혹은 비밀번호를 확인하세요')

    return token

# 회원정보 수정 하기
@router.post("/users/modify", response_model=pym.User)
async def create_user(user: pym.UserCreate, db:Session = Depends(get_db)):
    return auth.register(db, user)
