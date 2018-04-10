FROM python:3.6-slim-stretch

LABEL maintainer="adil.mouhssine@gmail.com"

RUN apt-get update && \
   apt-get install -y \
   supervisor\
   git \
   vim \
   && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir -p /src/static
RUN mkdir -p /src/media
RUN mkdir -p /logs/gunicorn
COPY requirements.txt /src
COPY gunicorn.conf /src
COPY aslm-supervisor-gunicorn.conf /etc/supervisor/conf.d
COPY ./aslm /src
WORKDIR /src
# install project dependencies
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "django_docker_entrypoint.sh"]


