#!/bin/sh

cd aslm
# collect static files
python manage.py collectstatic --no-input
# prepare init migration
python manage.py makemigrations
# migrate db, so we have the latest db schema
python manage.py migrate
# start development server on public ip interface, on port 8000
supervisord -c /etc/supervisor/conf.d/aslm-supervisor-gunicorn.conf