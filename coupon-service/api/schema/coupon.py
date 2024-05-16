from pydantic import BaseModel


class CouponBase(BaseModel):
    cno: str
    disc: str


class CouponCreate(CouponBase):
    class Config:
        from_attributes = True


class Coupon(CouponBase):
    dno: int
    disc_time: str
    usec: str

    class Config:
        from_attributes = True
