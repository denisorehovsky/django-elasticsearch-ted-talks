FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && apk add postgresql-client

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./docker/web/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app
