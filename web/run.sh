#!/bin/sh

# Record pipdeptree
_required=`mktemp`
_installed=`mktemp`
cat /www/requirements.txt | cut -d'=' -f1 | cut -d'>' -f1 | cut -d'[' -f1 | sed -e '/^#/d' -e '/^$/d' > $_required
pip freeze > $_installed
sed -i '/^##/d' /www/requirements.txt
grep -F -f $_required $_installed | sed 's/^/## /g' >> /www/requirements.txt
rm $_required $_installed
pipdeptree > /www/pipdeptree.txt

# Migrage DB
python manage.py makemigrations
python manage.py migrate
python manage.py migrate django_cron

# Collect static files
python manage.py collectstatic --noinput

# Load crontab and start in background
cat /crontab > /var/spool/cron/crontabs/root
crond

# Run
# tail -f /dev/null

gunicorn -b 0.0.0.0:8000 --workers 1 --chdir /www ITLabStore.wsgi:application

# gunicorn --keyfile /keys/live/example.com/privkey.pem \
#          --certfile /keys/live/example.com/cert.pem \
#          --workers 1 \
#          -b 0.0.0.0:8000 \
#          --chdir /www ITLabStore.wsgi:application