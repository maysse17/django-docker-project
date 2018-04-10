#!/bin/bash


echo Collect static files...
python manage.py collectstatic --no-input

echo Prepare init migration...
python manage.py makemigrations

echo Migrate db, so we have the latest db schema...
python manage.py migrate

echo Starting Supervisor to start Gunicorn...
exec supervisord -c /etc/supervisor/conf.d/aslm-supervisor-gunicorn.conf -n