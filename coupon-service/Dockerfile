FROM python:3.9-slim-bullseye

WORKDIR /app
COPY ./api/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./api /app/api

ENV PYTHONPATH=/app

EXPOSE 8040

VOLUME /app/coupons.db

CMD ["python","api/main.py"]