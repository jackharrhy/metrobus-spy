FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7

COPY ./app.py /app/main.py
COPY ./requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt

#COPY .env.dist /app/.env
