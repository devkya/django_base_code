#!/bin/sh
# django-run.sh

set -e

if [ "$DEBUG" = "True" ]; then
    export DJANGO_SETTINGS_MODULE=server.settings.development
    
    if [ "$CELERY_BEAT" = "True" ]; then
        celery -A config.celery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    elif [ "$CELERY_WORKER" = "True" ]; then
        celery -A config.celery worker -l info  
    else
        python manage.py makemigrations --no-input
        python manage.py migrate --no-input
        # 로컬망에서 접속 가능한 환경
        python manage.py runserver 0.0.0.0:8000
    fi
    
else
    export DJANGO_SETTINGS_MODULE=server.settings.production
    if [ "$CELERY_BEAT" = "True" ]; then
        celery -A config.celery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    elif [ "$CELERY_WORKER" = "True" ]; then
        celery -A config.celery worker -l info  
    else
        python manage.py collectstatic --noinput
        python manage.py migrate --no-input
        gunicorn server.wsgi:application --bind 0.0.0.0:8000
    fi
fi
