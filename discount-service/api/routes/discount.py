from typing import List

from api.schema.discount import Car
from api.dao import CarService
from api.database import db_startup
from fastapi import APIRouter, HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

templates = Jinja2Templates(directory='/views/templates')


car_router = APIRouter()

@car_router.on_event('startup')
async def on_startup():
    db_startup()

# 차량 데이터 조회

@car_router.get('/discount', response_class=HTMLResponse)
def cars(request: Request):
    return templates.TemplateResponse('discount.html', {'request': request, 'cars': cars})


@car_router.get("/discount/{cno}", response_model=List[Car])
def get_car_info_by_number(cno: str):
    car_info_list = CarService.get_car_info_by_number(cno)
    if car_info_list:
        for car_info in car_info_list:
            car_info.cno = str(car_info.cno)
        return car_info_list
    else:
        return JSONResponse(content={"error": "차량번호를 찾을 수 없습니다"}, status_code=404)

@car_router.get("/discount-by-number/{cno}", response_model=Car)
def get_car_info_by_number_exact(cno: str):
    car_info = CarService.get_car_info_by_number_exact(cno)
    if car_info:
        car_info.cno = str(car_info.cno)
        return car_info
    else:
        return JSONResponse(content={"error": "일치하는 차량번호를 찾을 수 없습니다"}, status_code=404)



@car_router.put("/discount/{cno}/discount", status_code=200)
def update_discount_info(cno: str, disc: str):
    # 할인 정보를 받아서 처리
    car_info = CarService.get_car_info_by_number(cno)
    if car_info:
        # 'discount'를 'disc'로 변경하여 업데이트
        CarService.apply_discount(car_info, disc)
        return JSONResponse(content={"message": "할인 정보가 업데이트되었습니다."})
    else:
        raise HTTPException(status_code=404, detail="차량을 찾을 수 없습니다.")
