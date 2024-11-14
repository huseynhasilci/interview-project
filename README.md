# interview-project
docker-compose build
docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose up

docker-compose run --rm app sh -c "python manage.py startapp core"


[Local address](http://127.0.0.1:8000/)