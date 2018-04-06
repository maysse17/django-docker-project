
# Create django application and deploy it using docker compose

## Django Development With Docker Compose and Machine

A docker-composer environment for local development in Django/Gunicorn/Postgresql/Celery/Redis/Ngnix

`docker-compose.yml`

```
version: '3'
services:
  nginx:
    build: nginx/
    container_name: nginx-django
    volumes:
      - ./django/aslm:/src
      - ./nginx/conf.d:/etc/nginx/conf.d
    ports:
      - "8000:8000"
    depends_on:
      - web
  web:
    build: ./django/
    container_name: aslm-django-guinicorn
    depends_on:
      - db
    volumes:
      - ./django/aslm:/src
    expose:
      - "8000"
    links:
      - redis
  db:
    image: postgres:latest
    container_name: postgredb-django
  redis:
    build: ./redis
    container_name: redis
    ports:
     - '6378:6378'
```

`nginx/Dockerfile`

```
FROM nginx:latest
RUN apt-get update -y
RUN apt-get upgrade -y
RUN mkdir logs
RUN mkdir /logs/nginx
```

`redis/Dockerfile`
```
FROM redis:latest
RUN apt-get update -y
RUN apt-get upgrade -y
COPY ./conf/redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
```

`django/Dockerfile`
```
FROM python:3.6

MAINTAINER Adil MOUHSSINE

RUN apt-get update && apt-get -y upgrade && \
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
COPY ./aslm /src
WORKDIR /src
# install project dependencies
RUN pip install -r requirements.txt
# collect static files
CMD ["python", "manage.py", "collectstatic", "--no-input"]
# prepare init migration
CMD ["python", "manage.py", "makemigrations"]
# migrate db, so we have the latest db schema
CMD ["python", "manage.py", "migrate"]
# start supervisor
CMD ["service", "supervisor", "start"]
CMD ["supervisorctl", "reread"]
CMD ["supervisorctl", "update"]
# start celery worker
CMD ["celery", "-A", "aslm", "worker", "-l", "debug"]
```

`Makefile`
```
build:
	sudo docker-compose build

up:
	sudo docker-compose up -d

start:
	sudo docker-compose start

stop:
	sudo docker-compose stop

bash-redis:
	sudo docker exec -it redis-django bash

bash-django:
	sudo docker exec -it aslm-django-guinicorn bash

bash-nginx:
	sudo docker exec -it nginx-django bash
```

# Contributors

[Adil MOUHSSINE](https://github.com/maysse17) for ASLM.
