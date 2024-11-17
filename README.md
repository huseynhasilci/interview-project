# interview-project
# Öncelikle teşekkür ederim. İş yoğunluğunun fazla olduğu bir döneme denk geldiği için çıkartabildiğim kadar çıkartmaya çalıştım docker ile back-end ayağa kalkıyor bazı endpointler için test caseler de yazılmıştır genel crud işlemleri çalışmakta ancak bütün fonsiyonileteleri ekleyemedim alttan swagger'a ulaşabilirsiniz.

# Şu adımları izleyerek docker üzerinden ayağa kaldırabilirsiniz.
docker-compose build
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
docker-compose up

[Local address](http://127.0.0.1:8000/)
[Swagger address](http://127.0.0.1:8000/api/docs/#/)


docker-compose build
docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose up

docker-compose run --rm app sh -c "python manage.py startapp core"



docker-compose down
docker volume rm interview-project_dev-db-data

admin@example.com
adminpassword


docker-compose run --rm app sh -c "python manage.py startapp user"


