# syntax=docker/dockerfile:1
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m pip install --upgrade pip
WORKDIR /instagram
COPY requirements.txt /instagram/
RUN pip install -r requirements.txt
COPY . /instagram/