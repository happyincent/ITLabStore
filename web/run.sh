#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py migrate django_cron
python manage.py collectstatic --noinput

crond && uwsgi --ini /www/ITLabStore.ini