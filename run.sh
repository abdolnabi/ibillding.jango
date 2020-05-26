#!/bin/sh

gunicorn bcm.wsgi:application --chdir bcm --bind 127.0.0.1:8000  --workers=1
