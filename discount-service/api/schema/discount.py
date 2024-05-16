from datetime import datetime

from pydantic import BaseModel


class Car(BaseModel):
    pno: int
    cno: str
    pname: str
    ent: str
    ent_time: datetime
    checks: str
    exit_time: datetime
    ptime: str
    disc: str

    class Config:
        from_attributes = True
