FROM python:3.9 AS base

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

WORKDIR /core

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

FROM base AS development

CMD python manage.py runserver 0:8000