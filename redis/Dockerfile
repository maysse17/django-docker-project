FROM redis:latest
RUN apt-get update -y
RUN apt-get upgrade -y
COPY ./conf/redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
