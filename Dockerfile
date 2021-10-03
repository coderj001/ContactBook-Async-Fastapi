FROM python:3.8-alpine

WORKDIR /app

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN apk add build-base

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
