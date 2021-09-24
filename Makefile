.PHONY: init 

init: 
	@make down
	@make up
	@make ps
	make fixtures
	@make logs
down:
	docker-compose down --volumes --remove-orphans
pull:
	docker-compose pull
build:
	docker-compose build
up: 
	make pull 
	make build
	docker-compose up -d
ps:
	docker-compose ps
logs:
	docker-compose logs core
migrations:
	docker-compose run --rm core python manage.py makemigrations
migrate: 
	@make migrations
	docker-compose run --rm core python manage.py migrate
fixtures:
	make migrate
	# docker-compose run --rm core python manage.py populatedb
	# docker-compose run --rm core python manage.py seed djangolery --number=5
reset_db:
	docker-compose run --rm core python manage.py reset_db --noinput --close-sessions
su:
	docker-compose run --rm core python manage.py createsuperuser
test:
	docker-compose run --rm core coverage run --source="." manage.py test
	docker-compose run --rm core coverage report -m
shell:
	docker-compose run --rm core python manage.py shell_plus --ipython
	######### For Autoreload #########
	## In [1]: %load_ext autoreload ##
	## In [2]: %autoreload 2        ##
	##################################
prune:
	make down
	docker volume prune -f
	docker system prune -f
format:
	docker-compose run --rm core black .
lint:
	docker-compose run --rm core black . --check
loaddata:
	docker-compose run --rm core python manage.py loaddata users menus
reset_celery:
	docker-compose stop celery && docker-compose start celery