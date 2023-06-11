FROM python:3.8.10-alpine

MAINTAINER "danhuazhou"

ENV PYTHONUNBUFFERED 1

WORKDIR /www

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com \
    && pip install uwsgi -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com  \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8000