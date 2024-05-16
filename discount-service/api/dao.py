from sqlalchemy.exc import SQLAlchemyError
from api.models.discount import Car
from database import Session


class CarService():
    @classmethod
    def get_car_info_by_number(cls, cno):
        last_four_digits = cno[-4:]  # cno의 뒤에서 4자리 추출

        try:
            with Session() as sess:
                car_info = sess.query(Car).filter(Car.cno.endswith(last_four_digits)).all()
                # cno의 뒷 4자리로 끝나는 데이터를 검색하고 모든 결과를 리스트로 반환
                return car_info
        except SQLAlchemyError as e:
            # 데이터베이스 작업 중 에러 발생 시 처리
            print("Error occurred while querying database:", e)
            return None

    @classmethod
    def get_car_info_by_number_exact(cls, cno):  # 함수명 변경
        try:
            with Session() as sess:
                car_info = sess.query(Car).filter(Car.cno == cno).first()  # 리스트로 반환하는 부분 삭제
                # cno와 일치하는 데이터를 검색하고 첫 번째 결과를 반환
                return car_info
        except SQLAlchemyError as e:
            # 데이터베이스 작업 중 에러 발생 시 처리
            print("Error occurred while querying database:", e)
            return None


    @classmethod
    def apply_discount(cls, car_info_list, discount):
        try:
            with Session() as sess:
                for car_info in car_info_list:
                    car_info.disc = discount
                    # 변경된 정보를 데이터베이스에 추가
                    sess.merge(car_info)  # merge 사용하여 변경된 엔티티를 데이터베이스에 반영
                sess.commit()  # 세션을 커밋하여 변경 사항을 실제로 데이터베이스에 반영

                return car_info_list
        except SQLAlchemyError as e:
            # 데이터베이스 작업 중 에러 발생 시 처리
            print("Error occurred while updating database:", e)
            return None

