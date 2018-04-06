FROM python:3.6

MAINTAINER Adil MOUHSSINE

RUN apt-get update && apt-get -y upgrade && \
   apt-get install -y \
   apt-utils \
   supervisor\
   git \
   vim \
   && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir src logs
RUN mkdir /src/static
RUN mkdir /src/media
RUN mkdir /logs/gunicorn
COPY requirements.txt /src
COPY gunicorn.conf /src
COPY aslm-supervisor-gunicorn.conf /etc/supervisor/conf.d
COPY run_django_app.sh /src
COPY ./aslm /src
WORKDIR /src
# install project dependencies
RUN pip install -r requirements.txt
