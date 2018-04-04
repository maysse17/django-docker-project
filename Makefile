build:
	docker-compose build

up:
	docker-compose up -d

start:
	docker-compose start

stop:
	docker-compose stop

test-react:
	curl -i http://localhost:3000
	curl -i http://localhost/react

test-django:
	curl -i http://localhost:8000
	curl -i http://localhost:8000/admin/login/?next=/admin/
	curl -i http://localhost/admin/login/?next=/admin/

bash-react:
	docker exec -it dockercomposernginxreactdjangodev_react_1 bash

bash-django:
	docker exec -it dockercomposernginxreactdjangodev_django_1 bash

bash-nginx:
	docker exec -it dockercomposernginxreactdjangodev_nginx_1 bash
