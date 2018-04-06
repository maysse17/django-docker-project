build:
	sudo docker-compose build

up:
	sudo docker-compose up

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
