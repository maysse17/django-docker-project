FROM python:3.6
RUN apt-get update \
   && apt-get install supervisor \
   && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir src
RUN mkdir static
WORKDIR /src
RUN mkdir logs
COPY requirements.txt /src
COPY ./gunicorn.conf /src
COPY ./aslm-gunicorn.conf /etc/supervisor
COPY ./aslm /src
RUN pip install -r requirements.txt
CMD python manage.py collectstatic --no-input
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD supervisorctl reread
CMD supervisorctl update
CMD celery -A aslm worker -l debug
