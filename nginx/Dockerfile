FROM nginx:latest
RUN apt-get update -y
RUN apt-get upgrade -y
RUN mkdir logs
RUN mkdir /logs/nginx
COPY ./conf.d/ngnix-django.conf /etc/nginx/conf.d/
