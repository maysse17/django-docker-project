FROM python:3.6

MAINTAINER Adil MOUHSSINE

RUN apt-get update && \
   apt-get install -y \
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
# collect static files
CMD python manage.py collectstatic --no-input
# prepare init migration
CMD python manage.py makemigrations
# migrate db, so we have the latest db schema
CMD python manage.py migrate

