#!/bin/sh
# django-run.sh

export DJANGO_SETTINGS_MODULE=server.settings.production
cd server
daphne -b 0.0.0.0 -p 6000 server.asgi:application
