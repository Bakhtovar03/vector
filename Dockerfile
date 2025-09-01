FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /vector

COPY requirements.txt /vector/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /vector/

RUN chmod +x entrypoint.sh

LABEL authors="bakhtovar"

ENTRYPOINT ["./entrypoint.sh"]