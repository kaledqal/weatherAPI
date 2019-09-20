FROM python:3.7-alpine
MAINTAINER Kalenshi Katebe

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /weatherApp
WORKDIR /weatherApp

COPY ./weatherApp /weatherApp

RUN adduser -D user
USER user
