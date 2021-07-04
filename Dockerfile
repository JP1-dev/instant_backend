FROM alpine

WORKDIR /app

COPY . /app

RUN apk update

#RUN apk add build-base

RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add py-pip

RUN pip install -r requirements.txt

RUN pip install psycopg2


