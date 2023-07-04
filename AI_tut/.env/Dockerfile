# syntax=docker/dockerfile:1
FROM python:3.10.8-alpine3.16

WORKDIR /application

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip
RUN apk update && apk add build-base
RUN apk update && \
    apk add python3-dev
RUN pip3 install -r requirements.txt

COPY . .

