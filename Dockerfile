FROM tiangolo/uwsgi-nginx-flask: python3.8-alpine-2020-08-16

WORKDIR /app

COPY ./app.py /app/main.py
COPY ./requirements.txt /app

RUN pip install -r requirements.txt
