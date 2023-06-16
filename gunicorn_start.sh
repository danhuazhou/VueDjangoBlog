#!/bin/bash

NAME="MyBlog"
DJANGODIR=/www/webapp/my-bolg #Django project directory
USER=www # the user to run as
GROUP=www # the group to run as
NUM_WORKERS=2 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=${NAME}.settings # which settings file should Django use
DJANGO_WSGI_MODULE=${NAME}.wsgi # WSGI module name
LOGDIR=/www/wwwlogs/blog_log

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /opt/archiconda3/bin/activate blog
# gunicorn -e DJANGO_SETTINGS_MODULE=myproject.settings_production
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE


# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/www/.local/bin/gunicorn  ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--bind=0.0.0.0:8001
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--log-level=info \
--access-logfile=${LOGDIR}/gunicorn.access.log \
--error-logfile=${LOGDIR}/gunicorn.error.log \
