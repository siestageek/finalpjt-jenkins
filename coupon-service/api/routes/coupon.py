from datetime import datetime

import api.models.coupon as sqlm
import api.schema.coupon as pym
from api.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello World"}


# 전체조회
@router.get("/coupons", response_model=list[pym.Coupon])
async def list_coupons(db: Session = Depends(get_db)):
    coupons = db.query(sqlm.Coupon).all()
    return [pym.Coupon.from_orm(p) for p in coupons]


# 조회
@router.get("/coupons/{cpg}", response_model=list[pym.Coupon])
async def list_coupons(cpg: int, db: Session = Depends(get_db)):
    stnum = (cpg - 1) * 10
    coupons = db.query(sqlm.Coupon).offset(stnum).limit(10)
    return [pym.Coupon.from_orm(p) for p in coupons]


# 입력
@router.post("/coupons", response_model=pym.Coupon)
async def create_coupons(coupon: pym.CouponCreate, db: Session = Depends(get_db)):
    coupon = sqlm.Coupon(**coupon.model_dump())
    coupon.disc_time = datetime.now().isoformat(' ', 'seconds')
    db.add(coupon)
    db.commit()
    db.refresh(coupon)
    return pym.Coupon.from_orm(coupon)


# 전체 검색 조회
@router.get("/cpfind/{skey}", response_model=list[pym.Coupon])
async def find_coupons(skey: str, db: Session = Depends(get_db)):
    coupons = db.query(sqlm.Coupon).filter(func.lower(sqlm.Coupon.disc_time).like('%' + skey + '%'))
    return [pym.Coupon.from_orm(p) for p in coupons]


# 검색 조회
@router.get("/cpfind/{skey}/{cpg}", response_model=list[pym.Coupon])
async def find_coupons(skey: str, cpg: int, db: Session = Depends(get_db)):
    stnum = (cpg - 1) * 10
    coupons = db.query(sqlm.Coupon).filter(func.lower(sqlm.Coupon.disc_time).like('%' + skey + '%')).offset(
        stnum).limit(10)
    return [pym.Coupon.from_orm(p) for p in coupons]


# 전체 그룹 조회
@router.get("/sumfind")
async def find_coupons(db: Session = Depends(get_db)):
    coupons = db.query(sqlm.Coupon, func.count(sqlm.Coupon.dno).label('count')) \
        .filter(sqlm.Coupon.usec.like('y')) \
        .order_by(sqlm.Coupon.disc).group_by(sqlm.Coupon.disc).all()
    result = []

    for coupon, count in coupons:
        coupon_data = {"disc": coupon.disc, "disc_time": coupon.disc_time, "count": count}
        result.append(coupon_data)
    return result


# 특정 그룹 검색 조회
@router.get("/sumfindall/{skey}")
async def find_coupons(skey: str, db: Session = Depends(get_db)):
    coupons = db.query(sqlm.Coupon, func.count(sqlm.Coupon.dno).label('count')) \
            .filter(func.lower(sqlm.Coupon.disc_time).like('%' + skey + '%'), sqlm.Coupon.usec.like('y')) \
            .order_by(sqlm.Coupon.disc).group_by(sqlm.Coupon.disc).all()
    result = []

    for coupon, count in coupons:
        coupon_data = {"disc": coupon.disc, "disc_time": coupon.disc_time, "count": count}
        result.append(coupon_data)
    return result


# 전체 차 조회
@router.get("/sumfind")
async def find_coupons(db: Session = Depends(get_db)):
    coupons = db.query(sqlm.Coupon, func.count(sqlm.Coupon.dno).label('count')) \
        .filter(sqlm.Coupon.usec.like('y')) \
        .order_by(sqlm.Coupon.disc).group_by(sqlm.Coupon.disc).all()
    result = []

    for coupon, count in coupons:
        coupon_data = {"disc": coupon.disc, "disc_time": coupon.disc_time, "count": count}
        result.append(coupon_data)
    return result
