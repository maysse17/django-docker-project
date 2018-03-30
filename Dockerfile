FROM python:3.6
RUN apt-get update \
   && apt-get install -y supervisor\
   && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir src
RUN mkdir /src/static
RUN mkdir /src/logs
COPY requirements.txt /src
COPY gunicorn.conf /src
COPY aslm-supervisor-gunicorn.conf /etc/supervisor/conf.d
COPY ./aslm /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD python manage.py collectstatic --no-input
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD service supervisor start
CMD supervisorctl reread
CMD supervisorctl update
CMD celery -A aslm worker -l debug
